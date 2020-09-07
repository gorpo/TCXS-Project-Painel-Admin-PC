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



def funcoesCadastroInfos(self):
    #eventos para limpar os campos, que buscam funçoes no arquivo main
    self.ui.input_playstation_infos.mousePressEvent = self.limpaInputInfos
    bancoDadosInfos(self)



def bancoDadosInfos(self):
    self.conexao_infos = sqlite3.connect('database.db')
    self.cursor_infos = self.conexao_infos.cursor()
    self.cursor_infos.execute(' SELECT * FROM dados_mysql; ')
    self.tabela_infos = self.cursor_infos.fetchall()
    self.databaseMysql_infos = self.tabela_infos[0][1]
    self.usuarioMysql_infos = self.tabela_infos[0][2]
    self.senhaMysql_infos = self.tabela_infos[0][3]
    self.hostMysql_infos = self.tabela_infos[0][4]
    self.conexao_infos.close()
    self.db_infos = QtSql.QSqlDatabase.addDatabase('QMYSQL')
    self.db_infos.setHostName(self.hostMysql_infos)
    self.db_infos.setDatabaseName(self.databaseMysql_infos)
    self.db_infos.setUserName(self.usuarioMysql_infos)
    self.db_infos.setPassword(self.senhaMysql_infos)
    self.ok = self.db_infos.open()
    if not self.ok: print(self.db_infos.lastError().text())
    # else: print("connected")
    self.query_infos = QSqlQuery(self.db_infos)
    self.model_infos = QtSql.QSqlTableModel()
    self.model_infos.setTable('playstation_infos')
    self.model_infos.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
    self.model_infos.select()
    self.model_infos.setHeaderData(0, QtCore.Qt.Horizontal, "Id")
    self.model_infos.setHeaderData(1, QtCore.Qt.Horizontal, "Informacao")
    #tabela de dados
    self.ui.tabela_dados_playstation_infos.setModel(self.model_infos)
    self.i_infos = self.model_infos.rowCount()
    # botoes das açoes
    self.ui.btn_adiciona_infos.clicked.connect(lambda: addToDbInfos(self))
    self.ui.btn_atualiza_infos.clicked.connect(lambda: updaterowInfos(self))
    self.ui.btn_deleta_infos.clicked.connect(lambda: delrowInfos(self))




def addToDbInfos(self):
    #print(self.i)
    if self.ui.tabela_dados_playstation_infos.currentIndex().row() == self.ui.tabela_dados_playstation_infos.currentIndex().row() +1:
        pass
    else:
        #insere os dados na database
        self.model_infos.insertRows(self.i_infos, 1)
        self.model_infos.setData(self.model_infos.index(self.i_infos, 1), self.ui.input_playstation_infos.text())
        self.model_infos.submitAll()
        self.i_infos += 1


def delrowInfos(self):
    if self.ui.tabela_dados_playstation_infos.currentIndex().row() > -1:
        self.model_infos.removeRow(self.ui.tabela_dados_playstation_infos.currentIndex().row())
        self.i_infos -= 1
        self.model_infos.select()
    else:
        QMessageBox.question(self,'Mensagem', "Selecione uma linha para deletar, clique sobre o numero a esquerda na tabela correspondente a linha.", QMessageBox.Ok)
        self.show()

def updaterowInfos(self):
    if self.ui.tabela_dados_playstation_infos.currentIndex().row() > -1:
        record = self.model_infos.record(self.ui.tabela_dados_playstation_infos.currentIndex().row())
        record.setValue("informacao",self.ui.input_playstation_infos.text())
        self.model_infos.setRecord(self.ui.tabela_dados_playstation_infos.currentIndex().row(), record)
    else:
        QMessageBox.question(self,'Mensagem', "Selecione uma linha para atualizar, clique sobre o numero a esquerda na tabela correspondente a linha.", QMessageBox.Ok)
        self.show()