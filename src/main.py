from fastapi import Depends, FastAPI, HTTPException
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from .routers import users, orders

from . import crud, models, schemas
from .database import SessionLocal, engine, get_db
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(orders.router)

templates = Jinja2Templates(directory="templates")

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        context={"request": request, "title": "Home Page", "id":"123"})
