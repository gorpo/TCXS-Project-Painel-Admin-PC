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

    # verificaPSP
    if self.verifica404_selecionada == 'playstation_psp':
        self.ui.textBrowser_verifica404.append(f"<h3 style='color: rgb(170,0,0);'>VERIFICAÇÃO PSP INICIADA</h3>")
        query = QSqlQuery(conexao.db_mysql)
        model = QtSql.QSqlTableModel()
        query.exec(f"""SELECT * FROM playstation_psp""")
        contador_progress = 0
        contador_erros = 0
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
                    texto_html = f""" <h3 style='color: #fff;'>Jogo: {titulo} | Cadastro: {data} | Erro: 404</h3>"""
                    link_html = f"""<a style='color: #fff;' href='{link}'>Link: {link}</a> """
                    self.ui.textBrowser_verifica404.append(texto_html)
                    self.ui.textBrowser_verifica404.append(link_html)
                    contador_erros += 1
            except Exception as e:
                pass
        #fim do loop testando os links da database | exibe o aviso final
        self.ui.textBrowser_verifica404.append(f"<h2 style='color: rgb(170,0,0);'>TOTAL DE ERROS: {contador_erros}</h2>")
        self.ui.textBrowser_verifica404.append(f"<h2 style='color: rgb(170,0,0);'>TODOS LINKS DE PSP FORAM VERIFICADOS</h2>")


    # verificaPS1
    if self.verifica404_selecionada == 'playstation_ps1':
        self.ui.textBrowser_verifica404.append(f"<h3 style='color: rgb(170,0,0);'>VERIFICAÇÃO PS1 INICIADA</h3>")
        query = QSqlQuery(conexao.db_mysql)
        model = QtSql.QSqlTableModel()
        query.exec(f"""SELECT * FROM playstation_ps1""")
        contador_progress = 0
        contador_erros = 0
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
                    texto_html = f""" <h3 style='color: #fff;'>Jogo: {titulo} | Cadastro: {data} | Erro: 404</h3>"""
                    link_html = f"""<a style='color: #fff;' href='{link}'>Link: {link}</a> """
                    self.ui.textBrowser_verifica404.append(texto_html)
                    self.ui.textBrowser_verifica404.append(link_html)
                    contador_erros += 1
            except Exception as e:
                pass
        #fim do loop testando os links da database | exibe o aviso final
        self.ui.textBrowser_verifica404.append(f"<h2 style='color: rgb(170,0,0);'>TOTAL DE ERROS: {contador_erros}</h2>")
        self.ui.textBrowser_verifica404.append(f"<h2 style='color: rgb(170,0,0);'>TODOS LINKS DE PS1 FORAM VERIFICADOS</h2>")

    # verificaPS2
    if self.verifica404_selecionada == 'playstation_ps2':
        self.ui.textBrowser_verifica404.append(f"<h3 style='color: rgb(170,0,0);'>VERIFICAÇÃO PS2 INICIADA</h3>")
        query = QSqlQuery(conexao.db_mysql)
        model = QtSql.QSqlTableModel()
        query.exec(f"""SELECT * FROM playstation_ps2""")
        contador_progress = 0
        contador_erros = 0
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
                    texto_html = f""" <h3 style='color: #fff;'>Jogo: {titulo} | Cadastro: {data} | Erro: 404</h3>"""
                    link_html = f"""<a style='color: #fff;' href='{link}'>Link: {link}</a> """
                    self.ui.textBrowser_verifica404.append(texto_html)
                    self.ui.textBrowser_verifica404.append(link_html)
                    contador_erros += 1
            except Exception as e:
                pass
        #fim do loop testando os links da database | exibe o aviso final
        self.ui.textBrowser_verifica404.append(f"<h2 style='color: rgb(170,0,0);'>TOTAL DE ERROS: {contador_erros}</h2>")
        self.ui.textBrowser_verifica404.append(f"<h2 style='color: rgb(170,0,0);'>TODOS LINKS DE PS2 FORAM VERIFICADOS</h2>")

    # verificaEMULADORES(RETRO)
    if self.verifica404_selecionada == 'playstation_emuladores':
        self.ui.textBrowser_verifica404.append(f"<h3 style='color: rgb(170,0,0);'>VERIFICAÇÃO EMULADORES INICIADA</h3>")
        query = QSqlQuery(conexao.db_mysql)
        model = QtSql.QSqlTableModel()
        query.exec(f"""SELECT * FROM playstation_emuladores""")
        contador_progress = 0
        contador_erros = 0
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
                    texto_html = f""" <h3 style='color: #fff;'>Jogo: {titulo} | Cadastro: {data} | Erro: 404</h3>"""
                    link_html = f"""<a style='color: #fff;' href='{link}'>Link: {link}</a> """
                    self.ui.textBrowser_verifica404.append(texto_html)
                    self.ui.textBrowser_verifica404.append(link_html)
                    contador_erros += 1
            except Exception as e:
                pass
        #fim do loop testando os links da database | exibe o aviso final
        self.ui.textBrowser_verifica404.append(f"<h2 style='color: rgb(170,0,0);'>TOTAL DE ERROS: {contador_erros}</h2>")
        self.ui.textBrowser_verifica404.append(f"<h2 style='color: rgb(170,0,0);'>TODOS LINKS DE EMULADORES FORAM VERIFICADOS</h2>")

    # verificaEXTRAS
    if self.verifica404_selecionada == 'playstation_extras':
        self.ui.textBrowser_verifica404.append(f"<h3 style='color: rgb(170,0,0);'>VERIFICAÇÃO EXTRAS INICIADA</h3>")
        query = QSqlQuery(conexao.db_mysql)
        model = QtSql.QSqlTableModel()
        query.exec(f"""SELECT * FROM playstation_extras""")
        contador_progress = 0
        contador_erros = 0
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
                    texto_html = f""" <h3 style='color: #fff;'>Jogo: {titulo} | Cadastro: {data} | Erro: 404</h3>"""
                    link_html = f"""<a style='color: #fff;' href='{link}'>Link: {link}</a> """
                    self.ui.textBrowser_verifica404.append(texto_html)
                    self.ui.textBrowser_verifica404.append(link_html)
                    contador_erros += 1
            except Exception as e:
                pass
        #fim do loop testando os links da database | exibe o aviso final
        self.ui.textBrowser_verifica404.append(f"<h2 style='color: rgb(170,0,0);'>TOTAL DE ERROS: {contador_erros}</h2>")
        self.ui.textBrowser_verifica404.append(f"<h2 style='color: rgb(170,0,0);'>TODOS LINKS EXTRAS FORAM VERIFICADOS</h2>")




# verificaPS3
    if self.verifica404_selecionada == 'playstation_ps3':
        self.ui.textBrowser_verifica404.append(f"<h3 style='color: rgb(170,0,0);'>VERIFICAÇÃO PS3 INICIADA</h3>")
        query = QSqlQuery(conexao.db_mysql)
        model = QtSql.QSqlTableModel()
        query.exec(f"""SELECT * FROM playstation_ps3""")

        contador_progress = 0
        contador_erros = 0

        self.ui.progressBar404.setMaximum(query.size()*30)

        while query.next():  # TESTA LINK1 PLAYSTATION3
            self.ui.progressBar404.setValue(contador_progress)
            contador_progress += 1
            titulo = query.value(1)
            data = query.value(5).toPyDateTime().strftime('%d/%m/%Y')
            try:  # TESTA LINK1 PLAYSTATION3
                link1 = query.value(6)
                if link1 == '---' or link1 == '':
                    pass
                else:
                    pagina = requests.get(link1.replace('=1', '=0'))
                    # passa a pagina para o BeautifulSoup verificar o texto no titulo <title>Dropbox - Error</title>
                    soup = BeautifulSoup(pagina.text, 'html.parser')
                    erro404 = soup.find_all('title')[0]
                    if str(erro404) == '<title>Dropbox - Error</title>':
                        texto_html = f""" <h3 style='color: #fff;'>Jogo: {titulo} | Cadastro: {data} | Erro: 404</h3>"""
                        link1_html = f"""<a style='color: #fff;' href='{link1}'>Link1: {link1}</a> """
                        self.ui.textBrowser_verifica404.append(texto_html)
                        self.ui.textBrowser_verifica404.append(link1_html)
                        contador_erros += 1
            except Exception as e:
                pass

        while query.next():  # TESTA LINK2 PLAYSTATION3
            self.ui.progressBar404.setValue(contador_progress)
            contador_progress += 1
            titulo = query.value(1)
            data = query.value(5).toPyDateTime().strftime('%d/%m/%Y')
            try:  # TESTA LINK2 PLAYSTATION3
                link2 = query.value(7)
                if link2 == '---' or link2 == '':
                    pass
                else:
                    pagina = requests.get(link2.replace('=1', '=0'))
                    # passa a pagina para o BeautifulSoup verificar o texto no titulo <title>Dropbox - Error</title>
                    soup = BeautifulSoup(pagina.text, 'html.parser')
                    erro404 = soup.find_all('title')[0]
                    if str(erro404) == '<title>Dropbox - Error</title>':
                        texto_html = f""" <h3 style='color: #fff;'>Jogo: {titulo} | Cadastro: {data} | Erro: 404</h3>"""
                        link2_html = f"""<a style='color: #fff;' href='{link2}'>Link2: {link2}</a> """
                        self.ui.textBrowser_verifica404.append(texto_html)
                        self.ui.textBrowser_verifica404.append(link2_html)
                        contador_erros += 1
            except Exception as e:
                pass

        while query.next():  # TESTA LINK3 PLAYSTATION3
            self.ui.progressBar404.setValue(contador_progress)
            contador_progress += 1
            titulo = query.value(1)
            data = query.value(5).toPyDateTime().strftime('%d/%m/%Y')
            try:  # TESTA LINK3 PLAYSTATION3
                link3 = query.value(8)
                if link3 == '---' or link3 == '':
                    pass
                else:
                    pagina = requests.get(link3.replace('=1', '=0'))
                    # passa a pagina para o BeautifulSoup verificar o texto no titulo <title>Dropbox - Error</title>
                    soup = BeautifulSoup(pagina.text, 'html.parser')
                    erro404 = soup.find_all('title')[0]
                    if str(erro404) == '<title>Dropbox - Error</title>':
                        texto_html = f""" <h3 style='color: #fff;'>Jogo: {titulo} | Cadastro: {data} | Erro: 404</h3>"""
                        link3_html = f"""<a style='color: #fff;' href='{link3}'>Link3: {link3}</a> """
                        self.ui.textBrowser_verifica404.append(texto_html)
                        self.ui.textBrowser_verifica404.append(link3_html)
                        contador_erros += 1
            except Exception as e:
                pass

        while query.next():  # TESTA LINK4 PLAYSTATION3
            self.ui.progressBar404.setValue(contador_progress)
            contador_progress += 1
            titulo = query.value(1)
            data = query.value(5).toPyDateTime().strftime('%d/%m/%Y')
            try:  # TESTA LINK4 PLAYSTATION3
                link4 = query.value(9)
                if link4 == '---' or link4 == '':
                    pass
                else:
                    pagina = requests.get(link4.replace('=1', '=0'))
                    # passa a pagina para o BeautifulSoup verificar o texto no titulo <title>Dropbox - Error</title>
                    soup = BeautifulSoup(pagina.text, 'html.parser')
                    erro404 = soup.find_all('title')[0]
                    if str(erro404) == '<title>Dropbox - Error</title>':
                        texto_html = f""" <h3 style='color: #fff;'>Jogo: {titulo} | Cadastro: {data} | Erro: 404</h3>"""
                        link4_html = f"""<a style='color: #fff;' href='{link4}'>Link4: {link4}</a> """
                        self.ui.textBrowser_verifica404.append(texto_html)
                        self.ui.textBrowser_verifica404.append(link4_html)
                        contador_erros += 1
            except Exception as e:
                pass

        while query.next():  # TESTA LINK5 PLAYSTATION3
            self.ui.progressBar404.setValue(contador_progress)
            contador_progress += 1
            titulo = query.value(1)
            data = query.value(5).toPyDateTime().strftime('%d/%m/%Y')
            try:  # TESTA LINK5 PLAYSTATION3
                link5 = query.value(10)
                if link5 == '---' or link5 == '':
                    pass
                else:
                    pagina = requests.get(link5.replace('=1', '=0'))
                    # passa a pagina para o BeautifulSoup verificar o texto no titulo <title>Dropbox - Error</title>
                    soup = BeautifulSoup(pagina.text, 'html.parser')
                    erro404 = soup.find_all('title')[0]
                    if str(erro404) == '<title>Dropbox - Error</title>':
                        texto_html = f""" <h3 style='color: #fff;'>Jogo: {titulo} | Cadastro: {data} | Erro: 404</h3>"""
                        link5_html = f"""<a style='color: #fff;' href='{link5}'>Link5: {link5}</a> """
                        self.ui.textBrowser_verifica404.append(texto_html)
                        self.ui.textBrowser_verifica404.append(link5_html)
                        contador_erros += 1
            except Exception as e:
                pass

        while query.next():  # TESTA LINK11 PLAYSTATION3
            self.ui.progressBar404.setValue(contador_progress)
            contador_progress += 1
            titulo = query.value(1)
            data = query.value(5).toPyDateTime().strftime('%d/%m/%Y')
            try:  # TESTA LINK11 PLAYSTATION3
                link11 = query.value(11)
                if link11 == '---' or link11 == '':
                    pass
                else:
                    pagina = requests.get(link11.replace('=1', '=0'))
                    # passa a pagina para o BeautifulSoup verificar o texto no titulo <title>Dropbox - Error</title>
                    soup = BeautifulSoup(pagina.text, 'html.parser')
                    erro404 = soup.find_all('title')[0]
                    if str(erro404) == '<title>Dropbox - Error</title>':
                        texto_html = f""" <h3 style='color: #fff;'>Jogo: {titulo} | Cadastro: {data} | Erro: 404</h3>"""
                        link11_html = f"""<a style='color: #fff;' href='{link11}'>Link11: {link11}</a> """
                        self.ui.textBrowser_verifica404.append(texto_html)
                        self.ui.textBrowser_verifica404.append(link11_html)
                        contador_erros += 1
            except Exception as e:
                pass

        while query.next():  # TESTA LINK7 PLAYSTATION3
            self.ui.progressBar404.setValue(contador_progress)
            contador_progress += 1
            titulo = query.value(1)
            data = query.value(5).toPyDateTime().strftime('%d/%m/%Y')
            try:  # TESTA LINK7 PLAYSTATION3
                link7 = query.value(12)
                if link7 == '---' or link7 == '':
                    pass
                else:
                    pagina = requests.get(link7.replace('=1', '=0'))
                    # passa a pagina para o BeautifulSoup verificar o texto no titulo <title>Dropbox - Error</title>
                    soup = BeautifulSoup(pagina.text, 'html.parser')
                    erro404 = soup.find_all('title')[0]
                    if str(erro404) == '<title>Dropbox - Error</title>':
                        texto_html = f""" <h3 style='color: #fff;'>Jogo: {titulo} | Cadastro: {data} | Erro: 404</h3>"""
                        link7_html = f"""<a style='color: #fff;' href='{link7}'>Link7: {link7}</a> """
                        self.ui.textBrowser_verifica404.append(texto_html)
                        self.ui.textBrowser_verifica404.append(link7_html)
                        contador_erros += 1
            except Exception as e:
                pass

        while query.next():  # TESTA LINK8 PLAYSTATION3
            self.ui.progressBar404.setValue(contador_progress)
            contador_progress += 1
            titulo = query.value(1)
            data = query.value(5).toPyDateTime().strftime('%d/%m/%Y')
            try:  # TESTA LINK8 PLAYSTATION3
                link8 = query.value(13)
                if link8 == '---' or link8 == '':
                    pass
                else:
                    pagina = requests.get(link8.replace('=1', '=0'))
                    # passa a pagina para o BeautifulSoup verificar o texto no titulo <title>Dropbox - Error</title>
                    soup = BeautifulSoup(pagina.text, 'html.parser')
                    erro404 = soup.find_all('title')[0]
                    if str(erro404) == '<title>Dropbox - Error</title>':
                        texto_html = f""" <h3 style='color: #fff;'>Jogo: {titulo} | Cadastro: {data} | Erro: 404</h3>"""
                        link8_html = f"""<a style='color: #fff;' href='{link8}'>Link8: {link8}</a> """
                        self.ui.textBrowser_verifica404.append(texto_html)
                        self.ui.textBrowser_verifica404.append(link8_html)
                        contador_erros += 1
            except Exception as e:
                pass

        while query.next():  # TESTA LINK9 PLAYSTATION3
            self.ui.progressBar404.setValue(contador_progress)
            contador_progress += 1
            titulo = query.value(1)
            data = query.value(5).toPyDateTime().strftime('%d/%m/%Y')
            try:  # TESTA LINK9 PLAYSTATION3
                link9 = query.value(14)
                if link9 == '---' or link9 == '':
                    pass
                else:
                    pagina = requests.get(link9.replace('=1', '=0'))
                    # passa a pagina para o BeautifulSoup verificar o texto no titulo <title>Dropbox - Error</title>
                    soup = BeautifulSoup(pagina.text, 'html.parser')
                    erro404 = soup.find_all('title')[0]
                    if str(erro404) == '<title>Dropbox - Error</title>':
                        texto_html = f""" <h3 style='color: #fff;'>Jogo: {titulo} | Cadastro: {data} | Erro: 404</h3>"""
                        link9_html = f"""<a style='color: #fff;' href='{link9}'>Link9: {link9}</a> """
                        self.ui.textBrowser_verifica404.append(texto_html)
                        self.ui.textBrowser_verifica404.append(link9_html)
                        contador_erros += 1
            except Exception as e:
                pass

        while query.next():  # TESTA LINK10 PLAYSTATION3
            self.ui.progressBar404.setValue(contador_progress)
            contador_progress += 1
            titulo = query.value(1)
            data = query.value(5).toPyDateTime().strftime('%d/%m/%Y')
            try:  # TESTA LINK10 PLAYSTATION3
                link10 = query.value(15)
                if link10 == '---' or link10 == '':
                    pass
                else:
                    pagina = requests.get(link10.replace('=1', '=0'))
                    # passa a pagina para o BeautifulSoup verificar o texto no titulo <title>Dropbox - Error</title>
                    soup = BeautifulSoup(pagina.text, 'html.parser')
                    erro404 = soup.find_all('title')[0]
                    if str(erro404) == '<title>Dropbox - Error</title>':
                        texto_html = f""" <h3 style='color: #fff;'>Jogo: {titulo} | Cadastro: {data} | Erro: 404</h3>"""
                        link10_html = f"""<a style='color: #fff;' href='{link10}'>Link10: {link10}</a> """
                        self.ui.textBrowser_verifica404.append(texto_html)
                        self.ui.textBrowser_verifica404.append(link10_html)
                        contador_erros += 1
            except Exception as e:
                pass

        while query.next():  # TESTA LINK11 PLAYSTATION3
            self.ui.progressBar404.setValue(contador_progress)
            contador_progress += 1
            titulo = query.value(1)
            data = query.value(5).toPyDateTime().strftime('%d/%m/%Y')
            try:  # TESTA LINK11 PLAYSTATION3
                link11 = query.value(16)
                if link11 == '---' or link11 == '':
                    pass
                else:
                    pagina = requests.get(link11.replace('=1', '=0'))
                    # passa a pagina para o BeautifulSoup verificar o texto no titulo <title>Dropbox - Error</title>
                    soup = BeautifulSoup(pagina.text, 'html.parser')
                    erro404 = soup.find_all('title')[0]
                    if str(erro404) == '<title>Dropbox - Error</title>':
                        texto_html = f""" <h3 style='color: #fff;'>Jogo: {titulo} | Cadastro: {data} | Erro: 404</h3>"""
                        link11_html = f"""<a style='color: #fff;' href='{link11}'>Link11: {link11}</a> """
                        self.ui.textBrowser_verifica404.append(texto_html)
                        self.ui.textBrowser_verifica404.append(link11_html)
                        contador_erros += 1
            except Exception as e:
                pass

        while query.next():  # TESTA LINK12 PLAYSTATION3
            self.ui.progressBar404.setValue(contador_progress)
            contador_progress += 1
            titulo = query.value(1)
            data = query.value(5).toPyDateTime().strftime('%d/%m/%Y')
            try:  # TESTA LINK12 PLAYSTATION3
                link12 = query.value(17)
                if link12 == '---' or link12 == '':
                    pass
                else:
                    pagina = requests.get(link12.replace('=1', '=0'))
                    # passa a pagina para o BeautifulSoup verificar o texto no titulo <title>Dropbox - Error</title>
                    soup = BeautifulSoup(pagina.text, 'html.parser')
                    erro404 = soup.find_all('title')[0]
                    if str(erro404) == '<title>Dropbox - Error</title>':
                        texto_html = f""" <h3 style='color: #fff;'>Jogo: {titulo} | Cadastro: {data} | Erro: 404</h3>"""
                        link12_html = f"""<a style='color: #fff;' href='{link12}'>Link12: {link12}</a> """
                        self.ui.textBrowser_verifica404.append(texto_html)
                        self.ui.textBrowser_verifica404.append(link12_html)
                        contador_erros += 1
            except Exception as e:
                pass

        while query.next():  # TESTA LINK13 PLAYSTATION3
            self.ui.progressBar404.setValue(contador_progress)
            contador_progress += 1
            titulo = query.value(1)
            data = query.value(5).toPyDateTime().strftime('%d/%m/%Y')
            try:  # TESTA LINK13 PLAYSTATION3
                link13 = query.value(18)
                if link13 == '---' or link13 == '':
                    pass
                else:
                    pagina = requests.get(link13.replace('=1', '=0'))
                    # passa a pagina para o BeautifulSoup verificar o texto no titulo <title>Dropbox - Error</title>
                    soup = BeautifulSoup(pagina.text, 'html.parser')
                    erro404 = soup.find_all('title')[0]
                    if str(erro404) == '<title>Dropbox - Error</title>':
                        texto_html = f""" <h3 style='color: #fff;'>Jogo: {titulo} | Cadastro: {data} | Erro: 404</h3>"""
                        link13_html = f"""<a style='color: #fff;' href='{link13}'>Link13: {link13}</a> """
                        self.ui.textBrowser_verifica404.append(texto_html)
                        self.ui.textBrowser_verifica404.append(link13_html)
                        contador_erros += 1
            except Exception as e:
                pass

        while query.next():  # TESTA LINK14 PLAYSTATION3
            self.ui.progressBar404.setValue(contador_progress)
            contador_progress += 1
            titulo = query.value(1)
            data = query.value(5).toPyDateTime().strftime('%d/%m/%Y')
            try:  # TESTA LINK14 PLAYSTATION3
                link14 = query.value(19)
                if link14 == '---' or link14 == '':
                    pass
                else:
                    pagina = requests.get(link14.replace('=1', '=0'))
                    # passa a pagina para o BeautifulSoup verificar o texto no titulo <title>Dropbox - Error</title>
                    soup = BeautifulSoup(pagina.text, 'html.parser')
                    erro404 = soup.find_all('title')[0]
                    if str(erro404) == '<title>Dropbox - Error</title>':
                        texto_html = f""" <h3 style='color: #fff;'>Jogo: {titulo} | Cadastro: {data} | Erro: 404</h3>"""
                        link14_html = f"""<a style='color: #fff;' href='{link14}'>Link14: {link14}</a> """
                        self.ui.textBrowser_verifica404.append(texto_html)
                        self.ui.textBrowser_verifica404.append(link14_html)
                        contador_erros += 1
            except Exception as e:
                pass

        while query.next():  # TESTA LINK15 PLAYSTATION3
            self.ui.progressBar404.setValue(contador_progress)
            contador_progress += 1
            titulo = query.value(1)
            data = query.value(5).toPyDateTime().strftime('%d/%m/%Y')
            try:  # TESTA LINK15 PLAYSTATION3
                link15 = query.value(20)
                if link15 == '---' or link15 == '':
                    pass
                else:
                    pagina = requests.get(link15.replace('=1', '=0'))
                    # passa a pagina para o BeautifulSoup verificar o texto no titulo <title>Dropbox - Error</title>
                    soup = BeautifulSoup(pagina.text, 'html.parser')
                    erro404 = soup.find_all('title')[0]
                    if str(erro404) == '<title>Dropbox - Error</title>':
                        texto_html = f""" <h3 style='color: #fff;'>Jogo: {titulo} | Cadastro: {data} | Erro: 404</h3>"""
                        link15_html = f"""<a style='color: #fff;' href='{link15}'>Link15: {link15}</a> """
                        self.ui.textBrowser_verifica404.append(texto_html)
                        self.ui.textBrowser_verifica404.append(link15_html)
                        contador_erros += 1
            except Exception as e:
                pass

        while query.next():  # TESTA LINK121 PLAYSTATION3
            self.ui.progressBar404.setValue(contador_progress)
            contador_progress += 1
            titulo = query.value(1)
            data = query.value(5).toPyDateTime().strftime('%d/%m/%Y')
            try:  # TESTA LINK121 PLAYSTATION3
                link121 = query.value(21)
                if link121 == '---' or link121 == '':
                    pass
                else:
                    pagina = requests.get(link121.replace('=1', '=0'))
                    # passa a pagina para o BeautifulSoup verificar o texto no titulo <title>Dropbox - Error</title>
                    soup = BeautifulSoup(pagina.text, 'html.parser')
                    erro404 = soup.find_all('title')[0]
                    if str(erro404) == '<title>Dropbox - Error</title>':
                        texto_html = f""" <h3 style='color: #fff;'>Jogo: {titulo} | Cadastro: {data} | Erro: 404</h3>"""
                        link121_html = f"""<a style='color: #fff;' href='{link121}'>Link121: {link121}</a> """
                        self.ui.textBrowser_verifica404.append(texto_html)
                        self.ui.textBrowser_verifica404.append(link121_html)
                        contador_erros += 1
            except Exception as e:
                pass

        while query.next():  # TESTA LINK17 PLAYSTATION3
            self.ui.progressBar404.setValue(contador_progress)
            contador_progress += 1
            titulo = query.value(1)
            data = query.value(5).toPyDateTime().strftime('%d/%m/%Y')
            try:  # TESTA LINK17 PLAYSTATION3
                link17 = query.value(22)
                if link17 == '---' or link17 == '':
                    pass
                else:
                    pagina = requests.get(link17.replace('=1', '=0'))
                    # passa a pagina para o BeautifulSoup verificar o texto no titulo <title>Dropbox - Error</title>
                    soup = BeautifulSoup(pagina.text, 'html.parser')
                    erro404 = soup.find_all('title')[0]
                    if str(erro404) == '<title>Dropbox - Error</title>':
                        texto_html = f""" <h3 style='color: #fff;'>Jogo: {titulo} | Cadastro: {data} | Erro: 404</h3>"""
                        link17_html = f"""<a style='color: #fff;' href='{link17}'>Link17: {link17}</a> """
                        self.ui.textBrowser_verifica404.append(texto_html)
                        self.ui.textBrowser_verifica404.append(link17_html)
                        contador_erros += 1
            except Exception as e:
                pass

        while query.next():  # TESTA LINK18 PLAYSTATION3
            self.ui.progressBar404.setValue(contador_progress)
            contador_progress += 1
            titulo = query.value(1)
            data = query.value(5).toPyDateTime().strftime('%d/%m/%Y')
            try:  # TESTA LINK18 PLAYSTATION3
                link18 = query.value(23)
                if link18 == '---' or link18 == '':
                    pass
                else:
                    pagina = requests.get(link18.replace('=1', '=0'))
                    # passa a pagina para o BeautifulSoup verificar o texto no titulo <title>Dropbox - Error</title>
                    soup = BeautifulSoup(pagina.text, 'html.parser')
                    erro404 = soup.find_all('title')[0]
                    if str(erro404) == '<title>Dropbox - Error</title>':
                        texto_html = f""" <h3 style='color: #fff;'>Jogo: {titulo} | Cadastro: {data} | Erro: 404</h3>"""
                        link18_html = f"""<a style='color: #fff;' href='{link18}'>Link18: {link18}</a> """
                        self.ui.textBrowser_verifica404.append(texto_html)
                        self.ui.textBrowser_verifica404.append(link18_html)
                        contador_erros += 1
            except Exception as e:
                pass

        while query.next():  # TESTA LINK19 PLAYSTATION3
            self.ui.progressBar404.setValue(contador_progress)
            contador_progress += 1
            titulo = query.value(1)
            data = query.value(5).toPyDateTime().strftime('%d/%m/%Y')
            try:  # TESTA LINK19 PLAYSTATION3
                link19 = query.value(24)
                if link19 == '---' or link19 == '':
                    pass
                else:
                    pagina = requests.get(link19.replace('=1', '=0'))
                    # passa a pagina para o BeautifulSoup verificar o texto no titulo <title>Dropbox - Error</title>
                    soup = BeautifulSoup(pagina.text, 'html.parser')
                    erro404 = soup.find_all('title')[0]
                    if str(erro404) == '<title>Dropbox - Error</title>':
                        texto_html = f""" <h3 style='color: #fff;'>Jogo: {titulo} | Cadastro: {data} | Erro: 404</h3>"""
                        link19_html = f"""<a style='color: #fff;' href='{link19}'>Link19: {link19}</a> """
                        self.ui.textBrowser_verifica404.append(texto_html)
                        self.ui.textBrowser_verifica404.append(link19_html)
                        contador_erros += 1
            except Exception as e:
                pass

        while query.next():  # TESTA LINK20 PLAYSTATION3
            self.ui.progressBar404.setValue(contador_progress)
            contador_progress += 1
            titulo = query.value(1)
            data = query.value(5).toPyDateTime().strftime('%d/%m/%Y')
            try:  # TESTA LINK20 PLAYSTATION3
                link20 = query.value(25)
                if link20 == '---' or link20 == '':
                    pass
                else:
                    pagina = requests.get(link20.replace('=1', '=0'))
                    # passa a pagina para o BeautifulSoup verificar o texto no titulo <title>Dropbox - Error</title>
                    soup = BeautifulSoup(pagina.text, 'html.parser')
                    erro404 = soup.find_all('title')[0]
                    if str(erro404) == '<title>Dropbox - Error</title>':
                        texto_html = f""" <h3 style='color: #fff;'>Jogo: {titulo} | Cadastro: {data} | Erro: 404</h3>"""
                        link20_html = f"""<a style='color: #fff;' href='{link20}'>Link20: {link20}</a> """
                        self.ui.textBrowser_verifica404.append(texto_html)
                        self.ui.textBrowser_verifica404.append(link20_html)
                        contador_erros += 1
            except Exception as e:
                pass

        while query.next():  # TESTA LINK21 PLAYSTATION3
            self.ui.progressBar404.setValue(contador_progress)
            contador_progress += 1
            titulo = query.value(1)
            data = query.value(5).toPyDateTime().strftime('%d/%m/%Y')
            try:  # TESTA LINK21 PLAYSTATION3
                link21 = query.value(26)
                if link21 == '---' or link21 == '':
                    pass
                else:
                    pagina = requests.get(link21.replace('=1', '=0'))
                    # passa a pagina para o BeautifulSoup verificar o texto no titulo <title>Dropbox - Error</title>
                    soup = BeautifulSoup(pagina.text, 'html.parser')
                    erro404 = soup.find_all('title')[0]
                    if str(erro404) == '<title>Dropbox - Error</title>':
                        texto_html = f""" <h3 style='color: #fff;'>Jogo: {titulo} | Cadastro: {data} | Erro: 404</h3>"""
                        link21_html = f"""<a style='color: #fff;' href='{link21}'>Link21: {link21}</a> """
                        self.ui.textBrowser_verifica404.append(texto_html)
                        self.ui.textBrowser_verifica404.append(link21_html)
                        contador_erros += 1
            except Exception as e:
                pass

        while query.next():  # TESTA LINK22 PLAYSTATION3
            self.ui.progressBar404.setValue(contador_progress)
            contador_progress += 1
            titulo = query.value(1)
            data = query.value(5).toPyDateTime().strftime('%d/%m/%Y')
            try:  # TESTA LINK22 PLAYSTATION3
                link22 = query.value(27)
                if link22 == '---' or link22 == '':
                    pass
                else:
                    pagina = requests.get(link22.replace('=1', '=0'))
                    # passa a pagina para o BeautifulSoup verificar o texto no titulo <title>Dropbox - Error</title>
                    soup = BeautifulSoup(pagina.text, 'html.parser')
                    erro404 = soup.find_all('title')[0]
                    if str(erro404) == '<title>Dropbox - Error</title>':
                        texto_html = f""" <h3 style='color: #fff;'>Jogo: {titulo} | Cadastro: {data} | Erro: 404</h3>"""
                        link22_html = f"""<a style='color: #fff;' href='{link22}'>Link22: {link22}</a> """
                        self.ui.textBrowser_verifica404.append(texto_html)
                        self.ui.textBrowser_verifica404.append(link22_html)
                        contador_erros += 1
            except Exception as e:
                pass

        while query.next():  # TESTA LINK23 PLAYSTATION3
            self.ui.progressBar404.setValue(contador_progress)
            contador_progress += 1
            titulo = query.value(1)
            data = query.value(5).toPyDateTime().strftime('%d/%m/%Y')
            try:  # TESTA LINK23 PLAYSTATION3
                link23 = query.value(28)
                if link23 == '---' or link23 == '':
                    pass
                else:
                    pagina = requests.get(link23.replace('=1', '=0'))
                    # passa a pagina para o BeautifulSoup verificar o texto no titulo <title>Dropbox - Error</title>
                    soup = BeautifulSoup(pagina.text, 'html.parser')
                    erro404 = soup.find_all('title')[0]
                    if str(erro404) == '<title>Dropbox - Error</title>':
                        texto_html = f""" <h3 style='color: #fff;'>Jogo: {titulo} | Cadastro: {data} | Erro: 404</h3>"""
                        link23_html = f"""<a style='color: #fff;' href='{link23}'>Link23: {link23}</a> """
                        self.ui.textBrowser_verifica404.append(texto_html)
                        self.ui.textBrowser_verifica404.append(link23_html)
                        contador_erros += 1
            except Exception as e:
                pass

        while query.next():  # TESTA LINK24 PLAYSTATION3
            self.ui.progressBar404.setValue(contador_progress)
            contador_progress += 1
            titulo = query.value(1)
            data = query.value(5).toPyDateTime().strftime('%d/%m/%Y')
            try:  # TESTA LINK24 PLAYSTATION3
                link24 = query.value(29)
                if link24 == '---' or link24 == '':
                    pass
                else:
                    pagina = requests.get(link24.replace('=1', '=0'))
                    # passa a pagina para o BeautifulSoup verificar o texto no titulo <title>Dropbox - Error</title>
                    soup = BeautifulSoup(pagina.text, 'html.parser')
                    erro404 = soup.find_all('title')[0]
                    if str(erro404) == '<title>Dropbox - Error</title>':
                        texto_html = f""" <h3 style='color: #fff;'>Jogo: {titulo} | Cadastro: {data} | Erro: 404</h3>"""
                        link24_html = f"""<a style='color: #fff;' href='{link24}'>Link24: {link24}</a> """
                        self.ui.textBrowser_verifica404.append(texto_html)
                        self.ui.textBrowser_verifica404.append(link24_html)
                        contador_erros += 1
            except Exception as e:
                pass

        while query.next():  # TESTA LINK25 PLAYSTATION3
            self.ui.progressBar404.setValue(contador_progress)
            contador_progress += 1
            titulo = query.value(1)
            data = query.value(5).toPyDateTime().strftime('%d/%m/%Y')
            try:  # TESTA LINK25 PLAYSTATION3
                link25 = query.value(30)
                if link25 == '---' or link25 == '':
                    pass
                else:
                    pagina = requests.get(link25.replace('=1', '=0'))
                    # passa a pagina para o BeautifulSoup verificar o texto no titulo <title>Dropbox - Error</title>
                    soup = BeautifulSoup(pagina.text, 'html.parser')
                    erro404 = soup.find_all('title')[0]
                    if str(erro404) == '<title>Dropbox - Error</title>':
                        texto_html = f""" <h3 style='color: #fff;'>Jogo: {titulo} | Cadastro: {data} | Erro: 404</h3>"""
                        link25_html = f"""<a style='color: #fff;' href='{link25}'>Link25: {link25}</a> """
                        self.ui.textBrowser_verifica404.append(texto_html)
                        self.ui.textBrowser_verifica404.append(link25_html)
                        contador_erros += 1
            except Exception as e:
                pass

        while query.next():  # TESTA LINK231 PLAYSTATION3
            self.ui.progressBar404.setValue(contador_progress)
            contador_progress += 1
            titulo = query.value(1)
            data = query.value(5).toPyDateTime().strftime('%d/%m/%Y')
            try:  # TESTA LINK231 PLAYSTATION3
                link231 = query.value(31)
                if link231 == '---' or link231 == '':
                    pass
                else:
                    pagina = requests.get(link231.replace('=1', '=0'))
                    # passa a pagina para o BeautifulSoup verificar o texto no titulo <title>Dropbox - Error</title>
                    soup = BeautifulSoup(pagina.text, 'html.parser')
                    erro404 = soup.find_all('title')[0]
                    if str(erro404) == '<title>Dropbox - Error</title>':
                        texto_html = f""" <h3 style='color: #fff;'>Jogo: {titulo} | Cadastro: {data} | Erro: 404</h3>"""
                        link231_html = f"""<a style='color: #fff;' href='{link231}'>Link231: {link231}</a> """
                        self.ui.textBrowser_verifica404.append(texto_html)
                        self.ui.textBrowser_verifica404.append(link231_html)
                        contador_erros += 1
            except Exception as e:
                pass

        while query.next():  # TESTA LINK27 PLAYSTATION3
            self.ui.progressBar404.setValue(contador_progress)
            contador_progress += 1
            titulo = query.value(1)
            data = query.value(5).toPyDateTime().strftime('%d/%m/%Y')
            try:  # TESTA LINK27 PLAYSTATION3
                link27 = query.value(32)
                if link27 == '---' or link27 == '':
                    pass
                else:
                    pagina = requests.get(link27.replace('=1', '=0'))
                    # passa a pagina para o BeautifulSoup verificar o texto no titulo <title>Dropbox - Error</title>
                    soup = BeautifulSoup(pagina.text, 'html.parser')
                    erro404 = soup.find_all('title')[0]
                    if str(erro404) == '<title>Dropbox - Error</title>':
                        texto_html = f""" <h3 style='color: #fff;'>Jogo: {titulo} | Cadastro: {data} | Erro: 404</h3>"""
                        link27_html = f"""<a style='color: #fff;' href='{link27}'>Link27: {link27}</a> """
                        self.ui.textBrowser_verifica404.append(texto_html)
                        self.ui.textBrowser_verifica404.append(link27_html)
                        contador_erros += 1
            except Exception as e:
                pass

        while query.next():  # TESTA LINK28 PLAYSTATION3
            self.ui.progressBar404.setValue(contador_progress)
            contador_progress += 1
            titulo = query.value(1)
            data = query.value(5).toPyDateTime().strftime('%d/%m/%Y')
            try:  # TESTA LINK28 PLAYSTATION3
                link28 = query.value(33)
                if link28 == '---' or link28 == '':
                    pass
                else:
                    pagina = requests.get(link28.replace('=1', '=0'))
                    # passa a pagina para o BeautifulSoup verificar o texto no titulo <title>Dropbox - Error</title>
                    soup = BeautifulSoup(pagina.text, 'html.parser')
                    erro404 = soup.find_all('title')[0]
                    if str(erro404) == '<title>Dropbox - Error</title>':
                        texto_html = f""" <h3 style='color: #fff;'>Jogo: {titulo} | Cadastro: {data} | Erro: 404</h3>"""
                        link28_html = f"""<a style='color: #fff;' href='{link28}'>Link28: {link28}</a> """
                        self.ui.textBrowser_verifica404.append(texto_html)
                        self.ui.textBrowser_verifica404.append(link28_html)
                        contador_erros += 1
            except Exception as e:
                pass

        while query.next():  # TESTA LINK29 PLAYSTATION3
            self.ui.progressBar404.setValue(contador_progress)
            contador_progress += 1
            titulo = query.value(1)
            data = query.value(5).toPyDateTime().strftime('%d/%m/%Y')
            try:  # TESTA LINK29 PLAYSTATION3
                link29 = query.value(34)
                if link29 == '---' or link29 == '':
                    pass
                else:
                    pagina = requests.get(link29.replace('=1', '=0'))
                    # passa a pagina para o BeautifulSoup verificar o texto no titulo <title>Dropbox - Error</title>
                    soup = BeautifulSoup(pagina.text, 'html.parser')
                    erro404 = soup.find_all('title')[0]
                    if str(erro404) == '<title>Dropbox - Error</title>':
                        texto_html = f""" <h3 style='color: #fff;'>Jogo: {titulo} | Cadastro: {data} | Erro: 404</h3>"""
                        link29_html = f"""<a style='color: #fff;' href='{link29}'>Link29: {link29}</a> """
                        self.ui.textBrowser_verifica404.append(texto_html)
                        self.ui.textBrowser_verifica404.append(link29_html)
                        contador_erros += 1
            except Exception as e:
                pass

        while query.next():  # TESTA LINK30 PLAYSTATION3
            self.ui.progressBar404.setValue(contador_progress)
            contador_progress += 1
            titulo = query.value(1)
            data = query.value(5).toPyDateTime().strftime('%d/%m/%Y')
            try:  # TESTA LINK30 PLAYSTATION3
                link30 = query.value(35)
                if link30 == '---' or link30 == '':
                    pass
                else:
                    pagina = requests.get(link30.replace('=1', '=0'))
                    # passa a pagina para o BeautifulSoup verificar o texto no titulo <title>Dropbox - Error</title>
                    soup = BeautifulSoup(pagina.text, 'html.parser')
                    erro404 = soup.find_all('title')[0]
                    if str(erro404) == '<title>Dropbox - Error</title>':
                        texto_html = f""" <h3 style='color: #fff;'>Jogo: {titulo} | Cadastro: {data} | Erro: 404</h3>"""
                        link30_html = f"""<a style='color: #fff;' href='{link30}'>Link30: {link30}</a> """
                        self.ui.textBrowser_verifica404.append(texto_html)
                        self.ui.textBrowser_verifica404.append(link30_html)
                        contador_erros += 1
            except Exception as e:
                pass



    #fim do loop testando os links da database | exibe o aviso final
        self.ui.textBrowser_verifica404.append(f"<h2 style='color: rgb(170,0,0);'>TOTAL DE ERROS: {contador_erros}</h2>")
        self.ui.textBrowser_verifica404.append(f"<h2 style='color: rgb(170,0,0);'>TODOS LINKS DE PS3 FORAM VERIFICADOS</h2>")