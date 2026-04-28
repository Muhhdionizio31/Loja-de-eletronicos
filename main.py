from fastapi import FastAPI, Depends, Request, Form, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import get_db
from models import Produto, Eletronico

app = FastAPI(title="Lojinha")

templates = Jinja2Templates(directory="templates")

@app.get("/")
def index(request:Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {"request":request}
    )

