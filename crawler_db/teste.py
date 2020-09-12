



for i in range(30):


    texto = """if (!empty($_POST['link'])) {
            $link = $_POST['link'];
        } else {
            $linkErro = 'O link  não é obrigatório, mantenha o nome --- intalterado caso não vá inserir link!';
            $link = '---';
        }
        """
    texto = texto.replace('link',f'link{i+1}')
    print(texto)
