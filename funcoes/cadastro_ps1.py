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


def funcoesCadastroPS1(self):
    # eventos para limpar os campos, que buscam funçoes no arquivo main | informações com o mouse sobre o item
    self.ui.imagem_ps1.setToolTip('Clique no botão e envie uma imagem.\nFormatos aceitos apenas .jpg e .png\nFormatos como .jpeg ou outros não são aceitos.\nSua imagem será enviada automáticamente redimensionada\naplicada a borda e enviada por ftp.\nCaso ocorra algum erro confira os dados de ftp.')
    self.ui.input_titulo_ps1.mousePressEvent = self.limpaInputTitulops1
    self.ui.input_titulo_ps1.setToolTip('Insira o titulo do jogo de PlayStation PS1.')
    self.ui.input_descricao_ps1.mousePressEvent = self.limpaInputDescricaops1
    self.ui.input_descricao_ps1.setToolTip(
        'Insira a descrição do jogo de PlayStation PS1.\nUse a tag <br> para pular linhas.\nEXEMPLO:\nIdioma: Ingles<br>Legenda: Ingles<br>Plataforma: PlayStation PS1\n[ATENÇÃO] Mantenha este padrão pois ele é usado na loja!')
    self.ui.input_contentid_ps1.mousePressEvent = self.limpaInputContentidps1
    self.ui.input_contentid_ps1.setToolTip(
        'Insira a content id do jogo de PlayStation PS1.\nCaso não queira inserir ou não tenha a content id\napenas insira qualquer coisa para não ficar em branco!')
    self.ui.input_link_ps1.mousePressEvent = self.limpaInputLinkps1
    self.ui.input_link_ps1.setToolTip('Insira o link do jogo de PlayStation PS1.')
    # botoes das açoes
    self.ui.botao_db_adiciona_ps1.clicked.connect(lambda: addToDbps1(self))
    self.ui.botao_db_atualiza_ps1.clicked.connect(lambda: updaterowps1(self))
    self.ui.botao_db_deleta_ps1.clicked.connect(lambda: delrowps1(self))
    # btn upload imagem_ps1
    self.ui.btn_upload_imagem_ps1.clicked.connect(lambda: selecionarImagemps1(self))


def selecionarImagemps1(self):
    self.imagem_recebida_ps1 = []
    try:
        janela2 = QWidget()
        janela2.resize(800, 600)
        janela2.move(100, 200)
        janela2.setWindowTitle('TCXS Project | Imagem PS1')
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(janela2, "TCXS STORE | PS1 | Escolha sua imagem", "",
                                                  "JPG (*.jpg);;PNG (*.png)", options=options)
        if fileName:
            # faz uma verificaçao na imagem para limpar a lista acima
            if fileName in self.imagem_recebida_ps1:
                self.imagem_recebida_ps1.clear()
            else:
                self.imagem_recebida_ps1.clear()
                self.imagem_recebida_ps1.append(fileName)
        # carrega na variavel do Image do pilow (PIL) a imagem aberta
        imagem_recebida = Image.open(self.imagem_recebida_ps1[0])
        # salva a imagem usando a extensao que quisermos
        # imagem_recebida = imagem_recebida.save("images/file.jpg")
        # TRATAMENTO DA IMAGEM RECEBIDA PONDO MARCA DAGUA E REDIMENSIONANDO
        # imagem de entrada e marca dagua
        # imagem_entrada = Image.open(imagem_recebida)
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
        self.nome_imagem_ps1 = fileName.split('/')[-1]
        # salva a imagem
        imagem_final.save(f'images/{self.nome_imagem_ps1}')
        # exibe a imagem
        # imagem_final.show()
        self.ui.imagem_ps1.setPixmap(
            QtGui.QPixmap(f'images/{self.nome_imagem_ps1}').scaled(250, 250, QtCore.Qt.KeepAspectRatio))
        # CONEXAO COM FTP PARA UPLOAD DA imagem
        # arquivo para ser enviado ao server
        file = open(f'images/{self.nome_imagem_ps1}', 'rb')  # file to send
        conexao.ftp.storbinary(f'STOR assets/images/ps1/{self.nome_imagem_ps1}', file)  # send the file
        file.close()  # close file and FTP and remove image
        #conexao.ftp.quit()
        os.remove(f'images/{self.nome_imagem_ps1}')
    except:
        pass


def bancoDadosps1(self):
    # usa o arquivo de conexao
    self.query_ps1 = QSqlQuery(conexao.db_mysql)
    self.model_ps1 = QtSql.QSqlTableModel()
    self.model_ps1.setTable('playstation_ps1')
    self.model_ps1.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
    self.model_ps1.select()
    # popula as tabelas
    self.model_ps1.setHeaderData(0, QtCore.Qt.Horizontal, "Id")
    self.model_ps1.setHeaderData(1, QtCore.Qt.Horizontal, "Titulo")
    self.model_ps1.setHeaderData(2, QtCore.Qt.Horizontal, "Descrição")
    self.model_ps1.setHeaderData(3, QtCore.Qt.Horizontal, "ContentID")
    self.model_ps1.setHeaderData(4, QtCore.Qt.Horizontal, "Imagem")
    self.model_ps1.setHeaderData(5, QtCore.Qt.Horizontal, "Cadastro")
    self.model_ps1.setHeaderData(6, QtCore.Qt.Horizontal, "Link")
    # tabela de dados
    self.ui.tabela_dados_db_ps1.setModel(self.model_ps1)
    self.ui.tabela_dados_db_ps1.setToolTip(
        'Tabela da dados:\nPara adicionar itens sempre preencha todos os campos.\nCaso queira editar clique sobre o numero de uma linha e clique em atualizar.\nCaso queira deletar clique sobre o numero de uma linha e delete.')
    self.i_ps1 = self.model_ps1.rowCount()


# ADICIONA CHAVES
def addToDbps1(self):
    # chama a função de conexao e popula a tabela | verificar com  print(self.i)
    bancoDadosps1(self)

    if self.ui.input_titulo_ps1.text() == 'Titutlo PS1' or self.ui.input_descricao_ps1.text() == 'Descrição | Usar tag <br> para pular linhas.' or self.ui.input_contentid_ps1.text() == 'Content ID' or self.ui.input_link_ps1.text() == 'Link':
        QMessageBox.question(self, 'Tutorial Adicionar Jogo PS1', """Para Adicionar Jogo de PlayStation PS1:
Sempre adicione os dados em todos os campos e insira uma imagem depois clique em adicionar.
Para Editar Jogo de  PlayStation PS1:
Para editar, preencha todos os campos, envie uma imagem e clique na linha que quer atualizar e no botao atualizar.
Para Deletar Jogo de PlayStation PS1:
Caso queira deletar, clique na linha que quer deletar e no botão deletar!""", QMessageBox.Ok)
        self.show()
    else:

        try:
            self.nome_imagem_ps1 = self.nome_imagem_ps1
            if self.nome_imagem_ps1:
                # hora e data para ser insidas no servidor
                self.hoje = datetime.now()
                self.data_formatada = self.hoje.strftime('%Y-%m-%d %H:%M:%S')
                # insere os dados na database
                self.model_ps1.insertRows(self.i_ps1, 1)
                self.model_ps1.setData(self.model_ps1.index(self.i_ps1, 1),
                                       self.ui.input_titulo_ps1.text())  # TITULO
                self.model_ps1.setData(self.model_ps1.index(self.i_ps1, 2),
                                       self.ui.input_descricao_ps1.text())  # DESCRIÇÃO
                self.model_ps1.setData(self.model_ps1.index(self.i_ps1, 3),
                                       self.ui.input_contentid_ps1.text())  # CONTENT_ID
                self.model_ps1.setData(self.model_ps1.index(self.i_ps1, 4), self.nome_imagem_ps1)  # IMAGEM
                self.model_ps1.setData(self.model_ps1.index(self.i_ps1, 5), self.data_formatada)  # CADASTRO
                self.model_ps1.setData(self.model_ps1.index(self.i_ps1, 6), self.ui.input_link_ps1.text())  # LINK
                self.model_ps1.submitAll()
                self.i_ps1 += 1
                QMessageBox.question(self, 'TCXS Project | AVISO!', """Dados inseridos, confira na tabela!""", QMessageBox.Ok)
                self.show()
        except AttributeError:
            QMessageBox.question(self, 'TCXS Project | AVISO!', """Faça o envio da imagem antes de adicionar!""",
                                 QMessageBox.Ok)
            self.show()
            pass


# ATUALIZA AS CHAVES
def updaterowps1(self):
    if self.ui.tabela_dados_db_ps1.currentIndex().row() > -1:
        # hora e data para ser insidas no servidor
        self.hoje = datetime.now()
        self.data_formatada = self.hoje.strftime('%Y-%m-%d %H:%M:%S')
        # atualiza os dados baseado no nome das row's
        record = self.model_ps1.record(self.ui.tabela_dados_db_ps1.currentIndex().row())
        record.setValue("titulo", self.ui.input_titulo_ps1.text())  # TITULO
        record.setValue("descricao", self.ui.input_descricao_ps1.text())  # DESCRIÇÃO
        record.setValue("content_id", self.ui.input_contentid_ps1.text())  # CONTENT_ID
        record.setValue("imagem", self.nome_imagem_ps1)  # IMAGEM
        record.setValue("cadastro", self.data_formatada)  # CADASTRO
        record.setValue("link", self.ui.input_descricao_ps1.text())  # LINK
        self.model_ps1.setRecord(self.ui.tabela_dados_db_ps1.currentIndex().row(), record)
        QMessageBox.question(self, 'TCXS Project | AVISO!', """Dados atualizados, confira na tabela!""", QMessageBox.Ok)
        self.show()
    else:
        QMessageBox.question(self, 'TCXS Project | Atualizar PS1',
                             "Selecione uma linha para atualizar, clique sobre o numero a esquerda na tabela correspondente a linha.",
                             QMessageBox.Ok)
        self.show()


# DELETA AS CHAVES
def delrowps1(self):
    if self.ui.tabela_dados_db_ps1.currentIndex().row() > -1:
        self.model_ps1.removeRow(self.ui.tabela_dados_db_ps1.currentIndex().row())
        self.i_ps1 -= 1
        self.model_ps1.select()
        QMessageBox.question(self, 'TCXS Project | AVISO!', """Dados deletados, confira na tabela!""", QMessageBox.Ok)
        self.show()
    else:
        QMessageBox.question(self, 'TCXS Project | Deletar PS1',
                             "Selecione uma linha para deletar, clique sobre o numero a esquerda na tabela correspondente a linha.",
                             QMessageBox.Ok)
        self.show()
