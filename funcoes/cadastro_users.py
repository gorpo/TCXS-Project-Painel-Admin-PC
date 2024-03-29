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



def funcoesCadastroUsers(self):
    #eventos para limpar os campos, que buscam funçoes no arquivo main
    self.ui.input_nome_user.mousePressEvent = self.limpaNomeCadastro
    self.ui.input_nome_user.setToolTip('Insira nome que será exibido na loja.')
    self.ui.input_username_user.mousePressEvent = self.limpaUserCadastro
    self.ui.input_username_user.setToolTip('Insira o username que o usuário irá logar na loja.')
    self.ui.input_senha_user.mousePressEvent = self.limpaSenhaCadastro
    self.ui.input_senha_user.setToolTip('Insira a senha que o usuário irá logar na loja.')
    #botoes de ação da pagina
    self.ui.btn_adiciona_user.clicked.connect(lambda: addToDbUser(self))
    self.ui.btn_atualiza_user.clicked.connect(lambda: updaterowUser(self))
    self.ui.btn_deleta_user.clicked.connect(lambda: delrowUser(self))


def bancoDadosUsers(self):
    self.i_user = 0
    # usa o arquivo de conexao
    self.query_user = QSqlQuery(conexao.db_mysql)
    self.model_user = QtSql.QSqlTableModel()
    # seleciona a tabela
    self.model_user.setTable('playstation_users')
    self.model_user.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
    self.model_user.select()
    # popula as tabelas
    self.model_user.setHeaderData(0, QtCore.Qt.Horizontal, "Id")
    self.model_user.setHeaderData(1, QtCore.Qt.Horizontal, "Usuario")
    self.model_user.setHeaderData(2, QtCore.Qt.Horizontal, "Senha")
    self.model_user.setHeaderData(3, QtCore.Qt.Horizontal, "Nome")
    self.model_user.setHeaderData(4, QtCore.Qt.Horizontal, "Cadastro")
    self.model_user.setHeaderData(5, QtCore.Qt.Horizontal, "Nivel")
    #tabela de dados
    self.ui.tabela_dados_usuarios.setModel(self.model_user)
    self.ui.tabela_dados_usuarios.setToolTip('Tabela da dados:\nPara adicionar itens sempre preencha todos os campos.\nCaso queira editar clique sobre o numero de uma linha e clique em atualizar.\nCaso queira deletar clique sobre o numero de uma linha e delete.')
    self.i_user = self.model_user.rowCount()


def addToDbUser(self):
    # chama a função de conexao e popula a tabela
    bancoDadosUsers(self)
    #print(self.i)
    if self.ui.input_username_user.text() == 'Nome Exibição' or self.ui.input_senha_user.text() == 'senha' or self.ui.input_nome_user.text() == 'user':
        QMessageBox.question(self, 'TCXS Project | Cadastro de Usuários', """Para cadastrar um usuário:
Informe o nome que será exibido na loja, usuario para login e senha para login.
Para editar um usuário:
Preencha todos os campos, clique sobre a linha que quer alterar e clique em atualizar. Somente via este programa é possivel a edição da data de cadastro do usuário, para isto basta alterar os dados na tabela e atualizar.
Para deletar um usuário:
Clique sobre a linha do usuário e depois clique em deletar.""", QMessageBox.Ok)
        self.show()
    else:
        self.hoje_user = datetime.now()
        self.data_formatada_user = self.hoje_user.strftime('%Y-%m-%d %H:%M:%S')
        #insere os dados na database
        self.model_user.insertRows(self.i_user, 1)
        self.model_user.setData(self.model_user.index(self.i_user, 1), self.ui.input_username_user.text())
        self.model_user.setData(self.model_user.index(self.i_user, 2), self.ui.input_senha_user.text())
        self.model_user.setData(self.model_user.index(self.i_user, 3), self.ui.input_nome_user.text())
        self.model_user.setData(self.model_user.index(self.i_user, 4), self.data_formatada_user)
        self.model_user.setData(self.model_user.index(self.i_user, 5), 'user')
        self.model_user.submitAll()
        self.i_user += 1
        QMessageBox.question(self, 'TCXS Project | AVISO!', """Dados inseridos, confira na tabela!""", QMessageBox.Ok)
        self.show()





def delrowUser(self):
    if self.ui.tabela_dados_usuarios.currentIndex().row() > -1:
        self.model_user.removeRow(self.ui.tabela_dados_usuarios.currentIndex().row())
        self.i_user -= 1
        self.model_user.select()
        QMessageBox.question(self, 'TCXS Project | AVISO!', """Dados deletados, confira na tabela!""", QMessageBox.Ok)
        self.show()
    else:
        QMessageBox.question(self,'Mensagem', "Selecione uma linha para deletar, clique sobre o numero a esquerda na tabela correspondente a linha.", QMessageBox.Ok)
        self.show()



def updaterowUser(self):
    self.hoje_user = datetime.now()
    self.data_formatada_user = self.hoje_user.strftime('%Y-%m-%d %H:%M:%S')
    if self.ui.tabela_dados_usuarios.currentIndex().row() > -1:
        record = self.model_user.record(self.ui.tabela_dados_usuarios.currentIndex().row())
        record.setValue("usuario",self.ui.input_username_user.text())
        record.setValue("senha",self.ui.input_senha_user.text())
        record.setValue("nome", self.ui.input_nome_user.text())
        record.setValue("cadastro", self.data_formatada_user)
        record.setValue("nivel", 'user')
        self.model_user.setRecord(self.ui.tabela_dados_usuarios.currentIndex().row(), record)
        QMessageBox.question(self, 'TCXS Project | AVISO!', """Dados atualizados, confira na tabela!""", QMessageBox.Ok)
        self.show()
    else:
        QMessageBox.question(self,'Mensagem', "Selecione uma linha para atualizar, clique sobre o numero a esquerda na tabela correspondente a linha.", QMessageBox.Ok)
        self.show()