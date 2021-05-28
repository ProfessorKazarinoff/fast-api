# fast-api

An example Fast API web API. Just a sample project, not for prouduction or a full website backend.

## Installation

```
# python==3.9.5
python -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

## Run

```
uvicorn main:api --reload
# http://localhost:8000/
# http://localhost:8000/api/calculate?x=7&y=2
# Ctrl-c to stop

uvicorn main2:app
# http://localhost:8000/
# http://localhost:8000/items/2


uvicorn template-app:app
# http://localhost:8000/items/2
```
