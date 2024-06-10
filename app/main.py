from fastapi import FastAPI

app = FastAPI()     #   вызываю класс fastapi

@app.get('/hotels')
def get_hotels():
    return "Какой то отель"