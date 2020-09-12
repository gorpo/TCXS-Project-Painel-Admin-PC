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
                    <li class="tm-nav-item"><a href="psp.php" class="tm-nav-item-link tm-button active">PlayStation PSP</a></li>
                    <li class="tm-nav-item"><a href="ps1.php" class="tm-nav-item-link tm-button ">PlayStation1</a></li>
                    <li class="tm-nav-item"><a href="ps2.php" class="tm-nav-item-link tm-button">PlayStation2</a></li>
                    <li class="tm-nav-item"><a href="ps3.php" class="tm-nav-item-link tm-button">PlayStation3</a></li>
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



<!-- id:0 inicio:  Air Conflicts: Aces of World War 2  | TCXS Project PSP -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/8ykm4hlzxf985hk/PSPPS3-ULUS10404_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/psp/airconflicts2.jpg'/> </td>
<td> <h2 class="titulo_jogo"> Air Conflicts: Aces of World War 2 </h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PSP</p> </a>
</td> </tr> </table> </div> 
<!-- id:0 fim:  Air Conflicts: Aces of World War 2  | TCXS Project PSP -->


<!-- id:1 inicio:  Armored Core: Formula Front  | TCXS Project PSP -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/j5r9n7sq7dsiulu/PSPPS3-ULJS00003_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/psp/armoredcoreformula.jpg'/> </td>
<td> <h2 class="titulo_jogo"> Armored Core: Formula Front </h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PSP</p> </a>
</td> </tr> </table> </div> 
<!-- id:1 fim:  Armored Core: Formula Front  | TCXS Project PSP -->


<!-- id:2 inicio:  Astonishia Story  | TCXS Project PSP -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/umn45hsdkp8cdv6/PSPPS3-ULUS10083_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/psp/astonishia.jpg'/> </td>
<td> <h2 class="titulo_jogo"> Astonishia Story </h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PSP</p> </a>
</td> </tr> </table> </div> 
<!-- id:2 fim:  Astonishia Story  | TCXS Project PSP -->


<!-- id:3 inicio:  Beats  | TCXS Project PSP -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/9b4n9njyhe4g9t6/PSPPS3-NPEG00001_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/psp/beats.jpg'/> </td>
<td> <h2 class="titulo_jogo"> Beats </h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PSP</p> </a>
</td> </tr> </table> </div> 
<!-- id:3 fim:  Beats  | TCXS Project PSP -->


<!-- id:4 inicio:  Ben 10: Alien Force  | TCXS Project PSP -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/abpzpsmy2lffqr2/PSPPS3-ULUS10387_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/psp/benalien.jpg'/> </td>
<td> <h2 class="titulo_jogo"> Ben 10: Alien Force </h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PSP</p> </a>
</td> </tr> </table> </div> 
<!-- id:4 fim:  Ben 10: Alien Force  | TCXS Project PSP -->


<!-- id:5 inicio:  Blade Dancer: Lineage of Light  | TCXS Project PSP -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/8td4rakag7tl0zz/PSPPS3-ULUS10124_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/psp/bladedancer.jpg'/> </td>
<td> <h2 class="titulo_jogo"> Blade Dancer: Lineage of Light </h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PSP</p> </a>
</td> </tr> </table> </div> 
<!-- id:5 fim:  Blade Dancer: Lineage of Light  | TCXS Project PSP -->


<!-- id:6 inicio:  Catlevania Dracula X Chronicles  | TCXS Project PSP -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/1vl6v9pq5iqnmgx/PSPPS3-ULUS10277_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/psp/castlevaniadraculaxchronicles.jpg'/> </td>
<td> <h2 class="titulo_jogo"> Catlevania Dracula X Chronicles </h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PSP</p> </a>
</td> </tr> </table> </div> 
<!-- id:6 fim:  Catlevania Dracula X Chronicles  | TCXS Project PSP -->


<!-- id:7 inicio:  Class of Heroes  | TCXS Project PSP -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/i1dmmrytwrb0ncl/PSPPS3-ULUS10396_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/psp/classofheroes.jpg'/> </td>
<td> <h2 class="titulo_jogo"> Class of Heroes </h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PSP</p> </a>
</td> </tr> </table> </div> 
<!-- id:7 fim:  Class of Heroes  | TCXS Project PSP -->


<!-- id:8 inicio:  Crash  | TCXS Project PSP -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/g3fh3md6cvfb1hd/PSPPS3-ULUS10377_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/psp/crashmom.jpg'/> </td>
<td> <h2 class="titulo_jogo"> Crash </h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PSP</p> </a>
</td> </tr> </table> </div> 
<!-- id:8 fim:  Crash  | TCXS Project PSP -->


<!-- id:9 inicio:  Dead Head Fred  | TCXS Project PSP -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/zjh68al7q5t15x2/PSPPS3-ULUS10495_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/psp/deadheadfred.jpg'/> </td>
<td> <h2 class="titulo_jogo"> Dead Head Fred </h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PSP</p> </a>
</td> </tr> </table> </div> 
<!-- id:9 fim:  Dead Head Fred  | TCXS Project PSP -->


<!-- id:10 inicio:  Exit 2  | TCXS Project PSP -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/link_do_jogo.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/psp/exit2.jpg'/> </td>
<td> <h2 class="titulo_jogo"> Exit 2 </h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PSP</p> </a>
</td> </tr> </table> </div> 
<!-- id:10 fim:  Exit 2  | TCXS Project PSP -->


<!-- id:11 inicio:  Fading Shadows  | TCXS Project PSP -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/c0fde57apeqskme/PSPPS3-ULES00285_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/psp/fadings.jpg'/> </td>
<td> <h2 class="titulo_jogo"> Fading Shadows </h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PSP</p> </a>
</td> </tr> </table> </div> 
<!-- id:11 fim:  Fading Shadows  | TCXS Project PSP -->


<!-- id:12 inicio:  Final Fantasy: Dissidia  | TCXS Project PSP -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/hic90fyynvkkmmk/PSPPS3-ULUS10437_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/psp/ffdissidia.jpg'/> </td>
<td> <h2 class="titulo_jogo"> Final Fantasy: Dissidia </h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PSP</p> </a>
</td> </tr> </table> </div> 
<!-- id:12 fim:  Final Fantasy: Dissidia  | TCXS Project PSP -->


<!-- id:13 inicio:  Final Fantasy: VII Crisis Core  | TCXS Project PSP -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/c0fde57apeqskme/PSPPS3-ULES00285_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/psp/ffcrisiscore.jpg'/> </td>
<td> <h2 class="titulo_jogo"> Final Fantasy: VII Crisis Core </h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PSP</p> </a>
</td> </tr> </table> </div> 
<!-- id:13 fim:  Final Fantasy: VII Crisis Core  | TCXS Project PSP -->


<!-- id:14 inicio:  Formula 1: 2009  | TCXS Project PSP -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/lenuson5qaqr8dc/PSPPS3-ULES01355_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/psp/f12009.jpg'/> </td>
<td> <h2 class="titulo_jogo"> Formula 1: 2009 </h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PSP</p> </a>
</td> </tr> </table> </div> 
<!-- id:14 fim:  Formula 1: 2009  | TCXS Project PSP -->


<!-- id:15 inicio:  Hellboy: The Science of Evil  | TCXS Project PSP -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/nwoyfxwlpzzosm2/PSPPS3-ULES00827_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/psp/hellboythescience.jpg'/> </td>
<td> <h2 class="titulo_jogo"> Hellboy: The Science of Evil </h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PSP</p> </a>
</td> </tr> </table> </div> 
<!-- id:15 fim:  Hellboy: The Science of Evil  | TCXS Project PSP -->


<!-- id:16 inicio:  Jeanne D'Arc  | TCXS Project PSP -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/lenuson5qaqr8dc/PSPPS3-ULES01355_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/psp/jeannedarc.jpg'/> </td>
<td> <h2 class="titulo_jogo"> Jeanne D'Arc </h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PSP</p> </a>
</td> </tr> </table> </div> 
<!-- id:16 fim:  Jeanne D'Arc  | TCXS Project PSP -->


<!-- id:17 inicio:  La Pucelle Ragnarok  | TCXS Project PSP -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/pdhlb8p4nrqkibq/PSPPS3-ULJS00244_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/psp/lapucelleragnarok.jpg'/> </td>
<td> <h2 class="titulo_jogo"> La Pucelle Ragnarok </h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PSP</p> </a>
</td> </tr> </table> </div> 
<!-- id:17 fim:  La Pucelle Ragnarok  | TCXS Project PSP -->


<!-- id:18 inicio:  Lunar: Silver Star Harmony  | TCXS Project PSP -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/oky9bxyz84itana/PSPPS3-ULUS10482_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/psp/lunar.jpg'/> </td>
<td> <h2 class="titulo_jogo"> Lunar: Silver Star Harmony </h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PSP</p> </a>
</td> </tr> </table> </div> 
<!-- id:18 fim:  Lunar: Silver Star Harmony  | TCXS Project PSP -->


<!-- id:19 inicio:  Mega Man Maverick Hunter X  | TCXS Project PSP -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/vntc0zivq6momuj/PSPPS3-ULUS10068_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/psp/megamanmx.jpg'/> </td>
<td> <h2 class="titulo_jogo"> Mega Man Maverick Hunter X </h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PSP</p> </a>
</td> </tr> </table> </div> 
<!-- id:19 fim:  Mega Man Maverick Hunter X  | TCXS Project PSP -->


<!-- id:20 inicio:  Metal Gear Ac!d 1  | TCXS Project PSP -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/lip0l0ceidqb36y/PSPPS3-ULUS10006_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/psp/mgsacid.jpg'/> </td>
<td> <h2 class="titulo_jogo"> Metal Gear Ac!d 1 </h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PSP</p> </a>
</td> </tr> </table> </div> 
<!-- id:20 fim:  Metal Gear Ac!d 1  | TCXS Project PSP -->


<!-- id:21 inicio:  Metal Slug XX  | TCXS Project PSP -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/ymsrnlwg4aokkew/PSPPS3-ULUS10495_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/psp/metalslugxx.jpg'/> </td>
<td> <h2 class="titulo_jogo"> Metal Slug XX </h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PSP</p> </a>
</td> </tr> </table> </div> 
<!-- id:21 fim:  Metal Slug XX  | TCXS Project PSP -->


<!-- id:22 inicio:  Prinny 1: Can I Really Be a Hero?  | TCXS Project PSP -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/hud7vusn8pnatrf/PSPPS3-ULUS10407_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/psp/prinny1.jpg'/> </td>
<td> <h2 class="titulo_jogo"> Prinny 1: Can I Really Be a Hero? </h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PSP</p> </a>
</td> </tr> </table> </div> 
<!-- id:22 fim:  Prinny 1: Can I Really Be a Hero?  | TCXS Project PSP -->


<!-- id:23 inicio:  Prinny 2: Dawn of Operation Panties, Dood!  | TCXS Project PSP -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/c5j55j8cx66u5eu/PSPPS3-ULUS10561_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/psp/prinny2.jpg'/> </td>
<td> <h2 class="titulo_jogo"> Prinny 2: Dawn of Operation Panties, Dood! </h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PSP</p> </a>
</td> </tr> </table> </div> 
<!-- id:23 fim:  Prinny 2: Dawn of Operation Panties, Dood!  | TCXS Project PSP -->


<!-- id:24 inicio:  Silent Hill Origins  | TCXS Project PSP -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/qouzncuofpup7j2/PSPPS3-ULUS10285_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/psp/silenthillorigins.jpg'/> </td>
<td> <h2 class="titulo_jogo"> Silent Hill Origins </h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PSP</p> </a>
</td> </tr> </table> </div> 
<!-- id:24 fim:  Silent Hill Origins  | TCXS Project PSP -->


<!-- id:25 inicio:  Soul Calibur: Broken Destiny  | TCXS Project PSP -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/tsycqnmmj9piak0/PSPPS3-ULES01298_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/psp/soulcaliburbrokendestiny.jpg'/> </td>
<td> <h2 class="titulo_jogo"> Soul Calibur: Broken Destiny </h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PSP</p> </a>
</td> </tr> </table> </div> 
<!-- id:25 fim:  Soul Calibur: Broken Destiny  | TCXS Project PSP -->


<!-- id:26 inicio:  Soul Eater: Battle Resonance  | TCXS Project PSP -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/7xykmok2d5i58nn/PSPPS3-ULJS00176_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/psp/souleater.jpg'/> </td>
<td> <h2 class="titulo_jogo"> Soul Eater: Battle Resonance </h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PSP</p> </a>
</td> </tr> </table> </div> 
<!-- id:26 fim:  Soul Eater: Battle Resonance  | TCXS Project PSP -->


<!-- id:27 inicio:  Spider Man 2  | TCXS Project PSP -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/3qhhzq7ohgjvci2/PSPPS3-ULES00022_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/psp/spiderman2.jpg'/> </td>
<td> <h2 class="titulo_jogo"> Spider Man 2 </h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PSP</p> </a>
</td> </tr> </table> </div> 
<!-- id:27 fim:  Spider Man 2  | TCXS Project PSP -->


<!-- id:28 inicio:  Star Wars: Battlefront 2  | TCXS Project PSP -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/ygyeic91sd7oc3p/PSPPS3-ULES00183_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/psp/starwarsbattlefront2.jpg'/> </td>
<td> <h2 class="titulo_jogo"> Star Wars: Battlefront 2 </h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PSP</p> </a>
</td> </tr> </table> </div> 
<!-- id:28 fim:  Star Wars: Battlefront 2  | TCXS Project PSP -->


<!-- id:29 inicio:  Strikers 1945 Plus  | TCXS Project PSP -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/nicbev3w69av7r4/PSPPS3-ULKS46198_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/psp/strikers1945plus.jpg'/> </td>
<td> <h2 class="titulo_jogo"> Strikers 1945 Plus </h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PSP</p> </a>
</td> </tr> </table> </div> 
<!-- id:29 fim:  Strikers 1945 Plus  | TCXS Project PSP -->


<!-- id:30 inicio:  Super Pocket Tennis  | TCXS Project PSP -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/tj7rzrb9saeduoc/PSPPS3-ULES00619_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/psp/superpt.jpg'/> </td>
<td> <h2 class="titulo_jogo"> Super Pocket Tennis </h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PSP</p> </a>
</td> </tr> </table> </div> 
<!-- id:30 fim:  Super Pocket Tennis  | TCXS Project PSP -->


<!-- id:31 inicio:  The 3rd Birthday  | TCXS Project PSP -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/link_do_jogo.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/psp/the3rd.jpg'/> </td>
<td> <h2 class="titulo_jogo"> The 3rd Birthday </h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PSP</p> </a>
</td> </tr> </table> </div> 
<!-- id:31 fim:  The 3rd Birthday  | TCXS Project PSP -->


<!-- id:32 inicio:  Valhalla Kinights 2  | TCXS Project PSP -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/1e73gscd5x8q6fm/PSPPS3-ULUS10366_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/psp/valhallaknights2.jpg'/> </td>
<td> <h2 class="titulo_jogo"> Valhalla Kinights 2 </h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PSP</p> </a>
</td> </tr> </table> </div> 
<!-- id:32 fim:  Valhalla Kinights 2  | TCXS Project PSP -->


<!-- id:33 inicio:  Wall | TCXS Project PSP -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/jna5djyhe7u2m8l/PSPPS3-ULES01072_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/psp/walle.jpg'/> </td>
<td> <h2 class="titulo_jogo"> Wall</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PSP</p> </a>
</td> </tr> </table> </div> 
<!-- id:33 fim:  Wall | TCXS Project PSP -->


<!-- final do container-fluid todo conteudo deve ficar antes desta div -->   
</div></div>
<footer class="tm-footer text-right" "><font color="#91060d" face="VT323" size="5"><font color="91060d"><b> TCXS Project PlayStation3 Store   |  2020   |   HAN HEN CFW   </b></font></footer> 
</div>
</body>
</html>