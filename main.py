#!/usr/bin/env python
# -*- coding: utf-8 -*-
#███╗   ███╗ █████╗ ███╗   ██╗██╗ ██████╗ ██████╗ ███╗   ███╗██╗ ██████╗
#████╗ ████║██╔══██╗████╗  ██║██║██╔════╝██╔═══██╗████╗ ████║██║██╔═══██╗
#██╔████╔██║███████║██╔██╗ ██║██║██║     ██║   ██║██╔████╔██║██║██║   ██║
#██║╚██╔╝██║██╔══██║██║╚██╗██║██║██║     ██║   ██║██║╚██╔╝██║██║██║   ██║
#██║ ╚═╝ ██║██║  ██║██║ ╚████║██║╚██████╗╚██████╔╝██║ ╚═╝ ██║██║╚██████╔╝
#╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝
#            @GorpoOrko | Manicomio TCXS Project | 2020

"""Anotações:

criar arquivo mainwindow.py:
    pyuic5 -x mainwindow.ui -o mainwindow.py

criar arquivo files_rc_rc.py
    pyrcc5 -o files_rc_rc.py files_rc.qrc

#necessario para rodar o QMysql do Pyqt5 versao | PyQT5==5.12  | pyqtwebengine==5.12


usando uma progress bar  (crie um contador)
self.ui.progressBar404.setValue(contador_progress)
contador_progress += 1


sempre que quisermos chamar um stackedWidget usamos o comando abaixo e mudar sua "indexação"
    self.ui.stackedWidget.setCurrentIndex(1)

usando o sistema para chamar os arquivos do layout:
    self.ui.string_do_objeto


Exemplo de layout limpo:
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QFile
from mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):

    # --------------FUNÇÃO DE INICIO
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
"""
from PyQt5 import QtCore, QtGui, QtWidgets,QtWebEngineWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PIL import Image, ImageQt
import subprocess
import sys
import time
import sqlite3
import sys
import os
from funcoes import conexao
from PyQt5 import QtSql
from PyQt5 import QtCore
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QMessageBox
import sys
import time
from PyQt5.QtWidgets import QApplication, QDialog,  QProgressBar, QPushButton
from funcoes import conexao
from PyQt5 import QtSql
from PyQt5 import QtCore
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QMessageBox
import requests
from bs4 import BeautifulSoup
from funcoes import conexao
from PyQt5 import QtSql
from PyQt5 import QtCore
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QMessageBox
from PIL import Image
import ftplib
import os
from datetime import datetime


#importaçoes pessoais-------------->
from mainwindow import Ui_MainWindow
from funcoes.db_handler import criaDbLocal
from funcoes import menus
from funcoes import home
from funcoes import cadastro_users
from funcoes import consulta_users
from funcoes import cadastro_infos
from funcoes import cadastro_psp
from funcoes import cadastro_ps1
from funcoes import cadastro_ps2
from funcoes import cadastro_ps3
from funcoes import cadastro_retro
from funcoes import cadastro_extras
from funcoes import verificar_databases
from funcoes import verificador404

class MainWindow(QMainWindow):
    #funções de clicar e movimentar a tela com mouse
    def movimentoMouse(self):
        self.mwidget = QMainWindow(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # remove a barra
        self.center()
        # cria uma falsa label em todo objeto para poder ser movido
        self.lbl = QLabel(self)
        # self.lbl.setText("cria um texto para achar a label, pois ali em baixo sumi com ela da tela")
        self.lbl.setGeometry(-50, -50, 60, 40)
        self.oldPos = self.pos()
        self.show()
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()
    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        # print(delta)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


    #limpa os campos da homepage
    def limpaNomedb(self,event):
        self.ui.input_nome_database_home.clear()
    def limpaUserdb(self,event):
        self.ui.input_user_database_home.clear()
    def limpaSenhadb(self,event):
        self.ui.input_senha_database_home.clear()
    def limpaHostdb(self,event):
        self.ui.input_host_database_home.clear()
    def limpaEnderecoFtp(self,event):
        self.ui.input_endereco_ftp.clear()
    def limpaUserFtp(self,event):
        self.ui.input_user_ftp.clear()
    def limpaSenhaFtp(self,event):
        self.ui.input_senha_ftp.clear()

    # limpa os campos da pagina Cadastro usuarios
    def limpaNomeCadastro(self, event):
        self.ui.input_nome_user.clear()
    def limpaUserCadastro(self, event):
        self.ui.input_username_user.clear()
    def limpaSenhaCadastro(self, event):
        self.ui.input_senha_user.clear()

    #limpa campos input_pesquisa_acessos_usuarios
    def limpaPesquisaAcessoUsers(self, event):
        self.ui.input_pesquisa_acessos_usuarios.clear()
    #limpa campos input_playstation_infos
    def limpaInputInfos(self, event):
        self.ui.input_playstation_infos.clear()

    # limpa campos input_playstation_psp
    def limpaInputTitulopsp(self, event):
        self.ui.input_titulo_jogo_psp.clear()
    def limpaInputDescricaopsp(self, event):
        self.ui.input_descricao_jogo_psp.clear()
    def limpaInputContentidpsp(self, event):
        self.ui.input_contentid_psp.clear()
    def limpaInputLinkpsp(self, event):
        self.ui.input_link_jogo_psp.clear()

    # limpa campos input_playstation_ps1
    def limpaInputTitulops1(self, event):
        self.ui.input_titulo_ps1.clear()
    def limpaInputDescricaops1(self, event):
        self.ui.input_descricao_ps1.clear()
    def limpaInputContentidps1(self, event):
        self.ui.input_contentid_ps1.clear()
    def limpaInputLinkps1(self, event):
        self.ui.input_link_ps1.clear()
    # limpa campos input_playstation_ps2
    def limpaInputTitulops2(self, event):
        self.ui.input_titulo_ps2.clear()
    def limpaInputDescricaops2(self, event):
        self.ui.input_descricao_ps2.clear()
    def limpaInputContentidps2(self, event):
        self.ui.input_contentid_ps2.clear()
    def limpaInputLinkps2(self, event):
        self.ui.input_link_ps2.clear()

    # limpa campos input_playstation_ps3
    def limpaInputTitulops3(self, event):
        self.ui.input_titulo_ps3.clear()
    def limpaInputDescricaops3(self, event):
        self.ui.input_descricao_ps3.clear()
    def limpaInputContentidps3(self, event):
        self.ui.input_content_id_ps3.clear()

    def limpaInputLink1ps3(self, event):
        self.ui.input_link1_ps3.clear()

    def limpaInputLink2ps3(self, event):
        self.ui.input_link2_ps3.clear()

    def limpaInputLink3ps3(self, event):
        self.ui.input_link3_ps3.clear()

    def limpaInputLink4ps3(self, event):
        self.ui.input_link4_ps3.clear()

    def limpaInputLink5ps3(self, event):
        self.ui.input_link5_ps3.clear()

    def limpaInputLink6ps3(self, event):
        self.ui.input_link6_ps3.clear()

    def limpaInputLink7ps3(self, event):
        self.ui.input_link7_ps3.clear()

    def limpaInputLink8ps3(self, event):
        self.ui.input_link8_ps3.clear()

    def limpaInputLink9ps3(self, event):
        self.ui.input_link9_ps3.clear()

    def limpaInputLink10ps3(self, event):
        self.ui.input_link10_ps3.clear()

    def limpaInputLink11ps3(self, event):
        self.ui.input_link11_ps3.clear()

    def limpaInputLink12ps3(self, event):
        self.ui.input_link12_ps3.clear()

    def limpaInputLink13ps3(self, event):
        self.ui.input_link13_ps3.clear()

    def limpaInputLink14ps3(self, event):
        self.ui.input_link14_ps3.clear()

    def limpaInputLink15ps3(self, event):
        self.ui.input_link15_ps3.clear()

    def limpaInputLink16ps3(self, event):
        self.ui.input_link16_ps3.clear()

    def limpaInputLink17ps3(self, event):
        self.ui.input_link17_ps3.clear()

    def limpaInputLink18ps3(self, event):
        self.ui.input_link18_ps3.clear()

    def limpaInputLink19ps3(self, event):
        self.ui.input_link19_ps3.clear()

    def limpaInputLink20ps3(self, event):
        self.ui.input_link20_ps3.clear()

    def limpaInputLink21ps3(self, event):
        self.ui.input_link21_ps3.clear()

    def limpaInputLink22ps3(self, event):
        self.ui.input_link22_ps3.clear()

    def limpaInputLink23ps3(self, event):
        self.ui.input_link23_ps3.clear()

    def limpaInputLink24ps3(self, event):
        self.ui.input_link24_ps3.clear()

    def limpaInputLink25ps3(self, event):
        self.ui.input_link25_ps3.clear()

    def limpaInputLink26ps3(self, event):
        self.ui.input_link26_ps3.clear()

    def limpaInputLink27ps3(self, event):
        self.ui.input_link27_ps3.clear()

    def limpaInputLink28ps3(self, event):
        self.ui.input_link28_ps3.clear()

    def limpaInputLink29ps3(self, event):
        self.ui.input_link29_ps3.clear()

    def limpaInputLink30ps3(self, event):
        self.ui.input_link30_ps3.clear()


    # limpa campos input_playstation_retro
    def limpaInputTituloretro(self, event):
        self.ui.input_titulo_retro.clear()
    def limpaInputDescricaoretro(self, event):
        self.ui.input_descricao_retro.clear()
    def limpaInputContentidretro(self, event):
        self.ui.input_contentid_retro.clear()
    def limpaInputLinkretro(self, event):
        self.ui.input_link_retro.clear()

    # limpa campos input_playstation_extras
    def limpaInputTituloextras(self, event):
        self.ui.input_titulo_extras.clear()
    def limpaInputDescricaoextras(self, event):
        self.ui.input_descricao_extras.clear()
    def limpaInputContentidextras(self, event):
        self.ui.input_contentid_extras.clear()
    def limpaInputLinkextras(self, event):
        self.ui.input_link_extras.clear()





    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.clic= pyqtSignal()
        #menus------------->
        self.movimentoMouse()
        menus.menusJanela(self)
        #estilos --------->
        self.setStyleSheet(""" QToolTip{ border: 1px solid rgb(45,45,45);
                                        border-radius: 2px;
                                        background-color: rgb(30,30,30);
                                        color: rgb(203, 203, 203);}""")
        #instruções
        self.ui.titulo_programa.setToolTip("""PAINEL ADMINISTRADOR TCXS PROJECT STORE 

versão: 1.0
desenvolvedor: @GorpoOrko
linguagem: Python

1. Sobre a conexão com a Database MySql e sistema de FTP.
    1.1 Necessário os dados da database: database | usuário | senha | host.
    1.2 Necessário os dados sistema FTP: endereço | usuário | senha.
    1.3 Caso estes dados sejam inseridos não será feita conexão e não será possivel edição.
    1.4 Os dados são salvos em uma database local, sendo necessário inserir eles apenas uma vez.
    1.5 Caso os dados do servidor atualizem, atualize os dados no inicio do programa.
    1.6 Caso não conecte após atualizar os dados, feche e abra novamente o programa.

2. Sobre o cadastro de usuários e consulta:
    2.1 Necessário os dados: Nome | user | senha - [Permite] cadastrar | atualizar | deletar.
    2.2 Necessário user que o usuário faz login - [Permite] apenas consultas (clean tables).

3. Sobre o cadastro de jogos e extras:
    3.1 Necessário os dados: Titulo | Descrição | Content ID | Imagem | Link 
    3.2 [Permite] cadastrar | atualizar | deletar | upload imagem FTP(resize, borda automatica).
    3.3 [ATENÇÃO] na descrição usar a tag <br> para pular linhas conforme exemplo:
    3.4 [EXEMPLO] Idioma: Ingles<br>Legenda: Ingles<br>Plataforma: PlayStation3

4. Sobre a conexão do Bot Telegram:
    4.1 Necessário os dados do Telegram: token bot | id canal | sua id
    4.2 O bot só funciona enquanto o programa estiver aberto e ele ativado pelo programa.

5. Sobre o verificador da database:
    5.1 Verifica todos os bancos de dados a procura de erros, apenas visualização e conferência.

6. Sobre o verificador 404:
    6.1 Crawler que busca todos os erros 404 e os apresenta para que possam ser alterados na loja.
    6.2 Este processo é demorado e o programa deve estar sendo usado exclusivamente para ele.
    6.3 Como este processo verifica link por link demora e podem ocorrer travas ou falhas.
    6.4 Aconselho que links quebrados sejam arrumados para que não apareçam na proxima verificação.""")
        #funcoes------------>
        home.funcoesHome(self)
        cadastro_users.funcoesCadastroUsers(self)
        consulta_users.funcoesConsultaUsers(self)
        cadastro_infos.funcoesCadastroInfos(self)
        cadastro_psp.funcoesCadastroPSP(self)
        cadastro_ps1.funcoesCadastroPS1(self)
        cadastro_ps2.funcoesCadastroPS2(self)
        cadastro_ps3.funcoesCadastroPS3(self)
        cadastro_retro.funcoesCadastroRETRO(self)
        cadastro_extras.funcoesCadastroEXTRAS(self)
        verificar_databases.verificarDatabase(self)
        verificador404.verificar404(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
