<!-- ████████╗ ██████╗██╗  ██╗███████╗    ██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗
    ╚══██╔══╝██╔════╝╚██╗██╔╝██╔════╝    ██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝
       ██║   ██║      ╚███╔╝ ███████╗    ██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║   
       ██║   ██║      ██╔██╗ ╚════██║    ██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║   
       ██║   ╚██████╗██╔╝ ██╗███████║    ██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║   
       ╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝   -->
<!-- @Gorpo Orko - 2020 -->



<!-- ==================================== INICIO DO PHP ======================================== -->
<?php
session_start();
//inclui o arquivo de conexao com Database de dados
include('../conexao.php');

//conexao com Database de dados para pegar a data
$usuario = mysqli_real_escape_string($conexao, $_SESSION['nome']);
$sql= "SELECT (cadastro) from playstation_users where usuario = '$usuario'"; //pega o usuario no Database de dados
$sqldata = mysqli_query($conexao, $sql); //conexao com a query
$rowdata = mysqli_fetch_array($sqldata); //array da variavel
$datacadastrada = $rowdata['cadastro']; //seleciona a data do usuario

//formata a data de entrada do usuario
$strdata = strtotime($datacadastrada);
$data_entrada_usuario = date('d-m-Y', $strdata);

//formata a data de expiração do usuario
$data_expira = strtotime($datacadastrada. '+33 days');
$data_expira_formatada = date('d-m-Y', $data_expira);
if(!$_SESSION['nome']) {
  header('Location: ../nao_logado.php');
  exit();
}
?>
<!-- ==================================== INICIO DO PHP ======================================== -->



<!-- ==================================== INICIO DO HTML ======================================== -->
<!DOCTYPE html>
<html lang="en">
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
      <link rel="stylesheet" href="../assets/css/bootstrap_loja.min.css">   
      <link rel="stylesheet" type="text/css" href="../assets/css/tooplate-style_loja.css">
      <link rel="stylesheet" type="text/css" href="../assets/css/style_loja.css" />
      <title>TCXS Project PlayStation3 Store</title>                                
</head>
<body>

<!-- ======= INICIO DO CORPO ====== -->    
<div class="container-fluid">
    <div class="tm-body">

    <!-- ===========================  MENU PRINCIPAL ====================================== -->
    <div class="tm-sidebar sticky">
        <section id="welcome" class="tm-content-box tm-banner margin-b-15">
            <!--LOGOTIPO TCXS PROJECT -->
            <div class="banner_logotipo">
                <a href='index.php'><img class="logo" src="../assets/images/logo2.png" si></a> 
            </div>              

            <!-- ==================  MENUS DA ESQUERDA ===================================  -->
            <nav class="tm-main-nav">
                <ul class="tm-main-nav-ul">
                    <li class="tm-nav-item"><a href="index.php" class="tm-nav-item-link tm-button ">Informações</a></li>
                    <li class="tm-nav-item"><a href="psp.php" class="tm-nav-item-link tm-button ">PlayStation PSP</a></li>
                    <li class="tm-nav-item"><a href="ps1.php" class="tm-nav-item-link tm-button ">PlayStation1</a></li>
                    <li class="tm-nav-item"><a href="ps2.php" class="tm-nav-item-link tm-button ">PlayStation2</a></li>
                    <li class="tm-nav-item"><a href="ps3.php" class="tm-nav-item-link tm-button ">PlayStation3</a></li>
                    <li class="tm-nav-item"><a href="emuladores.php" class="tm-nav-item-link tm-button active">Emuladores</a></li>
                    <li class="tm-nav-item"><a href="extras.php" class="tm-nav-item-link tm-button">Extras</a></li>
                    <li class="tm-nav-item"><a href="https://tcxsproject.com.br/dev/ps3xploit.com/" class="tm-nav-item-link tm-button">PS3Xploit</a></li>
                </ul>
            </nav>
            <div class="banner_infos"><div class="dados_user">
Bem vindo <?php echo  $usuario ?><br>
Seu IP: <?php echo $_SERVER['REMOTE_ADDR'];?><br>
Entrada: <?php echo  $data_entrada_usuario ?><br>
Expiração: <?php echo  $data_expira_formatada ?><br>
            </div></div>
        </section>
    </div>
 <div class="tm-main-content">
<!-- ============================== CODIGO PHP MYSQL JOGOS PARA DOWNLOAD  ==============================   -->
<?php
  include('../database.php');
  $pdo = Database::conectar();
  $sql = 'SELECT * FROM playstation_emuladores ORDER BY titulo ASC';

  foreach($pdo->query($sql)as $row)
  {
      echo '<div class="media-body  tm-bg-light-gray"><table> <tr> <td>';
      echo " <a href='javascript:#tcxsproject'". 'onclick="location.href='."'".$row['link']."'".'"'.'>';
      //echo '<a href="'.$row['link'].'">';
      echo '<img  class="caixa_imagem"  src="../assets/images/emuladores/'.$row['imagem'].'"/> </td>';
      echo '<td> <h2 class="titulo_jogo">'.$row['titulo'].'</h2>';
      echo '<p class="textoJogo">'.$row['descricao'].'</p> </a>';
      echo '</td> </tr> </table> </div> ';
  }
  Database::desconectar();
  ?>


<!-- final do container-fluid todo conteudo deve ficar antes desta div -->   
</div></div>
<footer class="tm-footer text-right" "><font color="#91060d" face="VT323" size="5"><font color="91060d"><b> TCXS Project PlayStation3 Store   |  2020   |   HAN HEN CFW   </b></font></footer> 
</div>
</body>
</html>