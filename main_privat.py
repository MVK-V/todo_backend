from fastapi import FastAPI
from pydantic_settings import BaseSettings
from EntryManager import EntryManager
from entry import Entry
import uvicorn

app = FastAPI(title='Todo Backend')

from fastapi.middleware.cors import CORSMiddleware

origins = [
    "https://wexler.io"  # адрес на котором работает фронт-энд
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["origins"],  # Список разрешенных доменов
    allow_credentials=True,  # Разрешить Cookies и Headers
    allow_methods=["*"],  # Разрешить все HTTP методы
    allow_headers=["*"],  # Разрешить все хедеры
)


@app.get('/')
async def hello_world():
    return {'Hello': 'World'}


@app.get('/api/entries/')
async def get_entries():
    entry_manager = EntryManager(data_path=settings.data_folder)
    entry_manager.load()

    if not entry_manager.entries:
        entry_manager.add_entry("Тестовая запись для фронтенда")    # ВРЕМЕННО


    return [entry.json() for entry in entry_manager.entries]




class Settings(BaseSettings):
    data_folder: str = '/tmp/'  # str = '/tmp/' - значение по умолчанию


settings = Settings()


@app.get('/api/get_data_folder/')
async def get_data_folder():
    return {'folder': settings.data_folder}


@app.post('/api/save_entries/')
async def save_entries(data):
    entry_manager = EntryManager(settings.data_folder)

    for item in data:
        entry = Entry.from_json(item)  # Создаем объект из данных
        entry_manager.entries.append(entry)

    entry_manager.save()

    return {'status': 'success'}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)