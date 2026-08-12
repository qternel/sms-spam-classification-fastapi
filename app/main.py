from fastapi import FastAPI
from routes import classify

app = FastAPI()
app.include_router(classify.router)
