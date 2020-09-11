#!/usr/bin/env python
# -*- coding: utf-8 -*-
#███╗   ███╗ █████╗ ███╗   ██╗██╗ ██████╗ ██████╗ ███╗   ███╗██╗ ██████╗
#████╗ ████║██╔══██╗████╗  ██║██║██╔════╝██╔═══██╗████╗ ████║██║██╔═══██╗
#██╔████╔██║███████║██╔██╗ ██║██║██║     ██║   ██║██╔████╔██║██║██║   ██║
#██║╚██╔╝██║██╔══██║██║╚██╗██║██║██║     ██║   ██║██║╚██╔╝██║██║██║   ██║
#██║ ╚═╝ ██║██║  ██║██║ ╚████║██║╚██████╗╚██████╔╝██║ ╚═╝ ██║██║╚██████╔╝
#╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝
#            @GorpoOrko | Manicomio TCXS Project | 2020

from TCXSProject import *


def funcoesConsultaUsers(self):
    #eventos para limpar os campos, que buscam funçoes no arquivo main
    self.ui.input_pesquisa_acessos_usuarios.mousePressEvent = self.limpaPesquisaAcessoUsers
    self.ui.input_pesquisa_acessos_usuarios.setToolTip('Insira o user que o usuário loga\nna loja para consultar seus acessos.')
    self.ui.btn_pesquisa_acessos_usuarios.clicked.connect(lambda: consultaUser(self))


def consultaUser(self):

    #usa o arquivo de conexao
    self.query_user = QSqlQuery(conexao.db_mysql)
    self.model_user = QtSql.QSqlTableModel()
    #seleciona a tabela
    self.pesquisar_usuario = f'user_{self.ui.input_pesquisa_acessos_usuarios.text()}'
    self.model_user.setTable(self.pesquisar_usuario)
    self.model_user.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)

    #retorna se achou a tabela do usuario | RETORNA: True e False
    self.achou_user = self.model_user.select()

    # usa o arquivo de conexao para procurar o nome do usuario se ainda esta cadastrado
    lista_users = []
    self.query_verifica_user = QSqlQuery(conexao.db_mysql)
    self.query_verifica_user.exec("""SELECT * FROM playstation_users""")
    while self.query_verifica_user.next():
        #retorna o nome dos usuarios cadastrados
        self.verifica_users_cadastrados = self.query_verifica_user.value(1)
        lista_users.append(self.verifica_users_cadastrados)

        #print(lista_users)

    #se achou a tabela do usuario user_usuario e ele esta cadastrado e ja na lista_users-->
    if self.achou_user and self.ui.input_pesquisa_acessos_usuarios.text() in lista_users:
        #popula as tabelas
        self.model_user.setHeaderData(0, QtCore.Qt.Horizontal, "Usuario")
        self.model_user.setHeaderData(1, QtCore.Qt.Horizontal, "Senha")
        self.model_user.setHeaderData(2, QtCore.Qt.Horizontal, "IP")
        self.model_user.setHeaderData(3, QtCore.Qt.Horizontal, "Cadastrado")
        #tabela de dados
        self.ui.tabela_pesquisa_acessos_usuarios.setModel(self.model_user)
        self.ui.tabela_pesquisa_acessos_usuarios.setToolTip('Informações sobre os acessos do usuário.\nCaso note algum IP suspeito delete o login do usuário.')
        self.i_user = self.model_user.rowCount()


    #se nao achou a tabela do user_usuario e ele nao esta na lista de cadastrados deleta a tabela para nao ficar lixo
    if self.achou_user and self.ui.input_pesquisa_acessos_usuarios.text() not in lista_users:
        self.query_user.exec(f"""DROP TABLE IF EXISTS user_{self.ui.input_pesquisa_acessos_usuarios.text()} """)
        QMessageBox.question(self, 'TCXS Project | Informações da Homepage',
 """Para obter informações de vazamento do login do user:
 Insira o user do usuário e clique em pesquisar, caso não retorne nenhum valor é porque o usuário ainda não fez login!
 É necessário ao menos uma vez o usuário ter logado para gravar a data, hora e ip de acesso a loja.
 """, QMessageBox.Ok)
        self.show()







