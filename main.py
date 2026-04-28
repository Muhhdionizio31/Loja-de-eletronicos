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

@app.get("/eletronico/cadastro")
def exibir_cadastro(request:Request):
    return templates.TemplateResponse(
        request,
        "cadastrar.html",
        {"request":request}
    )

@app.post("/eletronico")
def criar_eletronico(
    nome: str = Form(...),
    db: Session = Depends(get_db)
):
    novo_eletronico = Eletronico(nome=nome)
    db.add(novo_eletronico)
    db.commit()
    return RedirectResponse(url="/", status_code=303)