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
from funcoes import conexao


def funcoesConsultaUsers(self):
    #eventos para limpar os campos, que buscam funçoes no arquivo main
    self.ui.input_pesquisa_acessos_usuarios.mousePressEvent = self.limpaPesquisaAcessoUsers
    self.ui.btn_pesquisa_acessos_usuarios.clicked.connect(lambda: consultaUser(self))


def consultaUser(self):
    #usa o arquivo de conexao
    self.query_user = QSqlQuery(conexao.db_mysql)
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




