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
from funcoes import conexao
from PyQt5 import QtSql
from PyQt5 import QtCore
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QMessageBox


def verificarDatabase(self):
    self.ui.comboBox_databases.currentIndexChanged.connect(lambda: selecionaDatabase(self))


def selecionaDatabase(self):
    self.database_selecionada = self.ui.comboBox_databases.currentText()
    # usa o arquivo de conexao
    self.query_verdb = QSqlQuery(conexao.db_mysql)
    self.model_verdb = QtSql.QSqlTableModel()
    self.model_verdb.setTable(self.database_selecionada)
    self.model_verdb.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
    self.model_verdb.select()
    # popula as tabelas
    self.model_verdb.setHeaderData(0, QtCore.Qt.Horizontal, "Id")
    self.model_verdb.setHeaderData(1, QtCore.Qt.Horizontal, "Titulo")
    self.model_verdb.setHeaderData(2, QtCore.Qt.Horizontal, "Descrição")
    self.model_verdb.setHeaderData(3, QtCore.Qt.Horizontal, "ContentID")
    self.model_verdb.setHeaderData(4, QtCore.Qt.Horizontal, "Imagem")
    self.model_verdb.setHeaderData(5, QtCore.Qt.Horizontal, "Cadastro")
    self.model_verdb.setHeaderData(6, QtCore.Qt.Horizontal, "Link1")
    self.model_verdb.setHeaderData(7, QtCore.Qt.Horizontal, "Link2")
    self.model_verdb.setHeaderData(8, QtCore.Qt.Horizontal, "Link3")
    self.model_verdb.setHeaderData(9, QtCore.Qt.Horizontal, "Link4")
    self.model_verdb.setHeaderData(10, QtCore.Qt.Horizontal, "Link5")
    self.model_verdb.setHeaderData(11, QtCore.Qt.Horizontal, "Link6")
    self.model_verdb.setHeaderData(12, QtCore.Qt.Horizontal, "Link7")
    self.model_verdb.setHeaderData(13, QtCore.Qt.Horizontal, "Link8")
    self.model_verdb.setHeaderData(14, QtCore.Qt.Horizontal, "Link9")
    self.model_verdb.setHeaderData(15, QtCore.Qt.Horizontal, "Link10")
    self.model_verdb.setHeaderData(16, QtCore.Qt.Horizontal, "Link11")
    self.model_verdb.setHeaderData(17, QtCore.Qt.Horizontal, "Link12")
    self.model_verdb.setHeaderData(18, QtCore.Qt.Horizontal, "Link13")
    self.model_verdb.setHeaderData(19, QtCore.Qt.Horizontal, "Link14")
    self.model_verdb.setHeaderData(20, QtCore.Qt.Horizontal, "Link15")
    self.model_verdb.setHeaderData(21, QtCore.Qt.Horizontal, "Link16")
    self.model_verdb.setHeaderData(22, QtCore.Qt.Horizontal, "Link17")
    self.model_verdb.setHeaderData(23, QtCore.Qt.Horizontal, "Link18")
    self.model_verdb.setHeaderData(24, QtCore.Qt.Horizontal, "Link19")
    self.model_verdb.setHeaderData(25, QtCore.Qt.Horizontal, "Link20")
    self.model_verdb.setHeaderData(26, QtCore.Qt.Horizontal, "Link21")
    self.model_verdb.setHeaderData(27, QtCore.Qt.Horizontal, "Link22")
    self.model_verdb.setHeaderData(28, QtCore.Qt.Horizontal, "Link23")
    self.model_verdb.setHeaderData(29, QtCore.Qt.Horizontal, "Link24")
    self.model_verdb.setHeaderData(30, QtCore.Qt.Horizontal, "Link25")
    self.model_verdb.setHeaderData(31, QtCore.Qt.Horizontal, "Link26")
    self.model_verdb.setHeaderData(32, QtCore.Qt.Horizontal, "Link27")
    self.model_verdb.setHeaderData(33, QtCore.Qt.Horizontal, "Link28")
    self.model_verdb.setHeaderData(34, QtCore.Qt.Horizontal, "Link29")
    self.model_verdb.setHeaderData(35, QtCore.Qt.Horizontal, "Link30")

    # tabela de dados
    self.ui.tabela_dados_db_databases.setModel(self.model_verdb)
    self.ui.tabela_dados_db_databases.setToolTip(
        'Tabela de dados:\nSistema de verificação e leitura das databases')
    self.i_verdb = self.model_verdb.rowCount()
