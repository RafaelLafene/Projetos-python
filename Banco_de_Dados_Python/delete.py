import sqlite3
conexao = sqlite3.connect('loja.db')
cursor = conexao.cursor()
novo_codigo=input('Digite o codigo do loja para excluir:')
sql = '''DELETE FROM tb_produto
         WHERE codigo = ?'''

cursor.execute(sql, (novo_codigo,))

conexao.commit()
cursor.close()
conexao.close()
print("Codigo excluido com sucesso!")