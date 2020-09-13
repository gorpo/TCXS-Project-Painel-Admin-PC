<!-- ████████╗ ██████╗██╗  ██╗███████╗    ██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗
     ╚══██╔══╝██╔════╝╚██╗██╔╝██╔════╝    ██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝
        ██║   ██║      ╚███╔╝ ███████╗    ██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║   
        ██║   ██║      ██╔██╗ ╚════██║    ██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║   
        ██║   ╚██████╗██╔╝ ██╗███████║    ██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║   
        ╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝   -->
<!-- @Gorpo Orko - 2020 -->
<?php
// Inicia a sessão
session_start();
?>


<!DOCTYPE html>
  <head>      

      <meta charset="UTF-8">
      <meta http-equiv="refresh" content="120">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <meta property="og:site_name" content="TCXS Project PlayStation3"/>
      <meta property="og:title" content="TCXS Project PlayStation3"/>
      <meta property="og:url" content="https://tcxsproject.com.br/"/>
      <meta property="og:description" content="Para adquirir sua versão mais atual da TCXS Project Store PKG para o console PlayStation3 clique no botão COMO ADQUIRIR e leia todas as regras, após isto já fazer sua doação. Aceitamos todos os tipos de pagamento como cartão, pagamento online"/>
      <meta property="og:image" content="../assets/images/logo.png"/>
      <link rel="shortcut icon" href="../assets/images/icon.png" />
      <script src="https://kit.fontawesome.com/a80232805f.js" crossorigin="anonymous"></script>
      <script src="../assets/js/funcoesLogin.js"></script>
      <link rel="stylesheet" type="text/css" href="../assets/css/style.css" />
      <link rel="stylesheet" type="text/css" href="../assets/css/login.css" />
      <title>TCXS Project STORE</title>
    </head>

<body style="background-color: #000000;"> <!-- class="bghome" -->
  <!-- bloqueio do click direito do mouse -->
<script>document.oncontextmenu = document.body.oncontextmenu = function() {return false;}</script>
  <!-- função php que retorna se o usuario teve erro ao logar -->
<div class="login">
  <div class="login-header">
    <br>
    <img class='logo' src="../assets/images/logo.png">
  </div>
  <div class="login-form">
     <?php
    if(isset($_SESSION['nao_autenticado'])):
  ?>
    <div class="notification is-danger" style="font-size:20px; color:red;"><b>Usuário não cadastrado</b></div>
  <?php
    endif;
    unset($_SESSION['nao_autenticado']);
  ?>
    <form action="login.php" method="POST" autocomplete="off">
    <input type="text" name="usuario" autocomplete="off"  placeholder="Usuário"/><br>
    <input type="password" name="senha" placeholder="Senha"/>
    <br>
    <button type="submit" id="btnhome" type="button" class="btnlogar m-b-16 ">Entrar</button>
  </div></form></div>

  </body>
</html>


 

