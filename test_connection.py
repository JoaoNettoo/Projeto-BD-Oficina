from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:joaoneto@localhost/oficina_db")

try:
    with engine.connect() as connection:
        print("Conexão com o MySQL bem-sucedida!")
except Exception as e:
    print("Erro ao conectar:", e)
