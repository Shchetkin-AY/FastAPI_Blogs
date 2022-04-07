from blog.routers import blog, user, authenification
from fastapi import FastAPI
from blog import models
from blog.database import engine


app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authenification.router)