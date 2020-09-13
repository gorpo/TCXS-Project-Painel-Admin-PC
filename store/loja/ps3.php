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
                    <li class="tm-nav-item"><a href="ps3.php" class="tm-nav-item-link tm-button active">PlayStation3</a></li>
                    <li class="tm-nav-item"><a href="emuladores.php" class="tm-nav-item-link tm-button">Emuladores</a></li>
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
$sql = 'SELECT * FROM playstation_ps3 ORDER BY titulo ASC';
foreach($pdo->query($sql)as $row)
{
  echo '<div class="media-body  tm-bg-light-gray"><table> <tr> <td>';
  echo '<div class="dropdown"> <img  class="caixa_imagem" class="dropbtn" src="../assets/images/ps3/'.$row['imagem'].'" width="170" width="170"/>';
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

  echo	'</div> </div> </td>  <td><h2 class="titulo_jogo">'.$row['titulo'].'</h2>';
  echo  '<p class="textoJogo">'.$row['descricao'].'</p> </a> </td> </tr> </table> </div>';
}
Database::desconectar();
?>




<!-- final do container-fluid todo conteudo deve ficar antes desta div -->   
</div></div>
<footer class="tm-footer text-right" "><font color="#91060d" face="VT323" size="5"><font color="91060d"><b> TCXS Project PlayStation3 Store   |  2020   |   HAN HEN CFW   </b></font></footer> 
</div>
</body>
</html>