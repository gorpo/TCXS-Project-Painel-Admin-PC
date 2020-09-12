
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
    imagem = str(imagem).split('ps3/')[1].split('"/>')[0].replace('" width="170','')
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











if len(links) == 30:
    print('==== 30 LINKS ENCONTRADOS ======')
    print(f'Titulo: {titulos[0]}')
    print(f'Descrição: {descricoes[0]}')
    print(f'ContentID: {ids[0]}')
    print(f'Link:{links[0:]}')
    with conexao.cursor() as cursor:
        tabela = f"""INSERT INTO playstation_ps3 (titulo,descricao,content_id,imagem,cadastro,
        link1,link2,link3,link4,link5,link6,link7,link8,link9,link10,link11,link12,link13,link14,
        link15,link16,link17,link18,link19,link20,link21,link22,link23,link24,link25,link26,link27,
        link28,link29,link30) VALUES ('{titulos[0]}','{descricoes[0]}','{ids[0]}','{imagens[0]}','{hoje}', 
        '{links[0]}','{links[1]}','{links[2]}','{links[3]}','{links[4]}','{links[5]}','{links[6]}',
        '{links[7]}','{links[8]}','{links[9]}','{links[10]}','{links[11]}','{links[12]}','{links[13]}',
        '{links[14]}','{links[15]}','{links[16]}','{links[17]}','{links[18]}','{links[19]}','{links[20]}',
        '{links[21]}','{links[22]}','{links[23]}','{links[24]}','{links[25]}','{links[26]}','{links[27]}',
        '{links[28]}','{links[29]}') """
        cursor.execute(tabela)
        conexao.commit()
        conexao.close()

if len(links) == 29:
    print('==== 29 LINKS ENCONTRADOS ======')
    print(f'Titulo: {titulos[0]}')
    print(f'Descrição: {descricoes[0]}')
    print(f'ContentID: {ids[0]}')
    print(f'Link:{links[0:]}')
    with conexao.cursor() as cursor:
        tabela = f"""INSERT INTO playstation_ps3 (titulo,descricao,content_id,imagem,cadastro,
        link1,link2,link3,link4,link5,link6,link7,link8,link9,link10,link11,link12,link13,link14,
        link15,link16,link17,link18,link19,link20,link21,link22,link23,link24,link25,link26,link27,
        link28,link29,link30) VALUES ('{titulos[0]}','{descricoes[0]}','{ids[0]}','{imagens[0]}','{hoje}', 
        '{links[0]}','{links[1]}','{links[2]}','{links[3]}','{links[4]}','{links[5]}','{links[6]}',
        '{links[7]}','{links[8]}','{links[9]}','{links[10]}','{links[11]}','{links[12]}','{links[13]}',
        '{links[14]}','{links[15]}','{links[16]}','{links[17]}','{links[18]}','{links[19]}','{links[20]}',
        '{links[21]}','{links[22]}','{links[23]}','{links[24]}','{links[25]}','{links[26]}','{links[27]}',
        '{links[28]}','---') """
        cursor.execute(tabela)
        conexao.commit()
        conexao.close()

if len(links) == 28:
    print('==== 28 LINKS ENCONTRADOS ======')
    print(f'Titulo: {titulos[0]}')
    print(f'Descrição: {descricoes[0]}')
    print(f'ContentID: {ids[0]}')
    print(f'Link:{links[0:]}')
    with conexao.cursor() as cursor:
        tabela = f"""INSERT INTO playstation_ps3 (titulo,descricao,content_id,imagem,cadastro,
        link1,link2,link3,link4,link5,link6,link7,link8,link9,link10,link11,link12,link13,link14,
        link15,link16,link17,link18,link19,link20,link21,link22,link23,link24,link25,link26,link27,
        link28,link29,link30) VALUES ('{titulos[0]}','{descricoes[0]}','{ids[0]}','{imagens[0]}','{hoje}', 
        '{links[0]}','{links[1]}','{links[2]}','{links[3]}','{links[4]}','{links[5]}','{links[6]}',
        '{links[7]}','{links[8]}','{links[9]}','{links[10]}','{links[11]}','{links[12]}','{links[13]}',
        '{links[14]}','{links[15]}','{links[16]}','{links[17]}','{links[18]}','{links[19]}','{links[20]}',
        '{links[21]}','{links[22]}','{links[23]}','{links[24]}','{links[25]}','{links[26]}','{links[27]}',
        '---','---') """
        cursor.execute(tabela)
        conexao.commit()
        conexao.close()

if len(links) == 27:
    print('==== 27 LINKS ENCONTRADOS ======')
    print(f'Titulo: {titulos[0]}')
    print(f'Descrição: {descricoes[0]}')
    print(f'ContentID: {ids[0]}')
    print(f'Link:{links[0:]}')
    with conexao.cursor() as cursor:
        tabela = f"""INSERT INTO playstation_ps3 (titulo,descricao,content_id,imagem,cadastro,
        link1,link2,link3,link4,link5,link6,link7,link8,link9,link10,link11,link12,link13,link14,
        link15,link16,link17,link18,link19,link20,link21,link22,link23,link24,link25,link26,link27,
        link28,link29,link30) VALUES ('{titulos[0]}','{descricoes[0]}','{ids[0]}','{imagens[0]}','{hoje}', 
        '{links[0]}','{links[1]}','{links[2]}','{links[3]}','{links[4]}','{links[5]}','{links[6]}',
        '{links[7]}','{links[8]}','{links[9]}','{links[10]}','{links[11]}','{links[12]}','{links[13]}',
        '{links[14]}','{links[15]}','{links[16]}','{links[17]}','{links[18]}','{links[19]}','{links[20]}',
        '{links[21]}','{links[22]}','{links[23]}','{links[24]}','{links[25]}','{links[26]}','---',
        '---','---') """
        cursor.execute(tabela)
        conexao.commit()
        conexao.close()

if len(links) == 26:
    print('==== 26 LINKS ENCONTRADOS ======')
    print(f'Titulo: {titulos[0]}')
    print(f'Descrição: {descricoes[0]}')
    print(f'ContentID: {ids[0]}')
    print(f'Link:{links[0:]}')
    with conexao.cursor() as cursor:
        tabela = f"""INSERT INTO playstation_ps3 (titulo,descricao,content_id,imagem,cadastro,
        link1,link2,link3,link4,link5,link6,link7,link8,link9,link10,link11,link12,link13,link14,
        link15,link16,link17,link18,link19,link20,link21,link22,link23,link24,link25,link26,link27,
        link28,link29,link30) VALUES ('{titulos[0]}','{descricoes[0]}','{ids[0]}','{imagens[0]}','{hoje}', 
        '{links[0]}','{links[1]}','{links[2]}','{links[3]}','{links[4]}','{links[5]}','{links[6]}',
        '{links[7]}','{links[8]}','{links[9]}','{links[10]}','{links[11]}','{links[12]}','{links[13]}',
        '{links[14]}','{links[15]}','{links[16]}','{links[17]}','{links[18]}','{links[19]}','{links[20]}',
        '{links[21]}','{links[22]}','{links[23]}','{links[24]}','{links[25]}','---','---',
        '---','---') """
        cursor.execute(tabela)
        conexao.commit()
        conexao.close()

if len(links) == 25:
    print('====  25 LINKS ENCONTRADOS ======')
    print(f'Titulo: {titulos[0]}')
    print(f'Descrição: {descricoes[0]}')
    print(f'ContentID: {ids[0]}')
    print(f'Link:{links[0:]}')
    with conexao.cursor() as cursor:
        tabela = f"""INSERT INTO playstation_ps3 (titulo,descricao,content_id,imagem,cadastro,
        link1,link2,link3,link4,link5,link6,link7,link8,link9,link10,link11,link12,link13,link14,
        link15,link16,link17,link18,link19,link20,link21,link22,link23,link24,link25,link26,link27,
        link28,link29,link30) VALUES ('{titulos[0]}','{descricoes[0]}','{ids[0]}','{imagens[0]}','{hoje}', 
        '{links[0]}','{links[1]}','{links[2]}','{links[3]}','{links[4]}','{links[5]}','{links[6]}',
        '{links[7]}','{links[8]}','{links[9]}','{links[10]}','{links[11]}','{links[12]}','{links[13]}',
        '{links[14]}','{links[15]}','{links[16]}','{links[17]}','{links[18]}','{links[19]}','{links[20]}',
        '{links[21]}','{links[22]}','{links[23]}','{links[24]}','---','---','---',
        '---','---') """
        cursor.execute(tabela)
        conexao.commit()
        conexao.close()


if len(links) == 24:
    print('====  24 LINKS ENCONTRADOS ======')
    print(f'Titulo: {titulos[0]}')
    print(f'Descrição: {descricoes[0]}')
    print(f'ContentID: {ids[0]}')
    print(f'Link:{links[0:]}')
    with conexao.cursor() as cursor:
        tabela = f"""INSERT INTO playstation_ps3 (titulo,descricao,content_id,imagem,cadastro,
        link1,link2,link3,link4,link5,link6,link7,link8,link9,link10,link11,link12,link13,link14,
        link15,link16,link17,link18,link19,link20,link21,link22,link23,link24,link25,link26,link27,
        link28,link29,link30) VALUES ('{titulos[0]}','{descricoes[0]}','{ids[0]}','{imagens[0]}','{hoje}', 
        '{links[0]}','{links[1]}','{links[2]}','{links[3]}','{links[4]}','{links[5]}','{links[6]}',
        '{links[7]}','{links[8]}','{links[9]}','{links[10]}','{links[11]}','{links[12]}','{links[13]}',
        '{links[14]}','{links[15]}','{links[16]}','{links[17]}','{links[18]}','{links[19]}','{links[20]}',
        '{links[21]}','{links[22]}','{links[23]}','---','---','---','---',
        '---','---') """
        cursor.execute(tabela)
        conexao.commit()
        conexao.close()


if len(links) == 23:
    print('====  23 LINKS ENCONTRADOS ======')
    print(f'Titulo: {titulos[0]}')
    print(f'Descrição: {descricoes[0]}')
    print(f'ContentID: {ids[0]}')
    print(f'Link:{links[0:]}')
    with conexao.cursor() as cursor:
        tabela = f"""INSERT INTO playstation_ps3 (titulo,descricao,content_id,imagem,cadastro,
        link1,link2,link3,link4,link5,link6,link7,link8,link9,link10,link11,link12,link13,link14,
        link15,link16,link17,link18,link19,link20,link21,link22,link23,link24,link25,link26,link27,
        link28,link29,link30) VALUES ('{titulos[0]}','{descricoes[0]}','{ids[0]}','{imagens[0]}','{hoje}', 
        '{links[0]}','{links[1]}','{links[2]}','{links[3]}','{links[4]}','{links[5]}','{links[6]}',
        '{links[7]}','{links[8]}','{links[9]}','{links[10]}','{links[11]}','{links[12]}','{links[13]}',
        '{links[14]}','{links[15]}','{links[16]}','{links[17]}','{links[18]}','{links[19]}','{links[20]}',
        '{links[21]}','{links[22]}','---','---','---','---','---',
        '---','---') """
        cursor.execute(tabela)
        conexao.commit()
        conexao.close()

if len(links) == 22:
    print('====  22 LINKS ENCONTRADOS ======')
    print(f'Titulo: {titulos[0]}')
    print(f'Descrição: {descricoes[0]}')
    print(f'ContentID: {ids[0]}')
    print(f'Link:{links[0:]}')
    with conexao.cursor() as cursor:
        tabela = f"""INSERT INTO playstation_ps3 (titulo,descricao,content_id,imagem,cadastro,
        link1,link2,link3,link4,link5,link6,link7,link8,link9,link10,link11,link12,link13,link14,
        link15,link16,link17,link18,link19,link20,link21,link22,link23,link24,link25,link26,link27,
        link28,link29,link30) VALUES ('{titulos[0]}','{descricoes[0]}','{ids[0]}','{imagens[0]}','{hoje}', 
        '{links[0]}','{links[1]}','{links[2]}','{links[3]}','{links[4]}','{links[5]}','{links[6]}',
        '{links[7]}','{links[8]}','{links[9]}','{links[10]}','{links[11]}','{links[12]}','{links[13]}',
        '{links[14]}','{links[15]}','{links[16]}','{links[17]}','{links[18]}','{links[19]}','{links[20]}',
        '{links[21]}','---','---','---','---','---','---',
        '---','---') """
        cursor.execute(tabela)
        conexao.commit()
        conexao.close()



if len(links) == 21:
    print('====  21 LINKS ENCONTRADOS ======')
    print(f'Titulo: {titulos[0]}')
    print(f'Descrição: {descricoes[0]}')
    print(f'ContentID: {ids[0]}')
    print(f'Link:{links[0:]}')
    with conexao.cursor() as cursor:
        tabela = f"""INSERT INTO playstation_ps3 (titulo,descricao,content_id,imagem,cadastro,
        link1,link2,link3,link4,link5,link6,link7,link8,link9,link10,link11,link12,link13,link14,
        link15,link16,link17,link18,link19,link20,link21,link22,link23,link24,link25,link26,link27,
        link28,link29,link30) VALUES ('{titulos[0]}','{descricoes[0]}','{ids[0]}','{imagens[0]}','{hoje}', 
        '{links[0]}','{links[1]}','{links[2]}','{links[3]}','{links[4]}','{links[5]}','{links[6]}',
        '{links[7]}','{links[8]}','{links[9]}','{links[10]}','{links[11]}','{links[12]}','{links[13]}',
        '{links[14]}','{links[15]}','{links[16]}','{links[17]}','{links[18]}','{links[19]}','{links[20]}',
        '---','---','---','---','---','---','---',
        '---','---') """
        cursor.execute(tabela)
        conexao.commit()
        conexao.close()

if len(links) == 20:
    print('====  20 LINKS ENCONTRADOS ======')
    print(f'Titulo: {titulos[0]}')
    print(f'Descrição: {descricoes[0]}')
    print(f'ContentID: {ids[0]}')
    print(f'Link:{links[0:]}')
    with conexao.cursor() as cursor:
        tabela = f"""INSERT INTO playstation_ps3 (titulo,descricao,content_id,imagem,cadastro,
        link1,link2,link3,link4,link5,link6,link7,link8,link9,link10,link11,link12,link13,link14,
        link15,link16,link17,link18,link19,link20,link21,link22,link23,link24,link25,link26,link27,
        link28,link29,link30) VALUES ('{titulos[0]}','{descricoes[0]}','{ids[0]}','{imagens[0]}','{hoje}', 
        '{links[0]}','{links[1]}','{links[2]}','{links[3]}','{links[4]}','{links[5]}','{links[6]}',
        '{links[7]}','{links[8]}','{links[9]}','{links[10]}','{links[11]}','{links[12]}','{links[13]}',
        '{links[14]}','{links[15]}','{links[16]}','{links[17]}','{links[18]}','{links[19]}','---',
        '---','---','---','---','---','---','---',
        '---','---') """
        cursor.execute(tabela)
        conexao.commit()
        conexao.close()



if len(links) == 19:
    print('====  19 LINKS ENCONTRADOS ======')
    print(f'Titulo: {titulos[0]}')
    print(f'Descrição: {descricoes[0]}')
    print(f'ContentID: {ids[0]}')
    print(f'Link:{links[0:]}')
    with conexao.cursor() as cursor:
        tabela = f"""INSERT INTO playstation_ps3 (titulo,descricao,content_id,imagem,cadastro,
        link1,link2,link3,link4,link5,link6,link7,link8,link9,link10,link11,link12,link13,link14,
        link15,link16,link17,link18,link19,link20,link21,link22,link23,link24,link25,link26,link27,
        link28,link29,link30) VALUES ('{titulos[0]}','{descricoes[0]}','{ids[0]}','{imagens[0]}','{hoje}', 
        '{links[0]}','{links[1]}','{links[2]}','{links[3]}','{links[4]}','{links[5]}','{links[6]}',
        '{links[7]}','{links[8]}','{links[9]}','{links[10]}','{links[11]}','{links[12]}','{links[13]}',
        '{links[14]}','{links[15]}','{links[16]}','{links[17]}','{links[18]}','---','---',
        '---','---','---','---','---','---','---',
        '---','---') """
        cursor.execute(tabela)
        conexao.commit()
        conexao.close()


if len(links) == 18:
    print('====  18LINKS ENCONTRADOS ======')
    print(f'Titulo: {titulos[0]}')
    print(f'Descrição: {descricoes[0]}')
    print(f'ContentID: {ids[0]}')
    print(f'Link:{links[0:]}')
    with conexao.cursor() as cursor:
        tabela = f"""INSERT INTO playstation_ps3 (titulo,descricao,content_id,imagem,cadastro,
        link1,link2,link3,link4,link5,link6,link7,link8,link9,link10,link11,link12,link13,link14,
        link15,link16,link17,link18,link19,link20,link21,link22,link23,link24,link25,link26,link27,
        link28,link29,link30) VALUES ('{titulos[0]}','{descricoes[0]}','{ids[0]}','{imagens[0]}','{hoje}', 
        '{links[0]}','{links[1]}','{links[2]}','{links[3]}','{links[4]}','{links[5]}','{links[6]}',
        '{links[7]}','{links[8]}','{links[9]}','{links[10]}','{links[11]}','{links[12]}','{links[13]}',
        '{links[14]}','{links[15]}','{links[16]}','{links[17]}','---','---','---',
        '---','---','---','---','---','---','---',
        '---','---') """
        cursor.execute(tabela)
        conexao.commit()
        conexao.close()


if len(links) == 17:
    print('====  17 LINKS ENCONTRADOS ======')
    print(f'Titulo: {titulos[0]}')
    print(f'Descrição: {descricoes[0]}')
    print(f'ContentID: {ids[0]}')
    print(f'Link:{links[0:]}')
    with conexao.cursor() as cursor:
        tabela = f"""INSERT INTO playstation_ps3 (titulo,descricao,content_id,imagem,cadastro,
        link1,link2,link3,link4,link5,link6,link7,link8,link9,link10,link11,link12,link13,link14,
        link15,link16,link17,link18,link19,link20,link21,link22,link23,link24,link25,link26,link27,
        link28,link29,link30) VALUES ('{titulos[0]}','{descricoes[0]}','{ids[0]}','{imagens[0]}','{hoje}', 
        '{links[0]}','{links[1]}','{links[2]}','{links[3]}','{links[4]}','{links[5]}','{links[6]}',
        '{links[7]}','{links[8]}','{links[9]}','{links[10]}','{links[11]}','{links[12]}','{links[13]}',
        '{links[14]}','{links[15]}','{links[16]}','---','---','---','---',
        '---','---','---','---','---','---','---',
        '---','---') """
        cursor.execute(tabela)
        conexao.commit()
        conexao.close()

if len(links) == 16:
    print('====  16 LINKS ENCONTRADOS ======')
    print(f'Titulo: {titulos[0]}')
    print(f'Descrição: {descricoes[0]}')
    print(f'ContentID: {ids[0]}')
    print(f'Link:{links[0:]}')
    with conexao.cursor() as cursor:
        tabela = f"""INSERT INTO playstation_ps3 (titulo,descricao,content_id,imagem,cadastro,
        link1,link2,link3,link4,link5,link6,link7,link8,link9,link10,link11,link12,link13,link14,
        link15,link16,link17,link18,link19,link20,link21,link22,link23,link24,link25,link26,link27,
        link28,link29,link30) VALUES ('{titulos[0]}','{descricoes[0]}','{ids[0]}','{imagens[0]}','{hoje}', 
        '{links[0]}','{links[1]}','{links[2]}','{links[3]}','{links[4]}','{links[5]}','{links[6]}',
        '{links[7]}','{links[8]}','{links[9]}','{links[10]}','{links[11]}','{links[12]}','{links[13]}',
        '{links[14]}','{links[15]}','---','---','---','---','---',
        '---','---','---','---','---','---','---',
        '---','---') """
        cursor.execute(tabela)
        conexao.commit()
        conexao.close()

if len(links) == 15:
    print('====  15 LINKS ENCONTRADOS ======')
    print(f'Titulo: {titulos[0]}')
    print(f'Descrição: {descricoes[0]}')
    print(f'ContentID: {ids[0]}')
    print(f'Link:{links[0:]}')
    with conexao.cursor() as cursor:
        tabela = f"""INSERT INTO playstation_ps3 (titulo,descricao,content_id,imagem,cadastro,
        link1,link2,link3,link4,link5,link6,link7,link8,link9,link10,link11,link12,link13,link14,
        link15,link16,link17,link18,link19,link20,link21,link22,link23,link24,link25,link26,link27,
        link28,link29,link30) VALUES ('{titulos[0]}','{descricoes[0]}','{ids[0]}','{imagens[0]}','{hoje}', 
        '{links[0]}','{links[1]}','{links[2]}','{links[3]}','{links[4]}','{links[5]}','{links[6]}',
        '{links[7]}','{links[8]}','{links[9]}','{links[10]}','{links[11]}','{links[12]}','{links[13]}',
        '{links[14]}','---','---','---','---','---','---',
        '---','---','---','---','---','---','---',
        '---','---') """
        cursor.execute(tabela)
        conexao.commit()
        conexao.close()



if len(links) == 14:
    print('====  14 LINKS ENCONTRADOS ======')
    print(f'Titulo: {titulos[0]}')
    print(f'Descrição: {descricoes[0]}')
    print(f'ContentID: {ids[0]}')
    print(f'Link:{links[0:]}')
    with conexao.cursor() as cursor:
        tabela = f"""INSERT INTO playstation_ps3 (titulo,descricao,content_id,imagem,cadastro,
        link1,link2,link3,link4,link5,link6,link7,link8,link9,link10,link11,link12,link13,link14,
        link15,link16,link17,link18,link19,link20,link21,link22,link23,link24,link25,link26,link27,
        link28,link29,link30) VALUES ('{titulos[0]}','{descricoes[0]}','{ids[0]}','{imagens[0]}','{hoje}', 
        '{links[0]}','{links[1]}','{links[2]}','{links[3]}','{links[4]}','{links[5]}','{links[6]}',
        '{links[7]}','{links[8]}','{links[9]}','{links[10]}','{links[11]}','{links[12]}','{links[13]}',
        '---','---','---','---','---','---','---',
        '---','---','---','---','---','---','---',
        '---','---') """
        cursor.execute(tabela)
        conexao.commit()
        conexao.close()



if len(links) == 13:
    print('====  13 LINKS ENCONTRADOS ======')
    print(f'Titulo: {titulos[0]}')
    print(f'Descrição: {descricoes[0]}')
    print(f'ContentID: {ids[0]}')
    print(f'Link:{links[0:]}')
    with conexao.cursor() as cursor:
        tabela = f"""INSERT INTO playstation_ps3 (titulo,descricao,content_id,imagem,cadastro,
        link1,link2,link3,link4,link5,link6,link7,link8,link9,link10,link11,link12,link13,link14,
        link15,link16,link17,link18,link19,link20,link21,link22,link23,link24,link25,link26,link27,
        link28,link29,link30) VALUES ('{titulos[0]}','{descricoes[0]}','{ids[0]}','{imagens[0]}','{hoje}', 
        '{links[0]}','{links[1]}','{links[2]}','{links[3]}','{links[4]}','{links[5]}','{links[6]}',
        '{links[7]}','{links[8]}','{links[9]}','{links[10]}','{links[11]}','{links[12]}','---',
        '---','---','---','---','---','---','---',
        '---','---','---','---','---','---','---',
        '---','---') """
        cursor.execute(tabela)
        conexao.commit()
        conexao.close()






if len(links) == 12:
    print('====  12 LINKS ENCONTRADOS ======')
    print(f'Titulo: {titulos[0]}')
    print(f'Descrição: {descricoes[0]}')
    print(f'ContentID: {ids[0]}')
    print(f'Link:{links[0:]}')
    with conexao.cursor() as cursor:
        tabela = f"""INSERT INTO playstation_ps3 (titulo,descricao,content_id,imagem,cadastro,
        link1,link2,link3,link4,link5,link6,link7,link8,link9,link10,link11,link12,link13,link14,
        link15,link16,link17,link18,link19,link20,link21,link22,link23,link24,link25,link26,link27,
        link28,link29,link30) VALUES ('{titulos[0]}','{descricoes[0]}','{ids[0]}','{imagens[0]}','{hoje}', 
        '{links[0]}','{links[1]}','{links[2]}','{links[3]}','{links[4]}','{links[5]}','{links[6]}',
        '{links[7]}','{links[8]}','{links[9]}','{links[10]}','{links[11]}','---','---',
        '---','---','---','---','---','---','---',
        '---','---','---','---','---','---','---',
        '---','---') """
        cursor.execute(tabela)
        conexao.commit()
        conexao.close()



if len(links) == 11:
    print('====  11 LINKS ENCONTRADOS ======')
    print(f'Titulo: {titulos[0]}')
    print(f'Descrição: {descricoes[0]}')
    print(f'ContentID: {ids[0]}')
    print(f'Link:{links[0:]}')
    with conexao.cursor() as cursor:
        tabela = f"""INSERT INTO playstation_ps3 (titulo,descricao,content_id,imagem,cadastro,
        link1,link2,link3,link4,link5,link6,link7,link8,link9,link10,link11,link12,link13,link14,
        link15,link16,link17,link18,link19,link20,link21,link22,link23,link24,link25,link26,link27,
        link28,link29,link30) VALUES ('{titulos[0]}','{descricoes[0]}','{ids[0]}','{imagens[0]}','{hoje}', 
        '{links[0]}','{links[1]}','{links[2]}','{links[3]}','{links[4]}','{links[5]}','{links[6]}',
        '{links[7]}','{links[8]}','{links[9]}','{links[10]}','---','---','---',
        '---','---','---','---','---','---','---',
        '---','---','---','---','---','---','---',
        '---','---') """
        cursor.execute(tabela)
        conexao.commit()
        conexao.close()



if len(links) == 10:
    print('====  10 LINKS ENCONTRADOS ======')
    print(f'Titulo: {titulos[0]}')
    print(f'Descrição: {descricoes[0]}')
    print(f'ContentID: {ids[0]}')
    print(f'Link:{links[0:]}')
    with conexao.cursor() as cursor:
        tabela = f"""INSERT INTO playstation_ps3 (titulo,descricao,content_id,imagem,cadastro,
        link1,link2,link3,link4,link5,link6,link7,link8,link9,link10,link11,link12,link13,link14,
        link15,link16,link17,link18,link19,link20,link21,link22,link23,link24,link25,link26,link27,
        link28,link29,link30) VALUES ('{titulos[0]}','{descricoes[0]}','{ids[0]}','{imagens[0]}','{hoje}', 
        '{links[0]}','{links[1]}','{links[2]}','{links[3]}','{links[4]}','{links[5]}','{links[6]}',
        '{links[7]}','{links[8]}','{links[9]}','---','---','---','---',
        '---','---','---','---','---','---','---',
        '---','---','---','---','---','---','---',
        '---','---') """
        cursor.execute(tabela)
        conexao.commit()
        conexao.close()

if len(links) == 9:
    print('====  9 LINKS ENCONTRADOS ======')
    print(f'Titulo: {titulos[0]}')
    print(f'Descrição: {descricoes[0]}')
    print(f'ContentID: {ids[0]}')
    print(f'Link:{links[0:]}')
    with conexao.cursor() as cursor:
        tabela = f"""INSERT INTO playstation_ps3 (titulo,descricao,content_id,imagem,cadastro,
        link1,link2,link3,link4,link5,link6,link7,link8,link9,link10,link11,link12,link13,link14,
        link15,link16,link17,link18,link19,link20,link21,link22,link23,link24,link25,link26,link27,
        link28,link29,link30) VALUES ('{titulos[0]}','{descricoes[0]}','{ids[0]}','{imagens[0]}','{hoje}', 
        '{links[0]}','{links[1]}','{links[2]}','{links[3]}','{links[4]}','{links[5]}','{links[6]}',
        '{links[7]}','{links[8]}','---','---','---','---','---',
        '---','---','---','---','---','---','---',
        '---','---','---','---','---','---','---',
        '---','---') """
        cursor.execute(tabela)
        conexao.commit()
        conexao.close()


if len(links) == 8:
    print('====  8 LINKS ENCONTRADOS ======')
    print(f'Titulo: {titulos[0]}')
    print(f'Descrição: {descricoes[0]}')
    print(f'ContentID: {ids[0]}')
    print(f'Link:{links[0:]}')
    with conexao.cursor() as cursor:
        tabela = f"""INSERT INTO playstation_ps3 (titulo,descricao,content_id,imagem,cadastro,
        link1,link2,link3,link4,link5,link6,link7,link8,link9,link10,link11,link12,link13,link14,
        link15,link16,link17,link18,link19,link20,link21,link22,link23,link24,link25,link26,link27,
        link28,link29,link30) VALUES ('{titulos[0]}','{descricoes[0]}','{ids[0]}','{imagens[0]}','{hoje}', 
        '{links[0]}','{links[1]}','{links[2]}','{links[3]}','{links[4]}','{links[5]}','{links[6]}',
        '{links[7]}','---','---','---','---','---','---',
        '---','---','---','---','---','---','---',
        '---','---','---','---','---','---','---',
        '---','---') """
        cursor.execute(tabela)
        conexao.commit()
        conexao.close()




if len(links) == 7:
    print('====  7 LINKS ENCONTRADOS ======')
    print(f'Titulo: {titulos[0]}')
    print(f'Descrição: {descricoes[0]}')
    print(f'ContentID: {ids[0]}')
    print(f'Link:{links[0:]}')
    with conexao.cursor() as cursor:
        tabela = f"""INSERT INTO playstation_ps3 (titulo,descricao,content_id,imagem,cadastro,
        link1,link2,link3,link4,link5,link6,link7,link8,link9,link10,link11,link12,link13,link14,
        link15,link16,link17,link18,link19,link20,link21,link22,link23,link24,link25,link26,link27,
        link28,link29,link30) VALUES ('{titulos[0]}','{descricoes[0]}','{ids[0]}','{imagens[0]}','{hoje}', 
        '{links[0]}','{links[1]}','{links[2]}','{links[3]}','{links[4]}','{links[5]}','{links[6]}',
        '---','---','---','---','---','---','---',
        '---','---','---','---','---','---','---',
        '---','---','---','---','---','---','---',
        '---','---') """
        cursor.execute(tabela)
        conexao.commit()
        conexao.close()





if len(links) == 6:
    print('====  6 LINKS ENCONTRADOS ======')
    print(f'Titulo: {titulos[0]}')
    print(f'Descrição: {descricoes[0]}')
    print(f'ContentID: {ids[0]}')
    print(f'Link:{links[0:]}')
    with conexao.cursor() as cursor:
        tabela = f"""INSERT INTO playstation_ps3 (titulo,descricao,content_id,imagem,cadastro,
        link1,link2,link3,link4,link5,link6,link7,link8,link9,link10,link11,link12,link13,link14,
        link15,link16,link17,link18,link19,link20,link21,link22,link23,link24,link25,link26,link27,
        link28,link29,link30) VALUES ('{titulos[0]}','{descricoes[0]}','{ids[0]}','{imagens[0]}','{hoje}', 
        '{links[0]}','{links[1]}','{links[2]}','{links[3]}','{links[4]}','{links[5]}','---',
        '---','---','---','---','---','---','---',
        '---','---','---','---','---','---','---',
        '---','---','---','---','---','---','---',
        '---','---') """
        cursor.execute(tabela)
        conexao.commit()
        conexao.close()



if len(links) == 5:
    print('====  5 LINKS ENCONTRADOS ======')
    print(f'Titulo: {titulos[0]}')
    print(f'Descrição: {descricoes[0]}')
    print(f'ContentID: {ids[0]}')
    print(f'Link:{links[0:]}')
    with conexao.cursor() as cursor:
        tabela = f"""INSERT INTO playstation_ps3 (titulo,descricao,content_id,imagem,cadastro,
        link1,link2,link3,link4,link5,link6,link7,link8,link9,link10,link11,link12,link13,link14,
        link15,link16,link17,link18,link19,link20,link21,link22,link23,link24,link25,link26,link27,
        link28,link29,link30) VALUES ('{titulos[0]}','{descricoes[0]}','{ids[0]}','{imagens[0]}','{hoje}', 
        '{links[0]}','{links[1]}','{links[2]}','{links[3]}','{links[4]}','---','---',
        '---','---','---','---','---','---','---',
        '---','---','---','---','---','---','---',
        '---','---','---','---','---','---','---',
        '---','---') """
        cursor.execute(tabela)
        conexao.commit()
        conexao.close()




if len(links) == 4:
    print('====  4 LINKS ENCONTRADOS ======')
    print(f'Titulo: {titulos[0]}')
    print(f'Descrição: {descricoes[0]}')
    print(f'ContentID: {ids[0]}')
    print(f'Link:{links[0:]}')
    with conexao.cursor() as cursor:
        tabela = f"""INSERT INTO playstation_ps3 (titulo,descricao,content_id,imagem,cadastro,
        link1,link2,link3,link4,link5,link6,link7,link8,link9,link10,link11,link12,link13,link14,
        link15,link16,link17,link18,link19,link20,link21,link22,link23,link24,link25,link26,link27,
        link28,link29,link30) VALUES ('{titulos[0]}','{descricoes[0]}','{ids[0]}','{imagens[0]}','{hoje}', 
        '{links[0]}','{links[1]}','{links[2]}','{links[3]}','---','---','---',
        '---','---','---','---','---','---','---',
        '---','---','---','---','---','---','---',
        '---','---','---','---','---','---','---',
        '---','---') """
        cursor.execute(tabela)
        conexao.commit()
        conexao.close()



if len(links) == 3:
    print('====  3 LINKS ENCONTRADOS ======')
    print(f'Titulo: {titulos[0]}')
    print(f'Descrição: {descricoes[0]}')
    print(f'ContentID: {ids[0]}')
    print(f'Link:{links[0:]}')
    with conexao.cursor() as cursor:
        tabela = f"""INSERT INTO playstation_ps3 (titulo,descricao,content_id,imagem,cadastro,
        link1,link2,link3,link4,link5,link6,link7,link8,link9,link10,link11,link12,link13,link14,
        link15,link16,link17,link18,link19,link20,link21,link22,link23,link24,link25,link26,link27,
        link28,link29,link30) VALUES ('{titulos[0]}','{descricoes[0]}','{ids[0]}','{imagens[0]}','{hoje}', 
        '{links[0]}','{links[1]}','{links[2]}','---','---','---','---',
        '---','---','---','---','---','---','---',
        '---','---','---','---','---','---','---',
        '---','---','---','---','---','---','---',
        '---','---') """
        cursor.execute(tabela)
        conexao.commit()
        conexao.close()


if len(links) == 2:
    print('====  2 LINKS ENCONTRADOS ======')
    print(f'Titulo: {titulos[0]}')
    print(f'Descrição: {descricoes[0]}')
    print(f'ContentID: {ids[0]}')
    print(f'Link:{links[0:]}')
    with conexao.cursor() as cursor:
        tabela = f"""INSERT INTO playstation_ps3 (titulo,descricao,content_id,imagem,cadastro,
        link1,link2,link3,link4,link5,link6,link7,link8,link9,link10,link11,link12,link13,link14,
        link15,link16,link17,link18,link19,link20,link21,link22,link23,link24,link25,link26,link27,
        link28,link29,link30) VALUES ('{titulos[0]}','{descricoes[0]}','{ids[0]}','{imagens[0]}','{hoje}', 
        '{links[0]}','{links[1]}','---','---','---','---','---',
        '---','---','---','---','---','---','---',
        '---','---','---','---','---','---','---',
        '---','---','---','---','---','---','---',
        '---','---') """
        cursor.execute(tabela)
        conexao.commit()
        conexao.close()

















































































