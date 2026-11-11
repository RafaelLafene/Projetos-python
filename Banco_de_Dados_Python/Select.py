import sqlite3
conexao = sqlite3.connect('loja.db')
cursor = conexao.cursor()
sql = 'select * from tb_produto'
cursor.execute(sql)
registros = cursor.fetchall()
print(registros)
