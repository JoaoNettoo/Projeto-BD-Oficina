# 🛠️ Projeto Oficina

Gerenciamento de oficina mecânica, desenvolvido em **Python** com **SQLAlchemy** e banco de dados **MySQL**.  
Inclui mapeamento ORM, **Stored Procedures** e **Triggers**.

---

## 📂 Estrutura do projeto

projeto_oficina/
│
├── models.py # Classes SQLAlchemy mapeando as tabelas
├── insert_test.py # Teste de inserção de dados
├── test_connection.py # Teste de conexão com o MySQL
├── README.md
└── sql/
├── tables.sql # Script de criação das tabelas
├── procedures.sql # Stored Procedures
└── triggers.sql # Triggers do banco

---

## 🛠 Tecnologias utilizadas

- 🐍 Python 3.x  
- 🗄️ MySQL  
- 🛠 SQLAlchemy  
- 🖥️ MySQL Workbench  

---

## ⚡ Funcionalidades

- Criação de **10 tabelas** (clientes, veículos, ordens de serviço, serviços, peças, mecânicos, especialidades, fornecedores e tabelas de relacionamento)  
- **Mapeamento ORM** com SQLAlchemy  
- **4 Stored Procedures**:
  - Inserir ordem de serviço  
  - Atualizar valor de OS  
  - Listar serviços por veículo  
  - Remover cliente (com exclusão de veículos e ordens relacionadas)  
- **3 Triggers**:
  - Atualizar estoque de peças ao adicionar item de OS  
  - Atualizar data de modificação de OS  
  - Registrar logs de exclusão de cliente  

---

## 🚀 Como rodar

1. Clonar o repositório:

```bash
git clone https://github.com/JoaoNettoo/Projeto-BD-Oficina
Criar e configurar o banco de dados oficina_db no MySQL

Instalar dependências:

bash
Copiar código
pip install sqlalchemy pymysql
Testar a conexão:

bash
Copiar código
python test_connection.py
Inserir dados de teste:

bash
Copiar código
python insert_test.py
📌 Observações
Antes de criar triggers que dependem de tabelas adicionais (ex.: logs_clientes), certifique-se de criar a tabela primeiro

Todas as procedures e triggers foram testadas no MySQL Workbench

Para ver resultados, sempre use:

sql
Copiar código
SELECT * FROM tabela;
CALL procedure();
yaml
Copiar código

---

Se você quiser, eu posso fazer **uma versão ainda mais visual**, adicionando **emojis nas listas, blocos de código coloridos e instruções destacadas**, pra deixar o README com cara de projeto profissional.  

Quer que eu faça isso?






