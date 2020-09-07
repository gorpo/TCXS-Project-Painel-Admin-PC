#!/usr/bin/env python
# -*- coding: utf-8 -*-
#███╗   ███╗ █████╗ ███╗   ██╗██╗ ██████╗ ██████╗ ███╗   ███╗██╗ ██████╗
#████╗ ████║██╔══██╗████╗  ██║██║██╔════╝██╔═══██╗████╗ ████║██║██╔═══██╗
#██╔████╔██║███████║██╔██╗ ██║██║██║     ██║   ██║██╔████╔██║██║██║   ██║
#██║╚██╔╝██║██╔══██║██║╚██╗██║██║██║     ██║   ██║██║╚██╔╝██║██║██║   ██║
#██║ ╚═╝ ██║██║  ██║██║ ╚████║██║╚██████╗╚██████╔╝██║ ╚═╝ ██║██║╚██████╔╝
#╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝
#            @GorpoOrko | Manicomio TCXS Project | 2020
from main import *
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableView
from PyQt5 import QtSql
from PyQt5 import QtCore
import sqlite3



def funcoesHome(self):
    #eventos para limpar os campos, que buscam funçoes no arquivo main
    self.ui.input_nome_database_home.mousePressEvent = self.limpaNomedb
    self.ui.input_user_database_home.mousePressEvent = self.limpaUserdb
    self.ui.input_senha_database_home.mousePressEvent = self.limpaSenhadb
    self.ui.input_host_database_home.mousePressEvent = self.limpaHostdb
    self.ui.btn_database_home.clicked.connect(lambda: addDadosMysqlToDb(self))

def addDadosMysqlToDb(self):
    '''try:
        self.conexao = sqlite3.connect('database.db')
        self.cursor = self.conexao.cursor()
        self.cursor.execute("""DROP TABLE dados_mysql """)
        self.conexao.commit()
        self.conexao.close()
    except:
        pass'''
    self.conexao = sqlite3.connect('database.db')
    # self.conexao.row_factory = self.sqlite3.Row
    self.cursor = self.conexao.cursor()
    self.cursor.execute("""  CREATE TABLE IF NOT EXISTS dados_mysql  (id integer not null primary key autoincrement, nome_database varchar(5000), user_database varchar(5000), senha_database varchar(5000), host_database varchar(500));  """)
    self.nome_database = self.ui.input_nome_database_home.text()
    self.user_database = self.ui.input_user_database_home.text()
    self.senha_database = self.ui.input_senha_database_home.text()
    self.host_database = self.ui.input_host_database_home.text()
    self.cursor.execute(f""" INSERT INTO  dados_mysql ( nome_database, user_database, senha_database, host_database) VALUES ( '{self.nome_database}', '{self.user_database}', '{self.senha_database}', '{self.host_database}')""")
    self.conexao.commit()
    self.conexao.close()

