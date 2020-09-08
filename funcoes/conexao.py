#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ███╗   ███╗ █████╗ ███╗   ██╗██╗ ██████╗ ██████╗ ███╗   ███╗██╗ ██████╗
# ████╗ ████║██╔══██╗████╗  ██║██║██╔════╝██╔═══██╗████╗ ████║██║██╔═══██╗
# ██╔████╔██║███████║██╔██╗ ██║██║██║     ██║   ██║██╔████╔██║██║██║   ██║
# ██║╚██╔╝██║██╔══██║██║╚██╗██║██║██║     ██║   ██║██║╚██╔╝██║██║██║   ██║
# ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║╚██████╗╚██████╔╝██║ ╚═╝ ██║██║╚██████╔╝
# ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝
#            @GorpoOrko | Manicomio TCXS Project | 2020


from PyQt5 import QtSql  # pip install PyQT5==5.12
import sqlite3

# conexao sqlite para uso do programa
conexao_user = sqlite3.connect('database.db')
cursor_user = conexao_user.cursor()
cursor_user.execute(' SELECT * FROM dados_mysql; ')
tabela_user = cursor_user.fetchall()
databaseMysql_user = tabela_user[0][1]
usuarioMysql_user = tabela_user[0][2]
senhaMysql_user = tabela_user[0][3]
hostMysql_user = tabela_user[0][4]
conexao_user.close()

# conexao mysql Externa
"""Pra uso do Drive QMYSQL é necessário que o arquivo libmysql.dll esteja junto ao projeto.
 O Drive QMysql do pacote PyQT5 existe somente nas versoes:   
pip install PyQT5==5.12
pip install pyqtwebengine==5.12

[COMANDO PARA VERIFICAR SE O DRIVE EXISTE]
from PyQt5.QtSql import QSqlDatabase
print(list(map(str, QSqlDatabase.drivers())))
"""
db_mysql = QtSql.QSqlDatabase.addDatabase('QMYSQL')
db_mysql.setHostName(hostMysql_user)
db_mysql.setDatabaseName(databaseMysql_user)
db_mysql.setUserName(usuarioMysql_user)
db_mysql.setPassword(senhaMysql_user)
ok = db_mysql.open()
if not ok: print(db_mysql.lastError().text())
# else: print("connected")
db_mysql.close()
