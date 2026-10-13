from models import Cliente, Animal, Veterinario, Consulta, Base
from config import engine, Session
from datetime import datetime

Base.metadata.create_all(engine)

session = Session()

cliente = Cliente(nome="Gregory Paulo", telefone="12345-6789")
session.add(cliente)
session.commit()

animal = Animal(nome="Cody", especie="Cachorro", idade=5, dono=cliente)
session.add(animal)
session.commit()

veterinario = Veterinario(nome="Dra. Sabrina", especialidade="Veterinária Geral")
session.add(veterinario)
session.commit()

consulta = Consulta(data=datetime.now(), animal=animal, veterinario=veterinario)
session.add(consulta)
session.commit()

consultas = session.query(Consulta).all()
for consulta in consultas:
    print(f"Animal: {consulta.animal.nome}, Veterinário: {consulta.veterinario.nome}, Data: {consulta.data}")

session.close()
