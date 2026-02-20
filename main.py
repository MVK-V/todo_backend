from fastapi import FastAPI
from pydantic_settings import BaseSettings
from EntryManager import EntryManager
from entry import Entry
import uvicorn

app = FastAPI(title='Todo Backend')

from fastapi.middleware.cors import CORSMiddleware

origins = [
    "https://wexler.io"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["origins"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get('/api/entries/')
async def get_entries():
    entry_manager = EntryManager(data_path=settings.data_folder)
    entry_manager.load()

    return [entry.json() for entry in entry_manager.entries]



class Settings(BaseSettings):
    data_folder: str = '/tmp/'

settings = Settings()



@app.get('/api/get_data_folder/')
async def get_data_folder():
    return {'folder': settings.data_folder}


@app.post('/api/save_entries/')
async def save_entries(data):
    entry_manager = EntryManager(settings.data_folder)

    for item in data:
        entry = Entry.from_json(item)
        entry_manager.entries.append(entry)

    entry_manager.save()

    return {'status': 'success'}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
