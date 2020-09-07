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
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
import cvlib as cv
import cv2
from PIL import Image, ImageQt
import subprocess
import sys
import time
#importaçoes pessoais-------------->
from mainwindow import Ui_MainWindow
from funcoes import menus
from funcoes import home
from funcoes import  cadastro_users

class MainWindow(QMainWindow):
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

    # limpa os campos da pagina Cadastro usuarios
    def limpaNomeCadastro(self, event):
        self.ui.input_nome_user.clear()
    def limpaUserCadastro(self, event):
        self.ui.input_username_user.clear()
    def limpaSenhaCadastro(self, event):
        self.ui.input_senha_user.clear()





    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.clic= pyqtSignal()
        #menus------------->
        self.movimentoMouse()
        menus.menusJanela(self)
        #funcoes------------>
        home.funcoesHome(self)
        cadastro_users.funcoesCadastroUsers(self)










if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
