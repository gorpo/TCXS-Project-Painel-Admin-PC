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


def funcoesCadastroRETRO(self):
    # eventos para limpar os campos, que buscam funçoes no arquivo main | informações com o mouse sobre o item
    self.ui.imagem_retro.setToolTip('Clique no botão e envie uma imagem.\nFormatos aceitos apenas .jpg e .png\nFormatos como .jpeg ou outros não são aceitos.\nSua imagem será enviada automáticamente redimensionada\naplicada a borda e enviada por ftp.\nCaso ocorra algum erro confira os dados de ftp.')
    self.ui.input_titulo_retro.mousePressEvent = self.limpaInputTituloretro
    self.ui.input_titulo_retro.setToolTip('Insira o titulo do jogo de PlayStation RETRO.')
    self.ui.input_descricao_retro.mousePressEvent = self.limpaInputDescricaoretro
    self.ui.input_descricao_retro.setToolTip(
        'Insira a descrição do jogo de PlayStation RETRO.\nUse a tag <br> para pular linhas.\nEXEMPLO:\nIdioma: Ingles<br>Legenda: Ingles<br>Plataforma: PlayStation RETRO\n[ATENÇÃO] Mantenha este padrão pois ele é usado na loja!')
    self.ui.input_contentid_retro.mousePressEvent = self.limpaInputContentidretro
    self.ui.input_contentid_retro.setToolTip(
        'Insira a content id do jogo de PlayStation RETRO.\nCaso não queira inserir ou não tenha a content id\napenas insira qualquer coisa para não ficar em branco!')
    self.ui.input_link_retro.mousePressEvent = self.limpaInputLinkretro
    self.ui.input_link_retro.setToolTip('Insira o link do jogo de PlayStation RETRO.')
    # botoes das açoes
    self.ui.botao_db_adiciona_retro.clicked.connect(lambda: addToDbretro(self))
    self.ui.botao_db_atualiza_retro.clicked.connect(lambda: updaterowretro(self))
    self.ui.botao_db_deleta_retro.clicked.connect(lambda: delrowretro(self))
    # btn upload imagem_retro
    self.ui.btn_upload_imagem_retro.clicked.connect(lambda: selecionarImagemretro(self))


def selecionarImagemretro(self):
    self.imagem_recebida_retro = []
    try:
        janela2 = QWidget()
        janela2.resize(800, 600)
        janela2.move(100, 200)
        janela2.setWindowTitle('TCXS Project | Imagem RETRO')
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(janela2, "TCXS STORE | RETRO | Escolha sua imagem", "",
                                                  "JPG (*.jpg);;PNG (*.png)", options=options)
        if fileName:
            # faz uma verificaçao na imagem para limpar a lista acima
            if fileName in self.imagem_recebida_retro:
                self.imagem_recebida_retro.clear()
            else:
                self.imagem_recebida_retro.clear()
                self.imagem_recebida_retro.append(fileName)
        # carrega na variavel do Image do pilow (PIL) a imagem aberta
        imagem_recebida = Image.open(self.imagem_recebida_retro[0])
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
        self.nome_imagem_retro = fileName.split('/')[-1]
        # salva a imagem
        imagem_final.save(f'images/{self.nome_imagem_retro}')
        # exibe a imagem
        # imagem_final.show()

        # CONEXAO COM FTP PARA UPLOAD DA imagem
        # arquivo para ser enviado ao server
        file = open(f'images/{self.nome_imagem_retro}', 'rb')  # file to send
        conexao.ftp.storbinary(f'STOR store/assets/images/emuladores/{self.nome_imagem_retro}', file)  # send the file
        file.close()  # close file and FTP and remove image
        self.ui.imagem_retro.setPixmap(
            QtGui.QPixmap(f'images/{self.nome_imagem_retro}').scaled(250, 250, QtCore.Qt.KeepAspectRatio))
        #conexao.ftp.quit()
        os.remove(f'images/{self.nome_imagem_retro}')
        visita_site = QMessageBox.question(self, 'AVISO | ATENÇÃO',
                                           """Para ter certeza que sua imagem foi upada, clique em sim, você será redirecionado para a pasta de imagens e podera visualizar se a imagem foi upada com sucesso, caso queira ignorar clique em não!""",
                                           QMessageBox.Yes | QMessageBox.No)
        self.show()
        if str(visita_site) == '16384':  # numero do botao de confirmação do QMessageBox | negação = 65536
            webbrowser.open('https://tcxsproject.com.br/store/assets/images/emuladores/', new=2)
    except:
        pass


def bancoDadosretro(self):
    # usa o arquivo de conexao
    self.query_retro = QSqlQuery(conexao.db_mysql)
    self.model_retro = QtSql.QSqlTableModel()
    self.model_retro.setTable('playstation_emuladores')
    self.model_retro.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
    self.model_retro.select()
    # popula as tabelas
    self.model_retro.setHeaderData(0, QtCore.Qt.Horizontal, "Id")
    self.model_retro.setHeaderData(1, QtCore.Qt.Horizontal, "Titulo")
    self.model_retro.setHeaderData(2, QtCore.Qt.Horizontal, "Descrição")
    self.model_retro.setHeaderData(3, QtCore.Qt.Horizontal, "ContentID")
    self.model_retro.setHeaderData(4, QtCore.Qt.Horizontal, "Imagem")
    self.model_retro.setHeaderData(5, QtCore.Qt.Horizontal, "Cadastro")
    self.model_retro.setHeaderData(6, QtCore.Qt.Horizontal, "Link")
    # tabela de dados
    self.ui.tabela_database_retro.setModel(self.model_retro)
    self.ui.tabela_database_retro.setToolTip(
        'Tabela da dados:\nPara adicionar itens sempre preencha todos os campos.\nCaso queira editar clique sobre o numero de uma linha e clique em atualizar.\nCaso queira deletar clique sobre o numero de uma linha e delete.')
    self.i_retro = self.model_retro.rowCount()


# ADICIONA CHAVES
def addToDbretro(self):
    # chama a função de conexao e popula a tabela | verificar com  print(self.i)
    bancoDadosretro(self)

    if self.ui.input_titulo_retro.text() == 'Titutlo RETRO' or self.ui.input_descricao_retro.text() == 'Descrição | Usar tag <br> para pular linhas.' or self.ui.input_contentid_retro.text() == 'Content ID' or self.ui.input_link_retro.text() == 'Link':
        QMessageBox.question(self, 'Tutorial Adicionar Jogo RETRO', """Para Adicionar Jogo de PlayStation RETRO:
Sempre adicione os dados em todos os campos e insira uma imagem depois clique em adicionar.
Para Editar Jogo de  PlayStation RETRO:
Para editar, preencha todos os campos, envie uma imagem e clique na linha que quer atualizar e no botao atualizar.
Para Deletar Jogo de PlayStation RETRO:
Caso queira deletar, clique na linha que quer deletar e no botão deletar!""", QMessageBox.Ok)
        self.show()
    else:

        try:
            self.nome_imagem_retro = self.nome_imagem_retro
            if self.nome_imagem_retro:
                # hora e data para ser insidas no servidor
                self.hoje = datetime.now()
                self.data_formatada = self.hoje.strftime('%Y-%m-%d %H:%M:%S')
                # insere os dados na database
                self.model_retro.insertRows(self.i_retro, 1)
                self.model_retro.setData(self.model_retro.index(self.i_retro, 1),
                                       self.ui.input_titulo_retro.text())  # TITULO
                self.model_retro.setData(self.model_retro.index(self.i_retro, 2),
                                       self.ui.input_descricao_retro.text())  # DESCRIÇÃO
                self.model_retro.setData(self.model_retro.index(self.i_retro, 3),
                                       self.ui.input_contentid_retro.text())  # CONTENT_ID
                self.model_retro.setData(self.model_retro.index(self.i_retro, 4), self.nome_imagem_retro)  # IMAGEM
                self.model_retro.setData(self.model_retro.index(self.i_retro, 5), self.data_formatada)  # CADASTRO
                self.model_retro.setData(self.model_retro.index(self.i_retro, 6), self.ui.input_link_retro.text())  # LINK
                self.model_retro.submitAll()
                self.i_retro += 1
                QMessageBox.question(self, 'TCXS Project | AVISO!', """Dados inseridos, confira na tabela!""",
                                     QMessageBox.Ok)
                self.show()
        except AttributeError:
            QMessageBox.question(self, 'TCXS Project | AVISO!', """Faça o envio da imagem antes de adicionar!""",
                                 QMessageBox.Ok)
            self.show()
            pass


# ATUALIZA AS CHAVES
def updaterowretro(self):
    if self.ui.tabela_database_retro.currentIndex().row() > -1:
        # hora e data para ser insidas no servidor
        self.hoje = datetime.now()
        self.data_formatada = self.hoje.strftime('%Y-%m-%d %H:%M:%S')
        # atualiza os dados baseado no nome das row's
        record = self.model_retro.record(self.ui.tabela_database_retro.currentIndex().row())
        record.setValue("titulo", self.ui.input_titulo_retro.text())  # TITULO
        record.setValue("descricao", self.ui.input_descricao_retro.text())  # DESCRIÇÃO
        record.setValue("content_id", self.ui.input_contentid_retro.text())  # CONTENT_ID
        record.setValue("imagem", self.nome_imagem_retro)  # IMAGEM
        record.setValue("cadastro", self.data_formatada)  # CADASTRO
        record.setValue("link", self.ui.input_link_retro.text())  # LINK
        self.model_retro.setRecord(self.ui.tabela_database_retro.currentIndex().row(), record)
        QMessageBox.question(self, 'TCXS Project | AVISO!', """Dados atualizados, confira na tabela!""", QMessageBox.Ok)
        self.show()
    else:
        QMessageBox.question(self, 'TCXS Project | Atualizar RETRO',
                             "Selecione uma linha para atualizar, clique sobre o numero a esquerda na tabela correspondente a linha.",
                             QMessageBox.Ok)
        self.show()


# DELETA AS CHAVES
def delrowretro(self):
    if self.ui.tabela_database_retro.currentIndex().row() > -1:
        self.model_retro.removeRow(self.ui.tabela_database_retro.currentIndex().row())
        self.i_retro -= 1
        self.model_retro.select()
        QMessageBox.question(self, 'TCXS Project | AVISO!', """Dados deletados, confira na tabela!""", QMessageBox.Ok)
        self.show()
    else:
        QMessageBox.question(self, 'TCXS Project | Deletar RETRO',
                             "Selecione uma linha para deletar, clique sobre o numero a esquerda na tabela correspondente a linha.",
                             QMessageBox.Ok)
        self.show()
