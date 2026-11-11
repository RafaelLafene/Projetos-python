import sqlite3
conexao = sqlite3.connect('loja.db')
cursor = conexao.cursor()
sql= '''CREATE TABLE tb_produto(
      codigo INTEGER PRIMARY KEY,
      descricao TEXT NOT NULL,
      categoria TEXT NOT NULL,
      quantidade INTEGER NOT NULL,
      preco REAL NOT NULL)'''
cursor.execute(sql)
cursor.close()
conexao.close()
print('Tabela cadastrada com sucesso')