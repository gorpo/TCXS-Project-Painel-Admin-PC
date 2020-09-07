"""from PyQt5.QtSql import QSqlDatabase
print(list(map(str, QSqlDatabase.drivers())))"""

import sqlite3

conexao_user = sqlite3.connect('database.db')
#conexao_user.row_factory = sqlite3.Row
cursor_user = conexao_user.cursor()
cursor_user.execute(""" SELECT * FROM dados_mysql; """)
tabela_user = cursor_user.fetchall()
databaseMysql_user = tabela_user[0][1]
usuarioMysql_user = tabela_user[0][2]
senhaMysql_user = tabela_user[0][3]
hostMysql_user = tabela_user[0][4]
#conexao.commit()
conexao_user.close()
print(databaseMysql_user)
print(usuarioMysql_user)
print(senhaMysql_user)
print(hostMysql_user)