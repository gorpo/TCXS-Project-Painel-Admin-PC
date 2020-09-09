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
import sys
import time
from PyQt5.QtWidgets import QApplication, QDialog,  QProgressBar, QPushButton

import requests
from bs4 import BeautifulSoup

def verificar404(self):
    self.ui.comboBox_verifica404.currentIndexChanged.connect(lambda: selecionaVerifica404(self))


def selecionaVerifica404(self):
    #armazena o valor retornado pela ComboBox
    self.verifica404_selecionada = self.ui.comboBox_verifica404.currentText()


    #progress bar
    self.progress = QProgressBar(self)
    self.progress.setGeometry(0, 0, 300, 25)
    self.progress.setMaximum(100)
    self.show()

    # verificaPSP
    if self.verifica404_selecionada == 'playstation_psp':
        query = QSqlQuery(conexao.db_mysql)
        model = QtSql.QSqlTableModel()
        tamanho_lista = query.exec(f"""SELECT * FROM playstation_ps1""")
        contador_progress = 0
        self.ui.progressBar404.setMaximum(query.size())
        while query.next():
            self.ui.progressBar404.setValue(contador_progress)
            contador_progress += 1
            titulo = query.value(1)
            data = query.value(5).toPyDateTime().strftime('%d/%m/%Y')
            link = query.value(6)
            try:#faz tras a pagina do Dropbox com requests | print(titulo, pagina.status_code)
                pagina = requests.get(link.replace('=1', '=0'))
                # passa a pagina para o BeautifulSoup verificar o texto no titulo <title>Dropbox - Error</title>
                soup = BeautifulSoup(pagina.text, 'html.parser')
                erro404 = soup.find_all('title')[0]
                if str(erro404) == '<title>Dropbox - Error</title>':
                    texto_html = f""" <h2 style='color: #fff;'>Jogo: {titulo} | Cadastro: {data} | Erro: 404</h2>"""
                    link_html = f"""<a style='color: #fff;' href='{link}'>Link: {link}</a> """
                    self.ui.textBrowser_verifica404.append(texto_html)
                    self.ui.textBrowser_verifica404.append(link_html)
            except Exception as e:
                print(e)
                pass


