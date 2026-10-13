from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    telefone = Column(String)

    animais = relationship('Animal', back_populates='dono')

class Animal(Base):
    __tablename__ = 'animais'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    especie = Column(String)
    idade = Column(Integer)

    dono_id = Column(Integer, ForeignKey('clientes.id'))
    dono = relationship('Cliente', back_populates='animais')


    consultas = relationship('Consulta', back_populates='animal')

class Veterinario(Base):
    __tablename__ = 'veterinarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    especialidade = Column(String)


    consultas = relationship('Consulta', back_populates='veterinario')

class Consulta(Base):
    __tablename__ = 'consultas'
    id = Column(Integer, primary_key=True)
    data = Column(DateTime)

    animal_id = Column(Integer, ForeignKey('animais.id'))
    animal = relationship('Animal', back_populates='consultas')

    veterinario_id = Column(Integer, ForeignKey('veterinarios.id'))
    veterinario = relationship('Veterinario', back_populates='consultas')
