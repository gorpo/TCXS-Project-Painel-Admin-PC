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
//inclui o arquivo de conexao com banco de dados
include('../conexao.php');

//conexao com banco de dados para pegar a data
$usuario = mysqli_real_escape_string($conexao, $_SESSION['nome']);
$sql= "SELECT (data_cadastro) from usuarios where usuario = '$usuario'"; //pega o usuario no banco de dados
$sqldata = mysqli_query($conexao, $sql); //conexao com a query
$rowdata = mysqli_fetch_array($sqldata); //array da variavel
$datacadastrada = $rowdata['data_cadastro']; //seleciona a data do usuario

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
      <meta property="og:image" content="imagens/logo.png"/>
      <link rel="shortcut icon" href="imagens/icon.png" />
      <script src="https://kit.fontawesome.com/a80232805f.js" crossorigin="anonymous"></script>
      <link rel="stylesheet" href="css/bootstrap.min.css">   
      <link rel="stylesheet" type="text/css" href="css/tooplate-style.css">
      <link rel="stylesheet" type="text/css" href="css/style.css" />
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
                <a href='index.php'><img class="logo" src="imagens/logo2.png" si></a> 
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
                    <li class="tm-nav-item"><a href="https://tcxsproject.com.br/doadores/" class="tm-nav-item-link tm-button">Guia para Membros</a></li>
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

<!-- ============================== INICIO DOS JOGOS PARA DOWNLOAD ABAIXO ==============================   -->
 <div class="tm-main-content">
<!-- ============================== INICIO DOS JOGOS PARA DOWNLOAD ABAIXO ==============================   -->

<!--  inicio: EMULADORES -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/sqi9t251n8j8pxa/UP0000-SLUS20223_00-PS2CLASSICS00000.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/emuladores/retroarch.jpg'/> </td>
<td> <h2 class="titulo_jogo">Retroarch</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PS3</p> </a>
</td> </tr> </table> </div> 
<!--  fim: EMULADORES -->

<!--  inicio: EMULADORES -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/d4zlz6ey1xcm989/UP0000-SLUS00000_00-PS2CLASSICS00000.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/emuladores/pgen.jpg'/> </td>
<td> <h2 class="titulo_jogo">Mega Drive: PGEN</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PS3</p> </a>
</td> </tr> </table> </div> 
<!--  fim: EMULADORES -->

<!--  inicio: EMULADORES -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/q4miivo3x1ri61h/UP0000-SLUS00001_00-PS2CLASSICS00000.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/emuladores/snes.jpg'/> </td>
<td> <h2 class="titulo_jogo">Super Nintendo: SnesStation</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PS3</p> </a>
</td> </tr> </table> </div> 
<!--  fim: EMULADORES -->


<!--  inicio: EMULADORES -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/kjlgbgfvhf7yc3f/UP9000-SLUS00886_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/emuladores/nes.jpg'/> </td>
<td> <h2 class="titulo_jogo">Nintendo System: NES</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PS3</p> </a>
</td> </tr> </table> </div> 
<!--  fim: EMULADORES -->


<!--  inicio: EMULADORES -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/vy2uv77opfpkd9v/EP0000-SLES66654_00-PS2CLASSICS00000.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/emuladores/mastersystem.jpg'/> </td>
<td> <h2 class="titulo_jogo">Master System</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PS3</p> </a>
</td> </tr> </table> </div> 
<!--  fim: EMULADORES -->

<!--  inicio: EMULADORES -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/sqi9t251n8j8pxa/UP0000-SLUS20223_00-PS2CLASSICS00000.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/emuladores/gba.jpg'/> </td>
<td> <h2 class="titulo_jogo">Game Boy Advanced</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PS3</p> </a>
</td> </tr> </table> </div> 
<!--  fim: EMULADORES -->


<!--  inicio: EMULADORES -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/fspf83xq224jf5j/UP9000-SLUS00777_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/emuladores/atari.jpg'/> </td>
<td> <h2 class="titulo_jogo">Atari V1</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PS3</p> </a>
</td> </tr> </table> </div> 
<!--  fim: EMULADORES -->



<!--  inicio: EMULADORES -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/p8ggd3q8kej31hq/UP0000-SLUS20273_00-PS2CLASSICS00000.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/emuladores/atari.jpg'/> </td>
<td> <h2 class="titulo_jogo">Atari V2</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PS3</p> </a>
</td> </tr> </table> </div> 
<!--  fim: EMULADORES -->

<!--  inicio: EMULADORES -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/rqyfa2o21v5kl7d/UP0000-SLUS21076_00-PS2CLASSICS00000.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/emuladores/atari.jpg'/> </td>
<td> <h2 class="titulo_jogo">Atari V3</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PS3</p> </a>
</td> </tr> </table> </div> 
<!--  fim: EMULADORES -->




<!-- final do container-fluid todo conteudo deve ficar antes desta div -->   
</div></div>
<footer class="tm-footer text-right" "><font color="#91060d" face="VT323" size="5"><font color="91060d"><b> TCXS Project PlayStation3 Store   |  2020   |   HAN HEN CFW   </b></font></footer> 
</div>
</body>
</html>