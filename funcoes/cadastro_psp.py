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
from PIL import Image
import ftplib
import os
from datetime import datetime


def funcoesCadastroPsp(self):
    # eventos para limpar os campos, que buscam funçoes no arquivo main
    self.ui.input_titulo_jogo_psp.mousePressEvent = self.limpaInputTitulopsp
    self.ui.input_descricao_jogo_psp.mousePressEvent = self.limpaInputDescricaopsp
    self.ui.input_contentid_psp.mousePressEvent = self.limpaInputContentidpsp
    self.ui.input_link_jogo_psp.mousePressEvent = self.limpaInputLinkpsp
    # botoes das açoes
    self.ui.botao_db_adiciona_psp.clicked.connect(lambda: addToDbpsp(self))
    self.ui.botao_db_atualiza_psp.clicked.connect(lambda: updaterowpsp(self))
    self.ui.botao_db_deleta_psp.clicked.connect(lambda: delrowpsp(self))
    #btn upload imagem_psp
    self.ui.btn_upload_imagem_psp.clicked.connect(lambda: selecionarImagempsp(self))




def selecionarImagempsp(self):
    self.imagem_recebida = []
    try:
        janela2 = QWidget()
        janela2.resize(800, 600)
        janela2.move(100, 200)
        janela2.setWindowTitle('TCXS Project | Imagem PSP')
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(janela2, "TCXS STORE | PSP | Escolha sua imagem", "", "JPG (*.jpg);;PNG (*.png)", options=options)
        if fileName:
            #faz uma verificaçao na imagem para limpar a lista acima
            if fileName in self.imagem_recebida:
                self.imagem_recebida.clear()
            else:
                self.imagem_recebida.clear()
                self.imagem_recebida.append(fileName)
        # carrega na variavel do Image do pilow (PIL) a imagem aberta
        imagem_recebida = Image.open(self.imagem_recebida[0])
        # salva a imagem usando a extensao que quisermos
        #imagem_recebida = imagem_recebida.save("images/file.jpg")
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
        self.nome_imagem = fileName.split('/')[-1]
        # salva a imagem
        imagem_final.save(f'images/{self.nome_imagem}')
        # exibe a imagem
        # imagem_final.show()
        self.ui.imagem_psp.setPixmap(QtGui.QPixmap(f'images/{self.nome_imagem}').scaled(250, 250, QtCore.Qt.KeepAspectRatio))
        #CONEXAO COM FTP PARA UPLOAD DA imagem
        # arquivo para ser enviado ao server
        file = open(f'images/{self.nome_imagem}', 'rb')  # file to send
        conexao.ftp.storbinary(f'STOR assets/images/psp/{self.nome_imagem}', file)  # send the file
        file.close()  # close file and FTP and remove image
        conexao.ftp.quit()
        os.remove(f'images/{self.nome_imagem}')
    except:
        pass



def bancoDadospsp(self):
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
    self.model_psp.setHeaderData(4, QtCore.Qt.Horizontal, "Imagem")
    self.model_psp.setHeaderData(5, QtCore.Qt.Horizontal, "Cadastro")
    self.model_psp.setHeaderData(6, QtCore.Qt.Horizontal, "Link")
    # tabela de dados
    self.ui.tabela_dados_db_psp.setModel(self.model_psp)
    self.i_psp = self.model_psp.rowCount()


#ADICIONA CHAVES
def addToDbpsp(self):
    #chama a função de conexao e popula a tabela | verificar com  print(self.i)
    bancoDadospsp(self)

    if  self.ui.input_titulo_jogo_psp.text() == 'Titutlo PSP' or self.ui.input_descricao_jogo_psp.text() == 'Descrição | Usar tag <br> para pular linhas.' or self.ui.input_contentid_psp.text() == 'Content ID' or self.ui.input_link_jogo_psp.text() == 'Link':
        QMessageBox.question(self, 'Tutorial Adicionar Jogo PSP', """Para Adicionar Jogo de PlayStation PSP:
        Sempre adicione os dados em todos os campos e insira uma imagem depois clique em adicionar.
        Para Editar Jogo de  PlayStation PSP:
        Para editar, preencha todos os campos, envie uma imagem e clique na linha que quer atualizar e no botao atualizar.
        Para Deletar Jogo de PlayStation PSP:
        Caso queira deletar, clique na linha que quer deletar e no botão deletar!""", QMessageBox.Ok)
        self.show()
    else:

        try:
            self.nome_imagem = self.nome_imagem
            if self.nome_imagem:
                # hora e data para ser insidas no servidor
                self.hoje = datetime.now()
                self.data_formatada = self.hoje.strftime('%Y-%m-%d %H:%M:%S')
                # insere os dados na database
                self.model_psp.insertRows(self.i_psp, 1)
                self.model_psp.setData(self.model_psp.index(self.i_psp, 1), self.ui.input_titulo_jogo_psp.text())     # TITULO
                self.model_psp.setData(self.model_psp.index(self.i_psp, 2), self.ui.input_descricao_jogo_psp.text())  # DESCRIÇÃO
                self.model_psp.setData(self.model_psp.index(self.i_psp, 3), self.ui.input_contentid_psp.text())       # CONTENT_ID
                self.model_psp.setData(self.model_psp.index(self.i_psp, 4), self.nome_imagem)                         # IMAGEM
                self.model_psp.setData(self.model_psp.index(self.i_psp, 5), self.data_formatada)                      # CADASTRO
                self.model_psp.setData(self.model_psp.index(self.i_psp, 6), self.ui.input_link_jogo_psp.text())       # LINK
                self.model_psp.submitAll()
                self.i_psp += 1
        except AttributeError:
            QMessageBox.question(self, 'TCXS Project | AVISO!', """Faça o envio da imagem antes de adicionar!""", QMessageBox.Ok)
            self.show()
            pass

#ATUALIZA AS CHAVES
def updaterowpsp(self):
    if self.ui.tabela_dados_db_psp.currentIndex().row() > -1:
        # hora e data para ser insidas no servidor
        self.hoje = datetime.now()
        self.data_formatada = self.hoje.strftime('%Y-%m-%d %H:%M:%S')
        #atualiza os dados baseado no nome das row's
        record = self.model_psp.record(self.ui.tabela_dados_db_psp.currentIndex().row())
        record.setValue("titulo", self.ui.input_titulo_jogo_psp.text())       #TITULO
        record.setValue("descricao", self.ui.input_descricao_jogo_psp.text()) #DESCRIÇÃO
        record.setValue("content_id", self.ui.input_contentid_psp.text())     # CONTENT_ID
        record.setValue("imagem", self.nome_imagem)                           # IMAGEM
        record.setValue("cadastro", self.data_formatada)                      # CADASTRO
        record.setValue("link", self.ui.input_descricao_jogo_psp.text())      # LINK
        self.model_psp.setRecord(self.ui.tabela_dados_db_psp.currentIndex().row(), record)
    else:
        QMessageBox.question(self, 'TCXS Project | Atualizar PSP', "Selecione uma linha para atualizar, clique sobre o numero a esquerda na tabela correspondente a linha.", QMessageBox.Ok)
        self.show()



#DELETA AS CHAVES
def delrowpsp(self):
    if self.ui.tabela_dados_db_psp.currentIndex().row() > -1:
        self.model_psp.removeRow(self.ui.tabela_dados_db_psp.currentIndex().row())
        self.i_psp -= 1
        self.model_psp.select()
    else:
        QMessageBox.question(self, 'TCXS Project | Deletar PSP',"Selecione uma linha para deletar, clique sobre o numero a esquerda na tabela correspondente a linha.", QMessageBox.Ok)
        self.show()
