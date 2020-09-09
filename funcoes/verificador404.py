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
    verifica404_selecionada = self.ui.comboBox_verifica404.currentText()
    print(verifica404_selecionada)
    self.a = QSqlQuery(conexao.db_mysql)
    self.c = self.a.exec("""SELECT * FROM `playstation_ps1` """)
    print(self.a)
    print(self.c)
    while self.a.next():
        # retorna o nome dos usuarios cadastrados
        self.b = self.a.value(1)
        print(self.b)