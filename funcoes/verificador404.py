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


def verificar404(self):
    self.ui.comboBox_verifica404.currentIndexChanged.connect(lambda: selecionaVerifica404(self))


def selecionaVerifica404(self):
    self.verifica404_selecionada = self.ui.comboBox_verifica404.currentText()
    print(self.verifica404_selecionada)

    if self.verifica404_selecionada == 'playstation_psp':
        self.query_404 = QSqlQuery(conexao.db_mysql)
        self.model_404 = QtSql.QSqlTableModel()
        self.query_404.exec(f"""SELECT * FROM {self.verifica404_selecionada}""")
        while self.query_404.next():
            self.link_404 = self.query_404.value(6)
            print(self.link_404)