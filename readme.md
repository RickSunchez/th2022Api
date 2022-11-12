# simple th2022 api

## local install

- python3 -m venv .env
- ./.env/Scripts/Activate.ps1
- pip install -r req.txt
- uvicorn app:app --reload

## special for Artemka

- docker build . --tag th-fastapi
- docker compose up
