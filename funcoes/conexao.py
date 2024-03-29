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
import pymysql.cursors
import ftplib

# conexao sqlite para uso do programa
conexao_user = sqlite3.connect('database.db')
cursor_user = conexao_user.cursor()
try:
    cursor_user.execute("""  CREATE TABLE IF NOT EXISTS dados_mysql  (id integer not null primary key autoincrement, 
            nome_database varchar(5000), user_database varchar(5000), senha_database varchar(5000), host_database 
            varchar(500), endereco_ftp varchar(500), user_ftp varchar(500), senha_ftp varchar(500));  """)
    conexao_user.commit()
    cursor_user.execute(' SELECT * FROM dados_mysql; ')
    tabela_user = cursor_user.fetchall()
    databaseMysql_user = tabela_user[0][1]
    usuarioMysql_user = tabela_user[0][2]
    senhaMysql_user = tabela_user[0][3]
    hostMysql_user = tabela_user[0][4]
    enderecoFtp_user = tabela_user[0][5]
    usuarioFtp_user = tabela_user[0][6]
    senhaFtp_user = tabela_user[0][7]
    conexao_user.close()
except:
    pass


#CONEXAO PYMYSQL PARA BACKUP DA DATABASE ONLINE
try:
    conexao_pymysql = pymysql.connect(host=hostMysql_user, user=usuarioMysql_user, password=senhaMysql_user, db=databaseMysql_user, charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
except Exception as e:
    print(f'conexao mysql {e}')
    pass


#CONEXAO FTP ---------------------------
try:
    ftp = ftplib.FTP(host=enderecoFtp_user, user=usuarioFtp_user, passwd=senhaFtp_user)
    ftp.encoding = "utf-8"
    #print(ftp.getwelcome())

except:
    pass



# conexao mysql Externa
"""Pra uso do Drive QMYSQL é necessário que o arquivo libmysql.dll esteja junto ao projeto.
 O Drive QMysql do pacote PyQT5 existe somente nas versoes:   
pip install PyQT5==5.12
pip install pyqtwebengine==5.12

[COMANDO PARA VERIFICAR SE O DRIVE EXISTE]
from PyQt5.QtSql import QSqlDatabase
print(list(map(str, QSqlDatabase.drivers())))
"""
try:
    db_mysql = QtSql.QSqlDatabase.addDatabase('QMYSQL')
    db_mysql.setHostName(hostMysql_user)
    db_mysql.setDatabaseName(databaseMysql_user)
    db_mysql.setUserName(usuarioMysql_user)
    db_mysql.setPassword(senhaMysql_user)
    ok = db_mysql.open()
    if not ok:
        retorno_conexao_mysql = db_mysql.lastError().text()
    else:
        retorno_conexao_mysql = 'Conectado com sucesso ao banco de dados Mysql'
    db_mysql.close()
except:
    pass


