#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ███╗   ███╗ █████╗ ███╗   ██╗██╗ ██████╗ ██████╗ ███╗   ███╗██╗ ██████╗
# ████╗ ████║██╔══██╗████╗  ██║██║██╔════╝██╔═══██╗████╗ ████║██║██╔═══██╗
# ██╔████╔██║███████║██╔██╗ ██║██║██║     ██║   ██║██╔████╔██║██║██║   ██║
# ██║╚██╔╝██║██╔══██║██║╚██╗██║██║██║     ██║   ██║██║╚██╔╝██║██║██║   ██║
# ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║╚██████╗╚██████╔╝██║ ╚═╝ ██║██║╚██████╔╝
# ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝
#            @GorpoOrko | Manicomio TCXS Project | 2020

from TCXSProject import *


def backupDatabaseMysql(self):
    self.ui.btn_iniciar_backup.clicked.connect(lambda: backupdb(self))


def backupdb(self):

    QMessageBox.question(self, 'Backup Database TCXS Store', """Este sistema irá fazer o backup de toda Database de jogos e usuários!
O Backup será feito no formato de Banco de dados SqLite3, necessária conversão para dump.
Será feito um backup no formato de Dump Mysql para upload no servidor.
Será criada uma pasta com nome "backupDb", verifique-a após conclusão do backup.
Aguarde até que todo processo acabe, para garantia de successo impossibilitaremos o uso do programa.
Ao terminar o backup uma mensagem será exibida.""", QMessageBox.Ok)
    self.show()

    #CRIA A PASTA DE BACKUPS CASO ELA NÃO EXISTA OU TENHA SIDO DELETADA
    if not os.path.exists('backupDb'):
        os.makedirs('backupDb')

    # CONEXAO MYSQL
    cursor_pymysql = conexao.conexao_pymysql.cursor()
    # CRIA O BACKUP EM SQLITE E DUMP MYSQL--->
    conexao_sqlite = sqlite3.connect(f'backupDb/{datetime.now().strftime("%d_%m_%Y_%Y-%H_%M")}dump_SQLITE3.db')
    cursor_sqlite = conexao_sqlite.cursor()
    dump_mysql = open(f'backupDb/{datetime.now().strftime("%d_%m_%Y-%H_%M")}dump_MYSQL.sql','a')
    texto1psp_mysql = f"""-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Dev: @GorpoOrko
-- Site: httpd://tcxsproject.com.br
-- Github: https://github.com/gorpo
-- Este dump faz parte do sistema para PlayStation3 da TCXS Project Web Store PHP Mysql
-- Versão do servidor: 10.4.6-MariaDB
-- versão do PHP: 7.3.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `tcxs_store`
--

-- --------------------------------------------------------
"""
    dump_mysql.write(texto1psp_mysql)


    #SISTEMA DE BACKUP DA TABELA PLAYSTATION USERS
    #sqlite3
    cursor_pymysql.execute(f"SELECT * FROM playstation_users")
    cursor_sqlite.execute( """CREATE TABLE IF NOT EXISTS `playstation_users` ( id integer not null primary key autoincrement, `usuario` varchar(200) NOT NULL, `senha` varchar(329) NOT NULL, `nome` varchar(999) NOT NULL, `cadastro` datetime NOT NULL, `nivel` varchar(999)) """)
    conexao_sqlite.commit()
    #mysql
    texto2users_mysql = """-- --------------------------------------------------------

--
-- Estrutura da tabela `playstation_users`
--

CREATE TABLE `playstation_users` (
  `id` mediumint(9) NOT NULL,
  `usuario` varchar(200) NOT NULL,
  `senha` varchar(329) NOT NULL,
  `nome` varchar(999) NOT NULL,
  `cadastro` datetime NOT NULL,
  `nivel` varchar(999) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `playstation_users`
--

INSERT INTO `playstation_users` (`id`, `usuario`, `senha`, `nome`, `cadastro`, `nivel`) VALUES\n"""
    dump_mysql.write(texto2users_mysql)

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
            #sqlite3
            cursor_sqlite.execute(f"""INSERT INTO playstation_users ( `usuario`, `senha`, `nome`, `cadastro`,`nivel`) VALUES ('{usuario}','{senha}','{nome}','{cadastro}','{nivel}')""")
            conexao_sqlite.commit()

        except Exception as e:
            pass
        if contador_progress != len(tabela_users):
            texto3users_mysql = f"""('{contador_progress+2}','{usuario}','{senha}','{nome}','{cadastro}','{nivel}'),\n"""
            dump_mysql.write(texto3users_mysql)
        if contador_progress == len(tabela_users):
            texto3users_mysql = f"""('{contador_progress+2}','{usuario}','{senha}','{nome}','{cadastro}','{nivel}');"""
            dump_mysql.write(texto3users_mysql)

    cursor_pymysql.execute(f"SELECT * FROM playstation_infos")
    cursor_sqlite.execute(   """CREATE TABLE IF NOT EXISTS `playstation_infos` ( id integer not null primary key autoincrement, `informacao` varchar(999) NOT NULL) """)
    conexao_sqlite.commit()
    texto1infos_mysql = f"""-- --------------------------------------------------------

--
-- Estrutura da tabela `playstation_infos`
--

CREATE TABLE `playstation_infos` (
  `id` mediumint(9) NOT NULL,
  `informacao` varchar(999) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `playstation_infos`
--

INSERT INTO `playstation_infos` (`id`, `informacao`) VALUES\n"""
    dump_mysql.write(texto1infos_mysql)
    tabela_infos = cursor_pymysql.fetchall()
    conexao.conexao_pymysql.commit()
    contador_progress = 0
    self.ui.progressBar_backup_infos.setMaximum(len(tabela_infos))
    for dados_info in tabela_infos:
        self.ui.progressBar_backup_infos.setValue(contador_progress)
        contador_progress += 1
        try:
            info = dados_info['informacao']
            #sqlite
            cursor_sqlite.execute(f"""INSERT INTO playstation_infos (`informacao`) VALUES ('{info}')""")
            conexao_sqlite.commit()
        except Exception as e:
            pass
        # mysql
        if contador_progress != len(tabela_infos):
            texto3infos_mysql = f"""('{contador_progress + 2}','{info}'),\n"""
            dump_mysql.write(texto3infos_mysql)
        if contador_progress == len(tabela_infos):
            texto3infos_mysql = f"""('{contador_progress + 2}','{info}');"""
            dump_mysql.write(texto3infos_mysql)

    cursor_pymysql.execute(f"SELECT * FROM playstation_psp")
    cursor_sqlite.execute("""CREATE TABLE IF NOT EXISTS `playstation_psp` ( id integer not null primary key autoincrement,
     `titulo` varchar(999) NOT NULL, `descricao` varchar(999) NOT NULL, `content_id` varchar(999) NOT NULL,`imagem` varchar(999) NOT NULL, `cadastro` datetime NOT NULL, `link` varchar(999) NOT NULL) """)
    conexao_sqlite.commit()
    tabela_psp = cursor_pymysql.fetchall()
    conexao.conexao_pymysql.commit()
    texto1psp_mysql = """-- --------------------------------------------------------

--
-- Estrutura da tabela `playstation_psp`
--

CREATE TABLE `playstation_psp` (
  `id` int(255) NOT NULL,
  `titulo` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `descricao` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `content_id` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `imagem` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `cadastro` datetime NOT NULL,
  `link` mediumtext COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Extraindo dados da tabela `playstation_psp`
--

INSERT INTO `playstation_psp` (`id`, `titulo`, `descricao`, `content_id`, `imagem`, `cadastro`, `link`) VALUES\n"""
    dump_mysql.write(texto1psp_mysql)

    contador_progress = 0
    self.ui.progressBar_backup_psp.setMaximum(len(tabela_psp))
    for dados_user in tabela_psp:
        self.ui.progressBar_backup_psp.setValue(contador_progress)
        contador_progress += 1
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
        # mysql
        if contador_progress != len(tabela_psp):
            texto2psp_mysql = f"""('{contador_progress+2}','{titulo}','{descricao}','{content_id}','{imagem}','{cadastro}','{link}'),\n"""
            dump_mysql.write(texto2psp_mysql)
        if contador_progress == len(tabela_psp):
            texto2psp_mysql = f"""('{contador_progress+2}','{titulo}','{descricao}','{content_id}','{imagem}','{cadastro}','{link}');"""
            dump_mysql.write(texto2psp_mysql)


    #PLAYSTATION1
    cursor_pymysql.execute(f"SELECT * FROM playstation_ps1")
    cursor_sqlite.execute("""CREATE TABLE IF NOT EXISTS `playstation_ps1` ( id integer not null primary key autoincrement,
     `titulo` varchar(999) NOT NULL, `descricao` varchar(999) NOT NULL, `content_id` varchar(999) NOT NULL,`imagem` varchar(999) NOT NULL, `cadastro` datetime NOT NULL, `link` varchar(999) NOT NULL) """)
    conexao_sqlite.commit()
    texto1ps1_mysql = """-- --------------------------------------------------------

--
-- Estrutura da tabela `playstation_ps1`
--

CREATE TABLE `playstation_ps1` (
  `id` int(255) UNSIGNED NOT NULL,
  `titulo` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `descricao` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `content_id` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `imagem` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `cadastro` datetime NOT NULL,
  `link` mediumtext COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Extraindo dados da tabela `playstation_ps1`
--

INSERT INTO `playstation_ps1` (`id`, `titulo`, `descricao`, `content_id`, `imagem`, `cadastro`, `link`) VALUES\n"""
    dump_mysql.write(texto1ps1_mysql)
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
        # mysql
        if contador_progress != len(tabela_ps1):
            texto2ps1_mysql = f"""('{contador_progress+2}','{titulo}','{descricao}','{content_id}','{imagem}','{cadastro}','{link}'),\n"""
            dump_mysql.write(texto2ps1_mysql)
        if contador_progress == len(tabela_ps1):
            texto2ps1_mysql = f"""('{contador_progress+2}','{titulo}','{descricao}','{content_id}','{imagem}','{cadastro}','{link}');"""
            dump_mysql.write(texto2ps1_mysql)

    cursor_pymysql.execute(f"SELECT * FROM playstation_ps2")
    cursor_sqlite.execute("""CREATE TABLE IF NOT EXISTS `playstation_ps2` ( id integer not null primary key autoincrement,
     `titulo` varchar(999) NOT NULL, `descricao` varchar(999) NOT NULL, `content_id` varchar(999) NOT NULL,`imagem` varchar(999) NOT NULL, `cadastro` datetime NOT NULL, `link` varchar(999) NOT NULL) """)
    conexao_sqlite.commit()
    tabela_ps2 = cursor_pymysql.fetchall()
    conexao.conexao_pymysql.commit()
    texto1ps2_mysql = """-- --------------------------------------------------------

--
-- Estrutura da tabela `playstation_ps2`
--

CREATE TABLE `playstation_ps2` (
  `id` int(255) UNSIGNED NOT NULL,
  `titulo` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `descricao` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `content_id` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `imagem` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `cadastro` datetime NOT NULL,
  `link` mediumtext COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Extraindo dados da tabela `playstation_ps2`
--

INSERT INTO `playstation_ps2` (`id`, `titulo`, `descricao`, `content_id`, `imagem`, `cadastro`, `link`) VALUES\n"""
    dump_mysql.write(texto1ps2_mysql)
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
        # mysql
        if contador_progress != len(tabela_ps2):
            texto2ps2_mysql = f"""('{contador_progress+2}','{titulo}','{descricao}','{content_id}','{imagem}','{cadastro}','{link}'),\n"""
            dump_mysql.write(texto2ps2_mysql)
        if contador_progress == len(tabela_ps2):
            texto2ps2_mysql = f"""('{contador_progress+2}','{titulo}','{descricao}','{content_id}','{imagem}','{cadastro}','{link}');"""
            dump_mysql.write(texto2ps2_mysql)


#ps3----------------------------------------------------------------------------------------------------------------------------
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
    texto1ps3_mysql = """-- --------------------------------------------------------

--
-- Estrutura da tabela `playstation_ps3`
--

CREATE TABLE `playstation_ps3` (
  `id` int(255) UNSIGNED NOT NULL,
  `titulo` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `descricao` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `content_id` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `imagem` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `cadastro` datetime NOT NULL,
  `link1` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link2` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link3` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link4` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link5` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link6` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link7` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link8` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link9` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link10` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link11` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link12` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link13` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link14` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link15` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link16` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link17` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link18` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link19` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link20` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link21` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link22` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link23` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link24` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link25` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link26` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link27` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link28` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link29` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link30` mediumtext COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Extraindo dados da tabela `playstation_ps3`
--

INSERT INTO `playstation_ps3` (`id`, `titulo`, `descricao`, `content_id`, `imagem`, `cadastro`, `link1`, `link2`, `link3`, `link4`, `link5`, `link6`, `link7`, `link8`, `link9`, `link10`, `link11`, `link12`, `link13`, `link14`, `link15`, `link16`, `link17`, `link18`, `link19`, `link20`, `link21`, `link22`, `link23`, `link24`, `link25`, `link26`, `link27`, `link28`, `link29`, `link30`) VALUES\n"""
    dump_mysql.write(texto1ps3_mysql)
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
        if contador_progress != len(tabela_ps3):
            texto2ps3_mysql = f"""('{contador_progress+2}','{titulo}','{descricao}','{content_id}','{imagem}','{cadastro}',
    '{link1}','{link2}','{link3}','{link4}','{link5}','{link6}','{link7}','{link8}','{link9}','{link10}','{link11}','{link12}','{link13}',
    '{link14}','{link15}','{link16}','{link17}','{link18}','{link19}','{link20}','{link21}','{link22}','{link23}','{link24}','{link25}',
    '{link26}','{link27}','{link28}','{link29}','{link30}'),\n"""
            dump_mysql.write(texto2ps3_mysql)
        if contador_progress == len(tabela_ps3):
            texto2ps3_mysql = f"""('{contador_progress+2}','{titulo}','{descricao}','{content_id}','{imagem}','{cadastro}',
    '{link1}','{link2}','{link3}','{link4}','{link5}','{link6}','{link7}','{link8}','{link9}','{link10}','{link11}','{link12}','{link13}',
    '{link14}','{link15}','{link16}','{link17}','{link18}','{link19}','{link20}','{link21}','{link22}','{link23}','{link24}','{link25}',
    '{link26}','{link27}','{link28}','{link29}','{link30}');"""
            dump_mysql.write(texto2ps3_mysql)



    #emuladores------------------------------------------------>
    cursor_pymysql.execute(f"SELECT * FROM playstation_emuladores")
    cursor_sqlite.execute("""CREATE TABLE IF NOT EXISTS `playstation_emuladores` ( id integer not null primary key autoincrement,
     `titulo` varchar(999) NOT NULL, `descricao` varchar(999) NOT NULL, `content_id` varchar(999) NOT NULL,`imagem` varchar(999) NOT NULL, `cadastro` datetime NOT NULL, `link` varchar(999) NOT NULL) """)
    conexao_sqlite.commit()
    texto1psemu_mysql = """-- --------------------------------------------------------

--
-- Estrutura da tabela `playstation_emuladores`
--

CREATE TABLE `playstation_emuladores` (
  `id` int(255) UNSIGNED NOT NULL,
  `titulo` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `descricao` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `content_id` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `imagem` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `cadastro` datetime NOT NULL,
  `link` mediumtext COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Extraindo dados da tabela `playstation_emuladores`
--

INSERT INTO `playstation_emuladores` (`id`, `titulo`, `descricao`, `content_id`, `imagem`, `cadastro`, `link`) VALUES\n"""
    dump_mysql.write(texto1psemu_mysql)

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
        if contador_progress != len(tabela_emuladores):
            texto2psemu_mysql = f"""('{contador_progress+2}','{titulo}','{descricao}','{content_id}','{imagem}','{cadastro}','{link}'),\n"""
            dump_mysql.write(texto2psemu_mysql)
        if contador_progress == len(tabela_emuladores):
            texto2psemu_mysql = f"""('{contador_progress+2}','{titulo}','{descricao}','{content_id}','{imagem}','{cadastro}','{link}');"""
            dump_mysql.write(texto2psemu_mysql)


    cursor_pymysql.execute(f"SELECT * FROM playstation_extras")
    cursor_sqlite.execute("""CREATE TABLE IF NOT EXISTS `playstation_extras` ( id integer not null primary key autoincrement,
     `titulo` varchar(999) NOT NULL, `descricao` varchar(999) NOT NULL, `content_id` varchar(999) NOT NULL,`imagem` varchar(999) NOT NULL, `cadastro` datetime NOT NULL, `link` varchar(999) NOT NULL) """)
    conexao_sqlite.commit()
    texto1psex_mysql = """-- --------------------------------------------------------

--
-- Estrutura da tabela `playstation_extras`
--

CREATE TABLE `playstation_extras` (
  `id` int(255) UNSIGNED NOT NULL,
  `titulo` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `descricao` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `content_id` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `imagem` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `cadastro` datetime NOT NULL,
  `link` mediumtext COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Extraindo dados da tabela `playstation_extras`
--

INSERT INTO `playstation_extras` (`id`, `titulo`, `descricao`, `content_id`, `imagem`, `cadastro`, `link`) VALUES\n"""
    dump_mysql.write(texto1psex_mysql)
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
        if contador_progress != len(tabela_extras):
            texto2psex_mysql = f"""('{contador_progress+2}','{titulo}','{descricao}','{content_id}','{imagem}','{cadastro}','{link}'),\n"""
        if contador_progress == len(tabela_extras):
            texto2psex_mysql = f"""('{contador_progress+2}','{titulo}','{descricao}','{content_id}','{imagem}','{cadastro}','{link}');"""
        dump_mysql.write(texto2psex_mysql)

    #texto final para ser escrito no dump mysql informando as ids que devem começar as tabelas:

    texto_final_mysql = """--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `playstation_emuladores`
--
ALTER TABLE `playstation_emuladores`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `playstation_extras`
--
ALTER TABLE `playstation_extras`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `playstation_infos`
--
ALTER TABLE `playstation_infos`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `playstation_ps1`
--
ALTER TABLE `playstation_ps1`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `playstation_ps2`
--
ALTER TABLE `playstation_ps2`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `playstation_ps3`
--
ALTER TABLE `playstation_ps3`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `playstation_psp`
--
ALTER TABLE `playstation_psp`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `playstation_users`
--
ALTER TABLE `playstation_users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `playstation_emuladores`
--
ALTER TABLE `playstation_emuladores`
  MODIFY `id` int(255) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

--
-- AUTO_INCREMENT de tabela `playstation_extras`
--
ALTER TABLE `playstation_extras`
  MODIFY `id` int(255) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

--
-- AUTO_INCREMENT de tabela `playstation_infos`
--
ALTER TABLE `playstation_infos`
  MODIFY `id` mediumint(9) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

--
-- AUTO_INCREMENT de tabela `playstation_ps1`
--
ALTER TABLE `playstation_ps1`
  MODIFY `id` int(255) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

--
-- AUTO_INCREMENT de tabela `playstation_ps2`
--
ALTER TABLE `playstation_ps2`
  MODIFY `id` int(255) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

--
-- AUTO_INCREMENT de tabela `playstation_ps3`
--
ALTER TABLE `playstation_ps3`
  MODIFY `id` int(255) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

--
-- AUTO_INCREMENT de tabela `playstation_psp`
--
ALTER TABLE `playstation_psp`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

--
-- AUTO_INCREMENT de tabela `playstation_users`
--
ALTER TABLE `playstation_users`
  MODIFY `id` mediumint(9) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
"""
    dump_mysql.write(texto_final_mysql)

    #mensagem final de confirmação do backup
    QMessageBox.question(self, 'Backup Database TCXS Store', f"""Backup concluido com sucesso.\n Seu arquivo foi salvo com o nome: {datetime.now().strftime("%d_%m_%Y_")}dump_MYSQL.db""", QMessageBox.Ok)
    #abre a pasta
    os.startfile(os.path.realpath('backupDb'))