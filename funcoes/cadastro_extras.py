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

def funcoesCadastroEXTRAS(self):
    # eventos para limpar os campos, que buscam funçoes no arquivo main | informações com o mouse sobre o item
    self.ui.imagem_extras.setToolTip('Clique no botão e envie uma imagem.\nFormatos aceitos apenas .jpg e .png\nFormatos como .jpeg ou outros não são aceitos.\nSua imagem será enviada automáticamente redimensionada\naplicada a borda e enviada por ftp.\nCaso ocorra algum erro confira os dados de ftp.')
    self.ui.input_titulo_extras.mousePressEvent = self.limpaInputTituloextras
    self.ui.input_titulo_extras.setToolTip('Insira o titulo do jogo de PlayStation EXTRAS.')
    self.ui.input_descricao_extras.mousePressEvent = self.limpaInputDescricaoextras
    self.ui.input_descricao_extras.setToolTip(
        'Insira a descrição do jogo de PlayStation EXTRAS.\nUse a tag <br> para pular linhas.\nEXEMPLO:\nIdioma: Ingles<br>Legenda: Ingles<br>Plataforma: PlayStation EXTRAS\n[ATENÇÃO] Mantenha este padrão pois ele é usado na loja!')
    self.ui.input_contentid_extras.mousePressEvent = self.limpaInputContentidextras
    self.ui.input_contentid_extras.setToolTip(
        'Insira a content id do jogo de PlayStation EXTRAS.\nCaso não queira inserir ou não tenha a content id\napenas insira qualquer coisa para não ficar em branco!')
    self.ui.input_link_extras.mousePressEvent = self.limpaInputLinkextras
    self.ui.input_link_extras.setToolTip('Insira o link do jogo de PlayStation EXTRAS.')
    # botoes das açoes
    self.ui.botao_db_adiciona_extras.clicked.connect(lambda: addToDbextras(self))
    self.ui.botao_db_atualiza_extras.clicked.connect(lambda: updaterowextras(self))
    self.ui.botao_db_deleta_extras.clicked.connect(lambda: delrowextras(self))
    # btn upload imagem_extras
    self.ui.btn_upload_imagem_extras.clicked.connect(lambda: selecionarImagemextras(self))


def selecionarImagemextras(self):
    self.imagem_recebida_extras = []
    try:
        janela2 = QWidget()
        janela2.resize(800, 600)
        janela2.move(100, 200)
        janela2.setWindowTitle('TCXS Project | Imagem EXTRAS')
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(janela2, "TCXS STORE | EXTRAS | Escolha sua imagem", "",
                                                  "JPG (*.jpg);;PNG (*.png)", options=options)
        if fileName:
            # faz uma verificaçao na imagem para limpar a lista acima
            if fileName in self.imagem_recebida_extras:
                self.imagem_recebida_extras.clear()
            else:
                self.imagem_recebida_extras.clear()
                self.imagem_recebida_extras.append(fileName)
        # carrega na variavel do Image do pilow (PIL) a imagem aberta
        imagem_recebida = Image.open(self.imagem_recebida_extras[0])
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
        self.nome_imagem_extras = fileName.split('/')[-1]
        # salva a imagem
        imagem_final.save(f'images/{self.nome_imagem_extras}')
        # exibe a imagem
        # imagem_final.show()
        self.ui.imagem_extras.setPixmap(
            QtGui.QPixmap(f'images/{self.nome_imagem_extras}').scaled(250, 250, QtCore.Qt.KeepAspectRatio))
        # CONEXAO COM FTP PARA UPLOAD DA imagem
        # arquivo para ser enviado ao server
        file = open(f'images/{self.nome_imagem_extras}', 'rb')  # file to send
        conexao.ftp.storbinary(f'STOR store/assets/images/extras/{self.nome_imagem_extras}', file)  # send the file
        file.close()  # close file and FTP and remove image
        self.ui.imagem_extras.setPixmap(
            QtGui.QPixmap(f'images/{self.nome_imagem_extras}').scaled(250, 250, QtCore.Qt.KeepAspectRatio))
        #conexao.ftp.quit()
        os.remove(f'images/{self.nome_imagem_extras}')
        visita_site = QMessageBox.question(self, 'AVISO | ATENÇÃO',
                                           """Para ter certeza que sua imagem foi upada, clique em sim, você será redirecionado para a pasta de imagens e podera visualizar se a imagem foi upada com sucesso, caso queira ignorar clique em não!""",
                                           QMessageBox.Yes | QMessageBox.No)
        self.show()
        if str(visita_site) == '16384':  # numero do botao de confirmação do QMessageBox | negação = 65536
            webbrowser.open('https://tcxsproject.com.br/store/assets/images/extras/', new=2)
    except:
        pass


def bancoDadosextras(self):
    # usa o arquivo de conexao
    self.query_extras = QSqlQuery(conexao.db_mysql)
    self.model_extras = QtSql.QSqlTableModel()
    self.model_extras.setTable('playstation_extras')
    self.model_extras.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
    self.model_extras.select()
    # popula as tabelas
    self.model_extras.setHeaderData(0, QtCore.Qt.Horizontal, "Id")
    self.model_extras.setHeaderData(1, QtCore.Qt.Horizontal, "Titulo")
    self.model_extras.setHeaderData(2, QtCore.Qt.Horizontal, "Descrição")
    self.model_extras.setHeaderData(3, QtCore.Qt.Horizontal, "ContentID")
    self.model_extras.setHeaderData(4, QtCore.Qt.Horizontal, "Imagem")
    self.model_extras.setHeaderData(5, QtCore.Qt.Horizontal, "Cadastro")
    self.model_extras.setHeaderData(6, QtCore.Qt.Horizontal, "Link")
    # tabela de dados
    self.ui.tabela_database_extras.setModel(self.model_extras)
    self.ui.tabela_database_extras.setToolTip(
        'Tabela da dados:\nPara adicionar itens sempre preencha todos os campos.\nCaso queira editar clique sobre o numero de uma linha e clique em atualizar.\nCaso queira deletar clique sobre o numero de uma linha e delete.')
    self.i_extras = self.model_extras.rowCount()


# ADICIONA CHAVES
def addToDbextras(self):
    # chama a função de conexao e popula a tabela | verificar com  print(self.i)
    bancoDadosextras(self)

    if self.ui.input_titulo_extras.text() == 'Titutlo EXTRAS' or self.ui.input_descricao_extras.text() == 'Descrição | Usar tag <br> para pular linhas.' or self.ui.input_contentid_extras.text() == 'Content ID' or self.ui.input_link_extras.text() == 'Link':
        QMessageBox.question(self, 'Tutorial Adicionar Jogo EXTRAS', """Para Adicionar Jogo de PlayStation EXTRAS:
Sempre adicione os dados em todos os campos e insira uma imagem depois clique em adicionar.
Para Editar Jogo de  PlayStation EXTRAS:
Para editar, preencha todos os campos, envie uma imagem e clique na linha que quer atualizar e no botao atualizar.
Para Deletar Jogo de PlayStation EXTRAS:
Caso queira deletar, clique na linha que quer deletar e no botão deletar!""", QMessageBox.Ok)
        self.show()
    else:

        try:
            self.nome_imagem_extras = self.nome_imagem_extras
            if self.nome_imagem_extras:
                # hora e data para ser insidas no servidor
                self.hoje = datetime.now()
                self.data_formatada = self.hoje.strftime('%Y-%m-%d %H:%M:%S')
                # insere os dados na database
                self.model_extras.insertRows(self.i_extras, 1)
                self.model_extras.setData(self.model_extras.index(self.i_extras, 1),
                                       self.ui.input_titulo_extras.text())  # TITULO
                self.model_extras.setData(self.model_extras.index(self.i_extras, 2),
                                       self.ui.input_descricao_extras.text())  # DESCRIÇÃO
                self.model_extras.setData(self.model_extras.index(self.i_extras, 3),
                                       self.ui.input_contentid_extras.text())  # CONTENT_ID
                self.model_extras.setData(self.model_extras.index(self.i_extras, 4), self.nome_imagem_extras)  # IMAGEM
                self.model_extras.setData(self.model_extras.index(self.i_extras, 5), self.data_formatada)  # CADASTRO
                self.model_extras.setData(self.model_extras.index(self.i_extras, 6), self.ui.input_link_extras.text())  # LINK
                self.model_extras.submitAll()
                self.i_extras += 1
                QMessageBox.question(self, 'TCXS Project | AVISO!', """Dados inseridos, confira na tabela!""",
                                     QMessageBox.Ok)
                self.show()
        except AttributeError:
            QMessageBox.question(self, 'TCXS Project | AVISO!', """Faça o envio da imagem antes de adicionar!""",
                                 QMessageBox.Ok)
            self.show()
            pass


# ATUALIZA AS CHAVES
def updaterowextras(self):
    if self.ui.tabela_database_extras.currentIndex().row() > -1:
        # hora e data para ser insidas no servidor
        self.hoje = datetime.now()
        self.data_formatada = self.hoje.strftime('%Y-%m-%d %H:%M:%S')
        # atualiza os dados baseado no nome das row's
        record = self.model_extras.record(self.ui.tabela_database_extras.currentIndex().row())
        record.setValue("titulo", self.ui.input_titulo_extras.text())  # TITULO
        record.setValue("descricao", self.ui.input_descricao_extras.text())  # DESCRIÇÃO
        record.setValue("content_id", self.ui.input_contentid_extras.text())  # CONTENT_ID
        record.setValue("imagem", self.nome_imagem_extras)  # IMAGEM
        record.setValue("cadastro", self.data_formatada)  # CADASTRO
        record.setValue("link", self.ui.input_link_extras.text())  # LINK
        self.model_extras.setRecord(self.ui.tabela_database_extras.currentIndex().row(), record)
        QMessageBox.question(self, 'TCXS Project | AVISO!', """Dados atualizados, confira na tabela!""", QMessageBox.Ok)
        self.show()
    else:
        QMessageBox.question(self, 'TCXS Project | Atualizar EXTRAS',
                             "Selecione uma linha para atualizar, clique sobre o numero a esquerda na tabela correspondente a linha.",
                             QMessageBox.Ok)
        self.show()


# DELETA AS CHAVES
def delrowextras(self):
    if self.ui.tabela_database_extras.currentIndex().row() > -1:
        self.model_extras.removeRow(self.ui.tabela_database_extras.currentIndex().row())
        self.i_extras -= 1
        self.model_extras.select()
        QMessageBox.question(self, 'TCXS Project | AVISO!', """Dados deletados, confira na tabela!""", QMessageBox.Ok)
        self.show()
    else:
        QMessageBox.question(self, 'TCXS Project | Deletar EXTRAS',
                             "Selecione uma linha para deletar, clique sobre o numero a esquerda na tabela correspondente a linha.",
                             QMessageBox.Ok)
        self.show()
