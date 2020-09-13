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
      <meta property="og:image" content="../../../assets/images/logo.png"/>
      <link rel="shortcut icon" href="../../../assets/images/icon.png" />
      <script src="https://kit.fontawesome.com/a80232805f.js" crossorigin="anonymous"></script>
      <link rel="stylesheet" type="text/css" href="../../../assets/css/style.css" />
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
      <link href="https://fonts.googleapis.com/css?family=Rubik&display=swap" rel="stylesheet">
      <script src="https://kit.fontawesome.com/af562a2a63.js" crossorigin="anonymous"></script>
      <title>TCXS Project STORE</title>
</head>
<body>

<div class="container">

        <!-- inicio da tabela -->




        <table>
          <caption>
            <div class="barraTopo">
              <img class="logo" src="../../../assets/images/logo_ps2.png"><br>
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
                        <li class="item-menu"> <a href="../infos/index.php" class="link-menu">PlayStation Infos</a></li>
                         <li class="item-menu"> <a href="../psp/index.php" class="link-menu">PlayStation PSP</a></li>
                         <li class="item-menu"> <a href="../ps1/index.php" class="link-menu">PlayStation1</a></li>
                         <li class="item-menu"> <a href="index.php" class="link-menu">PlayStation2</a></li>
                         <li class="item-menu"> <a href="../ps3/index.php" class="link-menu">PlayStation3</a></li>
                         <li class="item-menu"> <a href="../emuladores/index.php" class="link-menu">Emuladores</a></li>
						 <li class="item-menu"> <a href="../extras/index.php" class="link-menu">Extras</a></li>
                </ul></label></div>
            </div>
            <a href="create.php" type="btn" class="login100-form-btn m-b-16">ADICIONAR JOGO PS2</a>
          </caption>

        <!-- colunas do topo -->
          <thead>
              <tr>
                  <td scope="col">IMAGEM</td>
                  <td scope="col">DADOS</td>
                  <td scope="col">OPÇÕES</td>
              </tr>
          </thead>
          <tbody>

        <!-- ============================== CODIGO PHP MYSQL JOGOS PARA DOWNLOAD  ==============================   -->
  <?php
  include('../../../database.php');
  $pdo = Database::conectar();
  $sql = 'SELECT * FROM playstation_ps2 ORDER BY titulo ASC';

  foreach($pdo->query($sql)as $row)
  {   
      echo '<table> <tr> <td class="preto">';
      echo " <a href='javascript:#tcxsproject'". 'onclick="location.href='."'".$row['link']."'".'"'.'>';
      //echo '<a href="'.$row['link'].'">';
      echo '<img  class="caixa_imagem"  src="../../../assets/images/ps2/'.$row['imagem'].'"/> </td>';
      echo '<td class="preto"> <h2 class="titulo_jogo">'.$row['titulo'].'</h2>';
      echo '<p class="textoJogo">'.$row['descricao'].'</p> </a>';
      echo '<td  data-label="" class="preto">';
      echo '<a class="botaoIcones" href="read.php?id='.$row['id'].'"><i class="fas fa-info" aria-hidden="true"></i></a>';
      echo ' ';
      echo '<a class="botaoIcones" href="update.php?id='.$row['id'].'"><i class="fas fa-pencil-square-o" aria-hidden="true" ></i></a>';
      echo ' ';
      echo '<a  class="botaoIcones" href="delete.php?id='.$row['id'].'"><i class="fas fa-trash" aria-hidden="true"></i></a>';
      echo '</td>';
      echo '</td> </tr> </table>  ';
  }
  Database::desconectar();
  ?>


                    </tbody>
                </table>
            </div>
        </div>
    <script src="https://code.jquery.com/jquery-3.3.1.js" integrity="sha256-2Kok7MbOyxpgUVvAk/HJ2jigOSYS2auK4Pfzbm7uH60=" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <!-- Latest compiled and minified JavaScript -->
    <script src="../../../assets/js/bootstrap.min.js"></script>
</body>

</html>
