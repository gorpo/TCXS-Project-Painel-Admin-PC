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

from PyQt5 import QtSql
from PyQt5 import QtCore
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QMessageBox
from datetime import datetime
from funcoes import conexao


def funcoesCadastroUsers(self):
    #eventos para limpar os campos, que buscam funçoes no arquivo main
    self.ui.input_nome_user.mousePressEvent = self.limpaNomeCadastro
    self.ui.input_username_user.mousePressEvent = self.limpaUserCadastro
    self.ui.input_senha_user.mousePressEvent = self.limpaSenhaCadastro
    #botoes de ação da pagina
    self.ui.btn_adiciona_user.clicked.connect(lambda: addToDbUser(self))
    self.ui.btn_atualiza_user.clicked.connect(lambda: updaterowUser(self))
    self.ui.btn_deleta_user.clicked.connect(lambda: delrowUser(self))


def bancoDadosUsers(self):
    self.i_user = 0
    # usa o arquivo de conexao
    self.query_user = QSqlQuery(conexao.db_mysql)
    self.model_user = QtSql.QSqlTableModel()
    # seleciona a tabela
    self.model_user.setTable('playstation_users')
    self.model_user.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
    self.model_user.select()
    # popula as tabelas
    self.model_user.setHeaderData(0, QtCore.Qt.Horizontal, "Id")
    self.model_user.setHeaderData(1, QtCore.Qt.Horizontal, "Usuario")
    self.model_user.setHeaderData(2, QtCore.Qt.Horizontal, "Senha")
    self.model_user.setHeaderData(3, QtCore.Qt.Horizontal, "Nome")
    self.model_user.setHeaderData(4, QtCore.Qt.Horizontal, "Cadastro")
    self.model_user.setHeaderData(5, QtCore.Qt.Horizontal, "Nivel")
    #tabela de dados
    self.ui.tabela_dados_usuarios.setModel(self.model_user)
    self.i_user = self.model_user.rowCount()


def addToDbUser(self):
    # chama a função de conexao e popula a tabela
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