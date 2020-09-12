
import  os
import pathlib
import sqlite3
from bs4 import BeautifulSoup
import pymysql.cursors
from datetime import datetime



#faz a conexao com o banco de dados
conexao = pymysql.connect(host = 'localhost',
                          user = 'root',
                          password = '',
                          db = 'tcxs_store',
                          charset = 'utf8mb4',
                          cursorclass = pymysql.cursors.DictCursor)


#variavies iniciais
dados = open('base.html', 'r', encoding="utf-8").read()
dados= BeautifulSoup(dados, 'html5lib')


key_titulo = dados.find_all('h2', {'class':'titulo_jogo'})
key_desc = dados.find_all('p', {'class':'textoJogo'})
key_contentid = dados.find_all('a', href=True)
key_imagem = dados.find_all('img',{'class':'caixa_imagem'})
key_links = dados.find_all('a', href=True)



titulos = []
for titulo in key_titulo:
    titulo = str(titulo).split('"titulo_jogo">')[1].split('</h')[0].replace("'","").replace('</h2>','').replace(':','')
    titulos.append(titulo)
    #print(titulo)

descricoes = []
for desc in key_desc:
    desc = str(desc).split('textoJogo">')[1].replace('</p>','')
    descricoes.append(desc)
    #print(desc)

ids = []
invalidar = ['index.php','psp.php','ps1.php','ps2.php','ps3.php','emuladores.php','https://tcxsproject.com.br/doadores/','https://tcxsproject.com.br/dev/ps3xploit.com/']
for id in key_contentid:
    id = id['href']
    if id in invalidar:
        pass
    else:
        try:
            id = id.split('/')[5].split('.pkg')[0]
            ids.append(id)
            #print(id)
        except:
            id = 'FALTA CONTENT_ID'
            ids.append(id)
            #print(id)




imagens = []
for imagem in key_imagem:
    imagem = str(imagem).split('ps1/')[1].split('"/>')[0].replace('" width="170','')
    imagens.append(imagem)
    print(imagem)


links = []
invalidar = ['index.php','psp.php','ps1.php','ps2.php','ps3.php','emuladores.php','https://tcxsproject.com.br/doadores/','https://tcxsproject.com.br/dev/ps3xploit.com/']
for link in key_links:
    link = link['href']
    if link in invalidar:
        #print(f'Pulando o {link}')
        pass
    else:
        links.append(link)
        #print(f'gravando o {link}')


print(len(titulos), len(descricoes), len(imagens), len(links))
dicionario_jogos = list(zip(list(titulos), list(imagens), list(links)))#--
#print(dicionario_jogos)
now = datetime.now()
hoje = now.strftime('%Y-%m-%d %H:%M:%S')









if len(links) == 1:
    print('====  1 LINKS ENCONTRADOS ======')
    print(f'Titulo: {titulos[0]}')
    print(f'Descrição: {descricoes[0]}')
    print(f'ContentID: {ids[0]}')
    print(f'Link:{links[0:]}')
    with conexao.cursor() as cursor:
        tabela = f"""INSERT INTO playstation_ps1 (titulo,descricao,content_id,imagem,cadastro,
        link ) VALUES ('{titulos[0]}','{descricoes[0]}','{ids[0]}','{imagens[0]}','{hoje}', 
        '{links[0]}') """
        cursor.execute(tabela)
        conexao.commit()
        conexao.close()

















































































