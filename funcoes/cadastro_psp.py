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


def funcoesCadastroPsp(self):
    # eventos para limpar os campos, que buscam funçoes no arquivo main
    self.ui.input_titulo_jogo_psp.mousePressEvent = self.limpaInputTituloPSp
    self.ui.input_descricao_jogo_psp.mousePressEvent = self.limpaInputDescricaoPSp
    self.ui.input_contentid_psp.mousePressEvent = self.limpaInputContentidPSp
    self.ui.input_link_jogo_psp.mousePressEvent = self.limpaInputLinkPSp
    # botoes das açoes
    self.ui.botao_db_adiciona_psp.clicked.connect(lambda: addToDbInfos(self))
    self.ui.botao_db_atualiza_psp.clicked.connect(lambda: updaterowInfos(self))
    self.ui.botao_db_deleta_psp.clicked.connect(lambda: delrowInfos(self))
    #btn upload imagem_psp
    self.ui.btn_upload_imagem_psp.clicked.connect(lambda: delrowInfos(self))









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
    self.i_infos = self.model_infos.rowCount()



def addToDbInfos(self):
    #chama a função de conexao e popula a tabela
    bancoDadosInfos(self)
    # print(self.i)
    if self.ui.tabela_dados_playstation_infos.currentIndex().row() == self.ui.tabela_dados_playstation_infos.currentIndex().row() + 1:
        pass
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
