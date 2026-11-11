import sqlite3
conexao = sqlite3.connect('loja.db')
cursor = conexao.cursor()
v_codigo= input('Digite o codigo : ')
v_descricao= input("Digite a descrição:")
v_categoria= input("Digite a categoria:")
v_quantidade= input("Digite a quantidade:")
v_preco= input("Digite o preço:")
sql = 'INSERT INTO tb_produto(codigo,descricao,categoria,quantidade,preco) VALUES (?,?,?,?,?)'
cursor.execute(sql,(v_codigo,v_descricao,v_categoria,v_quantidade,v_preco))
conexao.commit()
cursor.close()
conexao.close()
print("Valores adicionados a tabela!")