



for i in range(30):

    texto = ''' 
           while query.next(): #TESTA LINK PLAYSTATION3
            self.ui.progressBar404.setValue(contador_progress)
            contador_progress += 1
            titulo = query.value(1)
            data = query.value(5).toPyDateTime().strftime('%d/%m/%Y')
            try:  #TESTA LINK PLAYSTATION3
                link = query.value(6)
                if link == '---' or link == '':
                    pass
                else:
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
        '''

    texto = texto.replace('link',f'link{i+1}')
    texto = texto.replace('Link',f'Link{i+1}')
    texto = texto.replace('LINK',f'LINK{i+1}')
    texto = texto.replace('6',f'{i+6}')

    print(texto)