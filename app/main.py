from fastapi import FastAPI
from . import models, database
from .routers import users, posts, auth

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="FastAPI RESTful API")

app.include_router(users.router)
app.include_router(posts.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "FastAPI running successfully"}
