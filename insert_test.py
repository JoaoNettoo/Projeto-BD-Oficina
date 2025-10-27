from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Cliente, Veiculo
from datetime import datetime

# conexão com o banco
engine = create_engine("mysql+pymysql://root:joaoneto@localhost/oficina_db")
Session = sessionmaker(bind=engine)
session = Session()

# cria um cliente
novo_cliente = Cliente(nome="Carlos Silva", telefone="11999999999", email="carlos@email.com")
session.add(novo_cliente)
session.commit()

# cria um veículo a esse cliente
novo_veiculo = Veiculo(cliente_id=novo_cliente.id, placa="ABC1234", modelo="Fiat Uno", ano=2012)
session.add(novo_veiculo)
session.commit()

print("Dados inseridos com sucesso!")
