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
from PyQt5.QtWidgets import  QMessageBox
from PIL import Image
import ftplib
import os
from datetime import datetime


def funcoesCadastroPsp(self):
    # eventos para limpar os campos, que buscam funçoes no arquivo main
    self.ui.input_titulo_jogo_psp.mousePressEvent = self.limpaInputTituloPSp
    self.ui.input_descricao_jogo_psp.mousePressEvent = self.limpaInputDescricaoPSp
    self.ui.input_contentid_psp.mousePressEvent = self.limpaInputContentidPSp
    self.ui.input_link_jogo_psp.mousePressEvent = self.limpaInputLinkPSp
    # botoes das açoes
    self.ui.botao_db_adiciona_psp.clicked.connect(lambda: addToDbPSp(self))
    self.ui.botao_db_atualiza_psp.clicked.connect(lambda: updaterowPSp(self))
    self.ui.botao_db_deleta_psp.clicked.connect(lambda: delrowPSp(self))
    #btn upload imagem_psp
    self.ui.btn_upload_imagem_psp.clicked.connect(lambda: selecionarImagemPSp(self))




def selecionarImagemPSp(self):
    self.imagem_recebida = []
    try:
        janela2 = QWidget()
        janela2.resize(800, 600)
        janela2.move(100, 200)
        janela2.setWindowTitle('TCXS Project | Imagem PSP')
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(janela2, "TCXS STORE | PSP | Escolha sua imagem", "", "All Files (*);;JPG (*.jpg);;PNG (*.png)", options=options)
        if fileName:
            #self.ui.imagem_normal_deepnude.setPixmap(QtGui.QPixmap(fileName).scaled(800, 450, QtCore.Qt.KeepAspectRatio))  # aumentar imagem com qtcore .scaled(200,200, QtCore.Qt.KeepAspectRatio)
            #self.ui.imagem_renderizada_deepnude.setPixmap(QtGui.QPixmap('images/processando.png').scaled(300, 450, QtCore.Qt.KeepAspectRatio))  # aumentar imagem com qtcore .scaled(200,200, QtCore.Qt.KeepAspectRatio)
            if fileName in self.imagem_recebida:
                # print(fileName)
                # print(self.imagem_recebida)
                self.imagem_recebida.clear()
            else:
                # print(self.imagem_recebida)
                self.imagem_recebida.clear()
                self.imagem_recebida.append(fileName)
        # carrega na variavel do Image do pilow (PIL) a imagem aberta
        imagem_recebida = Image.open(self.imagem_recebida[0])
        # salva a imagem usando a extensao que quisermos
        #imagem_recebida = imagem_recebida.save("images/file.jpg")
        #fim da função de envio de imagem para o programa....

        #TRATAMENTO DA IMAGEM RECEBIDA PONDO MARCA DAGUA E REDIMENSIONANDO
        # imagem de entrada e marca dagua
        #imagem_entrada = Image.open(imagem_recebida)
        watermark = Image.open('images/watermark.png')
        # redimensiona imagem de entrada para 250px
        imagem_entrada = imagem_recebida.resize((250, 250), Image.ANTIALIAS)
        # pega as medidas da imagem de entrada
        width, height = imagem_entrada.size
        # cria uma imagem temporaria na memoria |  para transparent usar "RGBA" e (0,0,0,0)
        imagem_final = Image.new('RGB', (width, height), (0, 0, 0))
        # mescla as imagens de entrada e marca dagua na imagem da memoria
        imagem_final.paste(imagem_entrada, (0, 0))
        imagem_final.paste(watermark, (0, 0), mask=watermark)
        nome_imagem = fileName.split('/')[-1]
        print(nome_imagem)
        # exibe a imagem
        #self.ui.imagem_psp.setPixmap(QtGui.QPixmap(f'images/{nome_imagem}').scaled(250, 250, QtCore.Qt.KeepAspectRatio))
        #imagem_final.show()
        # salva a imagem
        imagem_final.save(f'images/{nome_imagem}')

        #CONEXAO COM FTP PARA UPLOAD DA imagem
        # conecta ao ftp | força UTF-8 encoding
        ftp = ftplib.FTP(host="192.168.0.3", user="gorpo", passwd="")
        ftp.encoding = "utf-8"
        # arquivo para ser enviado ao server
        file = open(f'images/{nome_imagem}', 'rb')  # file to send
        ftp.storbinary(f'STOR assets/images/psp/{nome_imagem}', file)  # send the file
        file.close()  # close file and FTP and remove image
        ftp.quit()
        os.remove(f'images/{nome_imagem}')
    except:
        pass





def bancoDadosPSp(self):
    # usa o arquivo de conexao
    self.query_psp = QSqlQuery(conexao.db_mysql)
    self.model_psp = QtSql.QSqlTableModel()
    self.model_psp.setTable('playstation_psp')
    self.model_psp.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
    self.model_psp.select()
    # popula as tabelas
    self.model_psp.setHeaderData(0, QtCore.Qt.Horizontal, "Id")
    self.model_psp.setHeaderData(1, QtCore.Qt.Horizontal, "Titulo")
    self.model_psp.setHeaderData(2, QtCore.Qt.Horizontal, "Descrição")
    self.model_psp.setHeaderData(3, QtCore.Qt.Horizontal, "ContentID")
    self.model_psp.setHeaderData(4, QtCore.Qt.Horizontal, "Titulo")
    self.model_psp.setHeaderData(5, QtCore.Qt.Horizontal, "Imagem")
    self.model_psp.setHeaderData(6, QtCore.Qt.Horizontal, "Cadastro")
    self.model_psp.setHeaderData(7, QtCore.Qt.Horizontal, "Link")
    # tabela de dados
    self.ui.tabela_dados_db_psp.setModel(self.model_psp)
    self.i_psp = self.model_psp.rowCount()



def addToDbPSp(self):
    print(self.imagem_recebida)
    #chama a função de conexao e popula a tabela
    bancoDadosPSp(self)
    # print(self.i)
    #hora e data para ser insidas no servidor
    self.hoje = datetime.now()
    self.data_formatada = self.hoje_user.strftime('%Y-%m-%d %H:%M:%S')
    # insere os dados na database
    self.model_psp.insertRows(self.i_psp, 1)
    self.model_psp.setData(self.model_psp.index(self.i_psp, 1), self.ui.input_titulo_jogo_psp.text())    #TITULO
    self.model_psp.setData(self.model_psp.index(self.i_psp, 2), self.ui.input_descricao_jogo_psp.text())          #DESCRIÇÃO
    self.model_psp.setData(self.model_psp.index(self.i_psp, 3), self.ui.input_contentid_psp.text())           #CONTENT_ID
    self.model_psp.setData(self.model_psp.index(self.i_psp, 4), self.data_formatada_psp)                #IMAGEM
    self.model_psp.setData(self.model_psp.index(self.i_psp, 3), self.data_formatada)          #CADASTRO
    self.model_psp.setData(self.model_psp.index(self.i_psp, 3), self.ui.input_link_jogo_psp.text())   #LINK
    self.model_psp.submitAll()
    self.i_psp += 1




def updaterowPSp(self):
    if self.ui.tabela_dados_db_psp.currentIndex().row() > -1:
        record = self.model_psp.record(self.ui.tabela_dados_db_psp.currentIndex().row())
        record.setValue("informacao", self.ui.input_playstation_psp.text())
        self.model_psp.setRecord(self.ui.tabela_dados_db_psp.currentIndex().row(), record)
    else:
        QMessageBox.question(self, 'Mensagem',
                             "Selecione uma linha para atualizar, clique sobre o numero a esquerda na tabela correspondente a linha.",
                             QMessageBox.Ok)
        self.show()




def delrowPSp(self):
    if self.ui.tabela_dados_db_psp.currentIndex().row() > -1:
        self.model_psp.removeRow(self.ui.tabela_dados_db_psp.currentIndex().row())
        self.i_psp -= 1
        self.model_psp.select()
    else:
        QMessageBox.question(self, 'Mensagem',
                             "Selecione uma linha para deletar, clique sobre o numero a esquerda na tabela correspondente a linha.",
                             QMessageBox.Ok)
        self.show()
