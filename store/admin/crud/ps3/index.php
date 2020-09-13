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
} ?>

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
              <img class="logo" src="../../../assets/images/logo_ps3.png"><br>
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
                         <li class="item-menu"> <a href="../ps2/index.php" class="link-menu">PlayStation2</a></li>
                         <li class="item-menu"> <a href="index.php" class="link-menu">PlayStation3</a></li>
                         <li class="item-menu"> <a href="../emuladores/index.php" class="link-menu">Emuladores</a></li>
						 <li class="item-menu"> <a href="../extras/index.php" class="link-menu">Extras</a></li>
                </ul></label></div>
            </div>
            <a href="create.php" type="btn" class="login100-form-btn m-b-16">ADICIONAR JOGO PS3</a>
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
        $sql = 'SELECT * FROM playstation_ps3 ORDER BY titulo ASC';
        foreach($pdo->query($sql)as $row)
        {
          echo '<table> <tr> <td class="preto">';
          echo '<div class="dropdown"> <img  class="caixa_imagemPs3crud" class="dropbdtn" src="../../../assets/images/ps3/'.$row['imagem'].'" width="170" width="170"/>';
          echo '<div class="dropdown-content">';
          
          //FUNÇÕES PARA MOSTRAR OS BOTOES QUANTOS EXISTIR
          if ($row['link1'] != "---") {
                echo " <a href='javascript:#tcxsproject'". 'onclick="location.href='."'".$row['link1']."'".'"'.'>'.$row['titulo'].' | Parte 1</a>';
                }
                
        if ($row['link2'] != "---") {
                echo " <a href='javascript:#tcxsproject'". 'onclick="location.href='."'".$row['link2']."'".'"'.'>'.$row['titulo'].' | Parte 2</a>';
                }
                
        if ($row['link3'] != "---") {
                echo " <a href='javascript:#tcxsproject'". 'onclick="location.href='."'".$row['link3']."'".'"'.'>'.$row['titulo'].' | Parte 3</a>';
                }
                
        if ($row['link4'] != "---") {
                echo " <a href='javascript:#tcxsproject'". 'onclick="location.href='."'".$row['link4']."'".'"'.'>'.$row['titulo'].' | Parte 4</a>';
                }
                
        if ($row['link5'] != "---") {
                echo " <a href='javascript:#tcxsproject'". 'onclick="location.href='."'".$row['link5']."'".'"'.'>'.$row['titulo'].' | Parte 5</a>';
                }
                
        if ($row['link6'] != "---") {
                echo " <a href='javascript:#tcxsproject'". 'onclick="location.href='."'".$row['link6']."'".'"'.'>'.$row['titulo'].' | Parte 6</a>';
                }
                
        if ($row['link7'] != "---") {
                echo " <a href='javascript:#tcxsproject'". 'onclick="location.href='."'".$row['link7']."'".'"'.'>'.$row['titulo'].' | Parte 7</a>';
                }
                
        if ($row['link8'] != "---") {
                echo " <a href='javascript:#tcxsproject'". 'onclick="location.href='."'".$row['link8']."'".'"'.'>'.$row['titulo'].' | Parte 8</a>';
                }
                
        if ($row['link9'] != "---") {
                echo " <a href='javascript:#tcxsproject'". 'onclick="location.href='."'".$row['link9']."'".'"'.'>'.$row['titulo'].' | Parte 9</a>';
                }
                
        if ($row['link10'] != "---") {
                echo " <a href='javascript:#tcxsproject'". 'onclick="location.href='."'".$row['link10']."'".'"'.'>'.$row['titulo'].' | Parte 10</a>';
                }
                
        if ($row['link11'] != "---") {
                echo " <a href='javascript:#tcxsproject'". 'onclick="location.href='."'".$row['link11']."'".'"'.'>'.$row['titulo'].' | Parte 11</a>';
                }
                
        if ($row['link12'] != "---") {
                echo " <a href='javascript:#tcxsproject'". 'onclick="location.href='."'".$row['link12']."'".'"'.'>'.$row['titulo'].' | Parte 12</a>';
                }
                
        if ($row['link13'] != "---") {
                echo " <a href='javascript:#tcxsproject'". 'onclick="location.href='."'".$row['link13']."'".'"'.'>'.$row['titulo'].' | Parte 13</a>';
                }
                
        if ($row['link14'] != "---") {
                echo " <a href='javascript:#tcxsproject'". 'onclick="location.href='."'".$row['link14']."'".'"'.'>'.$row['titulo'].' | Parte 14</a>';
                }
                
        if ($row['link15'] != "---") {
                echo " <a href='javascript:#tcxsproject'". 'onclick="location.href='."'".$row['link15']."'".'"'.'>'.$row['titulo'].' | Parte 15</a>';
                }
                
        if ($row['link16'] != "---") {
                echo " <a href='javascript:#tcxsproject'". 'onclick="location.href='."'".$row['link16']."'".'"'.'>'.$row['titulo'].' | Parte 16</a>';
                }
                
        if ($row['link17'] != "---") {
                echo " <a href='javascript:#tcxsproject'". 'onclick="location.href='."'".$row['link17']."'".'"'.'>'.$row['titulo'].' | Parte 17</a>';
                }
                
        if ($row['link18'] != "---") {
                echo " <a href='javascript:#tcxsproject'". 'onclick="location.href='."'".$row['link18']."'".'"'.'>'.$row['titulo'].' | Parte 18</a>';
                }
                
        if ($row['link19'] != "---") {
                echo " <a href='javascript:#tcxsproject'". 'onclick="location.href='."'".$row['link19']."'".'"'.'>'.$row['titulo'].' | Parte 19</a>';
                }
                
        if ($row['link20'] != "---") {
                echo " <a href='javascript:#tcxsproject'". 'onclick="location.href='."'".$row['link20']."'".'"'.'>'.$row['titulo'].' | Parte 20</a>';
                }
                
        if ($row['link21'] != "---") {
                echo " <a href='javascript:#tcxsproject'". 'onclick="location.href='."'".$row['link21']."'".'"'.'>'.$row['titulo'].' | Parte 21</a>';
                }
                
        if ($row['link22'] != "---") {
                echo " <a href='javascript:#tcxsproject'". 'onclick="location.href='."'".$row['link22']."'".'"'.'>'.$row['titulo'].' | Parte 22</a>';
                }
                
        if ($row['link23'] != "---") {
                echo " <a href='javascript:#tcxsproject'". 'onclick="location.href='."'".$row['link23']."'".'"'.'>'.$row['titulo'].' | Parte 23</a>';
                }
                
        if ($row['link24'] != "---") {
                echo " <a href='javascript:#tcxsproject'". 'onclick="location.href='."'".$row['link24']."'".'"'.'>'.$row['titulo'].' | Parte 24</a>';
                }
                
        if ($row['link25'] != "---") {
                echo " <a href='javascript:#tcxsproject'". 'onclick="location.href='."'".$row['link25']."'".'"'.'>'.$row['titulo'].' | Parte 25</a>';
                }
                
        if ($row['link26'] != "---") {
                echo " <a href='javascript:#tcxsproject'". 'onclick="location.href='."'".$row['link26']."'".'"'.'>'.$row['titulo'].' | Parte 26</a>';
                }
                
        if ($row['link27'] != "---") {
                echo " <a href='javascript:#tcxsproject'". 'onclick="location.href='."'".$row['link27']."'".'"'.'>'.$row['titulo'].' | Parte 27</a>';
                }
                
        if ($row['link28'] != "---") {
                echo " <a href='javascript:#tcxsproject'". 'onclick="location.href='."'".$row['link28']."'".'"'.'>'.$row['titulo'].' | Parte 28</a>';
                }
                
        if ($row['link29'] != "---") {
                echo " <a href='javascript:#tcxsproject'". 'onclick="location.href='."'".$row['link29']."'".'"'.'>'.$row['titulo'].' | Parte 29</a>';
                }
                
        if ($row['link30'] != "---") {
                echo " <a href='javascript:#tcxsproject'". 'onclick="location.href='."'".$row['link30']."'".'"'.'>'.$row['titulo'].' | Parte 30</a>';
                }

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




<!-- final do container-fluid todo conteudo deve ficar antes desta div -->   
</div></div>
<footer class="tm-footer text-right" "><font color="#91060d" face="VT323" size="5"><font color="91060d"><b> TCXS Project PlayStation3 Store   |  2020   |   HAN HEN CFW   </b></font></footer> 
</div>
</body>
</html>