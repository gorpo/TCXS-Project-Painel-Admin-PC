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



def funcoesCadastroUsers(self):
    #eventos para limpar os campos, que buscam funçoes no arquivo main
    self.ui.input_nome_user.mousePressEvent = self.limpaNomeCadastro
    self.ui.input_username_user.mousePressEvent = self.limpaUserCadastro
    self.ui.input_senha_user.mousePressEvent = self.limpaSenhaCadastro
    #self.ui.btn_database_home.clicked.connect(lambda: addDadosMysqlToDb(self))
    bancoDados(self)



def addDadosMysqlToDb(self):
    self.conexao = sqlite3.connect('database.db')
    self.conexao.row_factory = sqlite3.Row
    self.cursor = self.conexao.cursor()
    self.cursor.execute(""" SELECT * FROM dados_mysql; """)
    self.tabela = self.cursor.fetchall()
    self.databaseMysql = self.tabela[0][1]
    self.usuarioMysql = self.tabela[0][2]
    self.senhaMysql = self.tabela[0][3]
    self.hostMysql = self.tabela[0][4]
    #self.conexao.commit()
    self.conexao.close()

def bancoDados(self):
    self.db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
    self.db.setHostName("localhost")
    self.db.setDatabaseName("tcxs_store")
    self.db.setUserName("root")
    self.db.setPassword("")
    self.ok = self.db.open()
    print(self.db)
    print(self.ok)
    self.model = QtSql.QSqlTableModel()
    self.model.setTable('playstation_psp')

    #self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    #self.db.setDatabaseName('database.db')
    #self.model = QtSql.QSqlTableModel()
    #self.model.setTable('dados_mysql')

    self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
    self.model.select()
    self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Id")
    self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Titulo")
    self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Descrição")
    self.model.setHeaderData(3, QtCore.Qt.Horizontal, "ContentID")
    self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Imagem")
    self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Cadastro")
    self.model.setHeaderData(6, QtCore.Qt.Horizontal, "Link")
    #tabela de dados
    self.ui.tabela_dados_usuarios.setModel(self.model)
    self.i = self.model.rowCount()
    # botoes das açoes
    #self.ui.botao_db_adiciona.clicked.connect(lambda: addToDb(self))
    #self.ui.botao_db_atualiza.clicked.connect(lambda: updaterow(self))
    #self.ui.botao_db_deleta.clicked.connect(lambda:delrow(self))
"""
def addToDb(self):
    print(self.i)
    self.model.insertRows(self.i,1)
    self.model.setData(self.model.index(self.i,1),self.ui.db_texto_titulo.text())
    self.model.setData(self.model.index(self.i, 2), self.ui.db_texto_link.text())
    self.model.setData(self.model.index(self.i,4), self.ui.db_texto_observacao.toPlainText())
    self.model.setData(self.model.index(self.i,3), self.ui.db_texto_codigo.toPlainText())
    self.model.submitAll()
    self.i += 1


def delrow(self):
    if self.ui.tabela_dados_db.currentIndex().row() > -1:
        self.model.removeRow(self.ui.tabela_dados_db.currentIndex().row())
        self.i -= 1
        self.model.select()
    else:
        QMessageBox.question(self,'Mensagem', "Selecione uma linha para deletar", QMessageBox.Ok)
        self.show()

def updaterow(self):
    if self.ui.tabela_dados_db.currentIndex().row() > -1:
        record = self.model.record(self.ui.tabela_dados_db.currentIndex().row())
        record.setValue("Titulo",self.ui.db_texto_titulo.text())
        record.setValue("Link",self.ui.db_texto_link.text())
        record.setValue("Codigo", self.ui.db_texto_codigo.toPlainText())
        record.setValue("Observações", self.ui.db_texto_observacao.toPlainText())
        self.model.setRecord(self.ui.tabela_dados_db.currentIndex().row(), record)
    else:
        QMessageBox.question(self,'Mensgem', "Selecione uma linha para atualizar", QMessageBox.Ok)
        self.show()"""