from fastapi import FastAPI
from .routers import book
from .database import Base, engine


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(book.router)

@app.get("/")
def root():
    return {"message": "Hello FastAPI"}
