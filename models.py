# models é o arquivo onde fica as classes (tabelas)
# instalar = pip install sqlalchemy
# instalar = pip install alembic
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

#Tabelas Curso e aluno (1:N)
class Eletronico(Base):
    __tablename__ = "eletronicos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)

    produtos = relationship("Produto", back_populates="eletronicos")

    def __repr__(self):
        return f"Eletronico = id: {self.id} - nome: {self.nome}"

class Produto(Base):
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(String(150))

    eletronico_id = Column(Integer, ForeignKey("eletronicos.id"))

    eletronicos = relationship("Eletronico", back_populates="produtos")

    def __repr__(self):
        return f"Produto = id: {self.id} - nome: {self.nome} - Descrição: {self.descricao}"