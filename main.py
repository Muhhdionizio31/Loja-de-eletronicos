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
def exibir_cadastro(request: Request, db: Session = Depends(get_db)):
    categorias = db.query(Eletronico).all()
    return templates.TemplateResponse(
        request,
        "cadastrar.html",
        {"request": request, "categorias": categorias })
@app.post("/eletronico")
def criar_eletronico(
    nome: str = Form(...),
    db: Session = Depends(get_db)
):
    novo_eletronico = Eletronico(nome=nome)
    db.add(novo_eletronico)
    db.commit()
    return RedirectResponse(url="/eletronico/cadastro", status_code=303)

@app.post("/produto/salvar")
def salvar_produto(
    nome: str = Form(...),
    descricao: str = Form(...),
    eletronico_id: int = Form(...),
    db: Session = Depends(get_db)
):

    novo_produto = Produto(
        nome=nome, 
        descricao=descricao, 
        eletronico_id=eletronico_id
    )
    
    db.add(novo_produto)
    db.commit()
    return RedirectResponse(url="/produto_criado", status_code=303)