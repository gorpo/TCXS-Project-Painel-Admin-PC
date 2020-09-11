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

def verificar404(self):
    self.ui.comboBox_verifica404.currentIndexChanged.connect(lambda: selecionaVerifica404(self))


def selecionaVerifica404(self):
    #armazena o valor retornado pela ComboBox
    self.verifica404_selecionada = self.ui.comboBox_verifica404.currentText()

    # verificaPSP
    if self.verifica404_selecionada == 'playstation_psp':
        self.ui.textBrowser_verifica404.append(f"<h3 style='color: rgb(170,0,0);'>VERIFICAÇÃO PSP INICIADA</h3>")
        query = QSqlQuery(conexao.db_mysql)
        model = QtSql.QSqlTableModel()
        query.exec(f"""SELECT * FROM playstation_psp""")
        contador_progress = 0
        contador_erros = 0
        self.ui.progressBar404.setMaximum(query.size())
        while query.next():
            self.ui.progressBar404.setValue(contador_progress)
            contador_progress += 1
            titulo = query.value(1)
            data = query.value(5).toPyDateTime().strftime('%d/%m/%Y')
            link = query.value(6)
            try:#faz tras a pagina do Dropbox com requests | print(titulo, pagina.status_code)
                pagina = requests.get(link.replace('=1', '=0'))
                # passa a pagina para o BeautifulSoup verificar o texto no titulo <title>Dropbox - Error</title>
                soup = BeautifulSoup(pagina.text, 'html.parser')
                erro404 = soup.find_all('title')[0]
                if str(erro404) == '<title>Dropbox - Error</title>':
                    texto_html = f""" <h3 style='color: #fff;'>Jogo: {titulo} | Cadastro: {data} | Erro: 404</h3>"""
                    link_html = f"""<a style='color: #fff;' href='{link}'>Link: {link}</a> """
                    self.ui.textBrowser_verifica404.append(texto_html)
                    self.ui.textBrowser_verifica404.append(link_html)
                    contador_erros += 1
            except Exception as e:
                pass
        #fim do loop testando os links da database | exibe o aviso final
        self.ui.textBrowser_verifica404.append(f"<h2 style='color: rgb(170,0,0);'>TOTAL DE ERROS: {contador_erros}</h2>")
        self.ui.textBrowser_verifica404.append(f"<h2 style='color: rgb(170,0,0);'>TODOS LINKS DE PSP FORAM VERIFICADOS</h2>")


    # verificaPS1
    if self.verifica404_selecionada == 'playstation_ps1':
        self.ui.textBrowser_verifica404.append(f"<h3 style='color: rgb(170,0,0);'>VERIFICAÇÃO PS1 INICIADA</h3>")
        query = QSqlQuery(conexao.db_mysql)
        model = QtSql.QSqlTableModel()
        query.exec(f"""SELECT * FROM playstation_ps1""")
        contador_progress = 0
        contador_erros = 0
        self.ui.progressBar404.setMaximum(query.size())
        while query.next():
            self.ui.progressBar404.setValue(contador_progress)
            contador_progress += 1
            titulo = query.value(1)
            data = query.value(5).toPyDateTime().strftime('%d/%m/%Y')
            link = query.value(6)
            try:#faz tras a pagina do Dropbox com requests | print(titulo, pagina.status_code)
                pagina = requests.get(link.replace('=1', '=0'))
                # passa a pagina para o BeautifulSoup verificar o texto no titulo <title>Dropbox - Error</title>
                soup = BeautifulSoup(pagina.text, 'html.parser')
                erro404 = soup.find_all('title')[0]
                if str(erro404) == '<title>Dropbox - Error</title>':
                    texto_html = f""" <h3 style='color: #fff;'>Jogo: {titulo} | Cadastro: {data} | Erro: 404</h3>"""
                    link_html = f"""<a style='color: #fff;' href='{link}'>Link: {link}</a> """
                    self.ui.textBrowser_verifica404.append(texto_html)
                    self.ui.textBrowser_verifica404.append(link_html)
                    contador_erros += 1
            except Exception as e:
                pass
        #fim do loop testando os links da database | exibe o aviso final
        self.ui.textBrowser_verifica404.append(f"<h2 style='color: rgb(170,0,0);'>TOTAL DE ERROS: {contador_erros}</h2>")
        self.ui.textBrowser_verifica404.append(f"<h2 style='color: rgb(170,0,0);'>TODOS LINKS DE PS1 FORAM VERIFICADOS</h2>")

    # verificaPS2
    if self.verifica404_selecionada == 'playstation_ps2':
        self.ui.textBrowser_verifica404.append(f"<h3 style='color: rgb(170,0,0);'>VERIFICAÇÃO PS2 INICIADA</h3>")
        query = QSqlQuery(conexao.db_mysql)
        model = QtSql.QSqlTableModel()
        query.exec(f"""SELECT * FROM playstation_ps2""")
        contador_progress = 0
        contador_erros = 0
        self.ui.progressBar404.setMaximum(query.size())
        while query.next():
            self.ui.progressBar404.setValue(contador_progress)
            contador_progress += 1
            titulo = query.value(1)
            data = query.value(5).toPyDateTime().strftime('%d/%m/%Y')
            link = query.value(6)
            try:#faz tras a pagina do Dropbox com requests | print(titulo, pagina.status_code)
                pagina = requests.get(link.replace('=1', '=0'))
                # passa a pagina para o BeautifulSoup verificar o texto no titulo <title>Dropbox - Error</title>
                soup = BeautifulSoup(pagina.text, 'html.parser')
                erro404 = soup.find_all('title')[0]
                if str(erro404) == '<title>Dropbox - Error</title>':
                    texto_html = f""" <h3 style='color: #fff;'>Jogo: {titulo} | Cadastro: {data} | Erro: 404</h3>"""
                    link_html = f"""<a style='color: #fff;' href='{link}'>Link: {link}</a> """
                    self.ui.textBrowser_verifica404.append(texto_html)
                    self.ui.textBrowser_verifica404.append(link_html)
                    contador_erros += 1
            except Exception as e:
                pass
        #fim do loop testando os links da database | exibe o aviso final
        self.ui.textBrowser_verifica404.append(f"<h2 style='color: rgb(170,0,0);'>TOTAL DE ERROS: {contador_erros}</h2>")
        self.ui.textBrowser_verifica404.append(f"<h2 style='color: rgb(170,0,0);'>TODOS LINKS DE PS2 FORAM VERIFICADOS</h2>")

    # verificaEMULADORES(RETRO)
    if self.verifica404_selecionada == 'playstation_emuladores':
        self.ui.textBrowser_verifica404.append(f"<h3 style='color: rgb(170,0,0);'>VERIFICAÇÃO EMULADORES INICIADA</h3>")
        query = QSqlQuery(conexao.db_mysql)
        model = QtSql.QSqlTableModel()
        query.exec(f"""SELECT * FROM playstation_emuladores""")
        contador_progress = 0
        contador_erros = 0
        self.ui.progressBar404.setMaximum(query.size())
        while query.next():
            self.ui.progressBar404.setValue(contador_progress)
            contador_progress += 1
            titulo = query.value(1)
            data = query.value(5).toPyDateTime().strftime('%d/%m/%Y')
            link = query.value(6)
            try:#faz tras a pagina do Dropbox com requests | print(titulo, pagina.status_code)
                pagina = requests.get(link.replace('=1', '=0'))
                # passa a pagina para o BeautifulSoup verificar o texto no titulo <title>Dropbox - Error</title>
                soup = BeautifulSoup(pagina.text, 'html.parser')
                erro404 = soup.find_all('title')[0]
                if str(erro404) == '<title>Dropbox - Error</title>':
                    texto_html = f""" <h3 style='color: #fff;'>Jogo: {titulo} | Cadastro: {data} | Erro: 404</h3>"""
                    link_html = f"""<a style='color: #fff;' href='{link}'>Link: {link}</a> """
                    self.ui.textBrowser_verifica404.append(texto_html)
                    self.ui.textBrowser_verifica404.append(link_html)
                    contador_erros += 1
            except Exception as e:
                pass
        #fim do loop testando os links da database | exibe o aviso final
        self.ui.textBrowser_verifica404.append(f"<h2 style='color: rgb(170,0,0);'>TOTAL DE ERROS: {contador_erros}</h2>")
        self.ui.textBrowser_verifica404.append(f"<h2 style='color: rgb(170,0,0);'>TODOS LINKS DE EMULADORES FORAM VERIFICADOS</h2>")

    # verificaEXTRAS
    if self.verifica404_selecionada == 'playstation_extras':
        self.ui.textBrowser_verifica404.append(f"<h3 style='color: rgb(170,0,0);'>VERIFICAÇÃO EXTRAS INICIADA</h3>")
        query = QSqlQuery(conexao.db_mysql)
        model = QtSql.QSqlTableModel()
        query.exec(f"""SELECT * FROM playstation_extras""")
        contador_progress = 0
        contador_erros = 0
        self.ui.progressBar404.setMaximum(query.size())
        while query.next():
            self.ui.progressBar404.setValue(contador_progress)
            contador_progress += 1
            titulo = query.value(1)
            data = query.value(5).toPyDateTime().strftime('%d/%m/%Y')
            link = query.value(6)
            try:#faz tras a pagina do Dropbox com requests | print(titulo, pagina.status_code)
                pagina = requests.get(link.replace('=1', '=0'))
                # passa a pagina para o BeautifulSoup verificar o texto no titulo <title>Dropbox - Error</title>
                soup = BeautifulSoup(pagina.text, 'html.parser')
                erro404 = soup.find_all('title')[0]
                if str(erro404) == '<title>Dropbox - Error</title>':
                    texto_html = f""" <h3 style='color: #fff;'>Jogo: {titulo} | Cadastro: {data} | Erro: 404</h3>"""
                    link_html = f"""<a style='color: #fff;' href='{link}'>Link: {link}</a> """
                    self.ui.textBrowser_verifica404.append(texto_html)
                    self.ui.textBrowser_verifica404.append(link_html)
                    contador_erros += 1
            except Exception as e:
                pass
        #fim do loop testando os links da database | exibe o aviso final
        self.ui.textBrowser_verifica404.append(f"<h2 style='color: rgb(170,0,0);'>TOTAL DE ERROS: {contador_erros}</h2>")
        self.ui.textBrowser_verifica404.append(f"<h2 style='color: rgb(170,0,0);'>TODOS LINKS EXTRAS FORAM VERIFICADOS</h2>")




# verificaPS3
    if self.verifica404_selecionada == 'playstation_ps3':
        self.ui.textBrowser_verifica404.append(f"<h3 style='color: rgb(170,0,0);'>VERIFICAÇÃO PS3 INICIADA</h3>")
        query = QSqlQuery(conexao.db_mysql)
        model = QtSql.QSqlTableModel()
        query.exec(f"""SELECT * FROM playstation_ps3""")

        contador_progress = 0
        contador_erros = 0

        self.ui.progressBar404.setMaximum(query.size())


        while query.next():
            self.ui.progressBar404.setValue(contador_progress)
            contador_progress += 1
            titulo = query.value(1)
            data = query.value(5).toPyDateTime().strftime('%d/%m/%Y')
            link = query.value(6)
            if link == '---':
                pass
            else:
                try:  # TESTA LINK PLAYSTATION3
                    pagina = requests.get(link.replace('=1', '=0'))
                    # passa a pagina para o BeautifulSoup verificar o texto no titulo <title>Dropbox - Error</title>
                    soup = BeautifulSoup(pagina.text, 'html.parser')
                    erro404 = soup.find_all('title')[0]
                    if str(erro404) == '<title>Dropbox - Error</title>':
                        texto_html = f""" <h3 style='color: #fff;'>Jogo: {titulo} | Link: 01 | Cadastro: {data} | Erro: 404</h3>"""
                        link_html = f"""<a style='color: #fff;' href='{link}'>Link: {link}</a> """
                        self.ui.textBrowser_verifica404.append(texto_html)
                        self.ui.textBrowser_verifica404.append(link_html)
                        #contador_erros += 1
                except Exception as e:
                    pass
            link = query.value(8)
            if link == '---':
                pass
            else:
                try:  # TESTA LINK PLAYSTATION3
                    pagina = requests.get(link.replace('=1', '=0'))
                    # passa a pagina para o BeautifulSoup verificar o texto no titulo <title>Dropbox - Error</title>
                    soup = BeautifulSoup(pagina.text, 'html.parser')
                    erro404 = soup.find_all('title')[0]
                    if str(erro404) == '<title>Dropbox - Error</title>':
                        texto_html = f""" <h3 style='color: #fff;'>Jogo: {titulo} | Link: 03 | Cadastro: {data} | Erro: 404</h3>"""
                        link_html = f"""<a style='color: #fff;' href='{link}'>Link: {link}</a> """
                        self.ui.textBrowser_verifica404.append(texto_html)
                        self.ui.textBrowser_verifica404.append(link_html)
                        contador_erros += 1
                except Exception as e:
                    pass

















































        #fim do loop testando os links da database | exibe o aviso final
        self.ui.textBrowser_verifica404.append(f"<h2 style='color: rgb(170,0,0);'>TOTAL DE ERROS: {contador_erros}</h2>")
        self.ui.textBrowser_verifica404.append(f"<h2 style='color: rgb(170,0,0);'>TODOS LINKS DE PS3 FORAM VERIFICADOS</h2>")