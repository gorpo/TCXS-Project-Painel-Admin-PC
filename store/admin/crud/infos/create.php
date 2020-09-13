<!-- ████████╗ ██████╗██╗  ██╗███████╗    ██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗
     ╚══██╔══╝██╔════╝╚██╗██╔╝██╔════╝    ██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝
        ██║   ██║      ╚███╔╝ ███████╗    ██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║   
        ██║   ██║      ██╔██╗ ╚════██║    ██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║   
        ██║   ╚██████╗██╔╝ ██╗███████║    ██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║   
        ╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝   -->
<!-- @Gorpo Orko - 2020 -->

<?php
session_start();
if(!$_SESSION['nome']) {
  header('Location: ../../../nao_logado.php');
  exit();
}

require '../../../database.php';
//Acompanha os erros de validação
//id informacao descricao content_id imagem_db imagem link
// Processar so quando tenha uma chamada post
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $informacaoErro = null;

    if (!empty($_POST)) {
        $validacao = True;
        $novoUsuario = False;
        if (!empty($_POST['informacao'])) {
            $informacao = $_POST['informacao'];
        } else {
            $informacaoErro = 'Por favor digite a informacao!';
            $validacao = False;
        }

    }
//---------------------------------------------------------------------------------------------------------------------
//Inserindo o jogo na database:
    if ($validacao) {
        $pdo = Database::conectar();
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        $sql = "INSERT INTO playstation_infos (informacao) VALUES(?)";
        $q = $pdo->prepare($sql);
        $q->execute(array($informacao));
        database::desconectar();
        header("Location: index.php");
    }
}


?>


<!-- ============= TEMPLATE HTML ======== --->
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
      <meta http-equiv="refresh" content="120">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <meta property="og:site_name" content="TCXS Project PlayStation3"/>
      <meta property="og:title" content="TCXS Project PlayStation3"/>
      <meta property="og:url" content="https://tcxsproject.com.br/"/>
      <meta property="og:description" content="Sistema de administração TCXS Project"/>
      <meta property="og:image" content="../../../assets/images/logo.png"/>
      <link rel="shortcut icon" href="../../../assets/images/icon.png" />
      <script src="https://kit.fontawesome.com/a80232805f.js" crossorigin="anonymous"></script>
      <link rel="stylesheet" type="text/css" href="../../../assets/css/style.css" />
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
      <link href="https://fonts.googleapis.com/css?family=Rubik&display=swap" rel="stylesheet">
      <script src="https://kit.fontawesome.com/af562a2a63.js" crossorigin="anonymous"></script>
      <title>TCXS Project | ADD INFO</title>
</head>
<body>
<div class="container">

<!-- ============= MENUS PARA PC E CELULAR ======== --->
    <caption>
            <div class="barraTopo">
              <img class="logo" src="../../../assets/images/logo_info.png"><br>
                <!-- BARRA DE NAVEGAÇÃO DOS MENUS -->
                <div class="menu-content"> <label class="open-menu-all" for="open-menu-all">
                     <input class="input-menu-all" id="open-menu-all" type="checkbox" name="menu-open" />
                        <div class="navegacao-mobile">
                          <span class="linha-menu"></span>
                          <span class="linha-menu"></span>
                          <span class="linha-menu"></span>
                        </div>
                <ul class="list-menu">
                        <li class="item-menu"> <a href="../cadastro_usuarios.php" class="link-menu">CADASTRO USUARIO</a></li>
                        <li class="item-menu"> <a href="../consulta_usuarios.php" class="link-menu">VERIFICA USUARIO</a></li>
                         <li class="item-menu"> <a href="index.php" class="link-menu">PlayStation Infos</a></li>
                         <li class="item-menu"> <a href="../psp/index.php" class="link-menu">PlayStation PSP</a></li>
                         <li class="item-menu"> <a href="../ps1/index.php" class="link-menu">PlayStation1</a></li>
                         <li class="item-menu"> <a href="../ps2/index.php" class="link-menu">PlayStation2</a></li>
                         <li class="item-menu"> <a href="../ps3/index.php" class="link-menu">PlayStation3</a></li>
                         <li class="item-menu"> <a href="../emuladores/index.php" class="link-menu">Emuladores</a></li>
						 <li class="item-menu"> <a href="../extras/index.php" class="link-menu">Extras</a></li>
                </ul></label></div>
            </div>
          </caption>




<div class="barraBase">
  <div class="blocoDadosInputs">
  <h3 class="tituloRed"> Cadastrar INFO da HOME na Database </h3>
        <form class="form-horizontal" action="create.php" method="post"  autocomplete="off" enctype="multipart/form-data">


          <!-- =====   informacao ======   -->
          <div class="wrap-input100 validate-input m-b-16" >
            <div class="control-group  <?php echo !empty($informacaoErro) ? 'error ' : ''; ?>">
            <label class="titulo">INFORMAÇÃO AOS USUÁRIOS NA HOMEPAGE</label>
             <div class="controls">
            <input class="input100" type="text" name="informacao" type="text" placeholder="Insira o informacao para usuários."
                                   value="<?php echo !empty($informacao) ? $informacao : ''; ?>">
                                   <?php if (!empty($informacaoErro)): ?>
                                <span class="text-danger"><?php echo $informacaoErro; ?></span>
                            <?php endif; ?>
            <span class="focus-input100"></span>
            </span>
          </div></div></div>

                  


                    <div class="form-actions">
                        <br/>
                        <button type="submit" class="login100-form-btn m-b-16">Adicionar</button>
                        <a href="index.php" type="btn" class="login100-form-btn m-b-16">Voltar</a>
                    </div>
                </form>
            </div></div>
        </div>
    </div>
</div>
</div>
<script src="https://code.jquery.com/jquery-3.3.1.js" integrity="sha256-2Kok7MbOyxpgUVvAk/HJ2jigOSYS2auK4Pfzbm7uH60="
        crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"
        integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49"
        crossorigin="anonymous"></script>
<!-- Latest compiled and minified JavaScript -->
<script src="../../../assets/js/bootstrap.min.js"></script>
</body>

</html>

