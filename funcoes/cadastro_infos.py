#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ███╗   ███╗ █████╗ ███╗   ██╗██╗ ██████╗ ██████╗ ███╗   ███╗██╗ ██████╗
# ████╗ ████║██╔══██╗████╗  ██║██║██╔════╝██╔═══██╗████╗ ████║██║██╔═══██╗
# ██╔████╔██║███████║██╔██╗ ██║██║██║     ██║   ██║██╔████╔██║██║██║   ██║
# ██║╚██╔╝██║██╔══██║██║╚██╗██║██║██║     ██║   ██║██║╚██╔╝██║██║██║   ██║
# ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║╚██████╗╚██████╔╝██║ ╚═╝ ██║██║╚██████╔╝
# ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝
#            @GorpoOrko | Manicomio TCXS Project | 2020

from main import *
from PyQt5 import QtSql
from PyQt5 import QtCore
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import  QMessageBox
from funcoes import conexao


def funcoesCadastroInfos(self):
    # eventos para limpar os campos, que buscam funçoes no arquivo main
    self.ui.input_playstation_infos.mousePressEvent = self.limpaInputInfos
    self.ui.input_playstation_infos.setToolTip('Insira a informação(aviso) que irá aparecer na homepage da loja.\nEste input aceita códigos html simples!')
    # botoes das açoes
    self.ui.btn_adiciona_infos.clicked.connect(lambda: addToDbInfos(self))
    self.ui.btn_atualiza_infos.clicked.connect(lambda: updaterowInfos(self))
    self.ui.btn_deleta_infos.clicked.connect(lambda: delrowInfos(self))


def bancoDadosInfos(self):
    # usa o arquivo de conexao
    self.query_infos = QSqlQuery(conexao.db_mysql)
    self.model_infos = QtSql.QSqlTableModel()
    self.model_infos.setTable('playstation_infos')
    self.model_infos.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
    self.model_infos.select()
    # popula as tabelas
    self.model_infos.setHeaderData(0, QtCore.Qt.Horizontal, "Id")
    self.model_infos.setHeaderData(1, QtCore.Qt.Horizontal, "Informacao")
    # tabela de dados
    self.ui.tabela_dados_playstation_infos.setModel(self.model_infos)
    self.ui.tabela_dados_playstation_infos.setToolTip('Tabela da dados:\nPara adicionar itens sempre preencha todos os campos.\nCaso queira editar clique sobre o numero de uma linha e clique em atualizar.\nCaso queira deletar clique sobre o numero de uma linha e delete.')
    self.i_infos = self.model_infos.rowCount()



def addToDbInfos(self):
    #chama a função de conexao e popula a tabela
    bancoDadosInfos(self)
    # print(self.i)
    if self.ui.input_playstation_infos.text() == 'Informação da homepage':
        QMessageBox.question(self, 'TCXS Project | Informações da Homepage',
                             """Para adicionar informações a homepage da loja:
                             Insira sua informação e clique em enviar, este sistema aceita tag's html.
                             Para atualizar informação da homepage da loja:
                             Insira todos dados nos campos, clique sobre a linha que quer editar e no botao atualizar.
                             Para deletar uma informação da loja:
                             Selecione a linha da informação e clique em deletar.""",
                             QMessageBox.Ok)
        self.show()

    else:
        # insere os dados na database
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
        QMessageBox.question(self, 'Mensagem',
                             "Selecione uma linha para deletar, clique sobre o numero a esquerda na tabela correspondente a linha.",
                             QMessageBox.Ok)
        self.show()


def updaterowInfos(self):
    if self.ui.tabela_dados_playstation_infos.currentIndex().row() > -1:
        record = self.model_infos.record(self.ui.tabela_dados_playstation_infos.currentIndex().row())
        record.setValue("informacao", self.ui.input_playstation_infos.text())
        self.model_infos.setRecord(self.ui.tabela_dados_playstation_infos.currentIndex().row(), record)
    else:
        QMessageBox.question(self, 'Mensagem',
                             "Selecione uma linha para atualizar, clique sobre o numero a esquerda na tabela correspondente a linha.",
                             QMessageBox.Ok)
        self.show()
