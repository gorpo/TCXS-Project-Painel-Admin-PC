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


def backupDatabaseMysql(self):
    self.ui.btn_iniciar_backup.clicked.connect(lambda: backupdb(self))


def backupdb(self):

    QMessageBox.question(self, 'Backup Database TCXS Store', """Este sistema irá fazer o backup de toda Database de jogos e usuários!
O Backup será feito no formato de Banco de dados SqLite3, necessária conversão para dump.
O arquivo será salvo junto ao programa, verifique após conclusão do backup.
Aguarde até que todo processo acabe, para garantia de successo impossibilitaremos o uso do programa.
Ao terminar o backup uma mensagem será exibida.""", QMessageBox.Ok)
    self.show()

    # CONEXAO MYSQL
    cursor_pymysql = conexao.conexao_pymysql.cursor()
    # CONEXAO SQLITE
    conexao_sqlite = sqlite3.connect(f'{datetime.now().strftime("%d_%m_%Y_")}dump_MYSQL.db')
    cursor_sqlite = conexao_sqlite.cursor()
    cursor_pymysql.execute(f"SELECT * FROM playstation_users")
    cursor_sqlite.execute(
        """CREATE TABLE IF NOT EXISTS `playstation_users` ( id integer not null primary key autoincrement, `usuario` varchar(200) NOT NULL, `senha` varchar(329) NOT NULL, `nome` varchar(999) NOT NULL, `cadastro` datetime NOT NULL, `nivel` varchar(999)) """)
    conexao_sqlite.commit()
    tabela_users = cursor_pymysql.fetchall()
    conexao.conexao_pymysql.commit()
    contador_progress = 0
    self.ui.progressBar_backup_users.setMaximum(len(tabela_users))
    for dados_user in tabela_users:
        self.ui.progressBar_backup_users.setValue(contador_progress)
        contador_progress += 1
        try:
            usuario = dados_user['usuario']
            senha = dados_user['senha']
            nome = dados_user['nome']
            cadastro = datetime.fromisoformat(str(dados_user['cadastro']))
            nivel = dados_user['nivel']
            cursor_sqlite.execute(
                f"""INSERT INTO playstation_users ( `usuario`, `senha`, `nome`, `cadastro`,`nivel`) VALUES ('{usuario}','{senha}','{nome}','{cadastro}','{nivel}')""")
            conexao_sqlite.commit()
        except Exception as e:
            pass

    cursor_pymysql.execute(f"SELECT * FROM playstation_infos")
    cursor_sqlite.execute(
        """CREATE TABLE IF NOT EXISTS `playstation_infos` ( id integer not null primary key autoincrement, `informacao` varchar(999) NOT NULL) """)
    conexao_sqlite.commit()
    tabela_infos = cursor_pymysql.fetchall()
    conexao.conexao_pymysql.commit()
    contador_progress = 0
    self.ui.progressBar_backup_infos.setMaximum(len(tabela_infos))
    for dados_info in tabela_infos:
        self.ui.progressBar_backup_infos.setValue(contador_progress)
        contador_progress += 1
        try:
            info = dados_info['informacao']
            cursor_sqlite.execute(f"""INSERT INTO playstation_infos (`informacao`) VALUES ('{info}')""")
            conexao_sqlite.commit()
        except Exception as e:
            pass

    cursor_pymysql.execute(f"SELECT * FROM playstation_psp")
    cursor_sqlite.execute("""CREATE TABLE IF NOT EXISTS `playstation_psp` ( id integer not null primary key autoincrement,
     `titulo` varchar(999) NOT NULL, `descricao` varchar(999) NOT NULL, `content_id` varchar(999) NOT NULL,`imagem` varchar(999) NOT NULL, `cadastro` datetime NOT NULL, `link` varchar(999) NOT NULL) """)
    conexao_sqlite.commit()
    tabela_psp = cursor_pymysql.fetchall()
    conexao.conexao_pymysql.commit()
    contador_progress = 0
    self.ui.progressBar_backup_psp.setMaximum(len(tabela_psp))
    for dados_user in tabela_psp:
        self.ui.progressBar_backup_psp.setValue(contador_progress)
        contador_progress += 1
    for dados_user in tabela_psp:
        try:
            titulo = dados_user['titulo']
            descricao = dados_user['descricao']
            content_id = dados_user['content_id']
            imagem = dados_user['imagem']
            cadastro = datetime.fromisoformat(str(dados_user['cadastro']))
            link = dados_user['link']
            cursor_sqlite.execute(
                f"""INSERT INTO playstation_psp (titulo, descricao, content_id, imagem, cadastro, link) VALUES ('{titulo}','{descricao}','{content_id}','{imagem}','{cadastro}','{link}')""")
            conexao_sqlite.commit()
        except Exception as e:
            pass

    cursor_pymysql.execute(f"SELECT * FROM playstation_ps1")
    cursor_sqlite.execute("""CREATE TABLE IF NOT EXISTS `playstation_ps1` ( id integer not null primary key autoincrement,
     `titulo` varchar(999) NOT NULL, `descricao` varchar(999) NOT NULL, `content_id` varchar(999) NOT NULL,`imagem` varchar(999) NOT NULL, `cadastro` datetime NOT NULL, `link` varchar(999) NOT NULL) """)
    conexao_sqlite.commit()
    tabela_ps1 = cursor_pymysql.fetchall()
    conexao.conexao_pymysql.commit()
    contador_progress = 0
    self.ui.progressBar_backup_ps1.setMaximum(len(tabela_ps1))
    for dados_user in tabela_ps1:
        self.ui.progressBar_backup_ps1.setValue(contador_progress)
        contador_progress += 1
        try:
            titulo = dados_user['titulo']
            descricao = dados_user['descricao']
            content_id = dados_user['content_id']
            imagem = dados_user['imagem']
            cadastro = datetime.fromisoformat(str(dados_user['cadastro']))
            link = dados_user['link']
            cursor_sqlite.execute(
                f"""INSERT INTO playstation_ps1 (titulo, descricao, content_id, imagem, cadastro, link) VALUES ('{titulo}','{descricao}','{content_id}','{imagem}','{cadastro}','{link}')""")
            conexao_sqlite.commit()
        except Exception as e:
            pass

    cursor_pymysql.execute(f"SELECT * FROM playstation_ps2")
    cursor_sqlite.execute("""CREATE TABLE IF NOT EXISTS `playstation_ps2` ( id integer not null primary key autoincrement,
     `titulo` varchar(999) NOT NULL, `descricao` varchar(999) NOT NULL, `content_id` varchar(999) NOT NULL,`imagem` varchar(999) NOT NULL, `cadastro` datetime NOT NULL, `link` varchar(999) NOT NULL) """)
    conexao_sqlite.commit()
    tabela_ps2 = cursor_pymysql.fetchall()
    conexao.conexao_pymysql.commit()
    contador_progress = 0
    self.ui.progressBar_backup_ps2.setMaximum(len(tabela_ps2))
    for dados_user in tabela_ps2:
        self.ui.progressBar_backup_ps2.setValue(contador_progress)
        contador_progress += 1
        try:
            titulo = dados_user['titulo']
            descricao = dados_user['descricao']
            content_id = dados_user['content_id']
            imagem = dados_user['imagem']
            cadastro = datetime.fromisoformat(str(dados_user['cadastro']))
            link = dados_user['link']
            cursor_sqlite.execute(
                f"""INSERT INTO playstation_ps2 (titulo, descricao, content_id, imagem, cadastro, link) VALUES ('{titulo}','{descricao}','{content_id}','{imagem}','{cadastro}','{link}')""")
            conexao_sqlite.commit()
        except Exception as e:
            pass

    cursor_pymysql.execute(f"SELECT * FROM playstation_ps3")
    cursor_sqlite.execute("""CREATE TABLE IF NOT EXISTS `playstation_ps3` ( id integer not null primary key autoincrement,
         `titulo` varchar(999) NOT NULL, `descricao` varchar(999) NOT NULL, `content_id` varchar(999) NOT NULL,
         `imagem` varchar(999) NOT NULL, `cadastro` datetime NOT NULL,
          `link1` varchar(999) NOT NULL,`link2` varchar(999) NOT NULL,`link3` varchar(999) NOT NULL,`link4` varchar(999) NOT NULL,
          `link5` varchar(999) NOT NULL,`link6` varchar(999) NOT NULL,`link7` varchar(999) NOT NULL,`link8` varchar(999) NOT NULL,
          `link9` varchar(999) NOT NULL,`link10` varchar(999) NOT NULL,`link11` varchar(999) NOT NULL,`link12` varchar(999) NOT NULL,
          `link13` varchar(999) NOT NULL,`link14` varchar(999) NOT NULL,`link15` varchar(999) NOT NULL,`link16` varchar(999) NOT NULL,
          `link17` varchar(999) NOT NULL,`link18` varchar(999) NOT NULL,`link19` varchar(999) NOT NULL,`link20` varchar(999) NOT NULL,
          `link21` varchar(999) NOT NULL,`link22` varchar(999) NOT NULL,`link23` varchar(999) NOT NULL,`link24` varchar(999) NOT NULL,
          `link25` varchar(999) NOT NULL,`link26` varchar(999) NOT NULL,`link27` varchar(999) NOT NULL,`link28` varchar(999) NOT NULL,
          `link29` varchar(999) NOT NULL,`link30` varchar(999) NOT NULL) """)

    conexao_sqlite.commit()
    tabela_ps3 = cursor_pymysql.fetchall()
    conexao.conexao_pymysql.commit()
    contador_progress = 0
    self.ui.progressBar_backup_ps3.setMaximum(len(tabela_ps3))
    for dados_user in tabela_ps3:
        self.ui.progressBar_backup_ps3.setValue(contador_progress)
        contador_progress += 1
        try:
            titulo = dados_user['titulo']
            descricao = dados_user['descricao']
            content_id = dados_user['content_id']
            imagem = dados_user['imagem']
            cadastro = datetime.fromisoformat(str(dados_user['cadastro']))
            link1 = dados_user['link1']
            link2 = dados_user['link2']
            link3 = dados_user['link3']
            link4 = dados_user['link4']
            link5 = dados_user['link5']
            link6 = dados_user['link6']
            link7 = dados_user['link7']
            link8 = dados_user['link8']
            link9 = dados_user['link9']
            link10 = dados_user['link10']
            link11 = dados_user['link11']
            link12 = dados_user['link12']
            link13 = dados_user['link13']
            link14 = dados_user['link14']
            link15 = dados_user['link15']
            link16 = dados_user['link16']
            link17 = dados_user['link17']
            link18 = dados_user['link18']
            link19 = dados_user['link19']
            link20 = dados_user['link20']
            link21 = dados_user['link21']
            link22 = dados_user['link22']
            link23 = dados_user['link23']
            link24 = dados_user['link24']
            link25 = dados_user['link25']
            link26 = dados_user['link26']
            link27 = dados_user['link27']
            link28 = dados_user['link28']
            link29 = dados_user['link29']
            link30 = dados_user['link30']

            cursor_sqlite.execute(f"""INSERT INTO playstation_ps3 (titulo, descricao, content_id, imagem, cadastro,
        link1,link2,link3,link4,link5,link6,link7,link8,link9,link10,link11,link12,link13,link14,link15,
        link16,link17,link18,link19,link20,link21,link22,link23,link24,link25,link26,link27,link28,link29,link30) VALUES ('{titulo}','{descricao}','{content_id}','{imagem}','{cadastro}',
        '{link1}','{link2}','{link3}','{link4}','{link5}','{link6}','{link7}','{link8}','{link9}','{link10}','{link11}','{link12}','{link13}',
        '{link14}','{link15}','{link16}','{link17}','{link18}','{link19}','{link20}','{link21}','{link22}','{link23}','{link24}','{link25}',
        '{link26}','{link27}','{link28}','{link29}','{link30}')""")
            conexao_sqlite.commit()
        except Exception as e:
            pass


    cursor_pymysql.execute(f"SELECT * FROM playstation_emuladores")
    cursor_sqlite.execute("""CREATE TABLE IF NOT EXISTS `playstation_emuladores` ( id integer not null primary key autoincrement,
     `titulo` varchar(999) NOT NULL, `descricao` varchar(999) NOT NULL, `content_id` varchar(999) NOT NULL,`imagem` varchar(999) NOT NULL, `cadastro` datetime NOT NULL, `link` varchar(999) NOT NULL) """)
    conexao_sqlite.commit()
    tabela_emuladores = cursor_pymysql.fetchall()
    conexao.conexao_pymysql.commit()
    contador_progress = 0
    self.ui.progressBar_backup_emuladores.setMaximum(len(tabela_emuladores))
    for dados_user in tabela_emuladores:
        self.ui.progressBar_backup_emuladores.setValue(contador_progress)
        contador_progress += 1
        try:
            titulo = dados_user['titulo']
            descricao = dados_user['descricao']
            content_id = dados_user['content_id']
            imagem = dados_user['imagem']
            cadastro = datetime.fromisoformat(str(dados_user['cadastro']))
            link = dados_user['link']
            cursor_sqlite.execute(
                f"""INSERT INTO playstation_emuladores (titulo, descricao, content_id, imagem, cadastro, link) VALUES ('{titulo}','{descricao}','{content_id}','{imagem}','{cadastro}','{link}')""")
            conexao_sqlite.commit()
        except Exception as e:
            pass

    cursor_pymysql.execute(f"SELECT * FROM playstation_extras")
    cursor_sqlite.execute("""CREATE TABLE IF NOT EXISTS `playstation_extras` ( id integer not null primary key autoincrement,
     `titulo` varchar(999) NOT NULL, `descricao` varchar(999) NOT NULL, `content_id` varchar(999) NOT NULL,`imagem` varchar(999) NOT NULL, `cadastro` datetime NOT NULL, `link` varchar(999) NOT NULL) """)
    conexao_sqlite.commit()
    tabela_extras = cursor_pymysql.fetchall()
    conexao.conexao_pymysql.commit()
    contador_progress = 0
    self.ui.progressBar_backup_extras.setMaximum(len(tabela_extras))
    for dados_user in tabela_extras:
        self.ui.progressBar_backup_extras.setValue(contador_progress)
        contador_progress += 1
        try:
            titulo = dados_user['titulo']
            descricao = dados_user['descricao']
            content_id = dados_user['content_id']
            imagem = dados_user['imagem']
            cadastro = datetime.fromisoformat(str(dados_user['cadastro']))
            link = dados_user['link']
            cursor_sqlite.execute(
                f"""INSERT INTO playstation_extras (titulo, descricao, content_id, imagem, cadastro, link) VALUES ('{titulo}','{descricao}','{content_id}','{imagem}','{cadastro}','{link}')""")
            conexao_sqlite.commit()
        except Exception as e:
            pass
    #mensagem final de confirmação do backup
    QMessageBox.question(self, 'Backup Database TCXS Store', f"""Backup concluido com sucesso.\n Seu arquivo foi salvo com o nome: {datetime.now().strftime("%d_%m_%Y_")}dump_MYSQL.db""", QMessageBox.Ok)
    #abre a pasta
    os.startfile(os.path.realpath(''))