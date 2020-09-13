<!-- ████████╗ ██████╗██╗  ██╗███████╗    ██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗
     ╚══██╔══╝██╔════╝╚██╗██╔╝██╔════╝    ██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝
        ██║   ██║      ╚███╔╝ ███████╗    ██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║   
        ██║   ██║      ██╔██╗ ╚════██║    ██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║   
        ██║   ╚██████╗██╔╝ ██╗███████║    ██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║   
        ╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝   -->
<!-- @Gorpo Orko - 2020 -->

<?php
session_start();
//inclui o arquivo de conexao com banco de dados
include('../../conexao.php');

//nome usuario
$usuario =  $_SESSION['nome'];

//verifica se esta logado senao redireciona
if(!$_SESSION['nome']) {
    header('Location: ../../nao_logado.php');
  exit();  
}






$usuario = mysqli_real_escape_string($conexao, $_SESSION['nome']);
$sql= "SELECT (nivel) from playstation_users where usuario = '$usuario'"; //pega o usuario no banco de dados
$sqldata = mysqli_query($conexao, $sql); //conexao com a query
$rowdata = mysqli_fetch_array($sqldata); //array da variavel
$nivel = $rowdata['nivel']; //seleciona a data do usuario

//SE NAO FOR ADM É REDIRECIONADO PARA CAMINHO SETADO
if($nivel != 'admin') {
    header('Location: ../../nao_logado.php');
  exit();  
}

?>



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
      <meta property="og:image" content="../../assets/images/logo.png"/>
      <link rel="shortcut icon" href="../../assets/images/icon.png" />
      <script src="https://kit.fontawesome.com/a80232805f.js" crossorigin="anonymous"></script>
      <link rel="stylesheet" type="text/css" href="../../assets/css/style.css" />
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
      <link href="https://fonts.googleapis.com/css?family=Rubik&display=swap" rel="stylesheet">
      <script src="https://kit.fontawesome.com/af562a2a63.js" crossorigin="anonymous"></script>
      <title>TCXS Project STORE</title>
</head>
<body>

<div class="container">

        <!-- inicio da tabela -->

          <caption>
            <div class="barraTopo">
              <img class="logo" src="../../assets/images/logo_painel.png"><br>
                <!-- BARRA DE NAVEGAÇÃO DOS MENUS -->
                <div class="menu-content"> <label class="open-menu-all" for="open-menu-all">
                     <input class="input-menu-all" id="open-menu-all" type="checkbox" name="menu-open" />
                        <div class="navegacao-mobile">
                          <span class="linha-menu"></span>
                          <span class="linha-menu"></span>
                          <span class="linha-menu"></span>
                        </div>
                <ul class="list-menu" >
                          <li class="item-menu"> <a href="cadastro_usuarios.php" class="link-menu">Cadastro Usuarios</a></li>
                          <li class="item-menu"> <a href="consulta_usuarios.php" class="link-menu">Verifica Usuarios</a></li>
                          <li class="item-menu"> <a href="infos/index.php" class="link-menu">PlayStation Infos</a></li>
                         <li class="item-menu"> <a href="psp/index.php" class="link-menu">PlayStation PSP</a></li>
                         <li class="item-menu"> <a href="ps1/index.php" class="link-menu">PlayStation1</a></li>
                         <li class="item-menu"> <a href="ps2/index.php" class="link-menu">PlayStation2</a></li>
                         <li class="item-menu"> <a href="ps3/index.php" class="link-menu">PlayStation3</a></li>
                         <li class="item-menu"> <a href="emuladores/index.php" class="link-menu">Emuladores</a></li>
						 <li class="item-menu"> <a href="extras/index.php" class="link-menu">Extras</a></li>
                </ul></label></div>
            </div>
          </caption>

        <div class="barraBase">
          <div class="blocoDadosInputs">
          <h2 class="tituloWhiteHome">Bem vindo <?php echo  $usuario ?> <br> Painel Administrador V:1.0</h2>
          <br>
          <a href="cadastro_usuarios.php" type="btn" class="login100-form-btn m-b-16 ">Cadastro Usuarios</a>
          <a href="consulta_usuarios.php" type="btn" class="login100-form-btn m-b-16">Verifica Usuarios</a>
          <a href="infos/index.php" type="btn" class="login100-form-btn m-b-16">PlayStation Infos</a>
          <a href="psp/index.php" type="btn" class="login100-form-btn m-b-16">PlayStation PSP</a>
          <a href="ps1/index.php" type="btn" class="login100-form-btn m-b-16">PlayStation1</a>
          <a href="ps2/index.php" type="btn" class="login100-form-btn m-b-16">PlayStation2</a>
          <a href="ps3/index.php" type="btn" class="login100-form-btn m-b-16">PlayStation3</a>
          <a href="emuladores/index.php" type="btn" class="login100-form-btn m-b-16">Emuladores</a>
          <a href="extras/index.php" type="btn" class="login100-form-btn m-b-16">Extras</a>
          


        </div>
        


                </table>
            </div>
        </div>
    <script src="https://code.jquery.com/jquery-3.3.1.js" integrity="sha256-2Kok7MbOyxpgUVvAk/HJ2jigOSYS2auK4Pfzbm7uH60=" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <!-- Latest compiled and minified JavaScript -->
    <script src="../../assets/js/bootstrap.min.js"></script>
</body>

</html>
