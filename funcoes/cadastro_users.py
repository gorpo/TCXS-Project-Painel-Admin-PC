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


def funcoesCadastroUsers(self):
    #eventos para limpar os campos, que buscam funçoes no arquivo main
    self.ui.input_nome_user.mousePressEvent = self.limpaNomeCadastro
    self.ui.input_username_user.mousePressEvent = self.limpaUserCadastro
    self.ui.input_senha_user.mousePressEvent = self.limpaSenhaCadastro
    self.ui.btn_adiciona_user.clicked.connect(lambda: addToDbUser(self))
    self.ui.btn_atualiza_user.clicked.connect(lambda: updaterowUser(self))
    self.ui.btn_deleta_user.clicked.connect(lambda: delrowUser(self))




def bancoDadosUsers(self):
    self.i_user = 0

    """self.db_user = QtSql.QSqlDatabase.addDatabase('QMYSQL')
    self.db_user.setHostName(conexao.hostMysql_user)
    self.db_user.setDatabaseName(conexao.databaseMysql_user)
    self.db_user.setUserName(conexao.usuarioMysql_user)
    self.db_user.setPassword(conexao.senhaMysql_user)
    self.ok = self.db_user.open()
    if not self.ok: print(self.db_user.lastError().text())
    # else: print("connected")"""


    self.query_user = QSqlQuery(conexao.db_user)
    """#executar uma query na tabela caso preciso
    #self.b = query.exec_('SELECT * FROM playstation_users')"""
    self.model_user = QtSql.QSqlTableModel()
    self.model_user.setTable('playstation_users')
    """#sistema para uso com sqlite
    #self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    #self.db.setDatabaseName('database.db')
    #self.model = QtSql.QSqlTableModel()
    #self.model.setTable('dados_mysql')"""
    self.model_user.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
    self.model_user.select()
    self.model_user.setHeaderData(0, QtCore.Qt.Horizontal, "Id")
    self.model_user.setHeaderData(1, QtCore.Qt.Horizontal, "Usuario")
    self.model_user.setHeaderData(2, QtCore.Qt.Horizontal, "Senha")
    self.model_user.setHeaderData(3, QtCore.Qt.Horizontal, "Nome")
    self.model_user.setHeaderData(4, QtCore.Qt.Horizontal, "Cadastro")
    self.model_user.setHeaderData(5, QtCore.Qt.Horizontal, "Nivel")
    #tabela de dados
    self.ui.tabela_dados_usuarios.setModel(self.model_user)
    self.i_user = self.model_user.rowCount()
    print(self.i_user)
    # botoes das açoes
    #self.ui.btn_adiciona_user.clicked.connect(lambda: addToDbUser(self))
    #self.ui.btn_atualiza_user.clicked.connect(lambda: updaterowUser(self))
    #self.ui.btn_deleta_user.clicked.connect(lambda: delrowUser(self))





def addToDbUser(self):
    bancoDadosUsers(self)
    #print(self.i)
    self.hoje_user = datetime.now()
    self.data_formatada_user = self.hoje_user.strftime('%Y-%m-%d %H:%M:%S')
    #insere os dados na database
    self.model_user.insertRows(self.i_user, 1)
    self.model_user.setData(self.model_user.index(self.i_user, 1), self.ui.input_username_user.text())
    self.model_user.setData(self.model_user.index(self.i_user, 2), self.ui.input_senha_user.text())
    self.model_user.setData(self.model_user.index(self.i_user, 3), self.ui.input_nome_user.text())
    self.model_user.setData(self.model_user.index(self.i_user, 4), self.data_formatada_user)
    self.model_user.setData(self.model_user.index(self.i_user, 5), 'user')
    self.model_user.submitAll()
    self.i_user += 1




def delrowUser(self):
    if self.ui.tabela_dados_usuarios.currentIndex().row() > -1:
        self.model_user.removeRow(self.ui.tabela_dados_usuarios.currentIndex().row())
        self.i_user -= 1
        self.model_user.select()
    else:
        QMessageBox.question(self,'Mensagem', "Selecione uma linha para deletar, clique sobre o numero a esquerda na tabela correspondente a linha.", QMessageBox.Ok)
        self.show()

def updaterowUser(self):
    self.hoje_user = datetime.now()
    self.data_formatada_user = self.hoje_user.strftime('%Y-%m-%d %H:%M:%S')
    if self.ui.tabela_dados_usuarios.currentIndex().row() > -1:
        record = self.model_user.record(self.ui.tabela_dados_usuarios.currentIndex().row())
        record.setValue("usuario",self.ui.input_username_user.text())
        record.setValue("senha",self.ui.input_senha_user.text())
        record.setValue("nome", self.ui.input_nome_user.text())
        record.setValue("cadastro", self.data_formatada_user)
        record.setValue("nivel", 'user')
        self.model_user.setRecord(self.ui.tabela_dados_usuarios.currentIndex().row(), record)
    else:
        QMessageBox.question(self,'Mensagem', "Selecione uma linha para atualizar, clique sobre o numero a esquerda na tabela correspondente a linha.", QMessageBox.Ok)
        self.show()