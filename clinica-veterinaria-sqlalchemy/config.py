from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'sqlite:///clinica_veterinaria.db'

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
