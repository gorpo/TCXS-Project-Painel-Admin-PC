



for i in range(30):
    texto = """'{link}',"""
    texto = texto.replace('link',f'link{i+1}')
    print(texto,end='')
    #texto = f"""link{i+1} = dados_user['link{i+1}']"""
    #print(texto)