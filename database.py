import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='######',
    database='esquema'

)
#CRUD
#CREATE
# produto = "notebook"
# clientes = "guilherme"
# comando = f'INSERT INTO vendas (clientes, produto) VALUES ("{clientes}", "{produto}")'

# READ



# comando = f'SELECT * FROM VENDAS;'

# resultado = cursor.fetchall()
# print(resultado)


#update
# nome = "aquele_cara"
# pro = "nootbook"
# comando = f'UPDATE vendas SET clientes = "aquele_cara" WHERE idvendas = 127;'
# cursor = conexao.cursor()

#delete


nome = "aquele cara"
id= 127
comando = f'DELETE FROM vendas WHERE idvendas = {id}; '
cursor = conexao.cursor()
cursor.execute(comando)
conexao.commit()
conexao.close()


