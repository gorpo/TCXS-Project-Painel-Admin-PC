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


#funcoes principais-------------->
def menusJanela(self):
    funcoesJanela(self)
    menuEsquerda(self)

#funçoes extras ------------------>
def funcoesJanela(self):
    # sistema de redimensionamento da tela---------------->
    self.ui.botao_fechar.clicked.connect(lambda: sys.exit())
    self.ui.botao_maximizar.clicked.connect(lambda: maximizarPrograma(self))
    self.ui.botao_minimizar.clicked.connect(lambda: self.showMinimized())
    self.sizegrip = QSizeGrip(self.ui.redimensionador)
    self.sizegrip.setStyleSheet("width: 17px; height: 17px; margin 0px; padding: 0px;")
    self.sizegrip.setVisible(True)
def maximizarPrograma(self):
    self.ui.botao_maximizar.setStyleSheet("QPushButton {\n"
                                       "    \n"
                                       "    background-image: url('images/volta_full_screen.png');\n"
                                       "    background-color: transparent;\n"
                                       "    background-repeat: no-repeat;\n"
                                       "    background-position: center;\n"
                                       "    border: none;\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: rgb(30,144,255);\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: rgb(1,84,149);\n"
                                       "}")
    self.showMaximized()
    self.ui.botao_maximizar.clicked.connect(lambda: janela_normal(self))
def janela_normal(self):
    self.ui.botao_maximizar.setStyleSheet("QPushButton {\n"
                                       "    \n"
                                       "    background-image: url(:/maximizar/images/icons8-toggle-full-screen-24.png);\n"
                                       "    background-repeat: no-repeat;\n"
                                       "    background-position: center;\n"
                                       "    border: none;\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: rgb(30,144,255);\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: rgb(1,84,149);\n"
                                       "}")
    self.showNormal()
    self.ui.botao_maximizar.clicked.connect(lambda: maximizarPrograma(self))

#abre/fecha menu esquerda--------->
def menuEsquerda(self):
    self.ui.botao_abrir_menu.clicked.connect(lambda: abreMenu(self))
    self.ui.botao_abrir_menu.setToolTip('Clique para expandir\nClique para fechar')
    # botao homepage------------------------------------------>
    self.ui.botao_home.clicked.connect(lambda: paginaHome(self))
    self.ui.botao_home.setToolTip('Inicio | MYSQL FTP')
    # botao botao_cadastro_user---------------------------------------->
    self.ui.botao_cadastro_user.clicked.connect(lambda: paginaCadastroUser(self)  )
    self.ui.botao_cadastro_user.setToolTip('Cadastrar usuários | TCXS Store')
    #botao botao_verifica_user
    self.ui.botao_verifica_user.clicked.connect(lambda: paginaVerficaUser(self))
    self.ui.botao_verifica_user.setToolTip('Verificar acessos | TCXS Store')
    #botao botao_infos_store---------------------------------------------->
    self.ui.botao_infos_store.clicked.connect(lambda: paginaInfos(self))
    self.ui.botao_infos_store.setToolTip('PlayStation Homepage | TCXS Store')
    # botao botao_menu_psp------------------------------->
    self.ui.botao_menu_psp.clicked.connect(lambda: paginaPsp(self))
    self.ui.botao_menu_psp.setToolTip('PlayStation PSP | TCXS Store')
    # botao botao_menu_ps1----------------------->
    self.ui.botao_menu_ps1.clicked.connect(lambda: paginaPs1(self))
    self.ui.botao_menu_ps1.setToolTip('PlayStation PS1 | TCXS Store')
    #botao botao_menu_ps2---------------------------->
    self.ui.botao_menu_ps2.clicked.connect(lambda: paginaPs2(self))
    self.ui.botao_menu_ps2.setToolTip('PlayStation PS2 | TCXS Store')
    # botao botao_menu_ps3---------------------------->
    self.ui.botao_menu_ps3.clicked.connect(lambda: paginaPs3(self))
    self.ui.botao_menu_ps3.setToolTip('PlayStation PS3 | TCXS Store')
    # botao botao_menu_retro---------------------------->
    self.ui.botao_menu_retro.clicked.connect(lambda: paginaRetro(self))
    self.ui.botao_menu_retro.setToolTip('PlayStation RETRO | TCXS Store')
    # botao botao_menu_extras---------------------------->
    self.ui.botao_menu_extras.clicked.connect(lambda: paginaExtras(self))
    self.ui.botao_menu_extras.setToolTip('PlayStation EXTRAS | TCXS Store')
    # botao botao_menu_bottelegram---------------------------->
    self.ui.botao_menu_bottelegram.clicked.connect(lambda: paginaBot(self))
    self.ui.botao_menu_bottelegram.setToolTip('Bot TELEGRAM | TCXS Store')
    # botao botao_menu_database---------------------------->
    self.ui.botao_menu_database.clicked.connect(lambda: paginaDatabase(self))
    self.ui.botao_menu_database.setToolTip('PlayStation DATABASE | TCXS Store')
    # botao botao_menu_404---------------------------->
    self.ui.botao_menu_404.clicked.connect(lambda: pagina404(self))
    self.ui.botao_menu_404.setToolTip('PlayStation 404 | TCXS Store')


def abreMenu(self):
    self.ui.menu_esquerda.setMinimumSize(QtCore.QSize(220, 0))
    self.ui.botao_abrir_menu.clicked.connect(lambda : fechaMenu(self))
def fechaMenu(self):
    self.ui.menu_esquerda.setMinimumSize(QtCore.QSize(50, 0))
    self.ui.botao_abrir_menu.clicked.connect(lambda : abreMenu(self))
#INDEXAÇÃO DAS PAGINAS------------->

#homepage ------------------------->
def paginaHome(self):
    self.ui.stackedWidget.setCurrentIndex(0)
#cadastro user--------------------------->
def paginaCadastroUser(self):
    self.ui.stackedWidget.setCurrentIndex(1)

#pagina python--------------------->
def paginaVerficaUser(self):
    self.ui.stackedWidget.setCurrentIndex(2)
#pagina infos------------------->
def paginaInfos(self):
    self.ui.stackedWidget.setCurrentIndex(3)
#pagina psp------------------->
def paginaPsp(self):
    self.ui.stackedWidget.setCurrentIndex(4)
#pagina ps1------------------->
def paginaPs1(self):
    self.ui.stackedWidget.setCurrentIndex(5)
#pagina ps2------------------->
def paginaPs2(self):
    self.ui.stackedWidget.setCurrentIndex(6)
#pagina ps3------------------->
def paginaPs3(self):
    self.ui.stackedWidget.setCurrentIndex(7)
#pagina retro------------------->
def paginaRetro(self):
    self.ui.stackedWidget.setCurrentIndex(8)
#pagina Extras------------------->
def paginaExtras(self):
    self.ui.stackedWidget.setCurrentIndex(9)
#pagina bot------------------->
def paginaBot(self):
    self.ui.stackedWidget.setCurrentIndex(10)
# pagina database------------------->
def paginaDatabase(self):
    self.ui.stackedWidget.setCurrentIndex(11)
#pagina 404------------------->
def pagina404(self):
    self.ui.stackedWidget.setCurrentIndex(12)











