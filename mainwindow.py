# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(897, 700)
        self.janela_pai = QtWidgets.QWidget(MainWindow)
        self.janela_pai.setObjectName("janela_pai")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.janela_pai)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.menuTopo = QtWidgets.QFrame(self.janela_pai)
        self.menuTopo.setMaximumSize(QtCore.QSize(16777215, 45))
        self.menuTopo.setStyleSheet("background-color: rgb(31, 31, 31);")
        self.menuTopo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.menuTopo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menuTopo.setObjectName("menuTopo")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.menuTopo)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_abre_menu = QtWidgets.QFrame(self.menuTopo)
        self.frame_abre_menu.setMinimumSize(QtCore.QSize(50, 0))
        self.frame_abre_menu.setMaximumSize(QtCore.QSize(50, 50))
        self.frame_abre_menu.setStyleSheet("background-color: rgb(31,31,31);")
        self.frame_abre_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_abre_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_abre_menu.setObjectName("frame_abre_menu")
        self.botao_abrir_menu = QtWidgets.QPushButton(self.frame_abre_menu)
        self.botao_abrir_menu.setGeometry(QtCore.QRect(-10, -1, 75, 50))
        self.botao_abrir_menu.setMinimumSize(QtCore.QSize(50, 50))
        self.botao_abrir_menu.setStyleSheet("QPushButton {\n"
"    background-image: url(:/abre_menu/images/menu-4-24.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.botao_abrir_menu.setText("")
        self.botao_abrir_menu.setObjectName("botao_abrir_menu")
        self.horizontalLayout_2.addWidget(self.frame_abre_menu)
        self.frame_informacoes = QtWidgets.QFrame(self.menuTopo)
        self.frame_informacoes.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_informacoes.setStyleSheet("background-color: rgb(31,31,31);")
        self.frame_informacoes.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_informacoes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_informacoes.setObjectName("frame_informacoes")
        self.titulo_programa = QtWidgets.QLabel(self.frame_informacoes)
        self.titulo_programa.setGeometry(QtCore.QRect(10, 0, 192, 41))
        self.titulo_programa.setMinimumSize(QtCore.QSize(192, 0))
        self.titulo_programa.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"}")
        self.titulo_programa.setObjectName("titulo_programa")
        self.horizontalLayout_2.addWidget(self.frame_informacoes)
        self.frame_minimizar = QtWidgets.QFrame(self.menuTopo)
        self.frame_minimizar.setMinimumSize(QtCore.QSize(50, 50))
        self.frame_minimizar.setMaximumSize(QtCore.QSize(50, 50))
        self.frame_minimizar.setStyleSheet("background-color: rgb(31,31,31);")
        self.frame_minimizar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_minimizar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_minimizar.setObjectName("frame_minimizar")
        self.botao_minimizar = QtWidgets.QPushButton(self.frame_minimizar)
        self.botao_minimizar.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.botao_minimizar.setStyleSheet("QPushButton {\n"
"    background-image: url(:/minimizar/images/minimize.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.botao_minimizar.setText("")
        self.botao_minimizar.setObjectName("botao_minimizar")
        self.horizontalLayout_2.addWidget(self.frame_minimizar)
        self.frame_maximizar = QtWidgets.QFrame(self.menuTopo)
        self.frame_maximizar.setMinimumSize(QtCore.QSize(50, 50))
        self.frame_maximizar.setMaximumSize(QtCore.QSize(50, 50))
        self.frame_maximizar.setStyleSheet("background-color: rgb(31,31,31);")
        self.frame_maximizar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_maximizar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_maximizar.setObjectName("frame_maximizar")
        self.botao_maximizar = QtWidgets.QPushButton(self.frame_maximizar)
        self.botao_maximizar.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.botao_maximizar.setStyleSheet("QPushButton {\n"
"    \n"
"    background-image: url(:/maximizar/images/icons8-toggle-full-screen-24.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.botao_maximizar.setText("")
        self.botao_maximizar.setObjectName("botao_maximizar")
        self.horizontalLayout_2.addWidget(self.frame_maximizar)
        self.frame_fechar = QtWidgets.QFrame(self.menuTopo)
        self.frame_fechar.setMinimumSize(QtCore.QSize(50, 50))
        self.frame_fechar.setMaximumSize(QtCore.QSize(50, 50))
        self.frame_fechar.setStyleSheet("background-color: rgb(31,31,31);")
        self.frame_fechar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_fechar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_fechar.setObjectName("frame_fechar")
        self.botao_fechar = QtWidgets.QPushButton(self.frame_fechar)
        self.botao_fechar.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.botao_fechar.setStyleSheet("QPushButton {\n"
"    background-image: url(:/fechar/images/icons8-delete-24.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.botao_fechar.setText("")
        self.botao_fechar.setObjectName("botao_fechar")
        self.horizontalLayout_2.addWidget(self.frame_fechar)
        self.verticalLayout.addWidget(self.menuTopo)
        self.conteiner_central = QtWidgets.QFrame(self.janela_pai)
        self.conteiner_central.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.conteiner_central.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.conteiner_central.setFrameShadow(QtWidgets.QFrame.Raised)
        self.conteiner_central.setObjectName("conteiner_central")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.conteiner_central)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.menu_esquerda = QtWidgets.QFrame(self.conteiner_central)
        self.menu_esquerda.setMinimumSize(QtCore.QSize(50, 0))
        self.menu_esquerda.setMaximumSize(QtCore.QSize(50, 16777215))
        self.menu_esquerda.setStyleSheet("background-color: rgb(31, 31, 31);")
        self.menu_esquerda.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.menu_esquerda.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_esquerda.setObjectName("menu_esquerda")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.menu_esquerda)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.menu_home = QtWidgets.QFrame(self.menu_esquerda)
        self.menu_home.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QFrame:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.menu_home.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_home.setObjectName("menu_home")
        self.botao_home = QtWidgets.QPushButton(self.menu_home)
        self.botao_home.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.botao_home.setStyleSheet("QPushButton {\n"
"    background-image: url(:/home/images/home-5-24.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.botao_home.setText("")
        self.botao_home.setObjectName("botao_home")
        self.texto_menu_home = QtWidgets.QLabel(self.menu_home)
        self.texto_menu_home.setGeometry(QtCore.QRect(60, -1, 191, 51))
        self.texto_menu_home.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"}")
        self.texto_menu_home.setObjectName("texto_menu_home")
        self.verticalLayout_7.addWidget(self.menu_home)
        self.menu_cadastro_user = QtWidgets.QFrame(self.menu_esquerda)
        self.menu_cadastro_user.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QFrame:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.menu_cadastro_user.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_cadastro_user.setObjectName("menu_cadastro_user")
        self.botao_cadastro_user = QtWidgets.QPushButton(self.menu_cadastro_user)
        self.botao_cadastro_user.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.botao_cadastro_user.setStyleSheet("QPushButton {\n"
"background-image: url(:/user/images/userrrrrrr.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.botao_cadastro_user.setText("")
        self.botao_cadastro_user.setObjectName("botao_cadastro_user")
        self.texto_botao_cadastro_user = QtWidgets.QLabel(self.menu_cadastro_user)
        self.texto_botao_cadastro_user.setGeometry(QtCore.QRect(60, -1, 191, 51))
        self.texto_botao_cadastro_user.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"}")
        self.texto_botao_cadastro_user.setObjectName("texto_botao_cadastro_user")
        self.verticalLayout_7.addWidget(self.menu_cadastro_user)
        self.menu_verifica_user = QtWidgets.QFrame(self.menu_esquerda)
        self.menu_verifica_user.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QFrame:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.menu_verifica_user.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_verifica_user.setObjectName("menu_verifica_user")
        self.botao_verifica_user = QtWidgets.QPushButton(self.menu_verifica_user)
        self.botao_verifica_user.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.botao_verifica_user.setStyleSheet("QPushButton {\n"
"background-image: url(:/verUSER/images/veruser.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.botao_verifica_user.setText("")
        self.botao_verifica_user.setObjectName("botao_verifica_user")
        self.texto_botao_verifica_user = QtWidgets.QLabel(self.menu_verifica_user)
        self.texto_botao_verifica_user.setGeometry(QtCore.QRect(60, -1, 191, 51))
        self.texto_botao_verifica_user.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"}")
        self.texto_botao_verifica_user.setObjectName("texto_botao_verifica_user")
        self.verticalLayout_7.addWidget(self.menu_verifica_user)
        self.menu_infos_store = QtWidgets.QFrame(self.menu_esquerda)
        self.menu_infos_store.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QFrame:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.menu_infos_store.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_infos_store.setObjectName("menu_infos_store")
        self.botao_infos_store = QtWidgets.QPushButton(self.menu_infos_store)
        self.botao_infos_store.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.botao_infos_store.setStyleSheet("QPushButton {\n"
"    \n"
"background-image: url(:/ps/images/ps.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.botao_infos_store.setText("")
        self.botao_infos_store.setObjectName("botao_infos_store")
        self.texto_botao_infos_store = QtWidgets.QLabel(self.menu_infos_store)
        self.texto_botao_infos_store.setGeometry(QtCore.QRect(60, -1, 191, 51))
        self.texto_botao_infos_store.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"}")
        self.texto_botao_infos_store.setObjectName("texto_botao_infos_store")
        self.verticalLayout_7.addWidget(self.menu_infos_store)
        self.menu_psp = QtWidgets.QFrame(self.menu_esquerda)
        self.menu_psp.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QFrame:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.menu_psp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_psp.setObjectName("menu_psp")
        self.botao_menu_psp = QtWidgets.QPushButton(self.menu_psp)
        self.botao_menu_psp.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.botao_menu_psp.setStyleSheet("QPushButton {\n"
"background-image: url(:/ps/images/ps.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.botao_menu_psp.setText("")
        self.botao_menu_psp.setObjectName("botao_menu_psp")
        self.texto_menu_psp = QtWidgets.QLabel(self.menu_psp)
        self.texto_menu_psp.setGeometry(QtCore.QRect(60, -1, 191, 51))
        self.texto_menu_psp.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"}")
        self.texto_menu_psp.setObjectName("texto_menu_psp")
        self.verticalLayout_7.addWidget(self.menu_psp)
        self.menu_ps1 = QtWidgets.QFrame(self.menu_esquerda)
        self.menu_ps1.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QFrame:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.menu_ps1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_ps1.setObjectName("menu_ps1")
        self.botao_menu_ps1 = QtWidgets.QPushButton(self.menu_ps1)
        self.botao_menu_ps1.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.botao_menu_ps1.setStyleSheet("QPushButton {\n"
"background-image: url(:/ps/images/ps.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.botao_menu_ps1.setText("")
        self.botao_menu_ps1.setObjectName("botao_menu_ps1")
        self.texto_menu_ps1 = QtWidgets.QLabel(self.menu_ps1)
        self.texto_menu_ps1.setGeometry(QtCore.QRect(60, -1, 191, 51))
        self.texto_menu_ps1.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"}")
        self.texto_menu_ps1.setObjectName("texto_menu_ps1")
        self.verticalLayout_7.addWidget(self.menu_ps1)
        self.menu_ps2 = QtWidgets.QFrame(self.menu_esquerda)
        self.menu_ps2.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QFrame:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.menu_ps2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_ps2.setObjectName("menu_ps2")
        self.botao_menu_ps2 = QtWidgets.QPushButton(self.menu_ps2)
        self.botao_menu_ps2.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.botao_menu_ps2.setStyleSheet("QPushButton {\n"
"background-image: url(:/ps/images/ps.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.botao_menu_ps2.setText("")
        self.botao_menu_ps2.setObjectName("botao_menu_ps2")
        self.texto_menu_ps2 = QtWidgets.QLabel(self.menu_ps2)
        self.texto_menu_ps2.setGeometry(QtCore.QRect(60, -1, 191, 51))
        self.texto_menu_ps2.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"}")
        self.texto_menu_ps2.setObjectName("texto_menu_ps2")
        self.verticalLayout_7.addWidget(self.menu_ps2)
        self.menu_ps3 = QtWidgets.QFrame(self.menu_esquerda)
        self.menu_ps3.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QFrame:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.menu_ps3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_ps3.setObjectName("menu_ps3")
        self.botao_menu_ps3 = QtWidgets.QPushButton(self.menu_ps3)
        self.botao_menu_ps3.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.botao_menu_ps3.setStyleSheet("QPushButton {\n"
"background-image: url(:/ps/images/ps.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.botao_menu_ps3.setText("")
        self.botao_menu_ps3.setObjectName("botao_menu_ps3")
        self.texto_menu_ps3 = QtWidgets.QLabel(self.menu_ps3)
        self.texto_menu_ps3.setGeometry(QtCore.QRect(60, -1, 191, 51))
        self.texto_menu_ps3.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"}")
        self.texto_menu_ps3.setObjectName("texto_menu_ps3")
        self.verticalLayout_7.addWidget(self.menu_ps3)
        self.menu_retro = QtWidgets.QFrame(self.menu_esquerda)
        self.menu_retro.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QFrame:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.menu_retro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_retro.setObjectName("menu_retro")
        self.botao_menu_retro = QtWidgets.QPushButton(self.menu_retro)
        self.botao_menu_retro.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.botao_menu_retro.setStyleSheet("QPushButton {\n"
"background-image: url(:/snes/images/joystick-2-24.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.botao_menu_retro.setText("")
        self.botao_menu_retro.setObjectName("botao_menu_retro")
        self.texto_menu_retro = QtWidgets.QLabel(self.menu_retro)
        self.texto_menu_retro.setGeometry(QtCore.QRect(60, -1, 191, 51))
        self.texto_menu_retro.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"}")
        self.texto_menu_retro.setObjectName("texto_menu_retro")
        self.verticalLayout_7.addWidget(self.menu_retro)
        self.menu_extras = QtWidgets.QFrame(self.menu_esquerda)
        self.menu_extras.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QFrame:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.menu_extras.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_extras.setObjectName("menu_extras")
        self.botao_menu_extras = QtWidgets.QPushButton(self.menu_extras)
        self.botao_menu_extras.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.botao_menu_extras.setStyleSheet("QPushButton {\n"
"background-image: url(:/extras/images/download-24.ico);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.botao_menu_extras.setText("")
        self.botao_menu_extras.setObjectName("botao_menu_extras")
        self.texto_menu_extras = QtWidgets.QLabel(self.menu_extras)
        self.texto_menu_extras.setGeometry(QtCore.QRect(60, -1, 191, 51))
        self.texto_menu_extras.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"}")
        self.texto_menu_extras.setObjectName("texto_menu_extras")
        self.verticalLayout_7.addWidget(self.menu_extras)
        self.menu_database = QtWidgets.QFrame(self.menu_esquerda)
        self.menu_database.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QFrame:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.menu_database.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_database.setObjectName("menu_database")
        self.botao_menu_database = QtWidgets.QPushButton(self.menu_database)
        self.botao_menu_database.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.botao_menu_database.setStyleSheet("QPushButton {\n"
"background-image: url(:/banco de dados/images/data-configuration-24.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.botao_menu_database.setText("")
        self.botao_menu_database.setObjectName("botao_menu_database")
        self.texto_menu_database = QtWidgets.QLabel(self.menu_database)
        self.texto_menu_database.setGeometry(QtCore.QRect(60, -1, 191, 51))
        self.texto_menu_database.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"}")
        self.texto_menu_database.setObjectName("texto_menu_database")
        self.verticalLayout_7.addWidget(self.menu_database)
        self.menu_404 = QtWidgets.QFrame(self.menu_esquerda)
        self.menu_404.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QFrame:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.menu_404.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_404.setObjectName("menu_404")
        self.botao_menu_404 = QtWidgets.QPushButton(self.menu_404)
        self.botao_menu_404.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.botao_menu_404.setStyleSheet("QPushButton {\n"
"background-image: url(:/404/images/sitemap-2-24.ico);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.botao_menu_404.setText("")
        self.botao_menu_404.setObjectName("botao_menu_404")
        self.texto_menu_404 = QtWidgets.QLabel(self.menu_404)
        self.texto_menu_404.setGeometry(QtCore.QRect(60, -1, 191, 51))
        self.texto_menu_404.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"}")
        self.texto_menu_404.setObjectName("texto_menu_404")
        self.verticalLayout_7.addWidget(self.menu_404)
        self.menu_bottelegram = QtWidgets.QFrame(self.menu_esquerda)
        self.menu_bottelegram.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QFrame:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.menu_bottelegram.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_bottelegram.setObjectName("menu_bottelegram")
        self.botao_menu_bottelegram = QtWidgets.QPushButton(self.menu_bottelegram)
        self.botao_menu_bottelegram.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.botao_menu_bottelegram.setStyleSheet("QPushButton {\n"
"background-image: url(:/configuracoes/images/services-24.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.botao_menu_bottelegram.setText("")
        self.botao_menu_bottelegram.setObjectName("botao_menu_bottelegram")
        self.texto_menu_bottelegram = QtWidgets.QLabel(self.menu_bottelegram)
        self.texto_menu_bottelegram.setGeometry(QtCore.QRect(60, -1, 191, 51))
        self.texto_menu_bottelegram.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"}")
        self.texto_menu_bottelegram.setObjectName("texto_menu_bottelegram")
        self.verticalLayout_7.addWidget(self.menu_bottelegram)
        self.horizontalLayout.addWidget(self.menu_esquerda)
        self.janela_central = QtWidgets.QFrame(self.conteiner_central)
        self.janela_central.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.janela_central.setFrameShadow(QtWidgets.QFrame.Raised)
        self.janela_central.setObjectName("janela_central")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.janela_central)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.janela_central)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.pagina_home = QtWidgets.QWidget()
        self.pagina_home.setObjectName("pagina_home")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.pagina_home)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.background = QtWidgets.QLabel(self.pagina_home)
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/BACKGROUND_HOME/images/bg_home.jpg"))
        self.background.setScaledContents(True)
        self.background.setAlignment(QtCore.Qt.AlignCenter)
        self.background.setWordWrap(False)
        self.background.setObjectName("background")
        self.verticalLayout_6.addWidget(self.background)
        self.frame_inputs_gravar_database = QtWidgets.QFrame(self.pagina_home)
        self.frame_inputs_gravar_database.setMinimumSize(QtCore.QSize(0, 145))
        self.frame_inputs_gravar_database.setMaximumSize(QtCore.QSize(16777215, 145))
        self.frame_inputs_gravar_database.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_inputs_gravar_database.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_inputs_gravar_database.setObjectName("frame_inputs_gravar_database")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.frame_inputs_gravar_database)
        self.verticalLayout_27.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.titulo_topo_verifica_405 = QtWidgets.QLabel(self.frame_inputs_gravar_database)
        self.titulo_topo_verifica_405.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.titulo_topo_verifica_405.setScaledContents(False)
        self.titulo_topo_verifica_405.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo_topo_verifica_405.setObjectName("titulo_topo_verifica_405")
        self.verticalLayout_27.addWidget(self.titulo_topo_verifica_405)
        self.frame_4 = QtWidgets.QFrame(self.frame_inputs_gravar_database)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_22.setSpacing(5)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.input_nome_database_home = QtWidgets.QLineEdit(self.frame_4)
        self.input_nome_database_home.setMinimumSize(QtCore.QSize(0, 40))
        self.input_nome_database_home.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_nome_database_home.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_nome_database_home.setClearButtonEnabled(False)
        self.input_nome_database_home.setObjectName("input_nome_database_home")
        self.horizontalLayout_22.addWidget(self.input_nome_database_home)
        self.input_user_database_home = QtWidgets.QLineEdit(self.frame_4)
        self.input_user_database_home.setMinimumSize(QtCore.QSize(0, 40))
        self.input_user_database_home.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_user_database_home.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_user_database_home.setClearButtonEnabled(False)
        self.input_user_database_home.setObjectName("input_user_database_home")
        self.horizontalLayout_22.addWidget(self.input_user_database_home)
        self.input_senha_database_home = QtWidgets.QLineEdit(self.frame_4)
        self.input_senha_database_home.setMinimumSize(QtCore.QSize(0, 40))
        self.input_senha_database_home.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_senha_database_home.setObjectName("input_senha_database_home")
        self.horizontalLayout_22.addWidget(self.input_senha_database_home)
        self.input_host_database_home = QtWidgets.QLineEdit(self.frame_4)
        self.input_host_database_home.setMinimumSize(QtCore.QSize(0, 40))
        self.input_host_database_home.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_host_database_home.setObjectName("input_host_database_home")
        self.horizontalLayout_22.addWidget(self.input_host_database_home)
        self.verticalLayout_27.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_inputs_gravar_database)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.input_endereco_ftp = QtWidgets.QLineEdit(self.frame_5)
        self.input_endereco_ftp.setMinimumSize(QtCore.QSize(0, 40))
        self.input_endereco_ftp.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_endereco_ftp.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_endereco_ftp.setClearButtonEnabled(False)
        self.input_endereco_ftp.setObjectName("input_endereco_ftp")
        self.horizontalLayout_12.addWidget(self.input_endereco_ftp)
        self.input_user_ftp = QtWidgets.QLineEdit(self.frame_5)
        self.input_user_ftp.setMinimumSize(QtCore.QSize(0, 40))
        self.input_user_ftp.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_user_ftp.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_user_ftp.setClearButtonEnabled(False)
        self.input_user_ftp.setObjectName("input_user_ftp")
        self.horizontalLayout_12.addWidget(self.input_user_ftp)
        self.input_senha_ftp = QtWidgets.QLineEdit(self.frame_5)
        self.input_senha_ftp.setMinimumSize(QtCore.QSize(0, 40))
        self.input_senha_ftp.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_senha_ftp.setObjectName("input_senha_ftp")
        self.horizontalLayout_12.addWidget(self.input_senha_ftp)
        self.btn_database_home = QtWidgets.QPushButton(self.frame_5)
        self.btn_database_home.setMinimumSize(QtCore.QSize(210, 40))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_database_home.setFont(font)
        self.btn_database_home.setStyleSheet("QPushButton {\n"
"    background-color: rgb(30,30,30);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 18px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.btn_database_home.setFlat(False)
        self.btn_database_home.setObjectName("btn_database_home")
        self.horizontalLayout_12.addWidget(self.btn_database_home)
        self.verticalLayout_27.addWidget(self.frame_5)
        self.verticalLayout_6.addWidget(self.frame_inputs_gravar_database)
        self.stackedWidget.addWidget(self.pagina_home)
        self.pagina_cadastro_user = QtWidgets.QWidget()
        self.pagina_cadastro_user.setObjectName("pagina_cadastro_user")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.pagina_cadastro_user)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_explica_user = QtWidgets.QFrame(self.pagina_cadastro_user)
        self.frame_explica_user.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_explica_user.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_explica_user.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_explica_user.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_explica_user.setObjectName("frame_explica_user")
        self.explica1cadastro_users = QtWidgets.QLabel(self.frame_explica_user)
        self.explica1cadastro_users.setGeometry(QtCore.QRect(10, 30, 601, 31))
        self.explica1cadastro_users.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.explica1cadastro_users.setObjectName("explica1cadastro_users")
        self.titulo_cadastro_users = QtWidgets.QLabel(self.frame_explica_user)
        self.titulo_cadastro_users.setGeometry(QtCore.QRect(10, 10, 451, 21))
        self.titulo_cadastro_users.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"}")
        self.titulo_cadastro_users.setObjectName("titulo_cadastro_users")
        self.explica2cadastro_users = QtWidgets.QLabel(self.frame_explica_user)
        self.explica2cadastro_users.setGeometry(QtCore.QRect(10, 50, 511, 31))
        self.explica2cadastro_users.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.explica2cadastro_users.setObjectName("explica2cadastro_users")
        self.explica3cadastro_users = QtWidgets.QLabel(self.frame_explica_user)
        self.explica3cadastro_users.setGeometry(QtCore.QRect(10, 70, 471, 31))
        self.explica3cadastro_users.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.explica3cadastro_users.setObjectName("explica3cadastro_users")
        self.verticalLayout_2.addWidget(self.frame_explica_user)
        self.frame_inputs_users = QtWidgets.QFrame(self.pagina_cadastro_user)
        self.frame_inputs_users.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_inputs_users.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_inputs_users.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_inputs_users.setObjectName("frame_inputs_users")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_inputs_users)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.input_nome_user = QtWidgets.QLineEdit(self.frame_inputs_users)
        self.input_nome_user.setMinimumSize(QtCore.QSize(0, 40))
        self.input_nome_user.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_nome_user.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_nome_user.setClearButtonEnabled(False)
        self.input_nome_user.setObjectName("input_nome_user")
        self.verticalLayout_18.addWidget(self.input_nome_user)
        self.input_username_user = QtWidgets.QLineEdit(self.frame_inputs_users)
        self.input_username_user.setMinimumSize(QtCore.QSize(0, 40))
        self.input_username_user.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_username_user.setObjectName("input_username_user")
        self.verticalLayout_18.addWidget(self.input_username_user)
        self.input_senha_user = QtWidgets.QLineEdit(self.frame_inputs_users)
        self.input_senha_user.setMinimumSize(QtCore.QSize(0, 40))
        self.input_senha_user.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_senha_user.setObjectName("input_senha_user")
        self.verticalLayout_18.addWidget(self.input_senha_user)
        self.verticalLayout_2.addWidget(self.frame_inputs_users)
        self.frame_btns_user = QtWidgets.QFrame(self.pagina_cadastro_user)
        self.frame_btns_user.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_btns_user.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_btns_user.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btns_user.setObjectName("frame_btns_user")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_btns_user)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.btn_adiciona_user = QtWidgets.QPushButton(self.frame_btns_user)
        self.btn_adiciona_user.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 20px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.btn_adiciona_user.setObjectName("btn_adiciona_user")
        self.horizontalLayout_11.addWidget(self.btn_adiciona_user)
        self.btn_atualiza_user = QtWidgets.QPushButton(self.frame_btns_user)
        self.btn_atualiza_user.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 20px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.btn_atualiza_user.setObjectName("btn_atualiza_user")
        self.horizontalLayout_11.addWidget(self.btn_atualiza_user)
        self.btn_deleta_user = QtWidgets.QPushButton(self.frame_btns_user)
        self.btn_deleta_user.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 20px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.btn_deleta_user.setObjectName("btn_deleta_user")
        self.horizontalLayout_11.addWidget(self.btn_deleta_user)
        self.verticalLayout_2.addWidget(self.frame_btns_user)
        self.frame_tabela_db_users = QtWidgets.QFrame(self.pagina_cadastro_user)
        self.frame_tabela_db_users.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_tabela_db_users.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_tabela_db_users.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_tabela_db_users.setObjectName("frame_tabela_db_users")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.frame_tabela_db_users)
        self.verticalLayout_20.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.tabela_dados_usuarios = QtWidgets.QTableView(self.frame_tabela_db_users)
        self.tabela_dados_usuarios.setStyleSheet("QHeaderView {\n"
"background: rgb(30, 30, 30);\n"
"}\n"
"QHeaderView::section{\n"
"    color: rgb(255, 255, 255);\n"
"background: rgb(35,35,35);\n"
"}\n"
"QTableCornerButton::section{\n"
"background: rgb(35,35,35);\n"
"}\n"
"QHeaderView::section:pressed{\n"
"background: rgb(173,0,0);\n"
"}\n"
"QTableCornerButton::section:pressed{\n"
"background: rgb(173,0,0);\n"
"}\n"
"\n"
"\n"
"\n"
"QTableView{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QTableView:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QTableView:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}\n"
"* { gridline-color: gray }")
        self.tabela_dados_usuarios.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tabela_dados_usuarios.setGridStyle(QtCore.Qt.SolidLine)
        self.tabela_dados_usuarios.setObjectName("tabela_dados_usuarios")
        self.tabela_dados_usuarios.horizontalHeader().setDefaultSectionSize(200)
        self.verticalLayout_20.addWidget(self.tabela_dados_usuarios)
        self.frame_apoio_dbusers = QtWidgets.QFrame(self.frame_tabela_db_users)
        self.frame_apoio_dbusers.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_apoio_dbusers.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_apoio_dbusers.setObjectName("frame_apoio_dbusers")
        self.verticalLayout_20.addWidget(self.frame_apoio_dbusers)
        self.verticalLayout_2.addWidget(self.frame_tabela_db_users)
        self.stackedWidget.addWidget(self.pagina_cadastro_user)
        self.pagina_consulta_usuario = QtWidgets.QWidget()
        self.pagina_consulta_usuario.setObjectName("pagina_consulta_usuario")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.pagina_consulta_usuario)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_info_acessos_usuarios = QtWidgets.QFrame(self.pagina_consulta_usuario)
        self.frame_info_acessos_usuarios.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_info_acessos_usuarios.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_info_acessos_usuarios.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_info_acessos_usuarios.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_info_acessos_usuarios.setObjectName("frame_info_acessos_usuarios")
        self.ex3_acessos_usuarios = QtWidgets.QLabel(self.frame_info_acessos_usuarios)
        self.ex3_acessos_usuarios.setGeometry(QtCore.QRect(10, 70, 751, 31))
        self.ex3_acessos_usuarios.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex3_acessos_usuarios.setObjectName("ex3_acessos_usuarios")
        self.ex1_acessos_usuarios = QtWidgets.QLabel(self.frame_info_acessos_usuarios)
        self.ex1_acessos_usuarios.setGeometry(QtCore.QRect(10, 30, 601, 31))
        self.ex1_acessos_usuarios.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex1_acessos_usuarios.setObjectName("ex1_acessos_usuarios")
        self.titulo_acessos_usuarios = QtWidgets.QLabel(self.frame_info_acessos_usuarios)
        self.titulo_acessos_usuarios.setGeometry(QtCore.QRect(10, 10, 451, 21))
        self.titulo_acessos_usuarios.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"}")
        self.titulo_acessos_usuarios.setObjectName("titulo_acessos_usuarios")
        self.ex2_acessos_usuarios = QtWidgets.QLabel(self.frame_info_acessos_usuarios)
        self.ex2_acessos_usuarios.setGeometry(QtCore.QRect(10, 50, 511, 31))
        self.ex2_acessos_usuarios.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex2_acessos_usuarios.setObjectName("ex2_acessos_usuarios")
        self.verticalLayout_3.addWidget(self.frame_info_acessos_usuarios)
        self.frame_dados_pesquisa_acessos_usuarios = QtWidgets.QFrame(self.pagina_consulta_usuario)
        self.frame_dados_pesquisa_acessos_usuarios.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_dados_pesquisa_acessos_usuarios.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_dados_pesquisa_acessos_usuarios.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_dados_pesquisa_acessos_usuarios.setObjectName("frame_dados_pesquisa_acessos_usuarios")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_dados_pesquisa_acessos_usuarios)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.input_pesquisa_acessos_usuarios = QtWidgets.QLineEdit(self.frame_dados_pesquisa_acessos_usuarios)
        self.input_pesquisa_acessos_usuarios.setMinimumSize(QtCore.QSize(0, 40))
        self.input_pesquisa_acessos_usuarios.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_pesquisa_acessos_usuarios.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_pesquisa_acessos_usuarios.setClearButtonEnabled(False)
        self.input_pesquisa_acessos_usuarios.setObjectName("input_pesquisa_acessos_usuarios")
        self.verticalLayout_17.addWidget(self.input_pesquisa_acessos_usuarios)
        self.btn_pesquisa_acessos_usuarios = QtWidgets.QPushButton(self.frame_dados_pesquisa_acessos_usuarios)
        self.btn_pesquisa_acessos_usuarios.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 20px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.btn_pesquisa_acessos_usuarios.setObjectName("btn_pesquisa_acessos_usuarios")
        self.verticalLayout_17.addWidget(self.btn_pesquisa_acessos_usuarios)
        self.verticalLayout_3.addWidget(self.frame_dados_pesquisa_acessos_usuarios)
        self.frame_7 = QtWidgets.QFrame(self.pagina_consulta_usuario)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_21.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.tabela_pesquisa_acessos_usuarios = QtWidgets.QTableView(self.frame_7)
        self.tabela_pesquisa_acessos_usuarios.setStyleSheet("QHeaderView {\n"
"background: rgb(30, 30, 30);\n"
"}\n"
"QHeaderView::section{\n"
"    color: rgb(255, 255, 255);\n"
"background: rgb(35,35,35);\n"
"}\n"
"QTableCornerButton::section{\n"
"background: rgb(35,35,35);\n"
"}\n"
"QHeaderView::section:pressed{\n"
"background: rgb(30,144,255);\n"
"}\n"
"QTableCornerButton::section:pressed{\n"
"background: rgb(30,144,255);\n"
"}\n"
"\n"
"\n"
"\n"
"QTableView{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QTableView:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QTableView:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}\n"
"* { gridline-color: gray }")
        self.tabela_pesquisa_acessos_usuarios.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tabela_pesquisa_acessos_usuarios.setGridStyle(QtCore.Qt.SolidLine)
        self.tabela_pesquisa_acessos_usuarios.setObjectName("tabela_pesquisa_acessos_usuarios")
        self.tabela_pesquisa_acessos_usuarios.horizontalHeader().setDefaultSectionSize(200)
        self.verticalLayout_21.addWidget(self.tabela_pesquisa_acessos_usuarios)
        self.frame_tabela_pesquisa_acessos_usuarios = QtWidgets.QFrame(self.frame_7)
        self.frame_tabela_pesquisa_acessos_usuarios.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_tabela_pesquisa_acessos_usuarios.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_tabela_pesquisa_acessos_usuarios.setObjectName("frame_tabela_pesquisa_acessos_usuarios")
        self.verticalLayout_21.addWidget(self.frame_tabela_pesquisa_acessos_usuarios)
        self.verticalLayout_3.addWidget(self.frame_7)
        self.stackedWidget.addWidget(self.pagina_consulta_usuario)
        self.pagina_playstation_infos = QtWidgets.QWidget()
        self.pagina_playstation_infos.setObjectName("pagina_playstation_infos")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.pagina_playstation_infos)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_11 = QtWidgets.QFrame(self.pagina_playstation_infos)
        self.frame_11.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_11.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.ex3_playstation_infos = QtWidgets.QLabel(self.frame_11)
        self.ex3_playstation_infos.setGeometry(QtCore.QRect(10, 70, 751, 31))
        self.ex3_playstation_infos.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex3_playstation_infos.setObjectName("ex3_playstation_infos")
        self.ex1_playstation_infos = QtWidgets.QLabel(self.frame_11)
        self.ex1_playstation_infos.setGeometry(QtCore.QRect(10, 30, 601, 31))
        self.ex1_playstation_infos.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex1_playstation_infos.setObjectName("ex1_playstation_infos")
        self.titulo_playstation_infos = QtWidgets.QLabel(self.frame_11)
        self.titulo_playstation_infos.setGeometry(QtCore.QRect(10, 10, 451, 21))
        self.titulo_playstation_infos.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"}")
        self.titulo_playstation_infos.setObjectName("titulo_playstation_infos")
        self.ex2_playstation_infos = QtWidgets.QLabel(self.frame_11)
        self.ex2_playstation_infos.setGeometry(QtCore.QRect(10, 50, 511, 31))
        self.ex2_playstation_infos.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex2_playstation_infos.setObjectName("ex2_playstation_infos")
        self.verticalLayout_11.addWidget(self.frame_11)
        self.frame_inputs_playstation_infos = QtWidgets.QFrame(self.pagina_playstation_infos)
        self.frame_inputs_playstation_infos.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_inputs_playstation_infos.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_inputs_playstation_infos.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_inputs_playstation_infos.setObjectName("frame_inputs_playstation_infos")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_inputs_playstation_infos)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.input_playstation_infos = QtWidgets.QLineEdit(self.frame_inputs_playstation_infos)
        self.input_playstation_infos.setMinimumSize(QtCore.QSize(0, 40))
        self.input_playstation_infos.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_playstation_infos.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_playstation_infos.setClearButtonEnabled(False)
        self.input_playstation_infos.setObjectName("input_playstation_infos")
        self.verticalLayout_19.addWidget(self.input_playstation_infos)
        self.frame_btns_info_home = QtWidgets.QFrame(self.frame_inputs_playstation_infos)
        self.frame_btns_info_home.setMinimumSize(QtCore.QSize(0, 54))
        self.frame_btns_info_home.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_btns_info_home.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_btns_info_home.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btns_info_home.setObjectName("frame_btns_info_home")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_btns_info_home)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.btn_adiciona_infos = QtWidgets.QPushButton(self.frame_btns_info_home)
        self.btn_adiciona_infos.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 20px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.btn_adiciona_infos.setObjectName("btn_adiciona_infos")
        self.horizontalLayout_15.addWidget(self.btn_adiciona_infos)
        self.btn_atualiza_infos = QtWidgets.QPushButton(self.frame_btns_info_home)
        self.btn_atualiza_infos.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 20px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.btn_atualiza_infos.setObjectName("btn_atualiza_infos")
        self.horizontalLayout_15.addWidget(self.btn_atualiza_infos)
        self.btn_deleta_infos = QtWidgets.QPushButton(self.frame_btns_info_home)
        self.btn_deleta_infos.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 20px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.btn_deleta_infos.setObjectName("btn_deleta_infos")
        self.horizontalLayout_15.addWidget(self.btn_deleta_infos)
        self.verticalLayout_19.addWidget(self.frame_btns_info_home)
        self.verticalLayout_11.addWidget(self.frame_inputs_playstation_infos)
        self.frame_tabela_playstation_infos = QtWidgets.QFrame(self.pagina_playstation_infos)
        self.frame_tabela_playstation_infos.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_tabela_playstation_infos.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_tabela_playstation_infos.setObjectName("frame_tabela_playstation_infos")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.frame_tabela_playstation_infos)
        self.verticalLayout_22.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.tabela_dados_playstation_infos = QtWidgets.QTableView(self.frame_tabela_playstation_infos)
        self.tabela_dados_playstation_infos.setStyleSheet("QHeaderView {\n"
"background: rgb(30, 30, 30);\n"
"}\n"
"QHeaderView::section{\n"
"    color: rgb(255, 255, 255);\n"
"background: rgb(35,35,35);\n"
"}\n"
"QTableCornerButton::section{\n"
"background: rgb(35,35,35);\n"
"}\n"
"QHeaderView::section:pressed{\n"
"background: rgb(30,144,255);\n"
"}\n"
"QTableCornerButton::section:pressed{\n"
"background: rgb(30,144,255);\n"
"}\n"
"\n"
"\n"
"\n"
"QTableView{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QTableView:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QTableView:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}\n"
"* { gridline-color: gray }")
        self.tabela_dados_playstation_infos.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tabela_dados_playstation_infos.setGridStyle(QtCore.Qt.SolidLine)
        self.tabela_dados_playstation_infos.setObjectName("tabela_dados_playstation_infos")
        self.tabela_dados_playstation_infos.horizontalHeader().setDefaultSectionSize(200)
        self.verticalLayout_22.addWidget(self.tabela_dados_playstation_infos)
        self.frame_tabela_playstation_infos_2 = QtWidgets.QFrame(self.frame_tabela_playstation_infos)
        self.frame_tabela_playstation_infos_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_tabela_playstation_infos_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_tabela_playstation_infos_2.setObjectName("frame_tabela_playstation_infos_2")
        self.verticalLayout_22.addWidget(self.frame_tabela_playstation_infos_2)
        self.verticalLayout_11.addWidget(self.frame_tabela_playstation_infos)
        self.stackedWidget.addWidget(self.pagina_playstation_infos)
        self.pagina_jogos_psp = QtWidgets.QWidget()
        self.pagina_jogos_psp.setObjectName("pagina_jogos_psp")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.pagina_jogos_psp)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_geral_psp_dados = QtWidgets.QFrame(self.pagina_jogos_psp)
        self.frame_geral_psp_dados.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_geral_psp_dados.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_geral_psp_dados.setObjectName("frame_geral_psp_dados")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_geral_psp_dados)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_dados_psp = QtWidgets.QFrame(self.frame_geral_psp_dados)
        self.frame_dados_psp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_dados_psp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_dados_psp.setObjectName("frame_dados_psp")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.frame_dados_psp)
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.frame_ex_psp = QtWidgets.QFrame(self.frame_dados_psp)
        self.frame_ex_psp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ex_psp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ex_psp.setObjectName("frame_ex_psp")
        self.ex3__psp = QtWidgets.QLabel(self.frame_ex_psp)
        self.ex3__psp.setGeometry(QtCore.QRect(20, 70, 591, 21))
        self.ex3__psp.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex3__psp.setObjectName("ex3__psp")
        self.ex1__psp = QtWidgets.QLabel(self.frame_ex_psp)
        self.ex1__psp.setGeometry(QtCore.QRect(20, 30, 601, 20))
        self.ex1__psp.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex1__psp.setObjectName("ex1__psp")
        self.ex2__psp = QtWidgets.QLabel(self.frame_ex_psp)
        self.ex2__psp.setGeometry(QtCore.QRect(20, 50, 521, 21))
        self.ex2__psp.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex2__psp.setObjectName("ex2__psp")
        self.titulo_topo_psp = QtWidgets.QLabel(self.frame_ex_psp)
        self.titulo_topo_psp.setGeometry(QtCore.QRect(20, 0, 451, 21))
        self.titulo_topo_psp.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"}")
        self.titulo_topo_psp.setObjectName("titulo_topo_psp")
        self.ex4__psp = QtWidgets.QLabel(self.frame_ex_psp)
        self.ex4__psp.setGeometry(QtCore.QRect(20, 90, 631, 21))
        self.ex4__psp.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex4__psp.setObjectName("ex4__psp")
        self.ex5__psp = QtWidgets.QLabel(self.frame_ex_psp)
        self.ex5__psp.setGeometry(QtCore.QRect(20, 111, 671, 20))
        self.ex5__psp.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex5__psp.setObjectName("ex5__psp")
        self.ex6__psp = QtWidgets.QLabel(self.frame_ex_psp)
        self.ex6__psp.setGeometry(QtCore.QRect(20, 130, 671, 20))
        self.ex6__psp.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex6__psp.setObjectName("ex6__psp")
        self.verticalLayout_24.addWidget(self.frame_ex_psp)
        self.input_titulo_jogo_psp = QtWidgets.QLineEdit(self.frame_dados_psp)
        self.input_titulo_jogo_psp.setMinimumSize(QtCore.QSize(0, 40))
        self.input_titulo_jogo_psp.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_titulo_jogo_psp.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_titulo_jogo_psp.setClearButtonEnabled(False)
        self.input_titulo_jogo_psp.setObjectName("input_titulo_jogo_psp")
        self.verticalLayout_24.addWidget(self.input_titulo_jogo_psp)
        self.input_descricao_jogo_psp = QtWidgets.QLineEdit(self.frame_dados_psp)
        self.input_descricao_jogo_psp.setMinimumSize(QtCore.QSize(0, 40))
        self.input_descricao_jogo_psp.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_descricao_jogo_psp.setObjectName("input_descricao_jogo_psp")
        self.verticalLayout_24.addWidget(self.input_descricao_jogo_psp)
        self.input_contentid_psp = QtWidgets.QLineEdit(self.frame_dados_psp)
        self.input_contentid_psp.setMinimumSize(QtCore.QSize(0, 40))
        self.input_contentid_psp.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_contentid_psp.setObjectName("input_contentid_psp")
        self.verticalLayout_24.addWidget(self.input_contentid_psp)
        self.input_link_jogo_psp = QtWidgets.QLineEdit(self.frame_dados_psp)
        self.input_link_jogo_psp.setMinimumSize(QtCore.QSize(0, 40))
        self.input_link_jogo_psp.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_link_jogo_psp.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_link_jogo_psp.setClearButtonEnabled(False)
        self.input_link_jogo_psp.setObjectName("input_link_jogo_psp")
        self.verticalLayout_24.addWidget(self.input_link_jogo_psp)
        self.horizontalLayout_3.addWidget(self.frame_dados_psp)
        self.frame_botoes_db_psp = QtWidgets.QFrame(self.frame_geral_psp_dados)
        self.frame_botoes_db_psp.setMinimumSize(QtCore.QSize(260, 366))
        self.frame_botoes_db_psp.setMaximumSize(QtCore.QSize(270, 16777215))
        self.frame_botoes_db_psp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_botoes_db_psp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_botoes_db_psp.setObjectName("frame_botoes_db_psp")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.frame_botoes_db_psp)
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_23.setSpacing(6)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.frame_imagem_psp = QtWidgets.QFrame(self.frame_botoes_db_psp)
        self.frame_imagem_psp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_imagem_psp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_imagem_psp.setObjectName("frame_imagem_psp")
        self.imagem_psp = QtWidgets.QLabel(self.frame_imagem_psp)
        self.imagem_psp.setGeometry(QtCore.QRect(0, 10, 261, 261))
        self.imagem_psp.setText("")
        self.imagem_psp.setPixmap(QtGui.QPixmap(":/icone_tcxsgame/images/icone_tcxsgame.jpg"))
        self.imagem_psp.setScaledContents(True)
        self.imagem_psp.setObjectName("imagem_psp")
        self.verticalLayout_23.addWidget(self.frame_imagem_psp)
        self.btn_upload_imagem_psp = QtWidgets.QPushButton(self.frame_botoes_db_psp)
        self.btn_upload_imagem_psp.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_upload_imagem_psp.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 20px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.btn_upload_imagem_psp.setObjectName("btn_upload_imagem_psp")
        self.verticalLayout_23.addWidget(self.btn_upload_imagem_psp)
        self.frame_23 = QtWidgets.QFrame(self.frame_botoes_db_psp)
        self.frame_23.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_23)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.botao_db_adiciona_psp = QtWidgets.QPushButton(self.frame_23)
        self.botao_db_adiciona_psp.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.botao_db_adiciona_psp.setFont(font)
        self.botao_db_adiciona_psp.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 18px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.botao_db_adiciona_psp.setObjectName("botao_db_adiciona_psp")
        self.horizontalLayout_14.addWidget(self.botao_db_adiciona_psp)
        self.botao_db_atualiza_psp = QtWidgets.QPushButton(self.frame_23)
        self.botao_db_atualiza_psp.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.botao_db_atualiza_psp.setFont(font)
        self.botao_db_atualiza_psp.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 18px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.botao_db_atualiza_psp.setObjectName("botao_db_atualiza_psp")
        self.horizontalLayout_14.addWidget(self.botao_db_atualiza_psp)
        self.botao_db_deleta_psp = QtWidgets.QPushButton(self.frame_23)
        self.botao_db_deleta_psp.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.botao_db_deleta_psp.setFont(font)
        self.botao_db_deleta_psp.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 18px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.botao_db_deleta_psp.setObjectName("botao_db_deleta_psp")
        self.horizontalLayout_14.addWidget(self.botao_db_deleta_psp)
        self.verticalLayout_23.addWidget(self.frame_23)
        self.horizontalLayout_3.addWidget(self.frame_botoes_db_psp)
        self.verticalLayout_12.addWidget(self.frame_geral_psp_dados)
        self.frame_geral_tabela_psp = QtWidgets.QFrame(self.pagina_jogos_psp)
        self.frame_geral_tabela_psp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_geral_tabela_psp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_geral_tabela_psp.setObjectName("frame_geral_tabela_psp")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.frame_geral_tabela_psp)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.tabela_dados_db_psp = QtWidgets.QTableView(self.frame_geral_tabela_psp)
        self.tabela_dados_db_psp.setStyleSheet("QHeaderView {\n"
"background: rgb(30, 30, 30);\n"
"}\n"
"QHeaderView::section{\n"
"    color: rgb(255, 255, 255);\n"
"background: rgb(35,35,35);\n"
"}\n"
"QTableCornerButton::section{\n"
"background: rgb(35,35,35);\n"
"}\n"
"QHeaderView::section:pressed{\n"
"background: rgb(173,0,0);\n"
"}\n"
"QTableCornerButton::section:pressed{\n"
"background: rgb(173,0,0);\n"
"}\n"
"\n"
"\n"
"\n"
"QTableView{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QTableView:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QTableView:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}\n"
"* { gridline-color: gray }")
        self.tabela_dados_db_psp.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tabela_dados_db_psp.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tabela_dados_db_psp.setDragEnabled(True)
        self.tabela_dados_db_psp.setGridStyle(QtCore.Qt.SolidLine)
        self.tabela_dados_db_psp.setWordWrap(False)
        self.tabela_dados_db_psp.setObjectName("tabela_dados_db_psp")
        self.tabela_dados_db_psp.horizontalHeader().setDefaultSectionSize(200)
        self.verticalLayout_25.addWidget(self.tabela_dados_db_psp)
        self.frame_20 = QtWidgets.QFrame(self.frame_geral_tabela_psp)
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.verticalLayout_25.addWidget(self.frame_20)
        self.verticalLayout_12.addWidget(self.frame_geral_tabela_psp)
        self.stackedWidget.addWidget(self.pagina_jogos_psp)
        self.pagina_jogos_ps1 = QtWidgets.QWidget()
        self.pagina_jogos_ps1.setObjectName("pagina_jogos_ps1")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.pagina_jogos_ps1)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_24 = QtWidgets.QFrame(self.pagina_jogos_ps1)
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_24)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_32 = QtWidgets.QFrame(self.frame_24)
        self.frame_32.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout(self.frame_32)
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.frame_ex_ps1 = QtWidgets.QFrame(self.frame_32)
        self.frame_ex_ps1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ex_ps1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ex_ps1.setObjectName("frame_ex_ps1")
        self.ex3_ps1 = QtWidgets.QLabel(self.frame_ex_ps1)
        self.ex3_ps1.setGeometry(QtCore.QRect(20, 70, 591, 21))
        self.ex3_ps1.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex3_ps1.setObjectName("ex3_ps1")
        self.ex1_ps1 = QtWidgets.QLabel(self.frame_ex_ps1)
        self.ex1_ps1.setGeometry(QtCore.QRect(20, 30, 601, 20))
        self.ex1_ps1.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex1_ps1.setObjectName("ex1_ps1")
        self.ex2_ps1 = QtWidgets.QLabel(self.frame_ex_ps1)
        self.ex2_ps1.setGeometry(QtCore.QRect(20, 50, 521, 21))
        self.ex2_ps1.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex2_ps1.setObjectName("ex2_ps1")
        self.titulo_topo__ps1 = QtWidgets.QLabel(self.frame_ex_ps1)
        self.titulo_topo__ps1.setGeometry(QtCore.QRect(20, 0, 451, 21))
        self.titulo_topo__ps1.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"}")
        self.titulo_topo__ps1.setObjectName("titulo_topo__ps1")
        self.ex4_ps1 = QtWidgets.QLabel(self.frame_ex_ps1)
        self.ex4_ps1.setGeometry(QtCore.QRect(20, 90, 631, 21))
        self.ex4_ps1.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex4_ps1.setObjectName("ex4_ps1")
        self.ex5_ps1 = QtWidgets.QLabel(self.frame_ex_ps1)
        self.ex5_ps1.setGeometry(QtCore.QRect(20, 111, 671, 20))
        self.ex5_ps1.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex5_ps1.setObjectName("ex5_ps1")
        self.ex6_ps1 = QtWidgets.QLabel(self.frame_ex_ps1)
        self.ex6_ps1.setGeometry(QtCore.QRect(20, 130, 671, 20))
        self.ex6_ps1.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex6_ps1.setObjectName("ex6_ps1")
        self.verticalLayout_31.addWidget(self.frame_ex_ps1)
        self.input_titulo_ps1 = QtWidgets.QLineEdit(self.frame_32)
        self.input_titulo_ps1.setMinimumSize(QtCore.QSize(0, 40))
        self.input_titulo_ps1.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_titulo_ps1.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_titulo_ps1.setClearButtonEnabled(False)
        self.input_titulo_ps1.setObjectName("input_titulo_ps1")
        self.verticalLayout_31.addWidget(self.input_titulo_ps1)
        self.input_descricao_ps1 = QtWidgets.QLineEdit(self.frame_32)
        self.input_descricao_ps1.setMinimumSize(QtCore.QSize(0, 40))
        self.input_descricao_ps1.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_descricao_ps1.setObjectName("input_descricao_ps1")
        self.verticalLayout_31.addWidget(self.input_descricao_ps1)
        self.input_contentid_ps1 = QtWidgets.QLineEdit(self.frame_32)
        self.input_contentid_ps1.setMinimumSize(QtCore.QSize(0, 40))
        self.input_contentid_ps1.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_contentid_ps1.setObjectName("input_contentid_ps1")
        self.verticalLayout_31.addWidget(self.input_contentid_ps1)
        self.input_link_ps1 = QtWidgets.QLineEdit(self.frame_32)
        self.input_link_ps1.setMinimumSize(QtCore.QSize(0, 40))
        self.input_link_ps1.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_link_ps1.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_link_ps1.setClearButtonEnabled(False)
        self.input_link_ps1.setObjectName("input_link_ps1")
        self.verticalLayout_31.addWidget(self.input_link_ps1)
        self.horizontalLayout_5.addWidget(self.frame_32)
        self.frame_35 = QtWidgets.QFrame(self.frame_24)
        self.frame_35.setMinimumSize(QtCore.QSize(260, 366))
        self.frame_35.setMaximumSize(QtCore.QSize(270, 16777215))
        self.frame_35.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_35.setObjectName("frame_35")
        self.verticalLayout_32 = QtWidgets.QVBoxLayout(self.frame_35)
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_32.setSpacing(6)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.frame_imagem_ps1 = QtWidgets.QFrame(self.frame_35)
        self.frame_imagem_ps1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_imagem_ps1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_imagem_ps1.setObjectName("frame_imagem_ps1")
        self.imagem_ps1 = QtWidgets.QLabel(self.frame_imagem_ps1)
        self.imagem_ps1.setGeometry(QtCore.QRect(0, 10, 261, 261))
        self.imagem_ps1.setText("")
        self.imagem_ps1.setPixmap(QtGui.QPixmap(":/icone_tcxsgame/images/icone_tcxsgame.jpg"))
        self.imagem_ps1.setScaledContents(True)
        self.imagem_ps1.setObjectName("imagem_ps1")
        self.verticalLayout_32.addWidget(self.frame_imagem_ps1)
        self.btn_upload_imagem_ps1 = QtWidgets.QPushButton(self.frame_35)
        self.btn_upload_imagem_ps1.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_upload_imagem_ps1.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 20px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.btn_upload_imagem_ps1.setObjectName("btn_upload_imagem_ps1")
        self.verticalLayout_32.addWidget(self.btn_upload_imagem_ps1)
        self.frame_37 = QtWidgets.QFrame(self.frame_35)
        self.frame_37.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_37.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_37.setObjectName("frame_37")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.frame_37)
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.botao_db_adiciona_ps1 = QtWidgets.QPushButton(self.frame_37)
        self.botao_db_adiciona_ps1.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.botao_db_adiciona_ps1.setFont(font)
        self.botao_db_adiciona_ps1.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 18px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.botao_db_adiciona_ps1.setObjectName("botao_db_adiciona_ps1")
        self.horizontalLayout_20.addWidget(self.botao_db_adiciona_ps1)
        self.botao_db_atualiza_ps1 = QtWidgets.QPushButton(self.frame_37)
        self.botao_db_atualiza_ps1.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.botao_db_atualiza_ps1.setFont(font)
        self.botao_db_atualiza_ps1.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 18px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.botao_db_atualiza_ps1.setObjectName("botao_db_atualiza_ps1")
        self.horizontalLayout_20.addWidget(self.botao_db_atualiza_ps1)
        self.botao_db_deleta_ps1 = QtWidgets.QPushButton(self.frame_37)
        self.botao_db_deleta_ps1.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.botao_db_deleta_ps1.setFont(font)
        self.botao_db_deleta_ps1.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 18px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.botao_db_deleta_ps1.setObjectName("botao_db_deleta_ps1")
        self.horizontalLayout_20.addWidget(self.botao_db_deleta_ps1)
        self.verticalLayout_32.addWidget(self.frame_37)
        self.horizontalLayout_5.addWidget(self.frame_35)
        self.verticalLayout_8.addWidget(self.frame_24)
        self.frame_38_ps1 = QtWidgets.QFrame(self.pagina_jogos_ps1)
        self.frame_38_ps1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_38_ps1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_38_ps1.setObjectName("frame_38_ps1")
        self.verticalLayout_33 = QtWidgets.QVBoxLayout(self.frame_38_ps1)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.tabela_dados_db_ps1 = QtWidgets.QTableView(self.frame_38_ps1)
        self.tabela_dados_db_ps1.setStyleSheet("QHeaderView {\n"
"background: rgb(30, 30, 30);\n"
"}\n"
"QHeaderView::section{\n"
"    color: rgb(255, 255, 255);\n"
"background: rgb(35,35,35);\n"
"}\n"
"QTableCornerButton::section{\n"
"background: rgb(35,35,35);\n"
"}\n"
"QHeaderView::section:pressed{\n"
"background: rgb(173,0,0);\n"
"}\n"
"QTableCornerButton::section:pressed{\n"
"background: rgb(173,0,0);\n"
"}\n"
"\n"
"\n"
"\n"
"QTableView{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QTableView:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QTableView:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}\n"
"* { gridline-color: gray }")
        self.tabela_dados_db_ps1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tabela_dados_db_ps1.setGridStyle(QtCore.Qt.SolidLine)
        self.tabela_dados_db_ps1.setObjectName("tabela_dados_db_ps1")
        self.tabela_dados_db_ps1.horizontalHeader().setDefaultSectionSize(200)
        self.verticalLayout_33.addWidget(self.tabela_dados_db_ps1)
        self.frame_39_ps1 = QtWidgets.QFrame(self.frame_38_ps1)
        self.frame_39_ps1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_39_ps1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_39_ps1.setObjectName("frame_39_ps1")
        self.verticalLayout_33.addWidget(self.frame_39_ps1)
        self.verticalLayout_8.addWidget(self.frame_38_ps1)
        self.stackedWidget.addWidget(self.pagina_jogos_ps1)
        self.pagina_jogos_ps2 = QtWidgets.QWidget()
        self.pagina_jogos_ps2.setObjectName("pagina_jogos_ps2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.pagina_jogos_ps2)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_40_ps2 = QtWidgets.QFrame(self.pagina_jogos_ps2)
        self.frame_40_ps2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_40_ps2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_40_ps2.setObjectName("frame_40_ps2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_40_ps2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_41_ps2 = QtWidgets.QFrame(self.frame_40_ps2)
        self.frame_41_ps2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_41_ps2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_41_ps2.setObjectName("frame_41_ps2")
        self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.frame_41_ps2)
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.frame_42 = QtWidgets.QFrame(self.frame_41_ps2)
        self.frame_42.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_42.setObjectName("frame_42")
        self.label_40 = QtWidgets.QLabel(self.frame_42)
        self.label_40.setGeometry(QtCore.QRect(20, 70, 591, 21))
        self.label_40.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.frame_42)
        self.label_41.setGeometry(QtCore.QRect(20, 30, 601, 20))
        self.label_41.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.frame_42)
        self.label_42.setGeometry(QtCore.QRect(20, 50, 521, 21))
        self.label_42.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.frame_42)
        self.label_43.setGeometry(QtCore.QRect(20, 0, 451, 21))
        self.label_43.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"}")
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.frame_42)
        self.label_44.setGeometry(QtCore.QRect(20, 90, 631, 21))
        self.label_44.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(self.frame_42)
        self.label_45.setGeometry(QtCore.QRect(20, 111, 671, 20))
        self.label_45.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.frame_42)
        self.label_46.setGeometry(QtCore.QRect(20, 130, 671, 20))
        self.label_46.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.label_46.setObjectName("label_46")
        self.verticalLayout_34.addWidget(self.frame_42)
        self.input_titulo_ps2 = QtWidgets.QLineEdit(self.frame_41_ps2)
        self.input_titulo_ps2.setMinimumSize(QtCore.QSize(0, 40))
        self.input_titulo_ps2.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_titulo_ps2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_titulo_ps2.setClearButtonEnabled(False)
        self.input_titulo_ps2.setObjectName("input_titulo_ps2")
        self.verticalLayout_34.addWidget(self.input_titulo_ps2)
        self.input_descricao_ps2 = QtWidgets.QLineEdit(self.frame_41_ps2)
        self.input_descricao_ps2.setMinimumSize(QtCore.QSize(0, 40))
        self.input_descricao_ps2.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_descricao_ps2.setObjectName("input_descricao_ps2")
        self.verticalLayout_34.addWidget(self.input_descricao_ps2)
        self.input_contentid_ps2 = QtWidgets.QLineEdit(self.frame_41_ps2)
        self.input_contentid_ps2.setMinimumSize(QtCore.QSize(0, 40))
        self.input_contentid_ps2.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_contentid_ps2.setObjectName("input_contentid_ps2")
        self.verticalLayout_34.addWidget(self.input_contentid_ps2)
        self.input_link_ps2 = QtWidgets.QLineEdit(self.frame_41_ps2)
        self.input_link_ps2.setMinimumSize(QtCore.QSize(0, 40))
        self.input_link_ps2.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_link_ps2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_link_ps2.setClearButtonEnabled(False)
        self.input_link_ps2.setObjectName("input_link_ps2")
        self.verticalLayout_34.addWidget(self.input_link_ps2)
        self.horizontalLayout_6.addWidget(self.frame_41_ps2)
        self.frame_43 = QtWidgets.QFrame(self.frame_40_ps2)
        self.frame_43.setMinimumSize(QtCore.QSize(260, 366))
        self.frame_43.setMaximumSize(QtCore.QSize(270, 16777215))
        self.frame_43.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_43.setObjectName("frame_43")
        self.verticalLayout_35 = QtWidgets.QVBoxLayout(self.frame_43)
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_35.setSpacing(6)
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.frame_imagem_ps2 = QtWidgets.QFrame(self.frame_43)
        self.frame_imagem_ps2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_imagem_ps2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_imagem_ps2.setObjectName("frame_imagem_ps2")
        self.imagem_ps2 = QtWidgets.QLabel(self.frame_imagem_ps2)
        self.imagem_ps2.setGeometry(QtCore.QRect(0, 10, 261, 261))
        self.imagem_ps2.setText("")
        self.imagem_ps2.setPixmap(QtGui.QPixmap(":/icone_tcxsgame/images/icone_tcxsgame.jpg"))
        self.imagem_ps2.setScaledContents(True)
        self.imagem_ps2.setObjectName("imagem_ps2")
        self.verticalLayout_35.addWidget(self.frame_imagem_ps2)
        self.btn_upload_imagem_ps2 = QtWidgets.QPushButton(self.frame_43)
        self.btn_upload_imagem_ps2.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_upload_imagem_ps2.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 20px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.btn_upload_imagem_ps2.setObjectName("btn_upload_imagem_ps2")
        self.verticalLayout_35.addWidget(self.btn_upload_imagem_ps2)
        self.frame_45 = QtWidgets.QFrame(self.frame_43)
        self.frame_45.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_45.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_45.setObjectName("frame_45")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.frame_45)
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.botao_db_adiciona_ps2 = QtWidgets.QPushButton(self.frame_45)
        self.botao_db_adiciona_ps2.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.botao_db_adiciona_ps2.setFont(font)
        self.botao_db_adiciona_ps2.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 18px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.botao_db_adiciona_ps2.setObjectName("botao_db_adiciona_ps2")
        self.horizontalLayout_21.addWidget(self.botao_db_adiciona_ps2)
        self.botao_db_atualiza_ps2 = QtWidgets.QPushButton(self.frame_45)
        self.botao_db_atualiza_ps2.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.botao_db_atualiza_ps2.setFont(font)
        self.botao_db_atualiza_ps2.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 18px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.botao_db_atualiza_ps2.setObjectName("botao_db_atualiza_ps2")
        self.horizontalLayout_21.addWidget(self.botao_db_atualiza_ps2)
        self.botao_db_deleta_ps2 = QtWidgets.QPushButton(self.frame_45)
        self.botao_db_deleta_ps2.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.botao_db_deleta_ps2.setFont(font)
        self.botao_db_deleta_ps2.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 18px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.botao_db_deleta_ps2.setObjectName("botao_db_deleta_ps2")
        self.horizontalLayout_21.addWidget(self.botao_db_deleta_ps2)
        self.verticalLayout_35.addWidget(self.frame_45)
        self.horizontalLayout_6.addWidget(self.frame_43)
        self.verticalLayout_9.addWidget(self.frame_40_ps2)
        self.frame_46_ps2 = QtWidgets.QFrame(self.pagina_jogos_ps2)
        self.frame_46_ps2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_46_ps2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_46_ps2.setObjectName("frame_46_ps2")
        self.verticalLayout_36 = QtWidgets.QVBoxLayout(self.frame_46_ps2)
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.tabela_dados_db_ps2 = QtWidgets.QTableView(self.frame_46_ps2)
        self.tabela_dados_db_ps2.setStyleSheet("QHeaderView {\n"
"background: rgb(30, 30, 30);\n"
"}\n"
"QHeaderView::section{\n"
"    color: rgb(255, 255, 255);\n"
"background: rgb(35,35,35);\n"
"}\n"
"QTableCornerButton::section{\n"
"background: rgb(35,35,35);\n"
"}\n"
"QHeaderView::section:pressed{\n"
"background: rgb(173,0,0);\n"
"}\n"
"QTableCornerButton::section:pressed{\n"
"background: rgb(173,0,0);\n"
"}\n"
"\n"
"\n"
"\n"
"QTableView{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QTableView:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QTableView:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}\n"
"* { gridline-color: gray }")
        self.tabela_dados_db_ps2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tabela_dados_db_ps2.setGridStyle(QtCore.Qt.SolidLine)
        self.tabela_dados_db_ps2.setObjectName("tabela_dados_db_ps2")
        self.tabela_dados_db_ps2.horizontalHeader().setDefaultSectionSize(200)
        self.verticalLayout_36.addWidget(self.tabela_dados_db_ps2)
        self.frame_47_ps2 = QtWidgets.QFrame(self.frame_46_ps2)
        self.frame_47_ps2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_47_ps2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_47_ps2.setObjectName("frame_47_ps2")
        self.verticalLayout_36.addWidget(self.frame_47_ps2)
        self.verticalLayout_9.addWidget(self.frame_46_ps2)
        self.stackedWidget.addWidget(self.pagina_jogos_ps2)
        self.pagina_jogos_ps3 = QtWidgets.QWidget()
        self.pagina_jogos_ps3.setObjectName("pagina_jogos_ps3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.pagina_jogos_ps3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_2_ps3 = QtWidgets.QFrame(self.pagina_jogos_ps3)
        self.frame_2_ps3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_2_ps3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2_ps3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2_ps3.setObjectName("frame_2_ps3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_2_ps3)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_5.addWidget(self.frame_2_ps3)
        self.frame_68_ps3 = QtWidgets.QFrame(self.pagina_jogos_ps3)
        self.frame_68_ps3.setMaximumSize(QtCore.QSize(16777215, 350))
        self.frame_68_ps3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_68_ps3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_68_ps3.setObjectName("frame_68_ps3")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_68_ps3)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.frame_69_ps3 = QtWidgets.QFrame(self.frame_68_ps3)
        self.frame_69_ps3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_69_ps3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_69_ps3.setObjectName("frame_69_ps3")
        self.verticalLayout_46 = QtWidgets.QVBoxLayout(self.frame_69_ps3)
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_46.setObjectName("verticalLayout_46")
        self.frame_ex_ps3 = QtWidgets.QFrame(self.frame_69_ps3)
        self.frame_ex_ps3.setMinimumSize(QtCore.QSize(0, 173))
        self.frame_ex_ps3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ex_ps3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ex_ps3.setObjectName("frame_ex_ps3")
        self.ex3_ps3 = QtWidgets.QLabel(self.frame_ex_ps3)
        self.ex3_ps3.setGeometry(QtCore.QRect(20, 70, 591, 21))
        self.ex3_ps3.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex3_ps3.setObjectName("ex3_ps3")
        self.ex1_ps3 = QtWidgets.QLabel(self.frame_ex_ps3)
        self.ex1_ps3.setGeometry(QtCore.QRect(20, 30, 601, 20))
        self.ex1_ps3.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex1_ps3.setObjectName("ex1_ps3")
        self.ex2_ps3 = QtWidgets.QLabel(self.frame_ex_ps3)
        self.ex2_ps3.setGeometry(QtCore.QRect(20, 50, 521, 21))
        self.ex2_ps3.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex2_ps3.setObjectName("ex2_ps3")
        self.titulo_topo_ps3 = QtWidgets.QLabel(self.frame_ex_ps3)
        self.titulo_topo_ps3.setGeometry(QtCore.QRect(20, 0, 451, 21))
        self.titulo_topo_ps3.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"}")
        self.titulo_topo_ps3.setObjectName("titulo_topo_ps3")
        self.ex4_ps3 = QtWidgets.QLabel(self.frame_ex_ps3)
        self.ex4_ps3.setGeometry(QtCore.QRect(20, 90, 631, 21))
        self.ex4_ps3.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex4_ps3.setObjectName("ex4_ps3")
        self.ex5_ps3 = QtWidgets.QLabel(self.frame_ex_ps3)
        self.ex5_ps3.setGeometry(QtCore.QRect(20, 111, 671, 20))
        self.ex5_ps3.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex5_ps3.setObjectName("ex5_ps3")
        self.ex6_ps3 = QtWidgets.QLabel(self.frame_ex_ps3)
        self.ex6_ps3.setGeometry(QtCore.QRect(20, 130, 671, 20))
        self.ex6_ps3.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex6_ps3.setObjectName("ex6_ps3")
        self.ex7_ps3 = QtWidgets.QLabel(self.frame_ex_ps3)
        self.ex7_ps3.setGeometry(QtCore.QRect(20, 150, 711, 20))
        self.ex7_ps3.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex7_ps3.setObjectName("ex7_ps3")
        self.verticalLayout_46.addWidget(self.frame_ex_ps3)
        self.input_titulo_ps3 = QtWidgets.QLineEdit(self.frame_69_ps3)
        self.input_titulo_ps3.setMinimumSize(QtCore.QSize(0, 40))
        self.input_titulo_ps3.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_titulo_ps3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_titulo_ps3.setClearButtonEnabled(False)
        self.input_titulo_ps3.setObjectName("input_titulo_ps3")
        self.verticalLayout_46.addWidget(self.input_titulo_ps3)
        self.input_descricao_ps3 = QtWidgets.QLineEdit(self.frame_69_ps3)
        self.input_descricao_ps3.setMinimumSize(QtCore.QSize(0, 40))
        self.input_descricao_ps3.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_descricao_ps3.setObjectName("input_descricao_ps3")
        self.verticalLayout_46.addWidget(self.input_descricao_ps3)
        self.input_content_id_ps3 = QtWidgets.QLineEdit(self.frame_69_ps3)
        self.input_content_id_ps3.setMinimumSize(QtCore.QSize(0, 40))
        self.input_content_id_ps3.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_content_id_ps3.setObjectName("input_content_id_ps3")
        self.verticalLayout_46.addWidget(self.input_content_id_ps3)
        self.horizontalLayout_17.addWidget(self.frame_69_ps3)
        self.frame_73 = QtWidgets.QFrame(self.frame_68_ps3)
        self.frame_73.setMinimumSize(QtCore.QSize(260, 366))
        self.frame_73.setMaximumSize(QtCore.QSize(270, 16777215))
        self.frame_73.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_73.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_73.setObjectName("frame_73")
        self.btn_upload_imagem_ps3 = QtWidgets.QPushButton(self.frame_73)
        self.btn_upload_imagem_ps3.setGeometry(QtCore.QRect(0, 265, 251, 40))
        self.btn_upload_imagem_ps3.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_upload_imagem_ps3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.btn_upload_imagem_ps3.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 20px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.btn_upload_imagem_ps3.setObjectName("btn_upload_imagem_ps3")
        self.imagem_ps3 = QtWidgets.QLabel(self.frame_73)
        self.imagem_ps3.setGeometry(QtCore.QRect(0, 10, 250, 250))
        self.imagem_ps3.setText("")
        self.imagem_ps3.setPixmap(QtGui.QPixmap(":/icone_tcxsgame/images/icone_tcxsgame.jpg"))
        self.imagem_ps3.setScaledContents(True)
        self.imagem_ps3.setObjectName("imagem_ps3")
        self.horizontalLayout_17.addWidget(self.frame_73)
        self.verticalLayout_5.addWidget(self.frame_68_ps3)
        self.frame_76_ps3 = QtWidgets.QFrame(self.pagina_jogos_ps3)
        self.frame_76_ps3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_76_ps3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_76_ps3.setObjectName("frame_76_ps3")
        self.verticalLayout_49 = QtWidgets.QVBoxLayout(self.frame_76_ps3)
        self.verticalLayout_49.setObjectName("verticalLayout_49")
        self.tabWidget_ps3 = QtWidgets.QTabWidget(self.frame_76_ps3)
        self.tabWidget_ps3.setStyleSheet("\n"
"QTabWidget{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QTabWidget:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QTabWidget:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.tabWidget_ps3.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget_ps3.setObjectName("tabWidget_ps3")
        self.tabela_links_1a5 = QtWidgets.QWidget()
        self.tabela_links_1a5.setObjectName("tabela_links_1a5")
        self.verticalLayout_50 = QtWidgets.QVBoxLayout(self.tabela_links_1a5)
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName("verticalLayout_50")
        self.frame_74_ps3 = QtWidgets.QFrame(self.tabela_links_1a5)
        self.frame_74_ps3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_74_ps3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_74_ps3.setObjectName("frame_74_ps3")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.frame_74_ps3)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.frame_83input_link_ps3 = QtWidgets.QFrame(self.frame_74_ps3)
        self.frame_83input_link_ps3.setMaximumSize(QtCore.QSize(93, 16777215))
        self.frame_83input_link_ps3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_83input_link_ps3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_83input_link_ps3.setObjectName("frame_83input_link_ps3")
        self.verticalLayout_56 = QtWidgets.QVBoxLayout(self.frame_83input_link_ps3)
        self.verticalLayout_56.setObjectName("verticalLayout_56")
        self.info_link1 = QtWidgets.QLineEdit(self.frame_83input_link_ps3)
        self.info_link1.setMinimumSize(QtCore.QSize(0, 40))
        self.info_link1.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.info_link1.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.info_link1.setClearButtonEnabled(False)
        self.info_link1.setObjectName("info_link1")
        self.verticalLayout_56.addWidget(self.info_link1)
        self.info_link2 = QtWidgets.QLineEdit(self.frame_83input_link_ps3)
        self.info_link2.setMinimumSize(QtCore.QSize(0, 40))
        self.info_link2.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.info_link2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.info_link2.setClearButtonEnabled(False)
        self.info_link2.setObjectName("info_link2")
        self.verticalLayout_56.addWidget(self.info_link2)
        self.info_link3 = QtWidgets.QLineEdit(self.frame_83input_link_ps3)
        self.info_link3.setMinimumSize(QtCore.QSize(0, 40))
        self.info_link3.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.info_link3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.info_link3.setClearButtonEnabled(False)
        self.info_link3.setObjectName("info_link3")
        self.verticalLayout_56.addWidget(self.info_link3)
        self.info_link4 = QtWidgets.QLineEdit(self.frame_83input_link_ps3)
        self.info_link4.setMinimumSize(QtCore.QSize(0, 40))
        self.info_link4.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.info_link4.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.info_link4.setClearButtonEnabled(False)
        self.info_link4.setObjectName("info_link4")
        self.verticalLayout_56.addWidget(self.info_link4)
        self.info_link5 = QtWidgets.QLineEdit(self.frame_83input_link_ps3)
        self.info_link5.setMinimumSize(QtCore.QSize(0, 40))
        self.info_link5.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.info_link5.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.info_link5.setClearButtonEnabled(False)
        self.info_link5.setObjectName("info_link5")
        self.verticalLayout_56.addWidget(self.info_link5)
        self.horizontalLayout_25.addWidget(self.frame_83input_link_ps3)
        self.frame_82_ps3 = QtWidgets.QFrame(self.frame_74_ps3)
        self.frame_82_ps3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_82_ps3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_82_ps3.setObjectName("frame_82_ps3")
        self.verticalLayout_57 = QtWidgets.QVBoxLayout(self.frame_82_ps3)
        self.verticalLayout_57.setObjectName("verticalLayout_57")
        self.input_link1_ps3 = QtWidgets.QLineEdit(self.frame_82_ps3)
        self.input_link1_ps3.setMinimumSize(QtCore.QSize(0, 40))
        self.input_link1_ps3.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_link1_ps3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_link1_ps3.setClearButtonEnabled(False)
        self.input_link1_ps3.setObjectName("input_link1_ps3")
        self.verticalLayout_57.addWidget(self.input_link1_ps3)
        self.input_link2_ps3 = QtWidgets.QLineEdit(self.frame_82_ps3)
        self.input_link2_ps3.setMinimumSize(QtCore.QSize(0, 40))
        self.input_link2_ps3.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_link2_ps3.setObjectName("input_link2_ps3")
        self.verticalLayout_57.addWidget(self.input_link2_ps3)
        self.input_link3_ps3 = QtWidgets.QLineEdit(self.frame_82_ps3)
        self.input_link3_ps3.setMinimumSize(QtCore.QSize(0, 40))
        self.input_link3_ps3.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_link3_ps3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_link3_ps3.setClearButtonEnabled(False)
        self.input_link3_ps3.setObjectName("input_link3_ps3")
        self.verticalLayout_57.addWidget(self.input_link3_ps3)
        self.input_link4_ps3 = QtWidgets.QLineEdit(self.frame_82_ps3)
        self.input_link4_ps3.setMinimumSize(QtCore.QSize(0, 40))
        self.input_link4_ps3.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_link4_ps3.setObjectName("input_link4_ps3")
        self.verticalLayout_57.addWidget(self.input_link4_ps3)
        self.input_link5_ps3 = QtWidgets.QLineEdit(self.frame_82_ps3)
        self.input_link5_ps3.setMinimumSize(QtCore.QSize(0, 40))
        self.input_link5_ps3.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_link5_ps3.setObjectName("input_link5_ps3")
        self.verticalLayout_57.addWidget(self.input_link5_ps3)
        self.horizontalLayout_25.addWidget(self.frame_82_ps3)
        self.verticalLayout_50.addWidget(self.frame_74_ps3)
        self.tabWidget_ps3.addTab(self.tabela_links_1a5, "")
        self.tabela_links_6a10 = QtWidgets.QWidget()
        self.tabela_links_6a10.setObjectName("tabela_links_6a10")
        self.verticalLayout_48 = QtWidgets.QVBoxLayout(self.tabela_links_6a10)
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName("verticalLayout_48")
        self.frame_77input_link_ps3 = QtWidgets.QFrame(self.tabela_links_6a10)
        self.frame_77input_link_ps3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_77input_link_ps3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_77input_link_ps3.setObjectName("frame_77input_link_ps3")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.frame_77input_link_ps3)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.frame_84input_link_ps3 = QtWidgets.QFrame(self.frame_77input_link_ps3)
        self.frame_84input_link_ps3.setMaximumSize(QtCore.QSize(93, 16777215))
        self.frame_84input_link_ps3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_84input_link_ps3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_84input_link_ps3.setObjectName("frame_84input_link_ps3")
        self.verticalLayout_58 = QtWidgets.QVBoxLayout(self.frame_84input_link_ps3)
        self.verticalLayout_58.setObjectName("verticalLayout_58")
        self.info_link6 = QtWidgets.QLineEdit(self.frame_84input_link_ps3)
        self.info_link6.setMinimumSize(QtCore.QSize(0, 40))
        self.info_link6.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.info_link6.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.info_link6.setClearButtonEnabled(False)
        self.info_link6.setObjectName("info_link6")
        self.verticalLayout_58.addWidget(self.info_link6)
        self.info_link7 = QtWidgets.QLineEdit(self.frame_84input_link_ps3)
        self.info_link7.setMinimumSize(QtCore.QSize(0, 40))
        self.info_link7.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.info_link7.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.info_link7.setClearButtonEnabled(False)
        self.info_link7.setObjectName("info_link7")
        self.verticalLayout_58.addWidget(self.info_link7)
        self.info_link8 = QtWidgets.QLineEdit(self.frame_84input_link_ps3)
        self.info_link8.setMinimumSize(QtCore.QSize(0, 40))
        self.info_link8.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.info_link8.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.info_link8.setClearButtonEnabled(False)
        self.info_link8.setObjectName("info_link8")
        self.verticalLayout_58.addWidget(self.info_link8)
        self.info_link9 = QtWidgets.QLineEdit(self.frame_84input_link_ps3)
        self.info_link9.setMinimumSize(QtCore.QSize(0, 40))
        self.info_link9.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.info_link9.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.info_link9.setClearButtonEnabled(False)
        self.info_link9.setObjectName("info_link9")
        self.verticalLayout_58.addWidget(self.info_link9)
        self.info_link10 = QtWidgets.QLineEdit(self.frame_84input_link_ps3)
        self.info_link10.setMinimumSize(QtCore.QSize(0, 40))
        self.info_link10.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.info_link10.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.info_link10.setClearButtonEnabled(False)
        self.info_link10.setObjectName("info_link10")
        self.verticalLayout_58.addWidget(self.info_link10)
        self.horizontalLayout_26.addWidget(self.frame_84input_link_ps3)
        self.frame_85input_link_ps3 = QtWidgets.QFrame(self.frame_77input_link_ps3)
        self.frame_85input_link_ps3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_85input_link_ps3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_85input_link_ps3.setObjectName("frame_85input_link_ps3")
        self.verticalLayout_59 = QtWidgets.QVBoxLayout(self.frame_85input_link_ps3)
        self.verticalLayout_59.setObjectName("verticalLayout_59")
        self.input_link6_ps3 = QtWidgets.QLineEdit(self.frame_85input_link_ps3)
        self.input_link6_ps3.setMinimumSize(QtCore.QSize(0, 40))
        self.input_link6_ps3.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_link6_ps3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_link6_ps3.setClearButtonEnabled(False)
        self.input_link6_ps3.setObjectName("input_link6_ps3")
        self.verticalLayout_59.addWidget(self.input_link6_ps3)
        self.input_link7_ps3 = QtWidgets.QLineEdit(self.frame_85input_link_ps3)
        self.input_link7_ps3.setMinimumSize(QtCore.QSize(0, 40))
        self.input_link7_ps3.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_link7_ps3.setObjectName("input_link7_ps3")
        self.verticalLayout_59.addWidget(self.input_link7_ps3)
        self.input_link8_ps3 = QtWidgets.QLineEdit(self.frame_85input_link_ps3)
        self.input_link8_ps3.setMinimumSize(QtCore.QSize(0, 40))
        self.input_link8_ps3.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_link8_ps3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_link8_ps3.setClearButtonEnabled(False)
        self.input_link8_ps3.setObjectName("input_link8_ps3")
        self.verticalLayout_59.addWidget(self.input_link8_ps3)
        self.input_link9_ps3 = QtWidgets.QLineEdit(self.frame_85input_link_ps3)
        self.input_link9_ps3.setMinimumSize(QtCore.QSize(0, 40))
        self.input_link9_ps3.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_link9_ps3.setObjectName("input_link9_ps3")
        self.verticalLayout_59.addWidget(self.input_link9_ps3)
        self.input_link10_ps3 = QtWidgets.QLineEdit(self.frame_85input_link_ps3)
        self.input_link10_ps3.setMinimumSize(QtCore.QSize(0, 40))
        self.input_link10_ps3.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_link10_ps3.setObjectName("input_link10_ps3")
        self.verticalLayout_59.addWidget(self.input_link10_ps3)
        self.horizontalLayout_26.addWidget(self.frame_85input_link_ps3)
        self.verticalLayout_48.addWidget(self.frame_77input_link_ps3)
        self.tabWidget_ps3.addTab(self.tabela_links_6a10, "")
        self.tabela_links_11a15 = QtWidgets.QWidget()
        self.tabela_links_11a15.setObjectName("tabela_links_11a15")
        self.verticalLayout_51 = QtWidgets.QVBoxLayout(self.tabela_links_11a15)
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName("verticalLayout_51")
        self.frame_78input_link_ps3 = QtWidgets.QFrame(self.tabela_links_11a15)
        self.frame_78input_link_ps3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_78input_link_ps3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_78input_link_ps3.setObjectName("frame_78input_link_ps3")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.frame_78input_link_ps3)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.frame_86input_link_ps3 = QtWidgets.QFrame(self.frame_78input_link_ps3)
        self.frame_86input_link_ps3.setMaximumSize(QtCore.QSize(93, 16777215))
        self.frame_86input_link_ps3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_86input_link_ps3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_86input_link_ps3.setObjectName("frame_86input_link_ps3")
        self.verticalLayout_60 = QtWidgets.QVBoxLayout(self.frame_86input_link_ps3)
        self.verticalLayout_60.setObjectName("verticalLayout_60")
        self.info_link11 = QtWidgets.QLineEdit(self.frame_86input_link_ps3)
        self.info_link11.setMinimumSize(QtCore.QSize(0, 40))
        self.info_link11.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.info_link11.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.info_link11.setClearButtonEnabled(False)
        self.info_link11.setObjectName("info_link11")
        self.verticalLayout_60.addWidget(self.info_link11)
        self.info_link12 = QtWidgets.QLineEdit(self.frame_86input_link_ps3)
        self.info_link12.setMinimumSize(QtCore.QSize(0, 40))
        self.info_link12.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.info_link12.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.info_link12.setClearButtonEnabled(False)
        self.info_link12.setObjectName("info_link12")
        self.verticalLayout_60.addWidget(self.info_link12)
        self.info_link13 = QtWidgets.QLineEdit(self.frame_86input_link_ps3)
        self.info_link13.setMinimumSize(QtCore.QSize(0, 40))
        self.info_link13.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.info_link13.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.info_link13.setClearButtonEnabled(False)
        self.info_link13.setObjectName("info_link13")
        self.verticalLayout_60.addWidget(self.info_link13)
        self.info_link14 = QtWidgets.QLineEdit(self.frame_86input_link_ps3)
        self.info_link14.setMinimumSize(QtCore.QSize(0, 40))
        self.info_link14.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.info_link14.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.info_link14.setClearButtonEnabled(False)
        self.info_link14.setObjectName("info_link14")
        self.verticalLayout_60.addWidget(self.info_link14)
        self.info_link15 = QtWidgets.QLineEdit(self.frame_86input_link_ps3)
        self.info_link15.setMinimumSize(QtCore.QSize(0, 40))
        self.info_link15.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.info_link15.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.info_link15.setClearButtonEnabled(False)
        self.info_link15.setObjectName("info_link15")
        self.verticalLayout_60.addWidget(self.info_link15)
        self.horizontalLayout_27.addWidget(self.frame_86input_link_ps3)
        self.frame_87input_link_ps3 = QtWidgets.QFrame(self.frame_78input_link_ps3)
        self.frame_87input_link_ps3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_87input_link_ps3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_87input_link_ps3.setObjectName("frame_87input_link_ps3")
        self.verticalLayout_61 = QtWidgets.QVBoxLayout(self.frame_87input_link_ps3)
        self.verticalLayout_61.setObjectName("verticalLayout_61")
        self.input_link11_ps3 = QtWidgets.QLineEdit(self.frame_87input_link_ps3)
        self.input_link11_ps3.setMinimumSize(QtCore.QSize(0, 40))
        self.input_link11_ps3.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_link11_ps3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_link11_ps3.setClearButtonEnabled(False)
        self.input_link11_ps3.setObjectName("input_link11_ps3")
        self.verticalLayout_61.addWidget(self.input_link11_ps3)
        self.input_link12_ps3 = QtWidgets.QLineEdit(self.frame_87input_link_ps3)
        self.input_link12_ps3.setMinimumSize(QtCore.QSize(0, 40))
        self.input_link12_ps3.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_link12_ps3.setObjectName("input_link12_ps3")
        self.verticalLayout_61.addWidget(self.input_link12_ps3)
        self.input_link13_ps3 = QtWidgets.QLineEdit(self.frame_87input_link_ps3)
        self.input_link13_ps3.setMinimumSize(QtCore.QSize(0, 40))
        self.input_link13_ps3.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_link13_ps3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_link13_ps3.setClearButtonEnabled(False)
        self.input_link13_ps3.setObjectName("input_link13_ps3")
        self.verticalLayout_61.addWidget(self.input_link13_ps3)
        self.input_link14_ps3 = QtWidgets.QLineEdit(self.frame_87input_link_ps3)
        self.input_link14_ps3.setMinimumSize(QtCore.QSize(0, 40))
        self.input_link14_ps3.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_link14_ps3.setObjectName("input_link14_ps3")
        self.verticalLayout_61.addWidget(self.input_link14_ps3)
        self.input_link15_ps3 = QtWidgets.QLineEdit(self.frame_87input_link_ps3)
        self.input_link15_ps3.setMinimumSize(QtCore.QSize(0, 40))
        self.input_link15_ps3.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_link15_ps3.setObjectName("input_link15_ps3")
        self.verticalLayout_61.addWidget(self.input_link15_ps3)
        self.horizontalLayout_27.addWidget(self.frame_87input_link_ps3)
        self.verticalLayout_51.addWidget(self.frame_78input_link_ps3)
        self.tabWidget_ps3.addTab(self.tabela_links_11a15, "")
        self.tabela_links_16a20 = QtWidgets.QWidget()
        self.tabela_links_16a20.setObjectName("tabela_links_16a20")
        self.verticalLayout_52 = QtWidgets.QVBoxLayout(self.tabela_links_16a20)
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName("verticalLayout_52")
        self.frame_79input_link_ps3 = QtWidgets.QFrame(self.tabela_links_16a20)
        self.frame_79input_link_ps3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_79input_link_ps3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_79input_link_ps3.setObjectName("frame_79input_link_ps3")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.frame_79input_link_ps3)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.frame_88input_link_ps3 = QtWidgets.QFrame(self.frame_79input_link_ps3)
        self.frame_88input_link_ps3.setMaximumSize(QtCore.QSize(93, 16777215))
        self.frame_88input_link_ps3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_88input_link_ps3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_88input_link_ps3.setObjectName("frame_88input_link_ps3")
        self.verticalLayout_62 = QtWidgets.QVBoxLayout(self.frame_88input_link_ps3)
        self.verticalLayout_62.setObjectName("verticalLayout_62")
        self.info_link16 = QtWidgets.QLineEdit(self.frame_88input_link_ps3)
        self.info_link16.setMinimumSize(QtCore.QSize(0, 40))
        self.info_link16.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.info_link16.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.info_link16.setClearButtonEnabled(False)
        self.info_link16.setObjectName("info_link16")
        self.verticalLayout_62.addWidget(self.info_link16)
        self.info_link17 = QtWidgets.QLineEdit(self.frame_88input_link_ps3)
        self.info_link17.setMinimumSize(QtCore.QSize(0, 40))
        self.info_link17.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.info_link17.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.info_link17.setClearButtonEnabled(False)
        self.info_link17.setObjectName("info_link17")
        self.verticalLayout_62.addWidget(self.info_link17)
        self.info_link18 = QtWidgets.QLineEdit(self.frame_88input_link_ps3)
        self.info_link18.setMinimumSize(QtCore.QSize(0, 40))
        self.info_link18.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.info_link18.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.info_link18.setClearButtonEnabled(False)
        self.info_link18.setObjectName("info_link18")
        self.verticalLayout_62.addWidget(self.info_link18)
        self.info_link19 = QtWidgets.QLineEdit(self.frame_88input_link_ps3)
        self.info_link19.setMinimumSize(QtCore.QSize(0, 40))
        self.info_link19.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.info_link19.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.info_link19.setClearButtonEnabled(False)
        self.info_link19.setObjectName("info_link19")
        self.verticalLayout_62.addWidget(self.info_link19)
        self.info_link20 = QtWidgets.QLineEdit(self.frame_88input_link_ps3)
        self.info_link20.setMinimumSize(QtCore.QSize(0, 40))
        self.info_link20.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.info_link20.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.info_link20.setClearButtonEnabled(False)
        self.info_link20.setObjectName("info_link20")
        self.verticalLayout_62.addWidget(self.info_link20)
        self.horizontalLayout_28.addWidget(self.frame_88input_link_ps3)
        self.frame_89input_link_ps3 = QtWidgets.QFrame(self.frame_79input_link_ps3)
        self.frame_89input_link_ps3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_89input_link_ps3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_89input_link_ps3.setObjectName("frame_89input_link_ps3")
        self.verticalLayout_63 = QtWidgets.QVBoxLayout(self.frame_89input_link_ps3)
        self.verticalLayout_63.setObjectName("verticalLayout_63")
        self.input_link16_ps3 = QtWidgets.QLineEdit(self.frame_89input_link_ps3)
        self.input_link16_ps3.setMinimumSize(QtCore.QSize(0, 40))
        self.input_link16_ps3.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_link16_ps3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_link16_ps3.setClearButtonEnabled(False)
        self.input_link16_ps3.setObjectName("input_link16_ps3")
        self.verticalLayout_63.addWidget(self.input_link16_ps3)
        self.input_link17_ps3 = QtWidgets.QLineEdit(self.frame_89input_link_ps3)
        self.input_link17_ps3.setMinimumSize(QtCore.QSize(0, 40))
        self.input_link17_ps3.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_link17_ps3.setObjectName("input_link17_ps3")
        self.verticalLayout_63.addWidget(self.input_link17_ps3)
        self.input_link18_ps3 = QtWidgets.QLineEdit(self.frame_89input_link_ps3)
        self.input_link18_ps3.setMinimumSize(QtCore.QSize(0, 40))
        self.input_link18_ps3.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_link18_ps3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_link18_ps3.setClearButtonEnabled(False)
        self.input_link18_ps3.setObjectName("input_link18_ps3")
        self.verticalLayout_63.addWidget(self.input_link18_ps3)
        self.input_link19_ps3 = QtWidgets.QLineEdit(self.frame_89input_link_ps3)
        self.input_link19_ps3.setMinimumSize(QtCore.QSize(0, 40))
        self.input_link19_ps3.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_link19_ps3.setObjectName("input_link19_ps3")
        self.verticalLayout_63.addWidget(self.input_link19_ps3)
        self.input_link20_ps3 = QtWidgets.QLineEdit(self.frame_89input_link_ps3)
        self.input_link20_ps3.setMinimumSize(QtCore.QSize(0, 40))
        self.input_link20_ps3.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_link20_ps3.setObjectName("input_link20_ps3")
        self.verticalLayout_63.addWidget(self.input_link20_ps3)
        self.horizontalLayout_28.addWidget(self.frame_89input_link_ps3)
        self.verticalLayout_52.addWidget(self.frame_79input_link_ps3)
        self.tabWidget_ps3.addTab(self.tabela_links_16a20, "")
        self.tabela_links_21a25 = QtWidgets.QWidget()
        self.tabela_links_21a25.setObjectName("tabela_links_21a25")
        self.verticalLayout_53 = QtWidgets.QVBoxLayout(self.tabela_links_21a25)
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName("verticalLayout_53")
        self.frame_80input_link_ps3 = QtWidgets.QFrame(self.tabela_links_21a25)
        self.frame_80input_link_ps3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_80input_link_ps3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_80input_link_ps3.setObjectName("frame_80input_link_ps3")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout(self.frame_80input_link_ps3)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.frame_90input_link_ps3 = QtWidgets.QFrame(self.frame_80input_link_ps3)
        self.frame_90input_link_ps3.setMaximumSize(QtCore.QSize(93, 16777215))
        self.frame_90input_link_ps3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_90input_link_ps3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_90input_link_ps3.setObjectName("frame_90input_link_ps3")
        self.verticalLayout_64 = QtWidgets.QVBoxLayout(self.frame_90input_link_ps3)
        self.verticalLayout_64.setObjectName("verticalLayout_64")
        self.info_link21 = QtWidgets.QLineEdit(self.frame_90input_link_ps3)
        self.info_link21.setMinimumSize(QtCore.QSize(0, 40))
        self.info_link21.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.info_link21.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.info_link21.setClearButtonEnabled(False)
        self.info_link21.setObjectName("info_link21")
        self.verticalLayout_64.addWidget(self.info_link21)
        self.info_link22 = QtWidgets.QLineEdit(self.frame_90input_link_ps3)
        self.info_link22.setMinimumSize(QtCore.QSize(0, 40))
        self.info_link22.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.info_link22.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.info_link22.setClearButtonEnabled(False)
        self.info_link22.setObjectName("info_link22")
        self.verticalLayout_64.addWidget(self.info_link22)
        self.info_link23 = QtWidgets.QLineEdit(self.frame_90input_link_ps3)
        self.info_link23.setMinimumSize(QtCore.QSize(0, 40))
        self.info_link23.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.info_link23.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.info_link23.setClearButtonEnabled(False)
        self.info_link23.setObjectName("info_link23")
        self.verticalLayout_64.addWidget(self.info_link23)
        self.info_link24 = QtWidgets.QLineEdit(self.frame_90input_link_ps3)
        self.info_link24.setMinimumSize(QtCore.QSize(0, 40))
        self.info_link24.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.info_link24.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.info_link24.setClearButtonEnabled(False)
        self.info_link24.setObjectName("info_link24")
        self.verticalLayout_64.addWidget(self.info_link24)
        self.info_link25 = QtWidgets.QLineEdit(self.frame_90input_link_ps3)
        self.info_link25.setMinimumSize(QtCore.QSize(0, 40))
        self.info_link25.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.info_link25.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.info_link25.setClearButtonEnabled(False)
        self.info_link25.setObjectName("info_link25")
        self.verticalLayout_64.addWidget(self.info_link25)
        self.horizontalLayout_29.addWidget(self.frame_90input_link_ps3)
        self.frame_91input_link_ps3 = QtWidgets.QFrame(self.frame_80input_link_ps3)
        self.frame_91input_link_ps3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_91input_link_ps3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_91input_link_ps3.setObjectName("frame_91input_link_ps3")
        self.verticalLayout_65 = QtWidgets.QVBoxLayout(self.frame_91input_link_ps3)
        self.verticalLayout_65.setObjectName("verticalLayout_65")
        self.input_link21_ps3 = QtWidgets.QLineEdit(self.frame_91input_link_ps3)
        self.input_link21_ps3.setMinimumSize(QtCore.QSize(0, 40))
        self.input_link21_ps3.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_link21_ps3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_link21_ps3.setClearButtonEnabled(False)
        self.input_link21_ps3.setObjectName("input_link21_ps3")
        self.verticalLayout_65.addWidget(self.input_link21_ps3)
        self.input_link22_ps3 = QtWidgets.QLineEdit(self.frame_91input_link_ps3)
        self.input_link22_ps3.setMinimumSize(QtCore.QSize(0, 40))
        self.input_link22_ps3.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_link22_ps3.setObjectName("input_link22_ps3")
        self.verticalLayout_65.addWidget(self.input_link22_ps3)
        self.input_link23_ps3 = QtWidgets.QLineEdit(self.frame_91input_link_ps3)
        self.input_link23_ps3.setMinimumSize(QtCore.QSize(0, 40))
        self.input_link23_ps3.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_link23_ps3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_link23_ps3.setClearButtonEnabled(False)
        self.input_link23_ps3.setObjectName("input_link23_ps3")
        self.verticalLayout_65.addWidget(self.input_link23_ps3)
        self.input_link24_ps3 = QtWidgets.QLineEdit(self.frame_91input_link_ps3)
        self.input_link24_ps3.setMinimumSize(QtCore.QSize(0, 40))
        self.input_link24_ps3.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_link24_ps3.setObjectName("input_link24_ps3")
        self.verticalLayout_65.addWidget(self.input_link24_ps3)
        self.input_link25_ps3 = QtWidgets.QLineEdit(self.frame_91input_link_ps3)
        self.input_link25_ps3.setMinimumSize(QtCore.QSize(0, 40))
        self.input_link25_ps3.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_link25_ps3.setObjectName("input_link25_ps3")
        self.verticalLayout_65.addWidget(self.input_link25_ps3)
        self.horizontalLayout_29.addWidget(self.frame_91input_link_ps3)
        self.verticalLayout_53.addWidget(self.frame_80input_link_ps3)
        self.tabWidget_ps3.addTab(self.tabela_links_21a25, "")
        self.tabela_links_26a30 = QtWidgets.QWidget()
        self.tabela_links_26a30.setObjectName("tabela_links_26a30")
        self.verticalLayout_54 = QtWidgets.QVBoxLayout(self.tabela_links_26a30)
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName("verticalLayout_54")
        self.frame_81input_link_ps3 = QtWidgets.QFrame(self.tabela_links_26a30)
        self.frame_81input_link_ps3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_81input_link_ps3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_81input_link_ps3.setObjectName("frame_81input_link_ps3")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout(self.frame_81input_link_ps3)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.frame_92input_link_ps3 = QtWidgets.QFrame(self.frame_81input_link_ps3)
        self.frame_92input_link_ps3.setMaximumSize(QtCore.QSize(93, 16777215))
        self.frame_92input_link_ps3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_92input_link_ps3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_92input_link_ps3.setObjectName("frame_92input_link_ps3")
        self.verticalLayout_66 = QtWidgets.QVBoxLayout(self.frame_92input_link_ps3)
        self.verticalLayout_66.setObjectName("verticalLayout_66")
        self.info_link26 = QtWidgets.QLineEdit(self.frame_92input_link_ps3)
        self.info_link26.setMinimumSize(QtCore.QSize(0, 40))
        self.info_link26.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.info_link26.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.info_link26.setClearButtonEnabled(False)
        self.info_link26.setObjectName("info_link26")
        self.verticalLayout_66.addWidget(self.info_link26)
        self.info_link27 = QtWidgets.QLineEdit(self.frame_92input_link_ps3)
        self.info_link27.setMinimumSize(QtCore.QSize(0, 40))
        self.info_link27.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.info_link27.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.info_link27.setClearButtonEnabled(False)
        self.info_link27.setObjectName("info_link27")
        self.verticalLayout_66.addWidget(self.info_link27)
        self.info_link28 = QtWidgets.QLineEdit(self.frame_92input_link_ps3)
        self.info_link28.setMinimumSize(QtCore.QSize(0, 40))
        self.info_link28.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.info_link28.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.info_link28.setClearButtonEnabled(False)
        self.info_link28.setObjectName("info_link28")
        self.verticalLayout_66.addWidget(self.info_link28)
        self.info_link29 = QtWidgets.QLineEdit(self.frame_92input_link_ps3)
        self.info_link29.setMinimumSize(QtCore.QSize(0, 40))
        self.info_link29.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.info_link29.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.info_link29.setClearButtonEnabled(False)
        self.info_link29.setObjectName("info_link29")
        self.verticalLayout_66.addWidget(self.info_link29)
        self.info_link30 = QtWidgets.QLineEdit(self.frame_92input_link_ps3)
        self.info_link30.setMinimumSize(QtCore.QSize(0, 40))
        self.info_link30.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.info_link30.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.info_link30.setClearButtonEnabled(False)
        self.info_link30.setObjectName("info_link30")
        self.verticalLayout_66.addWidget(self.info_link30)
        self.horizontalLayout_30.addWidget(self.frame_92input_link_ps3)
        self.frame_93input_link_ps3 = QtWidgets.QFrame(self.frame_81input_link_ps3)
        self.frame_93input_link_ps3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_93input_link_ps3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_93input_link_ps3.setObjectName("frame_93input_link_ps3")
        self.verticalLayout_67 = QtWidgets.QVBoxLayout(self.frame_93input_link_ps3)
        self.verticalLayout_67.setObjectName("verticalLayout_67")
        self.input_link26_ps3 = QtWidgets.QLineEdit(self.frame_93input_link_ps3)
        self.input_link26_ps3.setMinimumSize(QtCore.QSize(0, 40))
        self.input_link26_ps3.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_link26_ps3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_link26_ps3.setClearButtonEnabled(False)
        self.input_link26_ps3.setObjectName("input_link26_ps3")
        self.verticalLayout_67.addWidget(self.input_link26_ps3)
        self.input_link27_ps3 = QtWidgets.QLineEdit(self.frame_93input_link_ps3)
        self.input_link27_ps3.setMinimumSize(QtCore.QSize(0, 40))
        self.input_link27_ps3.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_link27_ps3.setObjectName("input_link27_ps3")
        self.verticalLayout_67.addWidget(self.input_link27_ps3)
        self.input_link28_ps3 = QtWidgets.QLineEdit(self.frame_93input_link_ps3)
        self.input_link28_ps3.setMinimumSize(QtCore.QSize(0, 40))
        self.input_link28_ps3.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_link28_ps3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_link28_ps3.setClearButtonEnabled(False)
        self.input_link28_ps3.setObjectName("input_link28_ps3")
        self.verticalLayout_67.addWidget(self.input_link28_ps3)
        self.input_link29_ps3 = QtWidgets.QLineEdit(self.frame_93input_link_ps3)
        self.input_link29_ps3.setMinimumSize(QtCore.QSize(0, 40))
        self.input_link29_ps3.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_link29_ps3.setObjectName("input_link29_ps3")
        self.verticalLayout_67.addWidget(self.input_link29_ps3)
        self.input_link30_ps3 = QtWidgets.QLineEdit(self.frame_93input_link_ps3)
        self.input_link30_ps3.setMinimumSize(QtCore.QSize(0, 40))
        self.input_link30_ps3.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_link30_ps3.setObjectName("input_link30_ps3")
        self.verticalLayout_67.addWidget(self.input_link30_ps3)
        self.horizontalLayout_30.addWidget(self.frame_93input_link_ps3)
        self.verticalLayout_54.addWidget(self.frame_81input_link_ps3)
        self.tabWidget_ps3.addTab(self.tabela_links_26a30, "")
        self.frame_tabela_database_ps3 = QtWidgets.QWidget()
        self.frame_tabela_database_ps3.setObjectName("frame_tabela_database_ps3")
        self.verticalLayout_55 = QtWidgets.QVBoxLayout(self.frame_tabela_database_ps3)
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName("verticalLayout_55")
        self.tabela_database_ps3 = QtWidgets.QTableView(self.frame_tabela_database_ps3)
        self.tabela_database_ps3.setStyleSheet("QHeaderView {\n"
"background: rgb(30, 30, 30);\n"
"}\n"
"QHeaderView::section{\n"
"    color: rgb(255, 255, 255);\n"
"background: rgb(35,35,35);\n"
"}\n"
"QTableCornerButton::section{\n"
"background: rgb(35,35,35);\n"
"}\n"
"QHeaderView::section:pressed{\n"
"background: rgb(173,0,0);\n"
"}\n"
"QTableCornerButton::section:pressed{\n"
"background: rgb(173,0,0);\n"
"}\n"
"\n"
"\n"
"\n"
"QTableView{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QTableView:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QTableView:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}\n"
"* { gridline-color: gray }")
        self.tabela_database_ps3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tabela_database_ps3.setGridStyle(QtCore.Qt.SolidLine)
        self.tabela_database_ps3.setObjectName("tabela_database_ps3")
        self.tabela_database_ps3.horizontalHeader().setDefaultSectionSize(200)
        self.verticalLayout_55.addWidget(self.tabela_database_ps3)
        self.tabWidget_ps3.addTab(self.frame_tabela_database_ps3, "")
        self.verticalLayout_49.addWidget(self.tabWidget_ps3)
        self.frame_75_ps3 = QtWidgets.QFrame(self.frame_76_ps3)
        self.frame_75_ps3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_75_ps3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_75_ps3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_75_ps3.setObjectName("frame_75_ps3")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_75_ps3)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.botao_db_adiciona_ps3 = QtWidgets.QPushButton(self.frame_75_ps3)
        self.botao_db_adiciona_ps3.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.botao_db_adiciona_ps3.setFont(font)
        self.botao_db_adiciona_ps3.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 18px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.botao_db_adiciona_ps3.setObjectName("botao_db_adiciona_ps3")
        self.horizontalLayout_18.addWidget(self.botao_db_adiciona_ps3)
        self.botao_db_atualiza_ps3 = QtWidgets.QPushButton(self.frame_75_ps3)
        self.botao_db_atualiza_ps3.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.botao_db_atualiza_ps3.setFont(font)
        self.botao_db_atualiza_ps3.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 18px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.botao_db_atualiza_ps3.setObjectName("botao_db_atualiza_ps3")
        self.horizontalLayout_18.addWidget(self.botao_db_atualiza_ps3)
        self.botao_db_deleta_ps3 = QtWidgets.QPushButton(self.frame_75_ps3)
        self.botao_db_deleta_ps3.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.botao_db_deleta_ps3.setFont(font)
        self.botao_db_deleta_ps3.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 18px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.botao_db_deleta_ps3.setObjectName("botao_db_deleta_ps3")
        self.horizontalLayout_18.addWidget(self.botao_db_deleta_ps3)
        self.verticalLayout_49.addWidget(self.frame_75_ps3)
        self.verticalLayout_5.addWidget(self.frame_76_ps3)
        self.stackedWidget.addWidget(self.pagina_jogos_ps3)
        self.pagina_jogos_retro = QtWidgets.QWidget()
        self.pagina_jogos_retro.setObjectName("pagina_jogos_retro")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.pagina_jogos_retro)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.conteiner_menus_retro = QtWidgets.QFrame(self.pagina_jogos_retro)
        self.conteiner_menus_retro.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.conteiner_menus_retro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.conteiner_menus_retro.setObjectName("conteiner_menus_retro")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.conteiner_menus_retro)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_menus_retro = QtWidgets.QFrame(self.conteiner_menus_retro)
        self.frame_menus_retro.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_menus_retro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_menus_retro.setObjectName("frame_menus_retro")
        self.verticalLayout_39 = QtWidgets.QVBoxLayout(self.frame_menus_retro)
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        self.frame_ex_retro = QtWidgets.QFrame(self.frame_menus_retro)
        self.frame_ex_retro.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ex_retro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ex_retro.setObjectName("frame_ex_retro")
        self.ex3_retro = QtWidgets.QLabel(self.frame_ex_retro)
        self.ex3_retro.setGeometry(QtCore.QRect(20, 70, 591, 21))
        self.ex3_retro.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex3_retro.setObjectName("ex3_retro")
        self.ex1_retro = QtWidgets.QLabel(self.frame_ex_retro)
        self.ex1_retro.setGeometry(QtCore.QRect(20, 30, 601, 20))
        self.ex1_retro.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex1_retro.setObjectName("ex1_retro")
        self.ex2_retro = QtWidgets.QLabel(self.frame_ex_retro)
        self.ex2_retro.setGeometry(QtCore.QRect(20, 50, 521, 21))
        self.ex2_retro.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex2_retro.setObjectName("ex2_retro")
        self.titulo_topo_retro = QtWidgets.QLabel(self.frame_ex_retro)
        self.titulo_topo_retro.setGeometry(QtCore.QRect(20, 0, 451, 21))
        self.titulo_topo_retro.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"}")
        self.titulo_topo_retro.setObjectName("titulo_topo_retro")
        self.ex4_retro = QtWidgets.QLabel(self.frame_ex_retro)
        self.ex4_retro.setGeometry(QtCore.QRect(20, 90, 631, 21))
        self.ex4_retro.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex4_retro.setObjectName("ex4_retro")
        self.ex5_retro = QtWidgets.QLabel(self.frame_ex_retro)
        self.ex5_retro.setGeometry(QtCore.QRect(20, 111, 671, 20))
        self.ex5_retro.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex5_retro.setObjectName("ex5_retro")
        self.ex6_retro = QtWidgets.QLabel(self.frame_ex_retro)
        self.ex6_retro.setGeometry(QtCore.QRect(20, 130, 671, 20))
        self.ex6_retro.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex6_retro.setObjectName("ex6_retro")
        self.verticalLayout_39.addWidget(self.frame_ex_retro)
        self.input_titulo_retro = QtWidgets.QLineEdit(self.frame_menus_retro)
        self.input_titulo_retro.setMinimumSize(QtCore.QSize(0, 40))
        self.input_titulo_retro.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_titulo_retro.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_titulo_retro.setClearButtonEnabled(False)
        self.input_titulo_retro.setObjectName("input_titulo_retro")
        self.verticalLayout_39.addWidget(self.input_titulo_retro)
        self.input_descricao_retro = QtWidgets.QLineEdit(self.frame_menus_retro)
        self.input_descricao_retro.setMinimumSize(QtCore.QSize(0, 40))
        self.input_descricao_retro.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_descricao_retro.setObjectName("input_descricao_retro")
        self.verticalLayout_39.addWidget(self.input_descricao_retro)
        self.input_contentid_retro = QtWidgets.QLineEdit(self.frame_menus_retro)
        self.input_contentid_retro.setMinimumSize(QtCore.QSize(0, 40))
        self.input_contentid_retro.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_contentid_retro.setObjectName("input_contentid_retro")
        self.verticalLayout_39.addWidget(self.input_contentid_retro)
        self.input_link_retro = QtWidgets.QLineEdit(self.frame_menus_retro)
        self.input_link_retro.setMinimumSize(QtCore.QSize(0, 40))
        self.input_link_retro.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_link_retro.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_link_retro.setClearButtonEnabled(False)
        self.input_link_retro.setObjectName("input_link_retro")
        self.verticalLayout_39.addWidget(self.input_link_retro)
        self.horizontalLayout_10.addWidget(self.frame_menus_retro)
        self.frame_direira_menus_retro = QtWidgets.QFrame(self.conteiner_menus_retro)
        self.frame_direira_menus_retro.setMinimumSize(QtCore.QSize(260, 366))
        self.frame_direira_menus_retro.setMaximumSize(QtCore.QSize(270, 16777215))
        self.frame_direira_menus_retro.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_direira_menus_retro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_direira_menus_retro.setObjectName("frame_direira_menus_retro")
        self.verticalLayout_40 = QtWidgets.QVBoxLayout(self.frame_direira_menus_retro)
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_40.setSpacing(6)
        self.verticalLayout_40.setObjectName("verticalLayout_40")
        self.Frame_imagem_retro = QtWidgets.QFrame(self.frame_direira_menus_retro)
        self.Frame_imagem_retro.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Frame_imagem_retro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame_imagem_retro.setObjectName("Frame_imagem_retro")
        self.imagem_retro = QtWidgets.QLabel(self.Frame_imagem_retro)
        self.imagem_retro.setGeometry(QtCore.QRect(0, 10, 261, 261))
        self.imagem_retro.setText("")
        self.imagem_retro.setPixmap(QtGui.QPixmap(":/icone_tcxsgame/images/icone_tcxsgame.jpg"))
        self.imagem_retro.setScaledContents(True)
        self.imagem_retro.setObjectName("imagem_retro")
        self.verticalLayout_40.addWidget(self.Frame_imagem_retro)
        self.btn_upload_imagem_retro = QtWidgets.QPushButton(self.frame_direira_menus_retro)
        self.btn_upload_imagem_retro.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_upload_imagem_retro.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 20px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.btn_upload_imagem_retro.setObjectName("btn_upload_imagem_retro")
        self.verticalLayout_40.addWidget(self.btn_upload_imagem_retro)
        self.frame_58_retro = QtWidgets.QFrame(self.frame_direira_menus_retro)
        self.frame_58_retro.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_58_retro.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_58_retro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_58_retro.setObjectName("frame_58_retro")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.frame_58_retro)
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.botao_db_adiciona_retro = QtWidgets.QPushButton(self.frame_58_retro)
        self.botao_db_adiciona_retro.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.botao_db_adiciona_retro.setFont(font)
        self.botao_db_adiciona_retro.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 18px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.botao_db_adiciona_retro.setObjectName("botao_db_adiciona_retro")
        self.horizontalLayout_23.addWidget(self.botao_db_adiciona_retro)
        self.botao_db_atualiza_retro = QtWidgets.QPushButton(self.frame_58_retro)
        self.botao_db_atualiza_retro.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.botao_db_atualiza_retro.setFont(font)
        self.botao_db_atualiza_retro.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 18px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.botao_db_atualiza_retro.setObjectName("botao_db_atualiza_retro")
        self.horizontalLayout_23.addWidget(self.botao_db_atualiza_retro)
        self.botao_db_deleta_retro = QtWidgets.QPushButton(self.frame_58_retro)
        self.botao_db_deleta_retro.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.botao_db_deleta_retro.setFont(font)
        self.botao_db_deleta_retro.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 18px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.botao_db_deleta_retro.setObjectName("botao_db_deleta_retro")
        self.horizontalLayout_23.addWidget(self.botao_db_deleta_retro)
        self.verticalLayout_40.addWidget(self.frame_58_retro)
        self.horizontalLayout_10.addWidget(self.frame_direira_menus_retro)
        self.verticalLayout_10.addWidget(self.conteiner_menus_retro)
        self.frame_59_retro = QtWidgets.QFrame(self.pagina_jogos_retro)
        self.frame_59_retro.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_59_retro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_59_retro.setObjectName("frame_59_retro")
        self.verticalLayout_41 = QtWidgets.QVBoxLayout(self.frame_59_retro)
        self.verticalLayout_41.setObjectName("verticalLayout_41")
        self.tabela_database_retro = QtWidgets.QTableView(self.frame_59_retro)
        self.tabela_database_retro.setStyleSheet("QHeaderView {\n"
"background: rgb(30, 30, 30);\n"
"}\n"
"QHeaderView::section{\n"
"    color: rgb(255, 255, 255);\n"
"background: rgb(35,35,35);\n"
"}\n"
"QTableCornerButton::section{\n"
"background: rgb(35,35,35);\n"
"}\n"
"QHeaderView::section:pressed{\n"
"background: rgb(173,0,0);\n"
"}\n"
"QTableCornerButton::section:pressed{\n"
"background: rgb(173,0,0);\n"
"}\n"
"\n"
"\n"
"\n"
"QTableView{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QTableView:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QTableView:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}\n"
"* { gridline-color: gray }")
        self.tabela_database_retro.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tabela_database_retro.setGridStyle(QtCore.Qt.SolidLine)
        self.tabela_database_retro.setObjectName("tabela_database_retro")
        self.tabela_database_retro.horizontalHeader().setDefaultSectionSize(200)
        self.verticalLayout_41.addWidget(self.tabela_database_retro)
        self.frame_60_retro = QtWidgets.QFrame(self.frame_59_retro)
        self.frame_60_retro.setMaximumSize(QtCore.QSize(10, 10))
        self.frame_60_retro.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_60_retro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_60_retro.setObjectName("frame_60_retro")
        self.verticalLayout_41.addWidget(self.frame_60_retro)
        self.verticalLayout_10.addWidget(self.frame_59_retro)
        self.stackedWidget.addWidget(self.pagina_jogos_retro)
        self.pagina_jogos_extras = QtWidgets.QWidget()
        self.pagina_jogos_extras.setObjectName("pagina_jogos_extras")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.pagina_jogos_extras)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_48_extras = QtWidgets.QFrame(self.pagina_jogos_extras)
        self.frame_48_extras.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_48_extras.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_48_extras.setObjectName("frame_48_extras")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_48_extras)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.frame_inputs_extras = QtWidgets.QFrame(self.frame_48_extras)
        self.frame_inputs_extras.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_inputs_extras.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_inputs_extras.setObjectName("frame_inputs_extras")
        self.verticalLayout_42 = QtWidgets.QVBoxLayout(self.frame_inputs_extras)
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_42.setObjectName("verticalLayout_42")
        self.frame_ex_extras = QtWidgets.QFrame(self.frame_inputs_extras)
        self.frame_ex_extras.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ex_extras.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ex_extras.setObjectName("frame_ex_extras")
        self.ex3_extras = QtWidgets.QLabel(self.frame_ex_extras)
        self.ex3_extras.setGeometry(QtCore.QRect(20, 70, 591, 21))
        self.ex3_extras.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex3_extras.setObjectName("ex3_extras")
        self.ex1_extras = QtWidgets.QLabel(self.frame_ex_extras)
        self.ex1_extras.setGeometry(QtCore.QRect(20, 30, 601, 20))
        self.ex1_extras.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex1_extras.setObjectName("ex1_extras")
        self.ex2_extras = QtWidgets.QLabel(self.frame_ex_extras)
        self.ex2_extras.setGeometry(QtCore.QRect(20, 50, 521, 21))
        self.ex2_extras.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex2_extras.setObjectName("ex2_extras")
        self.titulo_topo_extras = QtWidgets.QLabel(self.frame_ex_extras)
        self.titulo_topo_extras.setGeometry(QtCore.QRect(20, 0, 451, 21))
        self.titulo_topo_extras.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"}")
        self.titulo_topo_extras.setObjectName("titulo_topo_extras")
        self.ex4_extras = QtWidgets.QLabel(self.frame_ex_extras)
        self.ex4_extras.setGeometry(QtCore.QRect(20, 90, 631, 21))
        self.ex4_extras.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex4_extras.setObjectName("ex4_extras")
        self.ex5_extras = QtWidgets.QLabel(self.frame_ex_extras)
        self.ex5_extras.setGeometry(QtCore.QRect(20, 111, 671, 20))
        self.ex5_extras.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex5_extras.setObjectName("ex5_extras")
        self.ex6_extras = QtWidgets.QLabel(self.frame_ex_extras)
        self.ex6_extras.setGeometry(QtCore.QRect(20, 130, 671, 20))
        self.ex6_extras.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex6_extras.setObjectName("ex6_extras")
        self.verticalLayout_42.addWidget(self.frame_ex_extras)
        self.input_titulo_extras = QtWidgets.QLineEdit(self.frame_inputs_extras)
        self.input_titulo_extras.setMinimumSize(QtCore.QSize(0, 40))
        self.input_titulo_extras.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_titulo_extras.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_titulo_extras.setClearButtonEnabled(False)
        self.input_titulo_extras.setObjectName("input_titulo_extras")
        self.verticalLayout_42.addWidget(self.input_titulo_extras)
        self.input_descricao_extras = QtWidgets.QLineEdit(self.frame_inputs_extras)
        self.input_descricao_extras.setMinimumSize(QtCore.QSize(0, 40))
        self.input_descricao_extras.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_descricao_extras.setObjectName("input_descricao_extras")
        self.verticalLayout_42.addWidget(self.input_descricao_extras)
        self.input_contentid_extras = QtWidgets.QLineEdit(self.frame_inputs_extras)
        self.input_contentid_extras.setMinimumSize(QtCore.QSize(0, 40))
        self.input_contentid_extras.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_contentid_extras.setObjectName("input_contentid_extras")
        self.verticalLayout_42.addWidget(self.input_contentid_extras)
        self.input_link_extras = QtWidgets.QLineEdit(self.frame_inputs_extras)
        self.input_link_extras.setMinimumSize(QtCore.QSize(0, 40))
        self.input_link_extras.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.input_link_extras.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_link_extras.setClearButtonEnabled(False)
        self.input_link_extras.setObjectName("input_link_extras")
        self.verticalLayout_42.addWidget(self.input_link_extras)
        self.horizontalLayout_13.addWidget(self.frame_inputs_extras)
        self.frame_57_extras = QtWidgets.QFrame(self.frame_48_extras)
        self.frame_57_extras.setMinimumSize(QtCore.QSize(260, 366))
        self.frame_57_extras.setMaximumSize(QtCore.QSize(270, 16777215))
        self.frame_57_extras.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_57_extras.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_57_extras.setObjectName("frame_57_extras")
        self.verticalLayout_43 = QtWidgets.QVBoxLayout(self.frame_57_extras)
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_43.setSpacing(6)
        self.verticalLayout_43.setObjectName("verticalLayout_43")
        self.frame_imagem_extras = QtWidgets.QFrame(self.frame_57_extras)
        self.frame_imagem_extras.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_imagem_extras.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_imagem_extras.setObjectName("frame_imagem_extras")
        self.imagem_extras = QtWidgets.QLabel(self.frame_imagem_extras)
        self.imagem_extras.setGeometry(QtCore.QRect(0, 10, 261, 261))
        self.imagem_extras.setText("")
        self.imagem_extras.setPixmap(QtGui.QPixmap(":/icone_tcxsgame/images/icone_tcxsgame.jpg"))
        self.imagem_extras.setScaledContents(True)
        self.imagem_extras.setObjectName("imagem_extras")
        self.verticalLayout_43.addWidget(self.frame_imagem_extras)
        self.btn_upload_imagem_extras = QtWidgets.QPushButton(self.frame_57_extras)
        self.btn_upload_imagem_extras.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_upload_imagem_extras.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 20px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.btn_upload_imagem_extras.setObjectName("btn_upload_imagem_extras")
        self.verticalLayout_43.addWidget(self.btn_upload_imagem_extras)
        self.frame_btns_extras = QtWidgets.QFrame(self.frame_57_extras)
        self.frame_btns_extras.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_btns_extras.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_btns_extras.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btns_extras.setObjectName("frame_btns_extras")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_btns_extras)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.botao_db_adiciona_extras = QtWidgets.QPushButton(self.frame_btns_extras)
        self.botao_db_adiciona_extras.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.botao_db_adiciona_extras.setFont(font)
        self.botao_db_adiciona_extras.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 18px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.botao_db_adiciona_extras.setObjectName("botao_db_adiciona_extras")
        self.horizontalLayout_16.addWidget(self.botao_db_adiciona_extras)
        self.botao_db_atualiza_extras = QtWidgets.QPushButton(self.frame_btns_extras)
        self.botao_db_atualiza_extras.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.botao_db_atualiza_extras.setFont(font)
        self.botao_db_atualiza_extras.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 18px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.botao_db_atualiza_extras.setObjectName("botao_db_atualiza_extras")
        self.horizontalLayout_16.addWidget(self.botao_db_atualiza_extras)
        self.botao_db_deleta_extras = QtWidgets.QPushButton(self.frame_btns_extras)
        self.botao_db_deleta_extras.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("SegoeUIl,12")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.botao_db_deleta_extras.setFont(font)
        self.botao_db_deleta_extras.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 18px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.botao_db_deleta_extras.setObjectName("botao_db_deleta_extras")
        self.horizontalLayout_16.addWidget(self.botao_db_deleta_extras)
        self.verticalLayout_43.addWidget(self.frame_btns_extras)
        self.horizontalLayout_13.addWidget(self.frame_57_extras)
        self.verticalLayout_13.addWidget(self.frame_48_extras)
        self.frame_63_extras = QtWidgets.QFrame(self.pagina_jogos_extras)
        self.frame_63_extras.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_63_extras.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_63_extras.setObjectName("frame_63_extras")
        self.verticalLayout_44 = QtWidgets.QVBoxLayout(self.frame_63_extras)
        self.verticalLayout_44.setObjectName("verticalLayout_44")
        self.tabela_database_extras = QtWidgets.QTableView(self.frame_63_extras)
        self.tabela_database_extras.setStyleSheet("QHeaderView {\n"
"background: rgb(30, 30, 30);\n"
"}\n"
"QHeaderView::section{\n"
"    color: rgb(255, 255, 255);\n"
"background: rgb(35,35,35);\n"
"}\n"
"QTableCornerButton::section{\n"
"background: rgb(35,35,35);\n"
"}\n"
"QHeaderView::section:pressed{\n"
"background: rgb(173,0,0);\n"
"}\n"
"QTableCornerButton::section:pressed{\n"
"background: rgb(173,0,0);\n"
"}\n"
"\n"
"\n"
"\n"
"QTableView{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QTableView:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QTableView:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}\n"
"* { gridline-color: gray }")
        self.tabela_database_extras.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tabela_database_extras.setGridStyle(QtCore.Qt.SolidLine)
        self.tabela_database_extras.setObjectName("tabela_database_extras")
        self.tabela_database_extras.horizontalHeader().setDefaultSectionSize(200)
        self.verticalLayout_44.addWidget(self.tabela_database_extras)
        self.frame_64_extras = QtWidgets.QFrame(self.frame_63_extras)
        self.frame_64_extras.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_64_extras.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_64_extras.setObjectName("frame_64_extras")
        self.verticalLayout_44.addWidget(self.frame_64_extras)
        self.verticalLayout_13.addWidget(self.frame_63_extras)
        self.stackedWidget.addWidget(self.pagina_jogos_extras)
        self.pagina_backup = QtWidgets.QWidget()
        self.pagina_backup.setObjectName("pagina_backup")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.pagina_backup)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.conteiner_topo_backup = QtWidgets.QFrame(self.pagina_backup)
        self.conteiner_topo_backup.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.conteiner_topo_backup.setFrameShadow(QtWidgets.QFrame.Raised)
        self.conteiner_topo_backup.setObjectName("conteiner_topo_backup")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.conteiner_topo_backup)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.frame_65backup = QtWidgets.QFrame(self.conteiner_topo_backup)
        self.frame_65backup.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_65backup.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_65backup.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_65backup.setObjectName("frame_65backup")
        self.ex3_backup = QtWidgets.QLabel(self.frame_65backup)
        self.ex3_backup.setGeometry(QtCore.QRect(10, 70, 561, 31))
        self.ex3_backup.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex3_backup.setObjectName("ex3_backup")
        self.ex2_backup = QtWidgets.QLabel(self.frame_65backup)
        self.ex2_backup.setGeometry(QtCore.QRect(10, 50, 511, 31))
        self.ex2_backup.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex2_backup.setObjectName("ex2_backup")
        self.titulo_backup = QtWidgets.QLabel(self.frame_65backup)
        self.titulo_backup.setGeometry(QtCore.QRect(10, 10, 491, 21))
        self.titulo_backup.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"}")
        self.titulo_backup.setObjectName("titulo_backup")
        self.ex1_backup = QtWidgets.QLabel(self.frame_65backup)
        self.ex1_backup.setGeometry(QtCore.QRect(10, 30, 601, 31))
        self.ex1_backup.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex1_backup.setObjectName("ex1_backup")
        self.btn_iniciar_backup = QtWidgets.QPushButton(self.frame_65backup)
        self.btn_iniciar_backup.setGeometry(QtCore.QRect(150, 100, 371, 42))
        self.btn_iniciar_backup.setMinimumSize(QtCore.QSize(10, 42))
        self.btn_iniciar_backup.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 20px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(173,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130,0,0);\n"
"}")
        self.btn_iniciar_backup.setObjectName("btn_iniciar_backup")
        self.verticalLayout_15.addWidget(self.frame_65backup)
        self.frame_66_backup = QtWidgets.QFrame(self.conteiner_topo_backup)
        self.frame_66_backup.setMinimumSize(QtCore.QSize(0, 450))
        self.frame_66_backup.setMaximumSize(QtCore.QSize(16777215, 450))
        self.frame_66_backup.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_66_backup.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_66_backup.setObjectName("frame_66_backup")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_66_backup)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_2 = QtWidgets.QFrame(self.frame_66_backup)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.t_backup = QtWidgets.QLabel(self.frame_2)
        self.t_backup.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.t_backup.setObjectName("t_backup")
        self.verticalLayout_29.addWidget(self.t_backup)
        self.progressBar_backup_users = QtWidgets.QProgressBar(self.frame_2)
        self.progressBar_backup_users.setStyleSheet("QProgressBar{\n"
"border: 2px solid rgba(45,45,45,0);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"background-color: rgb(170,0,0);\n"
"}")
        self.progressBar_backup_users.setProperty("value", 0)
        self.progressBar_backup_users.setTextVisible(False)
        self.progressBar_backup_users.setObjectName("progressBar_backup_users")
        self.verticalLayout_29.addWidget(self.progressBar_backup_users)
        self.explica1cadastro_users_4 = QtWidgets.QLabel(self.frame_2)
        self.explica1cadastro_users_4.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.explica1cadastro_users_4.setObjectName("explica1cadastro_users_4")
        self.verticalLayout_29.addWidget(self.explica1cadastro_users_4)
        self.progressBar_backup_psp = QtWidgets.QProgressBar(self.frame_2)
        self.progressBar_backup_psp.setStyleSheet("QProgressBar{\n"
"border: 2px solid rgba(45,45,45,0);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"background-color: rgb(170,0,0);\n"
"}")
        self.progressBar_backup_psp.setProperty("value", 0)
        self.progressBar_backup_psp.setTextVisible(False)
        self.progressBar_backup_psp.setObjectName("progressBar_backup_psp")
        self.verticalLayout_29.addWidget(self.progressBar_backup_psp)
        self.explica1cadastro_users_6 = QtWidgets.QLabel(self.frame_2)
        self.explica1cadastro_users_6.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.explica1cadastro_users_6.setObjectName("explica1cadastro_users_6")
        self.verticalLayout_29.addWidget(self.explica1cadastro_users_6)
        self.progressBar_backup_ps2 = QtWidgets.QProgressBar(self.frame_2)
        self.progressBar_backup_ps2.setStyleSheet("QProgressBar{\n"
"border: 2px solid rgba(45,45,45,0);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"background-color: rgb(170,0,0);\n"
"}")
        self.progressBar_backup_ps2.setProperty("value", 0)
        self.progressBar_backup_ps2.setTextVisible(False)
        self.progressBar_backup_ps2.setObjectName("progressBar_backup_ps2")
        self.verticalLayout_29.addWidget(self.progressBar_backup_ps2)
        self.explica1cadastro_users_7 = QtWidgets.QLabel(self.frame_2)
        self.explica1cadastro_users_7.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.explica1cadastro_users_7.setObjectName("explica1cadastro_users_7")
        self.verticalLayout_29.addWidget(self.explica1cadastro_users_7)
        self.progressBar_backup_emuladores = QtWidgets.QProgressBar(self.frame_2)
        self.progressBar_backup_emuladores.setStyleSheet("QProgressBar{\n"
"border: 2px solid rgba(45,45,45,0);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"background-color: rgb(170,0,0);\n"
"}")
        self.progressBar_backup_emuladores.setProperty("value", 0)
        self.progressBar_backup_emuladores.setTextVisible(False)
        self.progressBar_backup_emuladores.setObjectName("progressBar_backup_emuladores")
        self.verticalLayout_29.addWidget(self.progressBar_backup_emuladores)
        self.horizontalLayout_4.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(self.frame_66_backup)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.t_backup_2 = QtWidgets.QLabel(self.frame)
        self.t_backup_2.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.t_backup_2.setObjectName("t_backup_2")
        self.verticalLayout_28.addWidget(self.t_backup_2)
        self.progressBar_backup_infos = QtWidgets.QProgressBar(self.frame)
        self.progressBar_backup_infos.setStyleSheet("QProgressBar{\n"
"border: 2px solid rgba(45,45,45,0);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"background-color: rgb(170,0,0);\n"
"}")
        self.progressBar_backup_infos.setProperty("value", 0)
        self.progressBar_backup_infos.setTextVisible(False)
        self.progressBar_backup_infos.setObjectName("progressBar_backup_infos")
        self.verticalLayout_28.addWidget(self.progressBar_backup_infos)
        self.explica1cadastro_users_5 = QtWidgets.QLabel(self.frame)
        self.explica1cadastro_users_5.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.explica1cadastro_users_5.setObjectName("explica1cadastro_users_5")
        self.verticalLayout_28.addWidget(self.explica1cadastro_users_5)
        self.progressBar_backup_ps1 = QtWidgets.QProgressBar(self.frame)
        self.progressBar_backup_ps1.setStyleSheet("QProgressBar{\n"
"border: 2px solid rgba(45,45,45,0);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"background-color: rgb(170,0,0);\n"
"}")
        self.progressBar_backup_ps1.setProperty("value", 0)
        self.progressBar_backup_ps1.setTextVisible(False)
        self.progressBar_backup_ps1.setObjectName("progressBar_backup_ps1")
        self.verticalLayout_28.addWidget(self.progressBar_backup_ps1)
        self.explica1cadastro_users_8 = QtWidgets.QLabel(self.frame)
        self.explica1cadastro_users_8.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.explica1cadastro_users_8.setObjectName("explica1cadastro_users_8")
        self.verticalLayout_28.addWidget(self.explica1cadastro_users_8)
        self.progressBar_backup_ps3 = QtWidgets.QProgressBar(self.frame)
        self.progressBar_backup_ps3.setStyleSheet("QProgressBar{\n"
"border: 2px solid rgba(45,45,45,0);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"background-color: rgb(170,0,0);\n"
"}")
        self.progressBar_backup_ps3.setProperty("value", 0)
        self.progressBar_backup_ps3.setTextVisible(False)
        self.progressBar_backup_ps3.setObjectName("progressBar_backup_ps3")
        self.verticalLayout_28.addWidget(self.progressBar_backup_ps3)
        self.explica1cadastro_users_9 = QtWidgets.QLabel(self.frame)
        self.explica1cadastro_users_9.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.explica1cadastro_users_9.setObjectName("explica1cadastro_users_9")
        self.verticalLayout_28.addWidget(self.explica1cadastro_users_9)
        self.progressBar_backup_extras = QtWidgets.QProgressBar(self.frame)
        self.progressBar_backup_extras.setStyleSheet("QProgressBar{\n"
"border: 2px solid rgba(45,45,45,0);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"background-color: rgb(170,0,0);\n"
"}")
        self.progressBar_backup_extras.setProperty("value", 0)
        self.progressBar_backup_extras.setTextVisible(False)
        self.progressBar_backup_extras.setObjectName("progressBar_backup_extras")
        self.verticalLayout_28.addWidget(self.progressBar_backup_extras)
        self.horizontalLayout_4.addWidget(self.frame)
        self.verticalLayout_15.addWidget(self.frame_66_backup)
        self.verticalLayout_16.addWidget(self.conteiner_topo_backup)
        self.stackedWidget.addWidget(self.pagina_backup)
        self.pagina_databases = QtWidgets.QWidget()
        self.pagina_databases.setObjectName("pagina_databases")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.pagina_databases)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame_3_databases = QtWidgets.QFrame(self.pagina_databases)
        self.frame_3_databases.setMinimumSize(QtCore.QSize(0, 90))
        self.frame_3_databases.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3_databases.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3_databases.setObjectName("frame_3_databases")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.frame_3_databases)
        self.horizontalLayout_24.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.frame_67_databases = QtWidgets.QFrame(self.frame_3_databases)
        self.frame_67_databases.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_67_databases.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_67_databases.setObjectName("frame_67_databases")
        self.ex1_databases = QtWidgets.QLabel(self.frame_67_databases)
        self.ex1_databases.setGeometry(QtCore.QRect(20, 30, 601, 20))
        self.ex1_databases.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex1_databases.setObjectName("ex1_databases")
        self.ex2_databases = QtWidgets.QLabel(self.frame_67_databases)
        self.ex2_databases.setGeometry(QtCore.QRect(20, 50, 521, 21))
        self.ex2_databases.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex2_databases.setObjectName("ex2_databases")
        self.titulo_topo_databases = QtWidgets.QLabel(self.frame_67_databases)
        self.titulo_topo_databases.setGeometry(QtCore.QRect(20, 0, 451, 21))
        self.titulo_topo_databases.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"}")
        self.titulo_topo_databases.setObjectName("titulo_topo_databases")
        self.comboBox_databases = QtWidgets.QComboBox(self.frame_67_databases)
        self.comboBox_databases.setGeometry(QtCore.QRect(400, 10, 341, 40))
        self.comboBox_databases.setMinimumSize(QtCore.QSize(0, 40))
        self.comboBox_databases.setStyleSheet("QComboBox{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QComboBox:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QComboBox:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.comboBox_databases.setObjectName("comboBox_databases")
        self.comboBox_databases.addItem("")
        self.comboBox_databases.addItem("")
        self.comboBox_databases.addItem("")
        self.comboBox_databases.addItem("")
        self.comboBox_databases.addItem("")
        self.comboBox_databases.addItem("")
        self.comboBox_databases.addItem("")
        self.comboBox_databases.addItem("")
        self.comboBox_databases.addItem("")
        self.horizontalLayout_24.addWidget(self.frame_67_databases)
        self.verticalLayout_14.addWidget(self.frame_3_databases)
        self.frame_71_databases = QtWidgets.QFrame(self.pagina_databases)
        self.frame_71_databases.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_71_databases.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_71_databases.setObjectName("frame_71_databases")
        self.verticalLayout_47 = QtWidgets.QVBoxLayout(self.frame_71_databases)
        self.verticalLayout_47.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName("verticalLayout_47")
        self.tabela_dados_db_databases = QtWidgets.QTableView(self.frame_71_databases)
        self.tabela_dados_db_databases.setStyleSheet("QHeaderView {\n"
"background: rgb(30, 30, 30);\n"
"}\n"
"QHeaderView::section{\n"
"    color: rgb(255, 255, 255);\n"
"background: rgb(35,35,35);\n"
"}\n"
"QTableCornerButton::section{\n"
"background: rgb(35,35,35);\n"
"}\n"
"QHeaderView::section:pressed{\n"
"background: rgb(173,0,0);\n"
"}\n"
"QTableCornerButton::section:pressed{\n"
"background: rgb(173,0,0);\n"
"}\n"
"\n"
"\n"
"\n"
"QTableView{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QTableView:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QTableView:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}\n"
"* { gridline-color: gray }")
        self.tabela_dados_db_databases.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tabela_dados_db_databases.setGridStyle(QtCore.Qt.SolidLine)
        self.tabela_dados_db_databases.setObjectName("tabela_dados_db_databases")
        self.tabela_dados_db_databases.horizontalHeader().setDefaultSectionSize(200)
        self.verticalLayout_47.addWidget(self.tabela_dados_db_databases)
        self.frame_72_databases = QtWidgets.QFrame(self.frame_71_databases)
        self.frame_72_databases.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_72_databases.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_72_databases.setObjectName("frame_72_databases")
        self.verticalLayout_47.addWidget(self.frame_72_databases)
        self.verticalLayout_14.addWidget(self.frame_71_databases)
        self.stackedWidget.addWidget(self.pagina_databases)
        self.pagina_verifica_404 = QtWidgets.QWidget()
        self.pagina_verifica_404.setObjectName("pagina_verifica_404")
        self.verticalLayout_70 = QtWidgets.QVBoxLayout(self.pagina_verifica_404)
        self.verticalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_70.setSpacing(0)
        self.verticalLayout_70.setObjectName("verticalLayout_70")
        self.frame_94_verifica_404 = QtWidgets.QFrame(self.pagina_verifica_404)
        self.frame_94_verifica_404.setMinimumSize(QtCore.QSize(0, 70))
        self.frame_94_verifica_404.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_94_verifica_404.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_94_verifica_404.setObjectName("frame_94_verifica_404")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.frame_94_verifica_404)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.frame_96_verifica_404 = QtWidgets.QFrame(self.frame_94_verifica_404)
        self.frame_96_verifica_404.setMinimumSize(QtCore.QSize(0, 110))
        self.frame_96_verifica_404.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_96_verifica_404.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_96_verifica_404.setObjectName("frame_96_verifica_404")
        self.ex1_verifica_404 = QtWidgets.QLabel(self.frame_96_verifica_404)
        self.ex1_verifica_404.setGeometry(QtCore.QRect(20, 30, 601, 20))
        self.ex1_verifica_404.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex1_verifica_404.setObjectName("ex1_verifica_404")
        self.ex2_verifica_404 = QtWidgets.QLabel(self.frame_96_verifica_404)
        self.ex2_verifica_404.setGeometry(QtCore.QRect(20, 50, 521, 21))
        self.ex2_verifica_404.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 15px Segoe UI, bold;\n"
"}")
        self.ex2_verifica_404.setObjectName("ex2_verifica_404")
        self.titulo_topo_verifica_404 = QtWidgets.QLabel(self.frame_96_verifica_404)
        self.titulo_topo_verifica_404.setGeometry(QtCore.QRect(20, 0, 451, 21))
        self.titulo_topo_verifica_404.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"}")
        self.titulo_topo_verifica_404.setObjectName("titulo_topo_verifica_404")
        self.comboBox_verifica404 = QtWidgets.QComboBox(self.frame_96_verifica_404)
        self.comboBox_verifica404.setGeometry(QtCore.QRect(160, 70, 331, 40))
        self.comboBox_verifica404.setMinimumSize(QtCore.QSize(0, 40))
        self.comboBox_verifica404.setStyleSheet("QComboBox{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QComboBox:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QComboBox:focus{\n"
"border: 2px solid  rgb(170,0,0);\n"
"    color: rgb(170,0,0);\n"
"}")
        self.comboBox_verifica404.setObjectName("comboBox_verifica404")
        self.comboBox_verifica404.addItem("")
        self.comboBox_verifica404.addItem("")
        self.comboBox_verifica404.addItem("")
        self.comboBox_verifica404.addItem("")
        self.comboBox_verifica404.addItem("")
        self.comboBox_verifica404.addItem("")
        self.comboBox_verifica404.addItem("")
        self.horizontalLayout_31.addWidget(self.frame_96_verifica_404)
        self.verticalLayout_70.addWidget(self.frame_94_verifica_404)
        self.frame_97_verifica_404 = QtWidgets.QFrame(self.pagina_verifica_404)
        self.frame_97_verifica_404.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_97_verifica_404.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_97_verifica_404.setObjectName("frame_97_verifica_404")
        self.verticalLayout_69 = QtWidgets.QVBoxLayout(self.frame_97_verifica_404)
        self.verticalLayout_69.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_69.setSpacing(0)
        self.verticalLayout_69.setObjectName("verticalLayout_69")
        self.frame_98_verifica_404 = QtWidgets.QFrame(self.frame_97_verifica_404)
        self.frame_98_verifica_404.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_98_verifica_404.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_98_verifica_404.setObjectName("frame_98_verifica_404")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.frame_98_verifica_404)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.progressBar404 = QtWidgets.QProgressBar(self.frame_98_verifica_404)
        self.progressBar404.setStyleSheet("QProgressBar{\n"
"border: 2px solid rgba(45,45,45,0);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"background-color: rgb(170,0,0);\n"
"}")
        self.progressBar404.setProperty("value", 0)
        self.progressBar404.setTextVisible(False)
        self.progressBar404.setObjectName("progressBar404")
        self.verticalLayout_26.addWidget(self.progressBar404)
        self.textBrowser_verifica404 = QtWidgets.QTextBrowser(self.frame_98_verifica_404)
        self.textBrowser_verifica404.setOpenExternalLinks(True)
        self.textBrowser_verifica404.setObjectName("textBrowser_verifica404")
        self.verticalLayout_26.addWidget(self.textBrowser_verifica404)
        self.verticalLayout_69.addWidget(self.frame_98_verifica_404)
        self.verticalLayout_70.addWidget(self.frame_97_verifica_404)
        self.stackedWidget.addWidget(self.pagina_verifica_404)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.rodape = QtWidgets.QFrame(self.janela_central)
        self.rodape.setMinimumSize(QtCore.QSize(0, 17))
        self.rodape.setStyleSheet("background-color: rgb(31, 31, 31);")
        self.rodape.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.rodape.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rodape.setObjectName("rodape")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.rodape)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.rodape_desenvolvedor = QtWidgets.QLabel(self.rodape)
        self.rodape_desenvolvedor.setMinimumSize(QtCore.QSize(440, 0))
        self.rodape_desenvolvedor.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(98, 103, 111);\n"
"font: 10px ,Segoe UI;\n"
"margin-right: 5px;\n"
"}\n"
"\n"
"")
        self.rodape_desenvolvedor.setScaledContents(False)
        self.rodape_desenvolvedor.setObjectName("rodape_desenvolvedor")
        self.horizontalLayout_7.addWidget(self.rodape_desenvolvedor)
        self.rodape_versao = QtWidgets.QLabel(self.rodape)
        self.rodape_versao.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(98, 103, 111);\n"
"font: 10px ,Segoe UI;\n"
"margin-right: 5px;\n"
"}\n"
"\n"
"")
        self.rodape_versao.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rodape_versao.setObjectName("rodape_versao")
        self.horizontalLayout_7.addWidget(self.rodape_versao)
        self.redimensionador = QtWidgets.QFrame(self.rodape)
        self.redimensionador.setMaximumSize(QtCore.QSize(20, 20))
        self.redimensionador.setStyleSheet("QSizeGrip {\n"
"    \n"
"    background-image: url(:/redimensiona/images/cil-move.png);\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"}")
        self.redimensionador.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.redimensionador.setFrameShadow(QtWidgets.QFrame.Raised)
        self.redimensionador.setObjectName("redimensionador")
        self.horizontalLayout_7.addWidget(self.redimensionador)
        self.verticalLayout_4.addWidget(self.rodape)
        self.horizontalLayout.addWidget(self.janela_central)
        self.verticalLayout.addWidget(self.conteiner_central)
        MainWindow.setCentralWidget(self.janela_pai)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget_ps3.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titulo_programa.setText(_translate("MainWindow", "TCXS Project Store "))
        self.texto_menu_home.setText(_translate("MainWindow", "home"))
        self.texto_botao_cadastro_user.setText(_translate("MainWindow", "cadastro USERS"))
        self.texto_botao_verifica_user.setText(_translate("MainWindow", "verificar ACESSOS"))
        self.texto_botao_infos_store.setText(_translate("MainWindow", "infos STORE"))
        self.texto_menu_psp.setText(_translate("MainWindow", "jogos PSP"))
        self.texto_menu_ps1.setText(_translate("MainWindow", "jogos PS1"))
        self.texto_menu_ps2.setText(_translate("MainWindow", "jogos PS2"))
        self.texto_menu_ps3.setText(_translate("MainWindow", "jogos PS3"))
        self.texto_menu_retro.setText(_translate("MainWindow", "jogos RETRO"))
        self.texto_menu_extras.setText(_translate("MainWindow", "links EXTRAS"))
        self.texto_menu_database.setText(_translate("MainWindow", "database TCXS"))
        self.texto_menu_404.setText(_translate("MainWindow", "verificador 404"))
        self.texto_menu_bottelegram.setText(_translate("MainWindow", "backup DATABASE"))
        self.titulo_topo_verifica_405.setText(_translate("MainWindow", "MYSQL [database | user | senha | host]    |    FTP [endereço | user | senha]"))
        self.input_nome_database_home.setText(_translate("MainWindow", "nome database"))
        self.input_user_database_home.setText(_translate("MainWindow", "user database"))
        self.input_senha_database_home.setText(_translate("MainWindow", "senha database"))
        self.input_host_database_home.setText(_translate("MainWindow", "host database"))
        self.input_endereco_ftp.setText(_translate("MainWindow", "endereço ftp"))
        self.input_user_ftp.setText(_translate("MainWindow", "user ftp"))
        self.input_senha_ftp.setText(_translate("MainWindow", "senha ftp"))
        self.btn_database_home.setText(_translate("MainWindow", "enviar"))
        self.explica1cadastro_users.setText(_translate("MainWindow", "- insira o nome de exibição que o usuário irá receber ao entrar na loja."))
        self.titulo_cadastro_users.setText(_translate("MainWindow", "CADASTRO DE USUÁRIOS"))
        self.explica2cadastro_users.setText(_translate("MainWindow", "- insira o user que o que o usuário ira receber ao entrar na loja."))
        self.explica3cadastro_users.setText(_translate("MainWindow", "- insira a senha que o que o usuário ira receber ao entrar na loja."))
        self.input_nome_user.setText(_translate("MainWindow", "Nome Exibição"))
        self.input_username_user.setText(_translate("MainWindow", "user"))
        self.input_senha_user.setText(_translate("MainWindow", "senha"))
        self.btn_adiciona_user.setText(_translate("MainWindow", "adiciona"))
        self.btn_atualiza_user.setText(_translate("MainWindow", "atualiza"))
        self.btn_deleta_user.setText(_translate("MainWindow", "deleta"))
        self.ex3_acessos_usuarios.setText(_translate("MainWindow", "- tente mais tarde caso não apareça nada, é necessário ao menos um login do usuário para este sistema."))
        self.ex1_acessos_usuarios.setText(_translate("MainWindow", "- insira o user e clique em pesquisar."))
        self.titulo_acessos_usuarios.setText(_translate("MainWindow", "ACESSOS USUÁRIOS"))
        self.ex2_acessos_usuarios.setText(_translate("MainWindow", "- caso usuário ainda não tenha logado não aparecerá nada na tabela"))
        self.input_pesquisa_acessos_usuarios.setText(_translate("MainWindow", "user"))
        self.btn_pesquisa_acessos_usuarios.setText(_translate("MainWindow", "pesquisar"))
        self.ex3_playstation_infos.setText(_translate("MainWindow", "- o sistema aceita programação html, pode ser usado espaços, estilos e div\'s no formato html."))
        self.ex1_playstation_infos.setText(_translate("MainWindow", "- insira a informação que quiser para os usuários."))
        self.titulo_playstation_infos.setText(_translate("MainWindow", "CADASTRO DE INFORMAÇÕES DA HOMEPAGE"))
        self.ex2_playstation_infos.setText(_translate("MainWindow", "- estas informações aparecem logo após a tela de login do usuário exibindo avisos importantes."))
        self.input_playstation_infos.setText(_translate("MainWindow", "Informação da homepage"))
        self.btn_adiciona_infos.setText(_translate("MainWindow", "adiciona"))
        self.btn_atualiza_infos.setText(_translate("MainWindow", "atualiza"))
        self.btn_deleta_infos.setText(_translate("MainWindow", "deleta"))
        self.ex3__psp.setText(_translate("MainWindow", "- insira a content id, caso não tenha digite qualquer coisa jamais deixe o campo vazio."))
        self.ex1__psp.setText(_translate("MainWindow", "- insira o titulo do jogo de PlayStation PSP."))
        self.ex2__psp.setText(_translate("MainWindow", "<html><head/><body><p>- insira a descrição, atenção: para pular linhas use a tag html.<br/></p></body></html>"))
        self.titulo_topo_psp.setText(_translate("MainWindow", "CADASTRO PLAYSTATION PSP"))
        self.ex4__psp.setText(_translate("MainWindow", "- insira o link do jogo que o link, em caso de uso dropbox troque o final dl=0 por dl=1."))
        self.ex5__psp.setText(_translate("MainWindow", "- faça o upload da imagem, caso esteja editando copie e cole o nome da imagem cadastrada."))
        self.ex6__psp.setText(_translate("MainWindow", "- para atualizar preencha os dados normalmente, clique sobre o jogo na tabela  e em atualizar."))
        self.input_titulo_jogo_psp.setText(_translate("MainWindow", "Titulo PSP"))
        self.input_descricao_jogo_psp.setText(_translate("MainWindow", "Descrição | Usar tag <br> para pular linhas."))
        self.input_contentid_psp.setText(_translate("MainWindow", "Content ID"))
        self.input_link_jogo_psp.setText(_translate("MainWindow", "Link"))
        self.btn_upload_imagem_psp.setText(_translate("MainWindow", "upload de imagem"))
        self.botao_db_adiciona_psp.setText(_translate("MainWindow", "adicionar"))
        self.botao_db_atualiza_psp.setText(_translate("MainWindow", "atualizar"))
        self.botao_db_deleta_psp.setText(_translate("MainWindow", "deletar"))
        self.ex3_ps1.setText(_translate("MainWindow", "- insira a content id, caso não tenha digite qualquer coisa jamais deixe o campo vazio."))
        self.ex1_ps1.setText(_translate("MainWindow", "- insira o titulo do jogo de PlayStation PS1."))
        self.ex2_ps1.setText(_translate("MainWindow", "<html><head/><body><p>- insira a descrição, atenção: para pular linhas use a tag html.<br/></p></body></html>"))
        self.titulo_topo__ps1.setText(_translate("MainWindow", "CADASTRO PLAYSTATION PS1"))
        self.ex4_ps1.setText(_translate("MainWindow", "- insira o link do jogo que o link, em caso de uso dropbox troque o final dl=0 por dl=1."))
        self.ex5_ps1.setText(_translate("MainWindow", "- faça o upload da imagem, caso esteja editando copie e cole o nome da imagem cadastrada."))
        self.ex6_ps1.setText(_translate("MainWindow", "- para atualizar preencha os dados normalmente, clique sobre o jogo na tabela  e em atualizar."))
        self.input_titulo_ps1.setText(_translate("MainWindow", "Titulo PS1"))
        self.input_descricao_ps1.setText(_translate("MainWindow", "Descrição | Usar tag <br> para pular linhas."))
        self.input_contentid_ps1.setText(_translate("MainWindow", "Content ID"))
        self.input_link_ps1.setText(_translate("MainWindow", "Link"))
        self.btn_upload_imagem_ps1.setText(_translate("MainWindow", "upload de imagem"))
        self.botao_db_adiciona_ps1.setText(_translate("MainWindow", "adicionar"))
        self.botao_db_atualiza_ps1.setText(_translate("MainWindow", "atualizar"))
        self.botao_db_deleta_ps1.setText(_translate("MainWindow", "deletar"))
        self.label_40.setText(_translate("MainWindow", "- insira a content id, caso não tenha digite qualquer coisa jamais deixe o campo vazio."))
        self.label_41.setText(_translate("MainWindow", "- insira o titulo do jogo de PlayStation PS2."))
        self.label_42.setText(_translate("MainWindow", "<html><head/><body><p>- insira a descrição, atenção: para pular linhas use a tag html.<br/></p></body></html>"))
        self.label_43.setText(_translate("MainWindow", "CADASTRO PLAYSTATION PS2"))
        self.label_44.setText(_translate("MainWindow", "- insira o link do jogo que o link, em caso de uso dropbox troque o final dl=0 por dl=1."))
        self.label_45.setText(_translate("MainWindow", "- faça o upload da imagem, caso esteja editando copie e cole o nome da imagem cadastrada."))
        self.label_46.setText(_translate("MainWindow", "- para atualizar preencha os dados normalmente, clique sobre o jogo na tabela  e em atualizar."))
        self.input_titulo_ps2.setText(_translate("MainWindow", "Titulo PS2"))
        self.input_descricao_ps2.setText(_translate("MainWindow", "Descrição | Usar tag <br> para pular linhas."))
        self.input_contentid_ps2.setText(_translate("MainWindow", "Content ID"))
        self.input_link_ps2.setText(_translate("MainWindow", "Link"))
        self.btn_upload_imagem_ps2.setText(_translate("MainWindow", "upload de imagem"))
        self.botao_db_adiciona_ps2.setText(_translate("MainWindow", "adicionar"))
        self.botao_db_atualiza_ps2.setText(_translate("MainWindow", "atualizar"))
        self.botao_db_deleta_ps2.setText(_translate("MainWindow", "deletar"))
        self.ex3_ps3.setText(_translate("MainWindow", "- insira a content id, caso não tenha digite qualquer coisa jamais deixe o campo vazio."))
        self.ex1_ps3.setText(_translate("MainWindow", "- insira o titulo do jogo de PlayStation PS3."))
        self.ex2_ps3.setText(_translate("MainWindow", "<html><head/><body><p>- insira a descrição, atenção: para pular linhas use a tag html.<br/></p></body></html>"))
        self.titulo_topo_ps3.setText(_translate("MainWindow", "CADASTRO PLAYSTATION PS3"))
        self.ex4_ps3.setText(_translate("MainWindow", "- insira o link do jogo que o link, em caso de uso dropbox troque o final dl=0 por dl=1."))
        self.ex5_ps3.setText(_translate("MainWindow", "- faça o upload da imagem, caso esteja editando copie e cole o nome da imagem cadastrada."))
        self.ex6_ps3.setText(_translate("MainWindow", "- para atualizar preencha os dados normalmente, clique sobre o jogo na tabela  e em atualizar."))
        self.ex7_ps3.setText(_translate("MainWindow", "- somente remova os --- ( 3 traços) se for utilizar o link, caso contrário deixe exatamente como está."))
        self.input_titulo_ps3.setText(_translate("MainWindow", "Titulo PS3"))
        self.input_descricao_ps3.setText(_translate("MainWindow", "Descrição | Usar tag <br> para pular linhas."))
        self.input_content_id_ps3.setText(_translate("MainWindow", "Content ID"))
        self.btn_upload_imagem_ps3.setText(_translate("MainWindow", "upload de imagem"))
        self.info_link1.setText(_translate("MainWindow", "link 1"))
        self.info_link2.setText(_translate("MainWindow", "link 2"))
        self.info_link3.setText(_translate("MainWindow", "link 3"))
        self.info_link4.setText(_translate("MainWindow", "link 4"))
        self.info_link5.setText(_translate("MainWindow", "link 5"))
        self.input_link1_ps3.setText(_translate("MainWindow", "---"))
        self.input_link2_ps3.setText(_translate("MainWindow", "---"))
        self.input_link3_ps3.setText(_translate("MainWindow", "---"))
        self.input_link4_ps3.setText(_translate("MainWindow", "---"))
        self.input_link5_ps3.setText(_translate("MainWindow", "---"))
        self.tabWidget_ps3.setTabText(self.tabWidget_ps3.indexOf(self.tabela_links_1a5), _translate("MainWindow", "links1 à 5"))
        self.info_link6.setText(_translate("MainWindow", "link 6"))
        self.info_link7.setText(_translate("MainWindow", "link 7"))
        self.info_link8.setText(_translate("MainWindow", "link 8"))
        self.info_link9.setText(_translate("MainWindow", "link 9"))
        self.info_link10.setText(_translate("MainWindow", "link 10"))
        self.input_link6_ps3.setText(_translate("MainWindow", "---"))
        self.input_link7_ps3.setText(_translate("MainWindow", "---"))
        self.input_link8_ps3.setText(_translate("MainWindow", "---"))
        self.input_link9_ps3.setText(_translate("MainWindow", "---"))
        self.input_link10_ps3.setText(_translate("MainWindow", "---"))
        self.tabWidget_ps3.setTabText(self.tabWidget_ps3.indexOf(self.tabela_links_6a10), _translate("MainWindow", "links 6 à 10"))
        self.info_link11.setText(_translate("MainWindow", "link 11"))
        self.info_link12.setText(_translate("MainWindow", "link 12"))
        self.info_link13.setText(_translate("MainWindow", "link 13"))
        self.info_link14.setText(_translate("MainWindow", "link 14"))
        self.info_link15.setText(_translate("MainWindow", "link 15"))
        self.input_link11_ps3.setText(_translate("MainWindow", "---"))
        self.input_link12_ps3.setText(_translate("MainWindow", "---"))
        self.input_link13_ps3.setText(_translate("MainWindow", "---"))
        self.input_link14_ps3.setText(_translate("MainWindow", "---"))
        self.input_link15_ps3.setText(_translate("MainWindow", "---"))
        self.tabWidget_ps3.setTabText(self.tabWidget_ps3.indexOf(self.tabela_links_11a15), _translate("MainWindow", "links 11 à 15"))
        self.info_link16.setText(_translate("MainWindow", "link 16"))
        self.info_link17.setText(_translate("MainWindow", "link 17"))
        self.info_link18.setText(_translate("MainWindow", "link 18"))
        self.info_link19.setText(_translate("MainWindow", "link 19"))
        self.info_link20.setText(_translate("MainWindow", "link 20"))
        self.input_link16_ps3.setText(_translate("MainWindow", "---"))
        self.input_link17_ps3.setText(_translate("MainWindow", "---"))
        self.input_link18_ps3.setText(_translate("MainWindow", "---"))
        self.input_link19_ps3.setText(_translate("MainWindow", "---"))
        self.input_link20_ps3.setText(_translate("MainWindow", "---"))
        self.tabWidget_ps3.setTabText(self.tabWidget_ps3.indexOf(self.tabela_links_16a20), _translate("MainWindow", "links 16 à 20"))
        self.info_link21.setText(_translate("MainWindow", "link 21"))
        self.info_link22.setText(_translate("MainWindow", "link 22"))
        self.info_link23.setText(_translate("MainWindow", "link 23"))
        self.info_link24.setText(_translate("MainWindow", "link 24"))
        self.info_link25.setText(_translate("MainWindow", "link 25"))
        self.input_link21_ps3.setText(_translate("MainWindow", "---"))
        self.input_link22_ps3.setText(_translate("MainWindow", "---"))
        self.input_link23_ps3.setText(_translate("MainWindow", "---"))
        self.input_link24_ps3.setText(_translate("MainWindow", "---"))
        self.input_link25_ps3.setText(_translate("MainWindow", "---"))
        self.tabWidget_ps3.setTabText(self.tabWidget_ps3.indexOf(self.tabela_links_21a25), _translate("MainWindow", "links 21 à 25"))
        self.info_link26.setText(_translate("MainWindow", "link 26"))
        self.info_link27.setText(_translate("MainWindow", "link 27"))
        self.info_link28.setText(_translate("MainWindow", "link 28"))
        self.info_link29.setText(_translate("MainWindow", "link 29"))
        self.info_link30.setText(_translate("MainWindow", "link 30"))
        self.input_link26_ps3.setText(_translate("MainWindow", "---"))
        self.input_link27_ps3.setText(_translate("MainWindow", "---"))
        self.input_link28_ps3.setText(_translate("MainWindow", "---"))
        self.input_link29_ps3.setText(_translate("MainWindow", "---"))
        self.input_link30_ps3.setText(_translate("MainWindow", "---"))
        self.tabWidget_ps3.setTabText(self.tabWidget_ps3.indexOf(self.tabela_links_26a30), _translate("MainWindow", "links 26 à 30"))
        self.tabWidget_ps3.setTabText(self.tabWidget_ps3.indexOf(self.frame_tabela_database_ps3), _translate("MainWindow", "conferir | editar | deletar"))
        self.botao_db_adiciona_ps3.setText(_translate("MainWindow", "adicionar"))
        self.botao_db_atualiza_ps3.setText(_translate("MainWindow", "atualizar"))
        self.botao_db_deleta_ps3.setText(_translate("MainWindow", "deletar"))
        self.ex3_retro.setText(_translate("MainWindow", "- insira a content id, caso não tenha digite qualquer coisa jamais deixe o campo vazio."))
        self.ex1_retro.setText(_translate("MainWindow", "- insira o titulo do jogo de PlayStation RETRO."))
        self.ex2_retro.setText(_translate("MainWindow", "<html><head/><body><p>- insira a descrição, atenção: para pular linhas use a tag html.<br/></p></body></html>"))
        self.titulo_topo_retro.setText(_translate("MainWindow", "CADASTRO PLAYSTATION RETROS"))
        self.ex4_retro.setText(_translate("MainWindow", "- insira o link do jogo que o link, em caso de uso dropbox troque o final dl=0 por dl=1."))
        self.ex5_retro.setText(_translate("MainWindow", "- faça o upload da imagem, caso esteja editando copie e cole o nome da imagem cadastrada."))
        self.ex6_retro.setText(_translate("MainWindow", "- para atualizar preencha os dados normalmente, clique sobre o jogo na tabela  e em atualizar."))
        self.input_titulo_retro.setText(_translate("MainWindow", "Titulo RETRO"))
        self.input_descricao_retro.setText(_translate("MainWindow", "Descrição | Usar tag <br> para pular linhas."))
        self.input_contentid_retro.setText(_translate("MainWindow", "Content ID"))
        self.input_link_retro.setText(_translate("MainWindow", "Link"))
        self.btn_upload_imagem_retro.setText(_translate("MainWindow", "upload de imagem"))
        self.botao_db_adiciona_retro.setText(_translate("MainWindow", "adicionar"))
        self.botao_db_atualiza_retro.setText(_translate("MainWindow", "atualizar"))
        self.botao_db_deleta_retro.setText(_translate("MainWindow", "deletar"))
        self.ex3_extras.setText(_translate("MainWindow", "- insira a content id, caso não tenha digite qualquer coisa jamais deixe o campo vazio."))
        self.ex1_extras.setText(_translate("MainWindow", "- insira o titulo do jogo de PlayStation EXTRAS."))
        self.ex2_extras.setText(_translate("MainWindow", "<html><head/><body><p>- insira a descrição, atenção: para pular linhas use a tag html.<br/></p></body></html>"))
        self.titulo_topo_extras.setText(_translate("MainWindow", "CADASTRO PLAYSTATION EXTRAS"))
        self.ex4_extras.setText(_translate("MainWindow", "- insira o link do jogo que o link, em caso de uso dropbox troque o final dl=0 por dl=1."))
        self.ex5_extras.setText(_translate("MainWindow", "- faça o upload da imagem, caso esteja editando copie e cole o nome da imagem cadastrada."))
        self.ex6_extras.setText(_translate("MainWindow", "- para atualizar preencha os dados normalmente, clique sobre o jogo na tabela  e em atualizar."))
        self.input_titulo_extras.setText(_translate("MainWindow", "Titulo PSP"))
        self.input_descricao_extras.setText(_translate("MainWindow", "Descrição | Usar tag <br> para pular linhas."))
        self.input_contentid_extras.setText(_translate("MainWindow", "Content ID"))
        self.input_link_extras.setText(_translate("MainWindow", "Link"))
        self.btn_upload_imagem_extras.setText(_translate("MainWindow", "upload de imagem"))
        self.botao_db_adiciona_extras.setText(_translate("MainWindow", "adicionar"))
        self.botao_db_atualiza_extras.setText(_translate("MainWindow", "atualizar"))
        self.botao_db_deleta_extras.setText(_translate("MainWindow", "deletar"))
        self.ex3_backup.setText(_translate("MainWindow", "- guarde este backup caso preciso, ele precisa de conversão para ser reupado."))
        self.ex2_backup.setText(_translate("MainWindow", "- backup salvo no formato SqLite3 para usar no servidor o formato é Mysql."))
        self.titulo_backup.setText(_translate("MainWindow", "BACKUP DA DATABASE TCXS PROJECT STORE"))
        self.ex1_backup.setText(_translate("MainWindow", "- clique em iniciar e o backup será feito."))
        self.btn_iniciar_backup.setText(_translate("MainWindow", "iniciar"))
        self.t_backup.setText(_translate("MainWindow", "backup usuários"))
        self.explica1cadastro_users_4.setText(_translate("MainWindow", "backup playstation psp"))
        self.explica1cadastro_users_6.setText(_translate("MainWindow", "backup playstation ps2"))
        self.explica1cadastro_users_7.setText(_translate("MainWindow", "backup playstation emuladores"))
        self.t_backup_2.setText(_translate("MainWindow", "backup informações"))
        self.explica1cadastro_users_5.setText(_translate("MainWindow", "backup playstation ps1"))
        self.explica1cadastro_users_8.setText(_translate("MainWindow", "backup playstation ps3"))
        self.explica1cadastro_users_9.setText(_translate("MainWindow", "backup playstation extras"))
        self.ex1_databases.setText(_translate("MainWindow", "- basta selecionar uma das tabelas para ver seus dados."))
        self.ex2_databases.setText(_translate("MainWindow", "<html><head/><body><p>- <span style=\" font-weight:600;\">[ATENÇÃO]</span> não edite nada por aqui!</p></body></html>"))
        self.titulo_topo_databases.setText(_translate("MainWindow", "VERIFICADOR DO BANCO DE DADOS "))
        self.comboBox_databases.setItemText(0, _translate("MainWindow", "selecione"))
        self.comboBox_databases.setItemText(1, _translate("MainWindow", "playstation_users"))
        self.comboBox_databases.setItemText(2, _translate("MainWindow", "playstation_infos"))
        self.comboBox_databases.setItemText(3, _translate("MainWindow", "playstation_psp"))
        self.comboBox_databases.setItemText(4, _translate("MainWindow", "playstation_ps1"))
        self.comboBox_databases.setItemText(5, _translate("MainWindow", "playstation_ps2"))
        self.comboBox_databases.setItemText(6, _translate("MainWindow", "playstation_ps3"))
        self.comboBox_databases.setItemText(7, _translate("MainWindow", "playstation_emuladores"))
        self.comboBox_databases.setItemText(8, _translate("MainWindow", "playstation_extras"))
        self.ex1_verifica_404.setText(_translate("MainWindow", "- basta selecionar uma das tabelas para fazer uma análise."))
        self.ex2_verifica_404.setText(_translate("MainWindow", "<html><head/><body><p>- <span style=\" font-weight:600;\">[ATENÇÃO]</span> este processo demora pois verifica link por link o visitando.</p></body></html>"))
        self.titulo_topo_verifica_404.setText(_translate("MainWindow", "VERIFICADOR LINK QUEBRADOS | 404 ERROR"))
        self.comboBox_verifica404.setItemText(0, _translate("MainWindow", "Selecione"))
        self.comboBox_verifica404.setItemText(1, _translate("MainWindow", "playstation_psp"))
        self.comboBox_verifica404.setItemText(2, _translate("MainWindow", "playstation_ps1"))
        self.comboBox_verifica404.setItemText(3, _translate("MainWindow", "playstation_ps2"))
        self.comboBox_verifica404.setItemText(4, _translate("MainWindow", "playstation_ps3"))
        self.comboBox_verifica404.setItemText(5, _translate("MainWindow", "playstation_emuladores"))
        self.comboBox_verifica404.setItemText(6, _translate("MainWindow", "playstation_extras"))
        self.textBrowser_verifica404.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.rodape_desenvolvedor.setText(_translate("MainWindow", "TCXS Project | 2020"))
        self.rodape_versao.setText(_translate("MainWindow", "v1.0  "))


import files_rc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
