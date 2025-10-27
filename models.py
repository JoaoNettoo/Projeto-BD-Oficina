from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DECIMAL, DateTime, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# Tabelas

class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    telefone = Column(String(20))
    email = Column(String(100))
    veiculos = relationship("Veiculo", back_populates="cliente")


class Veiculo(Base):
    __tablename__ = 'veiculos'
    id = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey('clientes.id'))
    placa = Column(String(10))
    modelo = Column(String(50))
    ano = Column(Integer)
    cliente = relationship("Cliente", back_populates="veiculos")
    ordens_servico = relationship("OrdemServico", back_populates="veiculo")


class OrdemServico(Base):
    __tablename__ = 'ordens_servico'
    id = Column(Integer, primary_key=True)
    veiculo_id = Column(Integer, ForeignKey('veiculos.id'))
    data_abertura = Column(DateTime)
    status = Column(String(20))
    valor_total = Column(DECIMAL(10,2))
    veiculo = relationship("Veiculo", back_populates="ordens_servico")
    itens = relationship("ItemOS", back_populates="ordem_servico")


class Servico(Base):
    __tablename__ = 'servicos'
    id = Column(Integer, primary_key=True)
    descricao = Column(String(100))
    preco = Column(DECIMAL(10,2))
    itens = relationship("ItemOS", back_populates="servico")


class ItemOS(Base):
    __tablename__ = 'itens_os'
    id = Column(Integer, primary_key=True)
    os_id = Column(Integer, ForeignKey('ordens_servico.id'))
    servico_id = Column(Integer, ForeignKey('servicos.id'))
    ordem_servico = relationship("OrdemServico", back_populates="itens")
    servico = relationship("Servico", back_populates="itens")


class Mecanico(Base):
    __tablename__ = 'mecanicos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    telefone = Column(String(20))
    especialidades = relationship("Especialidade", secondary="mecanico_especialidade", back_populates="mecanicos")


class Especialidade(Base):
    __tablename__ = 'especialidades'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    mecanicos = relationship("Mecanico", secondary="mecanico_especialidade", back_populates="especialidades")


mecanico_especialidade = Table(
    'mecanico_especialidade', Base.metadata,
    Column('mecanico_id', Integer, ForeignKey('mecanicos.id')),
    Column('especialidade_id', Integer, ForeignKey('especialidades.id'))
)


class Peca(Base):
    __tablename__ = 'pecas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    preco = Column(DECIMAL(10,2))
    estoque = Column(Integer)


class Fornecedor(Base):
    __tablename__ = 'fornecedores'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    telefone = Column(String(20))

class LogCliente(Base):
    __tablename__ = 'logs_clientes'
    id = Column(Integer, primary_key=True)
    cliente_id = Column(Integer)
    nome = Column(String(100))
    deletado_em = Column(DateTime)
