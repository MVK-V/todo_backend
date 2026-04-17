# Nested Task Architect
> A robust Python backend for managing hierarchical data structures with automated JSON persistence.

##  Overview
This project is a back-end engine designed to handle nested "parent-child" relationships, commonly used in Todo-lists, Project Management tools, or Folder structures. It features a recursive logic that allows for infinite nesting of tasks.

##  Key Features
- **Recursive Data Modeling**: Each entry can host sub-entries, building a tree-like structure.
- **Automated Serialization**: Seamless conversion between Python objects and JSON format for long-term storage.
- **Smart Manager**: An orchestration layer (`EntryManager`) that handles bulk saving/loading from the local file system.
- **API Ready**: Integrated with **FastAPI** to serve data to web front-ends, including pre-configured CORS policies.

##  Tech Stack
- **Language**: Python 3.12+
- **Framework**: FastAPI
- **Data Handling**: JSON, Pydantic (Settings)
- **Environment**: Docker-ready

##  Project Structure
- `entry.py`: Core logic for the recursive data model.
- `EntryManager.py`: Management layer for file I/O operations.
- `main.py`: FastAPI entry point and middleware configuration.

##  Installation
```bash
pip install -r requirements.txt
uvicorn main:app --reload