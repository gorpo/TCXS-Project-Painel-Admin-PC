#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ███╗   ███╗ █████╗ ███╗   ██╗██╗ ██████╗ ██████╗ ███╗   ███╗██╗ ██████╗
# ████╗ ████║██╔══██╗████╗  ██║██║██╔════╝██╔═══██╗████╗ ████║██║██╔═══██╗
# ██╔████╔██║███████║██╔██╗ ██║██║██║     ██║   ██║██╔████╔██║██║██║   ██║
# ██║╚██╔╝██║██╔══██║██║╚██╗██║██║██║     ██║   ██║██║╚██╔╝██║██║██║   ██║
# ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║╚██████╗╚██████╔╝██║ ╚═╝ ██║██║╚██████╔╝
# ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝
#            @GorpoOrko | Manicomio TCXS Project | 2020


import sqlite3



def criaDbLocal():
    conexao = sqlite3.connect('database.db')
    # self.conexao.row_factory = self.sqlite3.Row
    cursor = conexao.cursor()
    cursor.execute("""  CREATE TABLE IF NOT EXISTS dados_mysql  (id integer not null primary key autoincrement, 
        nome_database varchar(5000), user_database varchar(5000), senha_database varchar(5000), host_database varchar(
        500), endereco_ftp varchar(500), user_ftp varchar(500), senha_ftp varchar(500));  """)
    conexao.commit()
    cursor.execute(f""" INSERT INTO  dados_mysql ( nome_database, user_database, senha_database, host_database, 
    endereco_ftp, user_ftp, senha_ftp) VALUES ('nome database','user database','senha database','host database',
'endereço ftp','user ftp','senha ftp' )""")
    conexao.commit()
    conexao.close()