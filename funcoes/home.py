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



def funcoesHome(self):
    exibeDadosMysql(self)
    # eventos para limpar os campos, que buscam funçoes no arquivo main
    self.ui.input_nome_database_home.mousePressEvent = self.limpaNomedb
    self.ui.input_nome_database_home.setToolTip('Insira o nome da Database Mysql')
    self.ui.input_user_database_home.mousePressEvent = self.limpaUserdb
    self.ui.input_user_database_home.setToolTip('Insira o usuário da Database Mysql')
    self.ui.input_senha_database_home.mousePressEvent = self.limpaSenhadb
    self.ui.input_senha_database_home.setToolTip('Insira a senha da Database Mysql')
    self.ui.input_host_database_home.mousePressEvent = self.limpaHostdb
    self.ui.input_host_database_home.setToolTip('Insira o hostname ou ip da Database Mysql')
    self.ui.input_endereco_ftp.mousePressEvent = self.limpaEnderecoFtp
    self.ui.input_endereco_ftp.setToolTip('Insira o endereço do Ftp')
    self.ui.input_user_ftp.mousePressEvent = self.limpaUserFtp
    self.ui.input_user_ftp.setToolTip('Insira o usuário do Ftp')
    self.ui.input_senha_ftp.mousePressEvent = self.limpaSenhaFtp
    self.ui.input_senha_ftp.setToolTip('Insira a senha do Ftp')
    self.ui.btn_database_home.clicked.connect(lambda: addDadosMysqlToDb(self))

    # CRIA A PASTA DE BACKUPS CASO ELA NÃO EXISTA OU TENHA SIDO DELETADA
    if not os.path.exists('images'):
        os.makedirs('images')

    #baixa a imagem watermark.png
    response = requests.get("https://ia801501.us.archive.org/24/items/prints_programa_tcxs/watermark.png")
    file = open("images/watermark.png", "wb")
    file.write(response.content)
    file.close()

    try:#VERIFICA A RESPOSTA DO SERVIR FTP ENVIANDO O COMANDO
        reposta_ftp = conexao.ftp.pwd()
    except:
        reposta_ftp = 0

    try:#exibe as mensagens caso não conectado aos sistemas ou caso seja o primeiro uso e nao tenha sido criado a database local
        # se ambos derem erro - ERRO MYSQL E FTP
        if conexao.retorno_conexao_mysql == conexao.db_mysql.lastError().text() and reposta_ftp == 0:
            QMessageBox.question(self, 'AVISO | ERRO DE CONEXÃO',"""Não conseguimos confirmar sua conexão com banco de dados Mysql, nem com o sistema de FTP. Insira os dados corretamente e tente novamente.""", QMessageBox.Ok)
            self.show()
        # se der ERRO MYSQL mas o FTP CONECTA
        elif conexao.retorno_conexao_mysql == conexao.db_mysql.lastError().text() and reposta_ftp != 0:
            QMessageBox.question(self, 'AVISO | ERRO DE CONEXÃO MYSQL', """Não conseguimos confirmar sua conexão com banco de dados Mysql, insira os dados corretamente e tente novamente.""", QMessageBox.Ok)
            self.show()
        #se a conexao ftp falhar e a mysql conectar avisa ERRO DE FTP
        elif reposta_ftp == 0 and conexao.retorno_conexao_mysql != conexao.db_mysql.lastError().text():
            QMessageBox.question(self, 'AVISO | ERRO DE CONEXÃO FTP',"""Não conseguimos confirmar sua conexão com o FTP, insira os dados corretamente e tente novamente.""",QMessageBox.Ok)
            self.show()
        elif conexao.retorno_conexao_mysql != conexao.db_mysql.lastError().text() and conexao.ftp.getwelcome() == '220 FTP Server ready.':
            QMessageBox.question(self, 'SUCESSO NA CONEXAO | ESTAMOS CONECTADOS',"""Nossa conexão com o sistema online foi um sucesso, podemos editar, porém tenha cautela, faça suas ações devagar para evitar erros e sempre confira se realmente as imagens foram por FTP.""", QMessageBox.Ok)
            self.show()
    except Exception as e:
        #se der erro é porque não existia o banco de dados local SqLite3 criado e nem os dados inseridos...
        QMessageBox.question(self, 'Bem vindo ao Painel de Administrador da TCXS Store',"""Insira os dados da Database MySql e os dados de FTP para iniciar o programa!

versão: 1.0
desenvolvedor: @GorpoOrko
linguagem: Python

1. Sobre a conexão com a Database MySql e sistema de FTP.
    1.1 Necessário os dados da database: database | usuário | senha | host.
    1.2 Necessário os dados sistema FTP: endereço | usuário | senha.
    1.3 Caso estes dados sejam inseridos não será feita conexão e não será possivel edição.
    1.4 Os dados são salvos em uma database local, sendo necessário inserir eles apenas uma vez.
    1.5 Caso os dados do servidor atualizem, atualize os dados no inicio do programa.
    1.6 Caso não conecte após atualizar os dados, feche e abra novamente o programa.

2. Sobre o cadastro de usuários e consulta:
    2.1 Necessário os dados: Nome | user | senha - [Permite] cadastrar | atualizar | deletar.
    2.2 Necessário user que o usuário faz login - [Permite] apenas consultas (clean tables).

3. Sobre o cadastro de jogos e extras:
    3.1 Necessário os dados: Titulo | Descrição | Content ID | Imagem | Link 
    3.2 [Permite] cadastrar | atualizar | deletar | upload imagem FTP(resize, borda automatica).
    3.3 [ATENÇÃO] na descrição usar a tag <br> para pular linhas conforme exemplo:
    3.4 [EXEMPLO] Idioma: Ingles<br>Legenda: Ingles<br>Plataforma: PlayStation3

4. Sobre o verificador da database:
    4.1 Verifica todos os bancos de dados a procura de erros, apenas visualização e conferência.

5. Sobre o verificador 404:
    5.1 Crawler que busca todos os erros 404 e os apresenta para que possam ser alterados na loja.
    5.2 Este processo é demorado e o programa deve estar sendo usado exclusivamente para ele.
    5.3 Como este processo verifica link por link demora e podem ocorrer travas ou falhas.
    5.4 Aconselho que links quebrados sejam arrumados para que não apareçam na proxima verificação.
    
6. Sobre o sistema de Backup:
    6.1 Este programa conta com um sistema automático de backup de toda loja.
    6.2 Para executar o backup basta apenas clicar no botão e aguardar.    
    6.3 Será criada uma pasta com nome "backupDb", seus arquivos estarão lá.
    6.4 Serão criados dois arquivos, um dump sql para upload no server e uma database SqLite3.
    6.5 Após salvar seu backup se quiser pode deletar a pasta "backupDb".    """, QMessageBox.Ok)
        QMessageBox.setStyleSheet("QLabel{min-width:900 px; font-size: 24px;} QPushButton{ width:250px; font-size: 18px; }")



def exibeDadosMysql(self):
    try:
        self.conexao = sqlite3.connect('database.db')
        self.conexao.row_factory = sqlite3.Row
        self.cursor = self.conexao.cursor()
        self.cursor.execute(""" SELECT * FROM dados_mysql; """)
        self.tabela = self.cursor.fetchall()
        self.databaseMysql = self.tabela[0][1]
        self.usuarioMysql = self.tabela[0][2]
        self.senhaMysql = self.tabela[0][3]
        self.hostMysql = self.tabela[0][4]
        self.enderecoFtp = self.tabela[0][5]
        self.userFtp = self.tabela[0][6]
        self.senhaFtp = self.tabela[0][7]
        self.ui.input_nome_database_home.setText(self.databaseMysql)
        self.ui.input_user_database_home.setText(self.usuarioMysql)
        self.ui.input_senha_database_home.setText(self.senhaMysql)
        self.ui.input_host_database_home.setText(self.hostMysql)
        self.ui.input_endereco_ftp.setText(self.enderecoFtp)
        self.ui.input_user_ftp.setText(self.userFtp)
        self.ui.input_senha_ftp.setText(self.senhaFtp)
        self.conexao.close()
    except:
        pass


def addDadosMysqlToDb(self):
    try:
        self.conexao = sqlite3.connect('database.db')
        self.cursor = self.conexao.cursor()
        self.cursor.execute("""DROP TABLE dados_mysql """)
        self.conexao.commit()
        self.conexao.close()
    except:
        pass
    self.conexao = sqlite3.connect('database.db')
    # self.conexao.row_factory = self.sqlite3.Row
    self.cursor = self.conexao.cursor()
    self.cursor.execute("""  CREATE TABLE IF NOT EXISTS dados_mysql  (id integer not null primary key autoincrement, 
    nome_database varchar(5000), user_database varchar(5000), senha_database varchar(5000), host_database varchar(
    500), endereco_ftp varchar(500), user_ftp varchar(500), senha_ftp varchar(500));  """)
    self.nome_database = self.ui.input_nome_database_home.text()
    self.user_database = self.ui.input_user_database_home.text()
    self.senha_database = self.ui.input_senha_database_home.text()
    self.host_database = self.ui.input_host_database_home.text()
    self.endereco_ftp = self.ui.input_endereco_ftp.text()
    self.user_ftp = self.ui.input_user_ftp.text()
    self.senha_ftp = self.ui.input_senha_ftp.text()
    self.cursor.execute(f""" INSERT INTO  dados_mysql ( nome_database, user_database, senha_database, host_database, 
endereco_ftp, user_ftp, senha_ftp) VALUES ( '{self.nome_database}', '{self.user_database}', '{self.senha_database}', 
'{self.host_database}', '{self.endereco_ftp}', '{self.user_ftp}', '{self.senha_ftp}')""")
    self.conexao.commit()
    self.conexao.close()
    self.ui.input_nome_database_home.setText('Nome database salvo')
    self.ui.input_user_database_home.setText('Usuário database salvo')
    self.ui.input_senha_database_home.setText('Senha database salva')
    self.ui.input_host_database_home.setText('Host database salvo')
    self.ui.input_endereco_ftp.setText('Endereço FTP Salvo')
    self.ui.input_user_ftp.setText('Usuário FTP salvo')
    self.ui.input_senha_ftp.setText('Senha FTP salva')

    #aviso:
    QMessageBox.question(self, 'TCXS Project | Cadastro de dados MySql FTP', f"""Bem vindo ao Programa de Administração da TCXS Project, obrigado por fornecer os dados necessários para uso do programa, confira as informações armazenadas, em caso de erros das informações as funções do programa não iráo funcionar, você terá certeza que inseriu as informações certas ao usar os menus e ver que ocorreu sua conexão com exito.

[Como usar após dados inseridos]
Após ter inserido os dados para conexão MySql e Ftp basta ir nos menus que você quer editar e clicar sobre os botões adicionar para ativar o sistema daquele menu e receber as instruções dele!

[Dados Mysql cadastrados]
    Nome database:    {self.nome_database}
    User database:    {self.user_database}
    Senha database:   {self.senha_database}
    Host database:    {self.host_database}

[Dados Ftp Cadastrados]
    Endereço Ftp:     {self.endereco_ftp}
    User Ftp:         {self.user_ftp}
    Senha Ftp:        {self.senha_ftp}

AVISO: O programa será reiniciado com os novos dados!
Quando o programa for reiniciado já pode ser usado os menus, seus dados ficarão salvos até que os altere novamente, somente use este campo quando for atualizar os dados do servidor no programa, caso ja tenah seus dados salvos apenas abra o programa e edite oque quiser. Vamos reiniciar o programa agora, por favor aguarde!
""",QMessageBox.Ok)
    self.show()


    #reinicia o programa caso salvo novos dados na database_Sqlite Local
    python = sys.executable
    os.execl(python, python, *sys.argv)
