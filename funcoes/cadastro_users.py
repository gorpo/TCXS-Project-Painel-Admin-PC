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



def funcoesCadastroUsers(self):
    #eventos para limpar os campos, que buscam funçoes no arquivo main
    self.ui.input_nome_user.mousePressEvent = self.limpaNomeCadastro
    self.ui.input_username_user.mousePressEvent = self.limpaUserCadastro
    self.ui.input_senha_user.mousePressEvent = self.limpaSenhaCadastro
    #self.ui.btn_database_home.clicked.connect(lambda: addDadosMysqlToDbUser(self))
    addDadosMysqlToDbUser(self)





def addDadosMysqlToDbUser(self):
    self.conexao_user = sqlite3.connect('database.db')
    #self.conexao_user.row_factory = sqlite3.Row
    self.cursor_user = self.conexao_user.cursor()
    self.cursor_user.execute(""" SELECT * FROM dados_mysql; """)
    self.tabela_user = self.cursor_user.fetchall()
    self.databaseMysql_user = self.tabela_user[0][1]
    self.usuarioMysql_user = self.tabela_user[0][2]
    self.senhaMysql_user = self.tabela_user[0][3]
    self.hostMysql_user = self.tabela_user[0][4]
    #self.conexao.commit()
    self.conexao_user.close()
    bancoDadosUser(self)

def bancoDadosUser(self):
    self.db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
    self.db.setHostName(self.hostMysql_user)
    self.db.setDatabaseName(self.databaseMysql_user)
    self.db.setUserName(self.usuarioMysql_user)
    self.db.setPassword(self.senhaMysql_user)
    self.ok = self.db.open()
    if not self.ok: print(self.db.lastError().text())
    # else: print("connected")
    self.query = QSqlQuery(self.db)
    """#executar uma query na tabela caso preciso
    #self.b = query.exec_('SELECT * FROM playstation_users')"""
    self.model = QtSql.QSqlTableModel()
    self.model.setTable('playstation_users')
    """#sistema para uso com sqlite
    #self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    #self.db.setDatabaseName('database.db')
    #self.model = QtSql.QSqlTableModel()
    #self.model.setTable('dados_mysql')"""
    self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
    self.model.select()
    self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Id")
    self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Username")
    self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Senha")
    self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Nome")
    self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Cadastro")
    self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Nivel")
    #tabela de dados
    self.ui.tabela_dados_usuarios.setModel(self.model)
    self.i = self.model.rowCount()
    # botoes das açoes
    self.ui.btn_adiciona_user.clicked.connect(lambda: addToDb(self))
    self.ui.btn_atualiza_user.clicked.connect(lambda: updaterow(self))
    self.ui.btn_deleta_user.clicked.connect(lambda:delrow(self))



def addToDb(self):
    #print(self.i)
    self.hoje = datetime.now()
    self.data_formatada = self.hoje.strftime('%Y-%m-%d %H:%M:%S')
    #insere os dados na database
    self.model.insertRows(self.i,1)
    self.model.setData(self.model.index(self.i,1),self.ui.input_username_user.text())
    self.model.setData(self.model.index(self.i, 2), self.ui.input_senha_user.text())
    self.model.setData(self.model.index(self.i,3), self.ui.input_nome_user.text())
    self.model.setData(self.model.index(self.i,4), self.data_formatada)
    self.model.setData(self.model.index(self.i, 5), 'user')
    self.model.submitAll()
    self.i += 1


def delrow(self):
    if self.ui.tabela_dados_usuarios.currentIndex().row() > -1:
        self.model.removeRow(self.ui.tabela_dados_usuarios.currentIndex().row())
        self.i -= 1
        self.model.select()
    else:
        QMessageBox.question(self,'Mensagem', "Selecione uma linha para deletar, clique sobre o numero a esquerda na tabela correspondente a linha.", QMessageBox.Ok)
        self.show()

def updaterow(self):
    self.hoje = datetime.now()
    self.data_formatada = self.hoje.strftime('%Y-%m-%d %H:%M:%S')
    if self.ui.tabela_dados_usuarios.currentIndex().row() > -1:
        record = self.model.record(self.ui.tabela_dados_usuarios.currentIndex().row())
        record.setValue("usuario",self.ui.input_username_user.text())
        record.setValue("senha",self.ui.input_senha_user.text())
        record.setValue("nome", self.ui.input_nome_user.text())
        record.setValue("cadastro", self.data_formatada)
        record.setValue("nivel", 'user')
        self.model.setRecord(self.ui.tabela_dados_usuarios.currentIndex().row(), record)
    else:
        QMessageBox.question(self,'Mensagem', "Selecione uma linha para atualizar, clique sobre o numero a esquerda na tabela correspondente a linha.", QMessageBox.Ok)
        self.show()