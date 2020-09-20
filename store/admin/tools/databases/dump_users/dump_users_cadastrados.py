import pymysql.cursors

# Connect to the database
conexao = pymysql.connect(host='localhost',user='root',password='',db='tcxs_store',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
cursor = conexao.cursor()



doc = open('dump_users.txt','r', encoding='utf8', errors='ignore').readlines()

for dado in doc:
    dado = dado.split(',')
    id = dado[0].replace('(','')
    usuario = dado[1].replace("'","")
    senha = dado[2].replace("'","")
    nome = dado[3].replace("'","")
    data = dado[4].replace("'","").replace(')','').replace(';','')
    print(id, usuario, senha, nome, data)

    cursor.execute(f"""INSERT INTO playstation_users (usuario, senha, nome, cadastro, nivel) VALUES ('{usuario}', '{senha}','{nome}','{data}', 'user')""")
    conexao.commit()









