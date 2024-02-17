from fastapi import FastAPI
from rotas import router

app = FastAPI()


@app.get("/")
def get_root():
    return {"message": "oioioi"}


app.include_router(router, prefix='')
