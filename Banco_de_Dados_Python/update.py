import sqlite3
conexao = sqlite3.connect('loja.db')
cursor = conexao.cursor()
novo_codigo= input('Digite o codigo do produto que iremos alterar: ')
nova_descricao= input("Digite a nova descrição:")
nova_categoria= input("Digite a nova categoria:")
nova_quantidade= input("Digite a nova quantidade:")
novo_preco= input("Digite o novo preço:")
sql = '''UPDATE tb_produto
         SET descricao = ?,
             categoria = ?,
             quantidade = ?,
             preco = ?
         WHERE codigo = ?'''
cursor.execute(sql,(nova_descricao,nova_categoria,nova_quantidade,novo_preco,novo_codigo))
conexao.commit()
cursor.close()
conexao.close()
print('Produto atualizado com sucesso!')