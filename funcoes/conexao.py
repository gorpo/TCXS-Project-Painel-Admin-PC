#!/usr/bin/env python
# -*- coding: utf-8 -*-
#███╗   ███╗ █████╗ ███╗   ██╗██╗ ██████╗ ██████╗ ███╗   ███╗██╗ ██████╗
#████╗ ████║██╔══██╗████╗  ██║██║██╔════╝██╔═══██╗████╗ ████║██║██╔═══██╗
#██╔████╔██║███████║██╔██╗ ██║██║██║     ██║   ██║██╔████╔██║██║██║   ██║
#██║╚██╔╝██║██╔══██║██║╚██╗██║██║██║     ██║   ██║██║╚██╔╝██║██║██║   ██║
#██║ ╚═╝ ██║██║  ██║██║ ╚████║██║╚██████╗╚██████╔╝██║ ╚═╝ ██║██║╚██████╔╝
#╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝
#            @GorpoOrko | Manicomio TCXS Project | 2020


from PyQt5 import QtSql
import sqlite3


#conexao sqlite para uso do programa
conexao_user = sqlite3.connect('database.db')
cursor_user = conexao_user.cursor()
cursor_user.execute(' SELECT * FROM dados_mysql; ')
tabela_user = cursor_user.fetchall()
databaseMysql_user = tabela_user[0][1]
usuarioMysql_user = tabela_user[0][2]
senhaMysql_user = tabela_user[0][3]
hostMysql_user = tabela_user[0][4]
conexao_user.close()


#conexao mysql Externa
db_user = QtSql.QSqlDatabase.addDatabase('QMYSQL')
db_user.setHostName(hostMysql_user)
db_user.setDatabaseName(databaseMysql_user)
db_user.setUserName(usuarioMysql_user)
db_user.setPassword(senhaMysql_user)
ok = db_user.open()
if not ok: print(db_user.lastError().text())
# else: print("connected")

fechar_conexao  = db_user.close()