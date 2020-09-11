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


def funcoesCadastroPS3(self):
    # eventos para limpar os campos, que buscam funçoes no arquivo main | informações com o mouse sobre o item
    self.ui.imagem_ps3.setToolTip('Clique no botão e envie uma imagem.\nFormatos aceitos apenas .jpg e .png\nFormatos como .jpeg ou outros não são aceitos.\nSua imagem será enviada automáticamente redimensionada\naplicada a borda e enviada por ftp.\nCaso ocorra algum erro confira os dados de ftp.')
    self.ui.input_titulo_ps3.mousePressEvent = self.limpaInputTitulops3
    self.ui.input_titulo_ps3.setToolTip('Insira o titulo do jogo de PlayStation PS3.')
    self.ui.input_descricao_ps3.mousePressEvent = self.limpaInputDescricaops3
    self.ui.input_descricao_ps3.setToolTip(
        'Insira a descrição do jogo de PlayStation PS3.\nUse a tag <br> para pular linhas.\nEXEMPLO:\nIdioma: Ingles<br>Legenda: Ingles<br>Plataforma: PlayStation PS3\n[ATENÇÃO] Mantenha este padrão pois ele é usado na loja!')
    self.ui.input_content_id_ps3.mousePressEvent = self.limpaInputContentidps3
    self.ui.input_content_id_ps3.setToolTip(
        'Insira a content id do jogo de PlayStation PS3.\nCaso não queira inserir ou não tenha a content id\napenas insira qualquer coisa para não ficar em branco!')

    self.ui.input_link1_ps3.mousePressEvent = self.limpaInputLink1ps3
    self.ui.input_link1_ps3.setToolTip('Insira o link1 do jogo de PlayStation PS3.')


    self.ui.input_link2_ps3.mousePressEvent = self.limpaInputLink2ps3
    self.ui.input_link2_ps3.setToolTip('Insira o link2 do jogo de PlayStation PS3.')

    self.ui.input_link3_ps3.mousePressEvent = self.limpaInputLink3ps3
    self.ui.input_link3_ps3.setToolTip('Insira o link3 do jogo de PlayStation PS3.')

    self.ui.input_link4_ps3.mousePressEvent = self.limpaInputLink4ps3
    self.ui.input_link4_ps3.setToolTip('Insira o link4 do jogo de PlayStation PS3.')

    self.ui.input_link5_ps3.mousePressEvent = self.limpaInputLink5ps3
    self.ui.input_link5_ps3.setToolTip('Insira o link5 do jogo de PlayStation PS3.')

    self.ui.input_link6_ps3.mousePressEvent = self.limpaInputLink6ps3
    self.ui.input_link6_ps3.setToolTip('Insira o link6 do jogo de PlayStation PS3.')

    self.ui.input_link7_ps3.mousePressEvent = self.limpaInputLink7ps3
    self.ui.input_link7_ps3.setToolTip('Insira o link7 do jogo de PlayStation PS3.')

    self.ui.input_link8_ps3.mousePressEvent = self.limpaInputLink8ps3
    self.ui.input_link8_ps3.setToolTip('Insira o link8 do jogo de PlayStation PS3.')

    self.ui.input_link9_ps3.mousePressEvent = self.limpaInputLink9ps3
    self.ui.input_link9_ps3.setToolTip('Insira o link9 do jogo de PlayStation PS3.')

    self.ui.input_link10_ps3.mousePressEvent = self.limpaInputLink10ps3
    self.ui.input_link10_ps3.setToolTip('Insira o link10 do jogo de PlayStation PS3.')

    self.ui.input_link11_ps3.mousePressEvent = self.limpaInputLink11ps3
    self.ui.input_link11_ps3.setToolTip('Insira o link11 do jogo de PlayStation PS3.')

    self.ui.input_link12_ps3.mousePressEvent = self.limpaInputLink12ps3
    self.ui.input_link12_ps3.setToolTip('Insira o link12 do jogo de PlayStation PS3.')

    self.ui.input_link13_ps3.mousePressEvent = self.limpaInputLink13ps3
    self.ui.input_link13_ps3.setToolTip('Insira o link13 do jogo de PlayStation PS3.')

    self.ui.input_link14_ps3.mousePressEvent = self.limpaInputLink14ps3
    self.ui.input_link14_ps3.setToolTip('Insira o link14 do jogo de PlayStation PS3.')

    self.ui.input_link15_ps3.mousePressEvent = self.limpaInputLink15ps3
    self.ui.input_link15_ps3.setToolTip('Insira o link15 do jogo de PlayStation PS3.')

    self.ui.input_link16_ps3.mousePressEvent = self.limpaInputLink16ps3
    self.ui.input_link16_ps3.setToolTip('Insira o link16 do jogo de PlayStation PS3.')

    self.ui.input_link17_ps3.mousePressEvent = self.limpaInputLink17ps3
    self.ui.input_link17_ps3.setToolTip('Insira o link17 do jogo de PlayStation PS3.')

    self.ui.input_link18_ps3.mousePressEvent = self.limpaInputLink18ps3
    self.ui.input_link18_ps3.setToolTip('Insira o link18 do jogo de PlayStation PS3.')

    self.ui.input_link19_ps3.mousePressEvent = self.limpaInputLink19ps3
    self.ui.input_link19_ps3.setToolTip('Insira o link19 do jogo de PlayStation PS3.')

    self.ui.input_link20_ps3.mousePressEvent = self.limpaInputLink20ps3
    self.ui.input_link20_ps3.setToolTip('Insira o link20 do jogo de PlayStation PS3.')

    self.ui.input_link21_ps3.mousePressEvent = self.limpaInputLink21ps3
    self.ui.input_link21_ps3.setToolTip('Insira o link21 do jogo de PlayStation PS3.')

    self.ui.input_link22_ps3.mousePressEvent = self.limpaInputLink22ps3
    self.ui.input_link22_ps3.setToolTip('Insira o link22 do jogo de PlayStation PS3.')

    self.ui.input_link23_ps3.mousePressEvent = self.limpaInputLink23ps3
    self.ui.input_link23_ps3.setToolTip('Insira o link23 do jogo de PlayStation PS3.')

    self.ui.input_link24_ps3.mousePressEvent = self.limpaInputLink24ps3
    self.ui.input_link24_ps3.setToolTip('Insira o link24 do jogo de PlayStation PS3.')

    self.ui.input_link25_ps3.mousePressEvent = self.limpaInputLink25ps3
    self.ui.input_link25_ps3.setToolTip('Insira o link25 do jogo de PlayStation PS3.')

    self.ui.input_link26_ps3.mousePressEvent = self.limpaInputLink26ps3
    self.ui.input_link26_ps3.setToolTip('Insira o link26 do jogo de PlayStation PS3.')

    self.ui.input_link27_ps3.mousePressEvent = self.limpaInputLink27ps3
    self.ui.input_link27_ps3.setToolTip('Insira o link27 do jogo de PlayStation PS3.')

    self.ui.input_link28_ps3.mousePressEvent = self.limpaInputLink28ps3
    self.ui.input_link28_ps3.setToolTip('Insira o link28 do jogo de PlayStation PS3.')

    self.ui.input_link29_ps3.mousePressEvent = self.limpaInputLink29ps3
    self.ui.input_link29_ps3.setToolTip('Insira o link29 do jogo de PlayStation PS3.')

    self.ui.input_link30_ps3.mousePressEvent = self.limpaInputLink30ps3
    self.ui.input_link30_ps3.setToolTip('Insira o link30 do jogo de PlayStation PS3.')

    # botoes das açoes
    self.ui.botao_db_adiciona_ps3.clicked.connect(lambda: addToDbps3(self))
    self.ui.botao_db_atualiza_ps3.clicked.connect(lambda: updaterowps3(self))
    self.ui.botao_db_deleta_ps3.clicked.connect(lambda: delrowps3(self))
    # btn upload imagem_ps3
    self.ui.btn_upload_imagem_ps3.clicked.connect(lambda: selecionarImagemps3(self))


def selecionarImagemps3(self):
    self.imagem_recebida_ps3 = []
    try:
        janela2 = QWidget()
        janela2.resize(800, 600)
        janela2.move(100, 200)
        janela2.setWindowTitle('TCXS Project | Imagem PS3')
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(janela2, "TCXS STORE | PS3 | Escolha sua imagem", "",
                                                  "JPG (*.jpg);;PNG (*.png)", options=options)
        if fileName:
            # faz uma verificaçao na imagem para limpar a lista acima
            if fileName in self.imagem_recebida_ps3:
                self.imagem_recebida_ps3.clear()
            else:
                self.imagem_recebida_ps3.clear()
                self.imagem_recebida_ps3.append(fileName)
        # carrega na variavel do Image do pilow (PIL) a imagem aberta
        imagem_recebida = Image.open(self.imagem_recebida_ps3[0])
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
        self.nome_imagem_ps3 = fileName.split('/')[-1]
        # salva a imagem
        imagem_final.save(f'images/{self.nome_imagem_ps3}')
        # exibe a imagem
        # imagem_final.show()
        # CONEXAO COM FTP PARA UPLOAD DA imagem
        # arquivo para ser enviado ao server
        file = open(f'images/{self.nome_imagem_ps3}', 'rb')  # file to send
        conexao.ftp.storbinary(f'STOR store/assets/images/ps3/{self.nome_imagem_ps3}', file)  # send the file
        file.close()  # close file and FTP and remove image
        self.ui.imagem_ps3.setPixmap(
            QtGui.QPixmap(f'images/{self.nome_imagem_ps3}').scaled(250, 250, QtCore.Qt.KeepAspectRatio))
        #conexao.ftp.quit()
        os.remove(f'images/{self.nome_imagem_ps3}')
        visita_site = QMessageBox.question(self, 'AVISO | ATENÇÃO',
                                           """Para ter certeza que sua imagem foi upada, clique em sim, você será redirecionado para a pasta de imagens e podera visualizar se a imagem foi upada com sucesso, caso queira ignorar clique em não!""",
                                           QMessageBox.Yes | QMessageBox.No)
        self.show()
        if str(visita_site) == '16384':  # numero do botao de confirmação do QMessageBox | negação = 65536
            webbrowser.open('https://tcxsproject.com.br/store/assets/images/ps3/', new=2)
    except:
        pass


def bancoDadosps3(self):
    # usa o arquivo de conexao
    self.query_ps3 = QSqlQuery(conexao.db_mysql)
    self.model_ps3 = QtSql.QSqlTableModel()
    self.model_ps3.setTable('playstation_ps3')
    self.model_ps3.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
    self.model_ps3.select()
    # popula as tabelas
    self.model_ps3.setHeaderData(0, QtCore.Qt.Horizontal, "Id")
    self.model_ps3.setHeaderData(1, QtCore.Qt.Horizontal, "Titulo")
    self.model_ps3.setHeaderData(2, QtCore.Qt.Horizontal, "Descrição")
    self.model_ps3.setHeaderData(3, QtCore.Qt.Horizontal, "ContentID")
    self.model_ps3.setHeaderData(4, QtCore.Qt.Horizontal, "Imagem")
    self.model_ps3.setHeaderData(5, QtCore.Qt.Horizontal, "Cadastro")
    self.model_ps3.setHeaderData(6, QtCore.Qt.Horizontal, "Link1")
    self.model_ps3.setHeaderData(7, QtCore.Qt.Horizontal, "Link2")
    self.model_ps3.setHeaderData(8, QtCore.Qt.Horizontal, "Link3")
    self.model_ps3.setHeaderData(9, QtCore.Qt.Horizontal, "Link4")
    self.model_ps3.setHeaderData(10, QtCore.Qt.Horizontal, "Link5")
    self.model_ps3.setHeaderData(11, QtCore.Qt.Horizontal, "Link6")
    self.model_ps3.setHeaderData(12, QtCore.Qt.Horizontal, "Link7")
    self.model_ps3.setHeaderData(13, QtCore.Qt.Horizontal, "Link8")
    self.model_ps3.setHeaderData(14, QtCore.Qt.Horizontal, "Link9")
    self.model_ps3.setHeaderData(15, QtCore.Qt.Horizontal, "Link10")
    self.model_ps3.setHeaderData(16, QtCore.Qt.Horizontal, "Link11")
    self.model_ps3.setHeaderData(17, QtCore.Qt.Horizontal, "Link12")
    self.model_ps3.setHeaderData(18, QtCore.Qt.Horizontal, "Link13")
    self.model_ps3.setHeaderData(19, QtCore.Qt.Horizontal, "Link14")
    self.model_ps3.setHeaderData(20, QtCore.Qt.Horizontal, "Link15")
    self.model_ps3.setHeaderData(21, QtCore.Qt.Horizontal, "Link16")
    self.model_ps3.setHeaderData(22, QtCore.Qt.Horizontal, "Link17")
    self.model_ps3.setHeaderData(23, QtCore.Qt.Horizontal, "Link18")
    self.model_ps3.setHeaderData(24, QtCore.Qt.Horizontal, "Link19")
    self.model_ps3.setHeaderData(25, QtCore.Qt.Horizontal, "Link20")
    self.model_ps3.setHeaderData(26, QtCore.Qt.Horizontal, "Link21")
    self.model_ps3.setHeaderData(27, QtCore.Qt.Horizontal, "Link22")
    self.model_ps3.setHeaderData(28, QtCore.Qt.Horizontal, "Link23")
    self.model_ps3.setHeaderData(29, QtCore.Qt.Horizontal, "Link24")
    self.model_ps3.setHeaderData(30, QtCore.Qt.Horizontal, "Link25")
    self.model_ps3.setHeaderData(31, QtCore.Qt.Horizontal, "Link26")
    self.model_ps3.setHeaderData(32, QtCore.Qt.Horizontal, "Link27")
    self.model_ps3.setHeaderData(33, QtCore.Qt.Horizontal, "Link28")
    self.model_ps3.setHeaderData(34, QtCore.Qt.Horizontal, "Link29")
    self.model_ps3.setHeaderData(35, QtCore.Qt.Horizontal, "Link30")

    # tabela de dados
    self.ui.tabela_database_ps3.setModel(self.model_ps3)
    self.ui.tabela_database_ps3.setToolTip(
        'Tabela de dados:\nPara adicionar itens sempre preencha todos os campos.\nCaso queira editar clique sobre o numero de uma linha e clique em atualizar.\nCaso queira deletar clique sobre o numero de uma linha e delete.')
    self.i_ps3 = self.model_ps3.rowCount()


# ADICIONA CHAVES
def addToDbps3(self):
    # chama a função de conexao e popula a tabela | verificar com  print(self.i)
    bancoDadosps3(self)

    if self.ui.input_titulo_ps3.text() == 'Titutlo PS3' or self.ui.input_descricao_ps3.text() == 'Descrição | Usar tag <br> para pular linhas.' or self.ui.input_content_id_ps3.text() == 'Content ID' or self.ui.input_link1_ps3.text() == '---':
        QMessageBox.question(self, 'Tutorial Adicionar Jogo PS3', """Para Adicionar Jogo de PlayStation PS3:
Sempre adicione os dados em todos os campos e insira uma imagem depois clique em adicionar.
Para Editar Jogo de  PlayStation PS3:
Para editar, preencha todos os campos, envie uma imagem e clique na linha que quer atualizar e no botao atualizar.
Para Deletar Jogo de PlayStation PS3:
Caso queira deletar, clique na linha que quer deletar e no botão deletar!""", QMessageBox.Ok)
        self.show()
    else:

        try:
            self.nome_imagem_ps3 = self.nome_imagem_ps3
            if self.nome_imagem_ps3:
                # hora e data para ser insidas no servidor
                self.hoje = datetime.now()
                self.data_formatada = self.hoje.strftime('%Y-%m-%d %H:%M:%S')
                # insere os dados na database
                self.model_ps3.insertRows(self.i_ps3, 1)
                self.model_ps3.setData(self.model_ps3.index(self.i_ps3, 1),self.ui.input_titulo_ps3.text())  # TITULO
                self.model_ps3.setData(self.model_ps3.index(self.i_ps3, 2),self.ui.input_descricao_ps3.text())  # DESCRIÇÃO
                self.model_ps3.setData(self.model_ps3.index(self.i_ps3, 3),self.ui.input_content_id_ps3.text())  # CONTENT_ID
                self.model_ps3.setData(self.model_ps3.index(self.i_ps3, 4), self.nome_imagem_ps3)  # IMAGEM
                self.model_ps3.setData(self.model_ps3.index(self.i_ps3, 5), self.data_formatada)  # CADASTRO
                self.model_ps3.setData(self.model_ps3.index(self.i_ps3, 6), self.ui.input_link1_ps3.text())
                self.model_ps3.setData(self.model_ps3.index(self.i_ps3, 7), self.ui.input_link2_ps3.text())
                self.model_ps3.setData(self.model_ps3.index(self.i_ps3, 8), self.ui.input_link3_ps3.text())
                self.model_ps3.setData(self.model_ps3.index(self.i_ps3, 9), self.ui.input_link4_ps3.text())
                self.model_ps3.setData(self.model_ps3.index(self.i_ps3, 10), self.ui.input_link5_ps3.text())
                self.model_ps3.setData(self.model_ps3.index(self.i_ps3, 11), self.ui.input_link6_ps3.text())
                self.model_ps3.setData(self.model_ps3.index(self.i_ps3, 12), self.ui.input_link7_ps3.text())
                self.model_ps3.setData(self.model_ps3.index(self.i_ps3, 13), self.ui.input_link8_ps3.text())
                self.model_ps3.setData(self.model_ps3.index(self.i_ps3, 14), self.ui.input_link9_ps3.text())
                self.model_ps3.setData(self.model_ps3.index(self.i_ps3, 15), self.ui.input_link10_ps3.text())
                self.model_ps3.setData(self.model_ps3.index(self.i_ps3, 16), self.ui.input_link11_ps3.text())
                self.model_ps3.setData(self.model_ps3.index(self.i_ps3, 17), self.ui.input_link12_ps3.text())
                self.model_ps3.setData(self.model_ps3.index(self.i_ps3, 18), self.ui.input_link13_ps3.text())
                self.model_ps3.setData(self.model_ps3.index(self.i_ps3, 19), self.ui.input_link14_ps3.text())
                self.model_ps3.setData(self.model_ps3.index(self.i_ps3, 20), self.ui.input_link15_ps3.text())
                self.model_ps3.setData(self.model_ps3.index(self.i_ps3, 21), self.ui.input_link16_ps3.text())
                self.model_ps3.setData(self.model_ps3.index(self.i_ps3, 22), self.ui.input_link17_ps3.text())
                self.model_ps3.setData(self.model_ps3.index(self.i_ps3, 23), self.ui.input_link18_ps3.text())
                self.model_ps3.setData(self.model_ps3.index(self.i_ps3, 24), self.ui.input_link19_ps3.text())
                self.model_ps3.setData(self.model_ps3.index(self.i_ps3, 25), self.ui.input_link20_ps3.text())
                self.model_ps3.setData(self.model_ps3.index(self.i_ps3, 26), self.ui.input_link21_ps3.text())
                self.model_ps3.setData(self.model_ps3.index(self.i_ps3, 27), self.ui.input_link22_ps3.text())
                self.model_ps3.setData(self.model_ps3.index(self.i_ps3, 28), self.ui.input_link23_ps3.text())
                self.model_ps3.setData(self.model_ps3.index(self.i_ps3, 29), self.ui.input_link24_ps3.text())
                self.model_ps3.setData(self.model_ps3.index(self.i_ps3, 30), self.ui.input_link25_ps3.text())
                self.model_ps3.setData(self.model_ps3.index(self.i_ps3, 31), self.ui.input_link26_ps3.text())
                self.model_ps3.setData(self.model_ps3.index(self.i_ps3, 32), self.ui.input_link27_ps3.text())
                self.model_ps3.setData(self.model_ps3.index(self.i_ps3, 33), self.ui.input_link28_ps3.text())
                self.model_ps3.setData(self.model_ps3.index(self.i_ps3, 34), self.ui.input_link29_ps3.text())
                self.model_ps3.setData(self.model_ps3.index(self.i_ps3, 35), self.ui.input_link30_ps3.text())
                self.model_ps3.submitAll()
                self.i_ps3 += 1
                QMessageBox.question(self, 'TCXS Project | AVISO!', """Dados inseridos, confira na tabela!""", QMessageBox.Ok)
                self.show()
        except AttributeError:
            QMessageBox.question(self, 'TCXS Project | AVISO!', """Faça o envio da imagem antes de adicionar!""",
                                 QMessageBox.Ok)
            self.show()
            pass


# ATUALIZA AS CHAVES
def updaterowps3(self):
    if self.ui.tabela_database_ps3.currentIndex().row() > -1:
        # hora e data para ser insidas no servidor
        self.hoje = datetime.now()
        self.data_formatada = self.hoje.strftime('%Y-%m-%d %H:%M:%S')
        # atualiza os dados baseado no nome das row's
        record = self.model_ps3.record(self.ui.tabela_database_ps3.currentIndex().row())
        record.setValue("titulo", self.ui.input_titulo_ps3.text())  # TITULO
        record.setValue("descricao", self.ui.input_descricao_ps3.text())  # DESCRIÇÃO
        record.setValue("content_id", self.ui.input_content_id_ps3.text())  # CONTENT_ID
        record.setValue("imagem", self.nome_imagem_ps3)  # IMAGEM
        record.setValue("cadastro", self.data_formatada)  # CADASTRO
        record.setValue("link1", self.ui.input_link1_ps3.text())
        record.setValue("link2", self.ui.input_link2_ps3.text())
        record.setValue("link3", self.ui.input_link3_ps3.text())
        record.setValue("link4", self.ui.input_link4_ps3.text())
        record.setValue("link5", self.ui.input_link5_ps3.text())
        record.setValue("link6", self.ui.input_link6_ps3.text())
        record.setValue("link7", self.ui.input_link7_ps3.text())
        record.setValue("link8", self.ui.input_link8_ps3.text())
        record.setValue("link9", self.ui.input_link9_ps3.text())
        record.setValue("link10", self.ui.input_link10_ps3.text())
        record.setValue("link11", self.ui.input_link11_ps3.text())
        record.setValue("link12", self.ui.input_link12_ps3.text())
        record.setValue("link13", self.ui.input_link13_ps3.text())
        record.setValue("link14", self.ui.input_link14_ps3.text())
        record.setValue("link15", self.ui.input_link15_ps3.text())
        record.setValue("link16", self.ui.input_link16_ps3.text())
        record.setValue("link17", self.ui.input_link17_ps3.text())
        record.setValue("link18", self.ui.input_link18_ps3.text())
        record.setValue("link19", self.ui.input_link19_ps3.text())
        record.setValue("link20", self.ui.input_link20_ps3.text())
        record.setValue("link21", self.ui.input_link21_ps3.text())
        record.setValue("link22", self.ui.input_link22_ps3.text())
        record.setValue("link23", self.ui.input_link23_ps3.text())
        record.setValue("link24", self.ui.input_link24_ps3.text())
        record.setValue("link25", self.ui.input_link25_ps3.text())
        record.setValue("link26", self.ui.input_link26_ps3.text())
        record.setValue("link27", self.ui.input_link27_ps3.text())
        record.setValue("link28", self.ui.input_link28_ps3.text())
        record.setValue("link29", self.ui.input_link29_ps3.text())
        record.setValue("link30", self.ui.input_link30_ps3.text())

        self.model_ps3.setRecord(self.ui.tabela_database_ps3.currentIndex().row(), record)
        QMessageBox.question(self, 'TCXS Project | AVISO!', """Dados atualizados, confira na tabela!""", QMessageBox.Ok)
        self.show()

    else:
        QMessageBox.question(self, 'TCXS Project | Atualizar PS3',
                             "Selecione uma linha para atualizar, clique sobre o numero a esquerda na tabela correspondente a linha.",
                             QMessageBox.Ok)
        self.show()


# DELETA AS CHAVES
def delrowps3(self):
    if self.ui.tabela_database_ps3.currentIndex().row() > -1:
        self.model_ps3.removeRow(self.ui.tabela_database_ps3.currentIndex().row())
        self.i_ps3 -= 1
        self.model_ps3.select()
        QMessageBox.question(self, 'TCXS Project | AVISO!', """Dados deletados, confira na tabela!""", QMessageBox.Ok)
        self.show()
    else:
        QMessageBox.question(self, 'TCXS Project | Deletar PS3',
                             "Selecione uma linha para deletar, clique sobre o numero a esquerda na tabela correspondente a linha.",
                             QMessageBox.Ok)
        self.show()
