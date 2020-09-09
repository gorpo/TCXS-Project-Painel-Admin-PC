import requests
import pymysql.cursors
from bs4 import BeautifulSoup

#cria conexao com banco de dados
conexao = pymysql.connect(host = 'localhost',
                          user= 'root',
                          password='',
                          db='tcxs_store',
                          charset='utf8mb4', cursorclass= pymysql.cursors.DictCursor )


with conexao.cursor() as cursor:
    cursor.execute("SELECT * from playstation_ps1")
    tabela = cursor.fetchall()
    for resultado in tabela:
        titulo = resultado['titulo']
        link = resultado['link']
        data = resultado['cadastro'].strftime('%d/%m/%Y')
        pagina = requests.get(link.replace('=1','=0'))
        #print(titulo, pagina.status_code)
        soup = BeautifulSoup(pagina.text, 'html.parser')
        erro404 = soup.find_all('title')[0]
        if str(erro404) == '<title>Dropbox - Error</title>':
            print(f'Jogo: {titulo} 404')

conexao.close()