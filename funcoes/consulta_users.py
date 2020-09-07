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
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt5.QtWidgets import QTableView, QApplication, QMessageBox
import sqlite3
from datetime import datetime
from funcoes import conexao


def funcoesConsultaUsers(self):
    #eventos para limpar os campos, que buscam funçoes no arquivo main
    self.ui.input_pesquisa_acessos_usuarios.mousePressEvent = self.limpaPesquisaAcessoUsers
    self.ui.btn_pesquisa_acessos_usuarios.clicked.connect(lambda: consultaUser(self))


def consultaUser(self):
    #conecta a db local para pegar o login mysql
    self.conexao_user = sqlite3.connect('database.db')
    self.cursor_user = self.conexao_user.cursor()
    self.cursor_user.execute(' SELECT * FROM dados_mysql; ')
    self.tabela_user = self.cursor_user.fetchall()
    self.databaseMysql_user = self.tabela_user[0][1]
    self.usuarioMysql_user = self.tabela_user[0][2]
    self.senhaMysql_user = self.tabela_user[0][3]
    self.hostMysql_user = self.tabela_user[0][4]
    self.conexao_user.close()
    #login mysql
    self.db_user = QtSql.QSqlDatabase.addDatabase('QMYSQL')
    self.db_user.setHostName(self.hostMysql_user)
    self.db_user.setDatabaseName(self.databaseMysql_user)
    self.db_user.setUserName(self.usuarioMysql_user)
    self.db_user.setPassword(self.senhaMysql_user)
    self.ok = self.db_user.open()
    if not self.ok: print(self.db_user.lastError().text())
    # else: print("connected")
    self.query_user = QSqlQuery(conexao.db_user)
    self.model_user = QtSql.QSqlTableModel()
    #seleciona a tabela
    self.tabela_pesquisar_usuario = f'user_{self.ui.input_pesquisa_acessos_usuarios.text()}'
    self.model_user.setTable(self.tabela_pesquisar_usuario)
    self.model_user.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
    self.model_user.select()
    #popula as tabelas
    self.model_user.setHeaderData(0, QtCore.Qt.Horizontal, "Usuario")
    self.model_user.setHeaderData(1, QtCore.Qt.Horizontal, "Senha")
    self.model_user.setHeaderData(2, QtCore.Qt.Horizontal, "IP")
    self.model_user.setHeaderData(3, QtCore.Qt.Horizontal, "Cadastrado")
    #tabela de dados
    self.ui.tabela_pesquisa_acessos_usuarios.setModel(self.model_user)
    self.i_user = self.model_user.rowCount()
    self.db_user.close()



