# Banco de dados projeto do Grupo3

import sqlite3

conex = sqlite3.connect('C:/Users/jaque/Projeto-Entra21/BD/BDprojeto.sqlite3')
cur = conex.cursor()

cur.execute(''' 
    DROP TABLE IF EXISTS CLIENTES; 
''')

cur.execute(''' 
    CREATE TABLE CLIENTES(
        CLIENTES_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        CLIENTES_NOME TEXT,
        CLIENTES_TELEFONE TEXT,
        CLIENTES_CPF TEXT,
        CLIENTES_LOGRADOURO TEXT,
        CLIENTES_BAIRRO TEXT,
        CLIENTES_NUMERO TEXT,
        CLIENTES_CEP TEXT,
        CLIENTES_COMPLEMENTO TEXT,
        CLIENTES_OBS TEXT,
        CLIENTES_CIDADE_ID INTEGER
    );
''')


cur.execute(''' 
    DROP TABLE IF EXISTS FORNECEDORES; 
''')

cur.execute(''' 
    CREATE TABLE FORNECEDORES(
        FORNECEDORES_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        FORNECEDORES_RAZAO_SOCIAL TEXT,
        FORNECEDORES_CPF_CNPJ TEXT,
        FORNECEDORES_CONTATO TEXT,
        FORNECEDORES_TELEFONE TEXT,
        FORNECEDORES_LOGRADOURO TEXT,
        FORNECEDORES_BAIRRO TEXT,
        FORNECEDORES_NUMERO TEXT,
        FORNECEDORES_CEP TEXT,
        FORNECEDORES_COMPLEMENTO TEXT,
        FORNECEDORES_OBS TEXT,
        FORNECEDORES_CIDADE_ID INTEGER
    );
''')

cur.execute(''' 
    DROP TABLE IF EXISTS CIDADES;
''')
cur.execute(''' 
    CREATE TABLE CIDADES (
        CIDADES_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        CIDADES_CIDADE TEXT NOT NULL,
        CIDADES_CEP TEXT NOT NULL
    );
''')

cur.execute(''' 
    DROP TABLE IF EXISTS SEGMENTO;     
''')

cur.execute(''' 
    CREATE TABLE SEGMENTO(
        SEGMENTO_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        SEGMENTO_NOME TEXT
    );
''')

cur.execute(''' 
    DROP TABLE IF EXISTS PRODUTOS; 
''')

cur.execute('''     
    CREATE TABLE PRODUTOS(
        PRODUTOS_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        PRODUTOS_NOME TEXT,
        PRODUTOS_DESCRICAO TEXT,
        PRODUTOS_VALOR_UNIT REAL,
        PRODUTOS_QTDE INTEGER,
        PRODUTOS_SEGMENTO_ID
    );
''')

cur.execute(''' 
    DROP TABLE IF EXISTS PEDIDOS; 
''')

cur.execute('''     
    CREATE TABLE PEDIDOS(
        PEDIDOS_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        PEDIDOS_CLIENTE_ID INTEGER,
        PEDIDOS_FORNECEDOR_ID INTEGER,
        PEDIDOS_DATA_PEDIDO DATE,
        PEDIDOS_PRAZO_ENTREGA DATE,
        PEDIDOS_OBS TEXT
    );
''')

cur.execute(''' 
    DROP TABLE IF EXISTS ITENSPED; 
''')

cur.execute('''     
    CREATE TABLE ITENSPED(
        ITENSPED_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        ITENSPED_PRODUTO_ID INTEGER,
        ITENSPED_QTDE INTEGER
    );
''')


conex.commit()
cur.close


