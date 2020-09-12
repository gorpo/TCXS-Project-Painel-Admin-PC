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
                    <li class="tm-nav-item"><a href="ps1.php" class="tm-nav-item-link tm-button active">PlayStation1</a></li>
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



<!-- id:0 inicio: 1Xtreme | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/rciydbdh5l7bvya/UP9000-SCUS94503_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/1xtreme.jpg'/> </td>
<td> <h2 class="titulo_jogo">1Xtreme</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:0 fim: 1Xtreme | TCXS Project PS1 -->


<!-- id:1 inicio: 3Xtreme | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/ib8157pwvirgqjh/UP9000-SCUS94231_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/3xtreme.jpg'/> </td>
<td> <h2 class="titulo_jogo">3Xtreme</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:1 fim: 3Xtreme | TCXS Project PS1 -->


<!-- id:2 inicio: Ace Combat 2 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/ptjalqzvcbns075/UP9000-SLUS00404_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/acecombat2.jpg'/> </td>
<td> <h2 class="titulo_jogo">Ace Combat 2</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:2 fim: Ace | TCXS Project PS1 -->


<!-- id:3 inicio: Adventures of Lomax | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/x6gsn7ll1sx0ndr/UP9000-SCUS94906_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/lomax.jpg'/> </td>
<td> <h2 class="titulo_jogo">Adventures of Lomax</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:3 fim: Adventures of Lomax | TCXS Project PS1 -->


<!-- id:4 inicio: Disney Aladin | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/5wnhbwcosy5m1rq/UP9000-SCES03008_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/aladdin.jpg'/> </td>
<td> <h2 class="titulo_jogo">Aladdin  La Venganza de Nasira</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:4 fim: Disney Aladin | TCXS Project PS1 -->


<!-- id:5 inicio: Alien Trilog | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/erkpjbktj4geijl/UP9000-SLUS00007_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/alientrilogy.jpg'/> </td>
<td> <h2 class="titulo_jogo">Alien Trilog</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:5 fim: Alien Trilog | TCXS Project PS1 -->


<!-- id:6 inicio: Alone in the Dark | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"> <table> <tr> <td>
<div class="dropdown"> <img  class="caixa_imagem" class="dropbtn" src="imagens/ps1/alone.jpg" width="170" width="170"/>
<div class="dropdown-content">
<a href="https://www.dropbox.com/s/6dhjjp0o0w9qwpn/UP9000-SLUS01201_00-0000000000000001.pkg?dl=1">CD1</a>  
<a href="https://www.dropbox.com/s/0isugqcd7f7a1v9/UP9000-SLUS01201_00-0000000000000001.pkg?dl=1">CD2</a> 
<td> <h2 class="titulo_jogo">Alone in the Dark</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:6 fim: Alone in the Dark | TCXS Project PS1 -->


<!-- id:7 inicio: Alundra | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/r02ysa4ulc9vx52/UP9000-SLUS00553_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/alundra.jpg'/> </td>
<td> <h2 class="titulo_jogo">Alundra</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:7 fim: Alundra | TCXS Project PS1 -->


<!-- id:8 inicio: Amerzone  O Testamento do Explorador | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"> <table> <tr> <td>
<div class="dropdown"> <img  class="caixa_imagem" class="dropbtn" src="imagens/ps1/amerzone.jpg" width="170" width="170"/>
<div class="dropdown-content">
<a href="https://www.dropbox.com/s/r02ysa4ulc9vx52/UP9000-SLUS00553_00-0000000000000001.pkg?dl=1">CD1</a>  
<a href="https://www.dropbox.com/s/rzjihxypo9z0k2p/UP9000-SLES12429_00-0000000000000001.pkg?dl=1">CD2</a>  
<td> <h2 class="titulo_jogo">Amerzone  O Testamento do Explorador</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:8 fim: Amerzone  O Testamento do Explorador | TCXS Project PS1 -->


<!-- id:9 inicio: Ape Scape | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/zq33zewbpoyri92/UP9000-SCUS94423_00-0000000000000001%20-%20Ape.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/apescape.jpg'/> </td>
<td> <h2 class="titulo_jogo">Ape Scape</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:9 fim: Ape Scape | TCXS Project PS1 -->


<!-- id:10 inicio: Apocalypse | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/ve7o0wdiqkdv6ix/UP9000-SLUS00373_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/apocalypse.jpg'/> </td>
<td> <h2 class="titulo_jogo">Apocalypse</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:10 fim: Apocalypse | TCXS Project PS1 -->


<!-- id:11 inicio: Asterix | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/g7ipy5aib08cnvs/UP9000-SLES01748_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/asterix.jpg'/> </td>
<td> <h2 class="titulo_jogo">Asterix</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:11 fim: Asterix | TCXS Project PS1 -->


<!-- id:12 inicio: Asteroids | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/p7whpkbfch7j173/UP9000-SLUS00773_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/asteroids.jpg'/> </td>
<td> <h2 class="titulo_jogo">Asteroids</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:12 fim: Asteroids | TCXS Project PS1 -->


<!-- id:13 inicio: Disneys Atlantis | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/yqf5u61k0ypffd0/UP9000-SCES03543_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/atlantis.jpg'/> </td>
<td> <h2 class="titulo_jogo">Atlantis - The Lost Empire</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:13 fim: Disneys Atlantis | TCXS Project PS1 -->


<!-- id:14 inicio: Attck Saucerman | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/m0i7co2x76bozwj/UP9000-SLUS01718_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/attackofthesaucerman.jpg'/> </td>
<td> <h2 class="titulo_jogo">Attack of the Saucerman</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:14 fim: Attck Saucerman | TCXS Project PS1 -->


<!-- id:15 inicio: Battle Arena Shinden1 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/mjlc06ltpwlg736/UP9000-SCUS94200_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/battlearenatoshinden.jpg'/> </td>
<td> <h2 class="titulo_jogo">Battle Arena Toshinden</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:15 fim: Battle Arena Shinden1 | TCXS Project PS1 -->


<!-- id:16 inicio: Battle Arena Shinden2 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/gl0q21bo7769l6b/UP9000-SLUS00220_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/battlearenatoshinden2.jpg'/> </td>
<td> <h2 class="titulo_jogo">Battle Arena Toshinden 2</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:16 fim: Battle Arena Shinden2 | TCXS Project PS1 -->


<!-- id:17 inicio: Battle Arena Toshiden3 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/v18unqcd3towqtg/UP9000-SLUS00483_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/battlearenatoshinden3.jpg'/> </td>
<td> <h2 class="titulo_jogo">Battle Arena Toshiden 3</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:17 fim: Battle Arena Toshiden3 | TCXS Project PS1 -->


<!-- id:18 inicio: Beyblade | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/suzxodu9j4p7nrn/UP9000-SLUS01489_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/beyblade.jpg'/> </td>
<td> <h2 class="titulo_jogo">Beyblade</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:18 fim: Beyblade | TCXS Project PS1 -->


<!-- id:19 inicio: Bloody Roar1 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/w4zg9jhcqlkjd37/UP9000-SCUS94199_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/bloodyroar1.jpg'/> </td>
<td> <h2 class="titulo_jogo">Bloody Roar</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:19 fim: Bloody Roar1 | TCXS Project PS1 -->


<!-- id:20 inicio: Bloody Roar2 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/ug7k41uq9mdfp6a/UP9000-SCUS94424_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/bloodyroar2.jpg'/> </td>
<td> <h2 class="titulo_jogo">Bloody Roar 2</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:20 fim: Bloody Roar2 | TCXS Project PS1 -->


<!-- id:19 inicio: BomberMan Party | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/awzleveedjsykio/UP9000-SLUS01189_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/bombermanp.jpg'/> </td>
<td> <h2 class="titulo_jogo">BomberMan Party</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:19 fim: BomberMan Party | TCXS Project PS1 -->


<!-- id:20 inicio: Bomberman Fantasy Race | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/pdcjrzjbf35x9of/UP9000-SLUS00823_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/bomberrace.jpg'/> </td>
<td> <h2 ="titulo_jogo">Bomberman Fantasy Race</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:20 fim: Bomberman Fantasy Race | TCXS Project PS1 -->


<!-- id:21 inicio: Bomberman World | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/vz49j71irfdum1q/UP9000-SLUS00680_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/bomberworld.jpg'/> </td>
<td> <h2 class="titulo_jogo">Bomberman World</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:21 fim: Bomberman World | TCXS Project PS1 -->


<!-- id:22 inicio: Breath of fire 3 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/35q024etak1vkhq/UP9000-SLUS00422_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/breath3.jpg'/> </td>
<td> <h2 class="titulo_jogo">Breath of fire 3</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:22 fim: Breath of fire 3 | TCXS Project PS1 -->


<!-- id:23 inicio: Breath of fire 4 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/4phjl6qyjsuz93h/UP9000-SLUS01324_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/breathoffire4.jpg'/> </td>
<td> <h2 class="titulo_jogo">Breath of fire 4</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:23 fim: Breath of fire 4 | TCXS Project PS1 -->


<!-- id:24 inicio: A Bugs Life | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/dxt415c3ha5oequ/UP9000-SCUS94288_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/bugslife.jpg'/> </td>
<td> <h2 class="titulo_jogo">A Bugs Life</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:24 fim: A Bugs Life | TCXS Project PS1 -->


<!-- id:25 inicio: Bugs Time | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/0hbfumesji6l06j/UP9000-SLUS01144_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/bugstime.jpg'/> </td>
<td> <h2 class="titulo_jogo">Bugs Bunny & Taz  Time Busters</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:25 fim: Bugs Time | TCXS Project PS1 -->


<!-- id:26 inicio: BustaGroove | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/7esvajs7x0bakvs/UP9000-SCUS94263_00-0000000000000001.pkg?dl=01">  
<img  class="caixa_imagem"  src='imagens/ps1/bustagroove.jpg'/> </td>
<td> <h2 class="titulo_jogo">Busta Groove</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:26 fim: BustaGroove | TCXS Project PS1 -->


<!-- id:27 inicio: BustaGroove2 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/izxgp89e1cfx0w2/UP9000-SLUS01159_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/bustagroove2.jpg'/> </td>
<td> <h2 class="titulo_jogo">Busta Groove 2</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:27 fim: BustaGroove2 | TCXS Project PS1 -->


<!-- id:28 inicio: Castlevania Simphony of Night | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/tcn2681rbyt9o1z/UP9000-SLUS00067_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/castlevaniasimphony.jpg'/> </td>
<td> <h2 class="titulo_jogo">Castlevania Simphony of Night</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:28 fim: Castlevania Simphony of Night | TCXS Project PS1 -->


<!-- id:29 inicio: Castlevania Chronicles | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/7szm2x9gilqnwnt/UP9000-SLUS01384_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/castlevaniasimphony.jpg'/> </td>
<td> <h2 class="titulo_jogo">Castlevania Chronicles</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:29 fim: Castlevania Chronicles | TCXS Project PS1 -->


<!-- id:30 inicio: Chrono Cross | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<div class="dropdown"> <img  class="caixa_imagem" class="dropbtn" src="imagens/ps1/chronocross.jpg" width="170" width="170"/>
<div class="dropdown-content">
<a href="https://www.dropbox.com/s/uwyneniae2lj97g/UP9000-SLUS01041_00-0000000000000001.pkg?dl=1">CD1</a>  
<a href="https://www.dropbox.com/s/5n7dn4jxyt5lo0z/UP9000-SLUS01041_00-0000000000000001.pkg?dl=1">CD2</a>  
</div> </div> </td>  <td><h2 class="titulo_jogo">Chrono Cross</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:30 fim: Chrono Cross | TCXS Project PS1 -->


<!-- id:31 inicio: Clock Tower | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/k6lsvbg1jjd1y0j/UP9000-SLUS00539_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/clocktower.jpg'/> </td>
<td> <h2 class="titulo_jogo">Clock Tower</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:31 fim: Clock Tower | TCXS Project PS1 -->


<!-- id:32 inicio: Clock Tower 2 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/mo9wf815gic03oi/UP9000-SLUS00695_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/clocktower2.jpg'/> </td>
<td> <h2 class="titulo_jogo">Clock Tower 2</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:32 fim: Clock Tower 2 | TCXS Project PS1 -->


<!-- id:33 inicio: Contra Legacy War | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/qieg3xkprzu80re/UP9000-SLUS00288_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/contrawar.jpg'/> </td>
<td> <h2 class="titulo_jogo">Contra Legacy War</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:33 fim: Contra Legacy War | TCXS Project PS1 -->


<!-- id:34 inicio: Courier Crisis | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/5df3cvhshxr8hmf/UP9000-SLUS00442_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/courier.jpg'/> </td>
<td> <h2 class="titulo_jogo">Courier Crisis</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:34 fim: Courier Crisis | TCXS Project PS1 -->


<!-- id:35 inicio: Crash1 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/ekbfyu2rv47zzdq/UP9000-SLUS94900_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/crash1.jpg'/> </td>
<td> <h2 class="titulo_jogo">Crash Bandicoot</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:35 fim: Crash1 | TCXS Project PS1 -->


<!-- id:36 inicio: Crash2 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/cyyeyuuxrhoncdp/UP9000-SCUS94154_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/crash2.jpg'/> </td>
<td> <h2 class="titulo_jogo">Crash Bandicoot 2</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:36 fim: Crash2 | TCXS Project PS1 -->


<!-- id:37 inicio: Crash3 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/9acaxhfa9x0wv0x/UP9000-SCUS94244_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/crash3.jpg'/> </td>
<td> <h2 class="titulo_jogo">Crash Bandicoot 3 Warped</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:37 fim: Crash3 | TCXS Project PS1 -->


<!-- id:38 inicio: Crime Killer | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/hngur5fzee5fdru/UP9000-SLUS00576_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/crimekiller.jpg'/> </td>
<td> <h2 class="titulo_jogo">Crime Killer</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:38 fim: Crime Killer | TCXS Project PS1 -->


<!-- id:39 inicio: Crash Team Racing | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/fa1tdp77pynyqe6/UP9000-SCUS94426_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/ctr.jpg'/> </td>
<td> <h2 class="titulo_jogo">Crash Team Racing</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:39 fim: Crash Team Racing | TCXS Project PS1 -->


<!-- id:40 inicio: DragonBall Final Bout | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/ypyo9os1kxzg70a/UP9000-SLPS00949_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/dbztrilgy.jpg'/> </td>
<td> <h2 class="titulo_jogo">DragonBall Final Bout</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:40 fim: DragonBall Final Bout | TCXS Project PS1 -->


<!-- id:41 inicio: Diablo | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/2lnaflzi1u14r3j/UP9000-SLUS00619_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/diablo.jpg'/> </td>
<td> <h2 class="titulo_jogo">Diablo</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:41 fim: Diablo | TCXS Project PS1 -->


<!-- id:42 inicio: Digimon Rumble Arena | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/zer8jfthndmxjbq/UP9000-SLUS01404_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/digimonrumble.jpg'/> </td>
<td> <h2 class="titulo_jogo">Digimon Rumble Arena</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:42 fim: Digimon Rumble Arena | TCXS Project PS1 -->


<!-- id:43 inicio: Digimon World | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/w0tgk3ff75baimi/UP9000-SLUS01032_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/digimonworld.jpg'/> </td>
<td> <h2 class="titulo_jogo">Digimon World</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:43 fim: Digimon World | TCXS Project PS1 -->


<!-- id:44 inicio: Digimon World 2 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/zinykh6ppj18go7/UP9000-SLUS01193_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/digmonw2.jpg'/> </td>
<td> <h2 class="titulo_jogo">Digimon World 2</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:44 fim: Digimon World 2 | TCXS Project PS1 -->


<!-- id:45 inicio: Digimon World 3 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/nub38r7r1ayj0j8/UP9000-SLUS01436_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/digmonw3.jpg'/> </td>
<td> <h2 class="titulo_jogo">Digimon World 3</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:45 fim: Digimon World 3 | TCXS Project PS1 -->


<!-- id:46 inicio: Dino Crisis | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/rwkju9486s5e8iu/UP0001-SLUS00922_00-0000111122223333.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/dinocrisis.jpg'/> </td>
<td> <h2 class="titulo_jogo">Dino Crisis</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:46 fim: Dino Crisis | TCXS Project PS1 -->


<!-- id:47 inicio: Dino Crisis 2 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/hlmzy4ki889sed0/UP0001-SLUS01279_00-0000111122223333.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/dinocrisis2.jpg'/> </td>
<td> <h2 class="titulo_jogo">Dino Crisis 2</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:47 fim: Dino Crisis 2 | TCXS Project PS1 -->


<!-- id:48 inicio: Dino Crisis [PSN] | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"> <table> <tr> <td>
<div class="dropdown"> <img  class="caixa_imagem" class="dropbtn" src="imagens/ps1/dinocrisis.jpg" width="170" width="170"/>
<div class="dropdown-content">
<a href="https://www.dropbox.com/s/s6jqlqac1assr3i/UP9000-NPUJ00922_00-0000000000000001.pkg?dl=1">JOGO</a>  
<a href="https://www.dropbox.com/s/8mjfj32ab2e5n8m/UP9000-NPUJ00922_00-FIX0000000000000.pkg?dl=1">FIX(caso necessário)</a>
</div> </div> </td>  <td><h2 class="titulo_jogo">Dino Crisis [PSN]</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:48 fim: Dino Crisis[PSN] | TCXS Project PS1 -->


<!-- id:49 inicio: Dracula | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"> <table> <tr> <td>
<div class="dropdown"> <img  class="caixa_imagem" class="dropbtn" src="imagens/ps1/dracular.jpg" width="170" width="170"/>
<div class="dropdown-content">
<a href="https://www.dropbox.com/s/rcxlkmx7iwxv6f6/UP9000-SLES02762_00-0000000000000001.pkg?dl=1">CD1</a>  
<a href="https://www.dropbox.com/s/0xbmvf6fna6xvri/UP9000-SLES12762_00-0000000000000001.pkg?dl=1">CD2</a>  
</div> </div> </td>  <td><h2 class="titulo_jogo">Dracula</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:49 fim: Dracula | TCXS Project PS1 -->


<!-- id:50 inicio: Dragon Ball GT FB | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/jo9n57s5g52nehi/UP9000-SLUS00493_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/dragonballfb.jpg'/> </td>
<td> <h2 class="titulo_jogo">Dragon Ball GT FB</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:50 fim: Dragon Ball GT FB | TCXS Project PS1 -->


<!-- id:51 inicio: Driver1 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/kwar04arm5vm3dn/UP9000-SLES01816_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/driver.jpg'/> </td>
<td> <h2 class="titulo_jogo">Driver</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:51 fim: Driver1 | TCXS Project PS1 -->


<!-- id:52 inicio: Driver2 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"> <table> <tr> <td>
<div class="dropdown"> <img  class="caixa_imagem" class="dropbtn" src="imagens/ps1/driver2.jpg" width="170" width="170"/>
<div class="dropdown-content">
<a href="https://www.dropbox.com/s/28cgepvy0txbg8s/UP9000-SLUS01161_00-0000000000000001.pkg?dl=1">CD1</a>
<a href="https://www.dropbox.com/s/hynaa8etjk5ml3b/UP9000-SLUS01161_00-0000000000000001.pkg?dl=1">CD2</a>
</div> </div> </td>  <td><h2 class="titulo_jogo">Driver 2</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:52 fim: Driver2 | TCXS Project PS1 -->


<!-- id:53 inicio: Echo Night | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/eho8z58g41xnhhq/UP9000-SLUS00820_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/echo.jpg'/> </td>
<td> <h2 class="titulo_jogo">Echo Night</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:53 fim: Echo Night | TCXS Project PS1 -->


<!-- id:54 inicio: Ehrgeiz | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/zaprhjz53kc551b/UP9000-SLUS00809_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/ehrgeiz.jpg'/> </td>
<td> <h2 class="titulo_jogo">Ehrgeiz - God Bless the Ring</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:54 fim: Ehrgeiz | TCXS Project PS1 -->


<!-- id:55 inicio: Gold and glory | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/osski1cq0goui28/UP9000-SLUS01312_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/eldorado.jpg'/> </td>
<td> <h2 class="titulo_jogo">Gold and Glory The Road to El Dorado</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:55 fim: Gold and glory | TCXS Project PS1 -->


<!-- id:56 inicio: Final Fantasy 7 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"> <table> <tr> <td>
<div class="dropdown"> <img  class="caixa_imagem" class="dropbtn" src="imagens/ps1/fantasy7.jpg" width="170" width="170"/>
<div class="dropdown-content">
<a href="https://www.dropbox.com/s/8kaugdvjizu4qlb/UP9000-SCUS94163_00-0000000000000001.pkg?dl=1">CD1</a>
<a href="https://www.dropbox.com/s/4i909lv9ucys5oh/UP9000-SCUS94163_00-0000000000000001.pkg?dl=1">CD2</a>
<a href="https://www.dropbox.com/s/124yrmalmb9layq/UP9000-SCUS94163_00-0000000000000001.pkg?dl=1">CD3</a>
<a href="https://www.dropbox.com/s/2crn5pb6il3z5ew/UP9000-SLUS94163_00-0000000000000001.pkg?dl=1">CD4</a>
</div> </div> </td>  <td><h2 class="titulo_jogo">Final Fantasy 7</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:56 fim: Final Fantasy 7 | TCXS Project PS1 -->


<!-- id:57 inicio: Final Fantasy8 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"> <table> <tr> <td>
<div class="dropdown"> <img  class="caixa_imagem" class="dropbtn" src="imagens/ps1/fantasy8.jpg" width="170" width="170"/>
<div class="dropdown-content">
<a href="https://www.dropbox.com/s/kii4cvsku6uiz6c/UP9000-SLUS00892_00-0000000000000001.pkg?dl=1">CD1</a>  
<a href="https://www.dropbox.com/s/4jo06pho0iuinln/UP9000-SLUS00892_00-0000000000000001.pkg?dl=1">CD2</a>  
<a href="https://www.dropbox.com/s/cm8qsox1g447fmd/UP9000-SLUS00892_00-0000000000000001.pkg?dl=1">CD3</a>  
<a href="https://www.dropbox.com/s/uqyxhke5u97rmts/UP9000-SLUS00892_00-0000000000000001.pkg?dl=1">CD4</a>  
</div> </div> </td>  <td><h2 class="titulo_jogo">Final Fantasy 8</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:57 fim: Final Fantasy8 | TCXS Project PS1 -->


<!-- id:58 inicio: Final Fantasy9 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"> <table> <tr> <td>
<div class="dropdown"> <img  class="caixa_imagem" class="dropbtn" src="imagens/ps1/fantasy9.jpg" width="170" width="170"/>
<div class="dropdown-content">
<a href="https://www.dropbox.com/s/yo9x8rib578ngf4/UP9000-SLUS01251_00-0000000000000001.pkg?dl=1">CD1</a>
<a href="https://www.dropbox.com/s/lan14j67wwzt3b3/UP9000-SLUS01251_00-0000000000000001.pkg?dl=1">CD2</a>
<a href="https://www.dropbox.com/s/tqih2h18zuwbvw3/UP9000-SLUS01251_00-0000000000000001.pkg?dl=1">CD3</a>
<a href="https://www.dropbox.com/s/f06y83fgipzfw14/UP9000-SLUS01251_00-0000000000000001.pkg?dl=1">CD4</a>
</div> </div> </td>  <td><h2 class="titulo_jogo">Final Fantasy9</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:58 fim: Final Fantasy9 | TCXS Project PS1 -->


<!-- id:59 inicio: Final Fantasy Chronicles | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/kw18ekl83zadehz/UP9000-SLUS01363_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/ffchrono.jpg'/> </td>
<td> <h2 class="titulo_jogo">Final Fantasy Chronicles</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:59 fim: Final Fantasy Chronicles | TCXS Project PS1 -->


<!-- id:60 inicio: Final Fantasy Tatics | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/z1k1fgpizve10rc/UP9000-SCUS94221_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/fftatics.jpg'/> </td>
<td> <h2 class="titulo_jogo">Final Fantasy Tatics</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:60 fim: Final Fantasy Tatics | TCXS Project PS1 -->


<!-- id:61 inicio: Fisherman's Bait Big Ol' Bass 2 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/26tuthcbqib2l9b/UP9000-SLUS01259_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/fisherman.jpg'/> </td>
<td> <h2 class="titulo_jogo">Fisherman's Bait Big Ol' Bass 2</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:61 fim: Fisherman's Bait Big Ol' Bass 2 | TCXS Project PS1 -->


<!-- id:62 inicio: Front Mission3 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/9yzc0iyl9wt7nlg/UP9000-SLUS01011_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/frontmission3.jpg'/> </td>
<td> <h2 class="titulo_jogo">Front Mission 3</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:62 fim: Front Mission3 | TCXS Project PS1 -->


<!-- id:63 inicio: Grandia | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/vwl4922ez4qfxgc/UP9000-SCUS94457_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/grandia1.jpg'/> </td>
<td> <h2 class="titulo_jogo">Grandia</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:63 fim: Grandia | TCXS Project PS1 -->


<!-- id:64 inicio: Gran Turismo | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/ss9cyvtmlb0caga/UP9000-SCUS94194_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/granturismo.jpg'/> </td>
<td> <h2 class="titulo_jogo">Gran Turismo</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:64 fim: Gran Turismo | TCXS Project PS1 -->


<!-- id:65 inicio: Gran Turismo2 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/o1jsfn17u6bcs0l/UP9000-SCUS94488_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/granturismo2.jpg'/> </td>
<td> <h2 class="titulo_jogo">Gran Turismo 2</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:65 fim: Gran Turismo2 | TCXS Project PS1 -->


<!-- id:66 inicio: gta2 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/mvp2ov6f5yj4sap/UP9000-SLUS00106_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/gta2.jpg'/> </td>
<td> <h2 class="titulo_jogo">GTA 2</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:66 fim: gta2 | TCXS Project PS1 -->


<!-- id:67 inicio: Gunfighter | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/7q5nfztdjd9ge96/UP9000-SLES03689_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/gunfighter.jpg'/> </td>
<td> <h2 class="titulo_jogo">Gunfighter The Legend of Jesse James</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:67 fim: Gunfighter | TCXS Project PS1 -->


<!-- id:68 inicio: Harry Potter e a Câmara Secreta | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/kf7dbfftqtxqo90/UP9000-SLES03973_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/harrycs.jpg'/> </td>
<td> <h2 class="titulo_jogo">Harry Potter e a Câmara Secreta</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:68 fim: Harry | TCXS Project PS1 -->


<!-- id:69 inicio: Harry Potter e a Pedra Filosofal | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/fzadgwlm4exgj3f/UP9000-SLES03663_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/harrypf.jpg'/> </td>
<td> <h2 class="titulo_jogo">Harry Potter e a Pedra Filosofal</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:69 fim: Harry Potter e a Pedra Filosofal | TCXS Project PS1 -->


<!-- id:70 inicio: Harvest Moon | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/h6u8j4yjcx0iwij/UP9000-SLUS01115_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/harvestmoon.jpg'/> </td>
<td> <h2 class="titulo_jogo">Harvest Moon</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:70 fim: Harvest Moon | TCXS Project PS1 -->


<!-- id:71 inicio: Heart od Darkness | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/zkb78whzoygf9ki/UP9000-SLUS00696_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/heartofdarkness.jpg'/> </td>
<td> <h2 class="titulo_jogo">Heart od Darkness</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:71 fim: Heart od Darkness | TCXS Project PS1 -->


<!-- id:72 inicio: Hoshigami Blue Earth | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/xu57q8k7sj1l7f2/UP9000-SLUS01375_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/blueearth.jpg'/> </td>
<td> <h2 class="titulo_jogo">Hoshigami Ruining Blue Earth</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:72 fim: Hoshigami Blue Earth | TCXS Project PS1 -->


<!-- id:73 inicio: Hugo | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/gusgxjclku9f6k9/UP9000-SLES02590_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/hugo.jpg'/> </td>
<td> <h2 class="titulo_jogo">Hugo Quest for the Sunstones</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:73 fim: Hugo | TCXS Project PS1 -->


<!-- id:74 inicio: Inuyasha | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/bpdk2huzpb2a6a6/UP9000-SLUS01534_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/inuyashafe.jpg'/> </td>
<td> <h2 class="titulo_jogo">Inuyasha - A Feudal Fairy Tale</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:74 fim: Inuyasha | TCXS Project PS1 -->


<!-- id:75 inicio: Jackie | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/0vo057fa8f85pjd/UP9000-SLUS00684_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/jackchan.jpg'/> </td>
<td> <h2 class="titulo_jogo">Jackie Chan Stuntmaster</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:75 fim: Jackie | TCXS Project PS1 -->


<!-- id:76 inicio: Kagero | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/v3s1f7wms1ojg32/UP9000-SLUS00677_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/kagerod2.jpg'/> </td>
<td> <h2 class="titulo_jogo">Kagero Deception 2</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:76 fim: Kagero | TCXS Project PS1 -->


<!-- id:77 inicio: Klonoa | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/50nf6i3uzhhqjaa/UP9000-SLUS00585_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/klonoa.jpg'/> </td>
<td> <h2 class="titulo_jogo">Klonoa - Door to Phantomile</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:77 fim: Klonoa | TCXS Project PS1 -->


<!-- id:78 inicio: Konami Classics | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/1gpiu54hu4utujb/UP9000-SLUS00945_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/konamiclassic.jpg'/> </td>
<td> <h2 class="titulo_jogo">Konami Arcade Classics</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:78 fim: Konami Classics | TCXS Project PS1 -->


<!-- id:79 inicio: Legacy of kain | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/bw133eiu6ril20u/UP9000-SLUS00708_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/legacyofkain1.jpg'/> </td>
<td> <h2 class="titulo_jogo">Legacy of Kain Soul Reaven</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:79 fim: Legacy of kain | TCXS Project PS1 -->


<!-- id:80 inicio: Legend of Legaia | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/rhukvrmke699fiv/UP9000-SLUS94254_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/legendoflegaia.jpg'/> </td>
<td> <h2 class="titulo_jogo">Legend of Legaia</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:80 fim: Legend of Legaia | TCXS Project PS1 -->


<!-- id:81 inicio: Legend of Mana | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/e1lv1hu85x86h97/UP9000-SLUS01013_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/legendofmana.jpg'/> </td>
<td> <h2 class="titulo_jogo">Legend of Mana</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:81 fim: Legend of Mana | TCXS Project PS1 -->


<!-- id:82 inicio: Looney Racing | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/nwuaa04bbszhm3f/UP9000-SLUS01145_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/looneytunesracing.jpg'/> </td>
<td> <h2 class="titulo_jogo">Looney Tunes Racing</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:82 fim: Looney Racing | TCXS Project PS1 -->

<!-- id:83 inicio: Marvel x Capcom | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/gn1tdpeqixlv0jd/UP9000-SLUS01059_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/marvelvscapcom.jpg'/> </td>
<td> <h2 class="titulo_jogo">Marvel x Capcom</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:83 fim: Marvel x Capcom | TCXS Project PS1 -->


<!-- id:84 inicio: Matt Hoffman's Pro BMX | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/udz6s5h816nfywg/UP9000-SLUS01113_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/matthoffman.jpg'/> </td>
<td> <h2 class="titulo_jogo">Matt Hoffman's Pro BMX</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:84 fim: Matt Hoffman's Pro BMX | TCXS Project PS1 -->


<!-- id:85 inicio: Medal of Honor | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/y3tdqg5jm6h4iun/UP9000-SLUS00974_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/medal.jpg'/> </td>
<td> <h2 class="titulo_jogo">Medal of Honor</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:85 fim: Medal of Honor | TCXS Project PS1 -->


<!-- id:86 inicio: Medievil | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/9qoixwwg17zvkf1/UP9000-SCUS94227_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/medievil.jpg'/> </td>
<td> <h2 class="titulo_jogo">Medievil</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:86 fim: Medievil | TCXS Project PS1 -->


<!-- id:87 inicio: Medievil 2 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/kiz4d6r1luswfm1/UP9000-SCUS94564_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/medievil2.jpg'/> </td>
<td> <h2 class="titulo_jogo">Medievil 2</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:87 fim: Medievil 2 | TCXS Project PS1 -->


<!-- id:88 inicio: MegaMan 8 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/bwwtvpuw3ofc2a7/UP9000-SLUS00453_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/megaman8.jpg'/> </td>
<td> <h2 class="titulo_jogo">MegaMan 8</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:88 fim: MegaMan 8 | TCXS Project PS1 -->


<!-- id:89 inicio: MegaMan Legends | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/ml44v46qul0m008/UP9000-SLUS00603_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/megamanlegends.jpg'/> </td>
<td> <h2 class="titulo_jogo">MegaMan Legends</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:89 fim: MegaMan Legends | TCXS Project PS1 -->


<!-- id:90 inicio: MegaMan Legends 2 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/78rqej7l4bpnh06/UP9000-SLUS01140_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/megamanlegends2.jpg'/> </td>
<td> <h2 class="titulo_jogo">MegaMan Legends 2</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:90 fim: MegaMan Legends 2 | TCXS Project PS1 -->


<!-- id:91 inicio: MegaMan X3 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/ufkavndkvtefoje/UP9000-SLUS00353_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/megamanx3.jpg'/> </td>
<td> <h2 class="titulo_jogo">MegaMan X3</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:91 fim: MegaMan X3 | TCXS Project PS1 -->


<!-- id:92 inicio: MegaMan X4 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/25b836r80ko0u43/UP9000-SLUS00561_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/megamanx4.jpg'/> </td>
<td> <h2 class="titulo_jogo">MegaMan X4</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:92 fim: MegaMan X4 | TCXS Project PS1 -->


<!-- id:93 inicio: MegaMan X5 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/bwwhup5xvyq5mcb/UP9000-SLUS01334_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/megamanx5.jpg'/> </td>
<td> <h2 class="titulo_jogo">MegaMan X5</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:93 fim: MegaMan X5 | TCXS Project PS1 -->


<!-- id:94 inicio: MegaMan X6 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/es0vzk2v1v1l9ns/UP9000-SLUS01395_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/megamanx6.jpg'/> </td>
<td> <h2 class="titulo_jogo">MegaMan X6</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:94 fim: MegaMan X6 | TCXS Project PS1 -->


<!-- id:95 inicio: Metal Gear Solid | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"> <table> <tr> <td>
<div class="dropdown"> <img  class="caixa_imagem" class="dropbtn" src="imagens/ps1/metalgear.jpg" width="170" width="170"/>
<div class="dropdown-content">
<a href="https://www.dropbox.com/s/0oc9k6mjbthmo53/UP9000-SLUS00594_00-0000000000000001.pkg?dl=1">CD1</a>
<a href="https://www.dropbox.com/s/3sp8z76f6qi0usd/UP9000-SLUS00594_00-0000000000000001.pkg?dl=1">CD2</a>
</div> </div> </td>  <td><h2 class="titulo_jogo">Metal Gear Solid</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:95 fim: Metal Gear Solid | TCXS Project PS1 -->


<!-- id:96 inicio: Metal Gear Solid VR Missions (1999) | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/whdeifim4kb8unp/UP9000-SLUS00957_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/metalgearvr.jpg'/> </td>
<td> <h2 class="titulo_jogo">Metal Gear Solid VR Missions (1999)</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:96 fim: Metal Gear Solid VR Missions (1999) | TCXS Project PS1 -->


<!-- id:97 inicio: Metal Slug X | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/987l3fq8ctwuuck/UP9000-SLUS01212_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/metalslugx.jpg'/> </td>
<td> <h2 class="titulo_jogo">Metal Slug X</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:97 fim: Metal Slug X | TCXS Project PS1 -->


<!-- id:98 inicio: Mickey's Wild Adventure (1996) | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/l27r6ck24xkumoz/UP9000-SCES00163_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/mickey.jpg'/> </td>
<td> <h2 class="titulo_jogo">Mickey's Wild Adventure (1996)</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:98 fim: Mickey's Wild Adventure (1996) | TCXS Project PS1 -->


<!-- id:99 inicio: Millennium Soldier  Expendable | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/29ok4g88v8cd7nz/UP9000-SLES01716_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/millennium.jpg'/> </td>
<td> <h2 class="titulo_jogo">Millennium Soldier  Expendable</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:99 fim: Millennium Soldier  Expendable | TCXS Project PS1 -->


<!-- id:100 inicio: Monster Racer | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/kxbyez002fa3cjs/UP9000-SLES03246_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/monsterracer.jpg'/> </td>
<td> <h2 class="titulo_jogo">Monster Racer</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:100 fim: Monster Racer | TCXS Project PS1 -->


<!-- id:101 inicio: Monsters,Inc (2001) | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/uuzy54ja76ncdkg/UP9000-SCES03769_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/monsters.jpg'/> </td>
<td> <h2 class="titulo_jogo">Monsters,Inc (2001)</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:101 fim: Monsters,Inc (2001) | TCXS Project PS1 -->


<!-- id:102 inicio: Mortal Kombat 4 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/0ztum7d1wq16w3a/UP9000-SLUS00605_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/mk4.jpg'/> </td>
<td> <h2 class="titulo_jogo">Mortal Kombat 4</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:103 fim: Mortal Kombat 4 | TCXS Project PS1 -->


<!-- id:103 inicio: Mortal Kombat Special Forces | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/5a541iupspbnk72/UP9000-SLUS00824_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/mksf.jpg'/> </td>
<td> <h2 class="titulo_jogo">Mortal Kombat Special Forces</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:104 fim: Mortal Kombat Special Forces | TCXS Project PS1 -->


<!-- id:105 inicio: Mortal Kombat Mythologies Sub-Zero | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/07cvmi9m62y5bcu/UP9000-SLUS00476_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/mortalkombatmsz.jpg'/> </td>
<td> <h2 class="titulo_jogo">Mortal Kombat Mythologies Sub-Zero</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:105 fim: Mortal Kombat Mythologies Sub-Zero | TCXS Project PS1 -->


<!-- id:106 inicio: Mortal Kombat Trilogy | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/jw014t6bcy8ck15/UP9000-SLUS00330_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/mortalkombattrilogy.jpg'/> </td>
<td> <h2 class="titulo_jogo">Mortal Kombat Trilogy</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:106 fim: Mortal Kombat Trilogy | TCXS Project PS1 -->


<!-- id:107 inicio: Necronomicon O Despertar das Trevas | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"> <table> <tr> <td>
<div class="dropdown"> <img  class="caixa_imagem" class="dropbtn" src="imagens/ps1/necronomicon.jpg" width="170" width="170"/>
<div class="dropdown-content">
<a href="https://www.dropbox.com/s/h8jzrf1506x1wmy/UP9000-SLES03498_00-0000000000000001.pkg?dl=1">CD1</a>
<a href="https://www.dropbox.com/s/j45evvhj5h7zcjs/UP9000-SLES13498_00-0000000000000001.pkg?dl=1">CD2</a>
</div> </div> </td>  <td><h2 class="titulo_jogo">Necronomicon O Despertar das Trevas</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:107 fim: Necronomicon O Despertar das Trevas | TCXS Project PS1 -->


<!-- id:108 inicio: Need for Speed The Road &amp; Track Presents | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/nns2evyvd7scyh9/UP9000-SLUS00204_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/nfs.jpg'/> </td>
<td> <h2 class="titulo_jogo">Jogo: Need for Speed The Road & Track Presents</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:108 fim: Need for Speed The Road &amp; Track Presents | TCXS Project PS1 -->


<!-- id:109 inicio: Need for Speed 2 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/2aukbdamo9klfnk/UP9000-SLUS00276_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/nfs2.jpg'/> </td>
<td> <h2 class="titulo_jogo">Need for Speed 2</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:109 fim: Need for Speed 2 | TCXS Project PS1 -->


<!-- id:110 inicio: Need for Speed 3 - Hot Pursuit | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/jkdm3e5hgw5lqps/UP9000-SLUS00620_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/nfs3.jpg'/> </td>
<td> <h2 class="titulo_jogo">Need for Speed 3 - Hot Pursuit</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:110 fim: Need for Speed 3 - Hot Pursuit | TCXS Project PS1 -->


<!-- id:111 inicio: Need for Speed - High Stakes | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/641wfu5p5lyzw2e/UP9000-SLUS00826_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/nfshigh.jpg'/> </td>
<td> <h2 class="titulo_jogo">Need for Speed - High Stakes</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:111 fim: Need for Speed - High Stakes | TCXS Project PS1 -->


<!-- id:112 inicio: Need for Speed - Porsche Unleashed | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/vgt4l3q84iq4zku/UP9000-SLUS01104_00-0000000000000001.pkg?dl=11">  
<img  class="caixa_imagem"  src='imagens/ps1/nfsporche.jpg'/> </td>
<td> <h2 class="titulo_jogo">Need for Speed - Porsche Unleashed</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:112 fim: Need for Speed - Porsche Unleashed | TCXS Project PS1 -->


<!-- id:113 inicio: Need for Speed - V-Rally | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/s87lojypef66d4l/UP9000-SLUS00590_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/nfsrally.jpg'/> </td>
<td> <h2 class="titulo_jogo">Need for Speed - V-Rally</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:113 fim: Need for Speed - V-Rally | TCXS Project PS1 -->


<!-- id:114 inicio: Need for Speed - V-Rally 2 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/6club3g2mujd0kq/UP9000-SLUS01003_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/nfsrally2.jpg'/> </td>
<td> <h2 class="titulo_jogo">Need for Speed - V-Rally 2</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:115 fim: Need for Speed - V-Rally 2 | TCXS Project PS1 -->


<!-- id:116 inicio: Nicktoons Racing | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/6yrbiaqgnh21jsh/UP9000-SLES03153_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/nicktoons.jpg'/> </td>
<td> <h2 class="titulo_jogo">Nicktoons Racing</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:116 fim: Nicktoons Racing | TCXS Project PS1 -->


<!-- id:117 inicio: Nightmare Creatures 2 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/d2224xqcbu5uq1r/UP9000-SLUS01112_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/nightmare2.jpg'/> </td>
<td> <h2 class="titulo_jogo">Nightmare Creatures 2</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:117 fim: Nightmare Creatures 2 | TCXS Project PS1 -->


<!-- id:118 inicio: Parasite Eve | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/ezfemg52e1itgzc/UP9000-SLUS00662_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/parasite.jpg'/> </td>
<td> <h2 class="titulo_jogo">Parasite Eve</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:118 fim: Parasite Eve | TCXS Project PS1 -->


<!-- id:119 inicio: Parasite Eve 2 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/tryo5b6fj9r46xg/UP9000-SLUS01042_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/parasite2.jpg'/> </td>
<td> <h2 class="titulo_jogo">Parasite Eve 2</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:119 fim: Parasite Eve 2 | TCXS Project PS1 -->


<!-- id:120 inicio: Pitfall 3D - Beyond The Jungle | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/6cwfhpu7qxqjy4t/UP9000-SLUS00254_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/pitfall3d.jpg'/> </td>
<td> <h2 class="titulo_jogo">Pitfall 3D - Beyond The Jungle</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:120 fim: Pitfall 3D - Beyond The Jungle | TCXS Project PS1 -->


<!-- id:121 inicio: Resident Evil | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/h6xhsq547kip5y5/UP9000-SLUS00170_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/resident1.jpg'/> </td>
<td> <h2 class="titulo_jogo">Resident Evil</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:121 fim: Resident Evil | TCXS Project PS1 -->


<!-- id:122 inicio: Resident Evil 2 Clarie | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/8w0zsdz9uq3ebpj/UP9000-SLUS00756_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/resident2claire.jpg'/> </td>
<td> <h2 class="titulo_jogo">Resident Evil 2 Clarie</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:122 fim: Resident Evil 2 Clarie | TCXS Project PS1 -->


<!-- id:123 inicio: Resident Evil 2 Leon | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="button" onclick="window.location.href='https://www.dropbox.com/s/1ihzxz4f4z9vhfb/UP9000-SLUS00748_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/resident2leon.jpg'/> </td>
<td> <h2 class="titulo_jogo">Resident Evil 2 Leon</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:123 fim: Resident Evil 2 Leon | TCXS Project PS1 -->


<!-- id:124 inicio: Resident Evil 3 Nemesis Ultimate Edition | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/m9lq61m5oza75xt/UP9000-SLUS00923_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/resident3.jpg'/> </td>
<td> <h2 class="titulo_jogo">Resident Evil 3 Nemesis Ultimate Edition</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:124 fim: Resident Evil 3 Nemesis Ultimate Edition | TCXS Project PS1 -->


<!-- id:125 inicio: Road Rash | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/qxypjrwqjiy9kng/UP9000-SLUS00035_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/roadrash.jpg'/> </td>
<td> <h2 class="titulo_jogo">Road Rash</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:125 fim: Road Rash | TCXS Project PS1 -->


<!-- id:126 inicio: Samurai Showdown Warriors Rage | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/mftg3ndr2wofk4x/UP9000-SLUS01039_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/samuraishodown.jpg'/> </td>
<td> <h2 class="titulo_jogo">Samurai Showdown Warriors Rage</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:126 fim: Samurai Showdown Warriors Rage | TCXS Project PS1 -->


<!-- id:127 inicio: Silent Hill | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/fzjnlgy27ilfhru/UP9000-SLUS00707_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/silenthill1.jpg'/> </td>
<td> <h2 class="titulo_jogo">Silent Hill</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:127 fim: Silent Hill | TCXS Project PS1 -->


<!-- id:128 inicio: Shadow Man | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/j7gmtof73ym38h7/UP9000-SLUS00895_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/shadowman.jpg'/> </td>
<td> <h2 class="titulo_jogo">Shadow Man</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:129 fim: Shadow Man | TCXS Project PS1 -->


<!-- id:130 inicio: Sheep Raider  O Coiote | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/1bodzcqr2nvndmf/UP9000-SLUS01369_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/sheepraider.jpg'/> </td>
<td> <h2 class="titulo_jogo">Sheep Raider  O Coiote</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:130 fim: Sheep Raider  O Coiote | TCXS Project PS1 -->


<!-- id:131 inicio: Sol Divide | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/mf7kqc3y5nhpte8/UP9000-SLUS01519_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/soldivide.jpg'/> </td>
<td> <h2 class="titulo_jogo">Sol Divide</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:131 fim: Sol Divide | TCXS Project PS1 -->


<!-- id:132 inicio: Spider Man | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/fure26btiqk4tg1/UP9000-SLUS00875_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/spiderman.jpg'/> </td>
<td> <h2 class="titulo_jogo">Spider Man</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:132 fim: Spider Man | TCXS Project PS1 -->


<!-- id:133 inicio: Spider-man 2 Enter Electro | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/xdofdajt5sl361h/UP9000-SLUS01378_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/spiderman2.jpg'/> </td>
<td> <h2 class="titulo_jogo">Spider-man 2 Enter Electro</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:133 fim: Spider-man 2 Enter Electro | TCXS Project PS1 -->


<!-- id:134 inicio: Spyro the Dragon | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/spaufpcfy4qwi47/UP9000-SCUS94228_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/spyrothedragon.jpg'/> </td>
<td> <h2 class="titulo_jogo">Spyro the Dragon</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:134 fim: Spyro the Dragon | TCXS Project PS1 -->


<!-- id:135 inicio: Street Fighter EX Plus Alpha | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/et1p077hnf71j82/UP9000-SLUS00548_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/streetplusalfa.jpg'/> </td>
<td> <h2 class="titulo_jogo">Street Fighter EX Plus Alpha</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:135 fim: Street Fighter EX Plus Alpha | TCXS Project PS1 -->


<!-- id:136 inicio: Street Fighter EX 2 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/upkodqvabk9sx60/UP9000-SLUS01105_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/streetex2.jpg'/> </td>
<td> <h2 class="titulo_jogo">Street Fighter EX 2</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:136 fim: Street Fighter EX 2 | TCXS Project PS1 -->


<!-- id:137 inicio: Stuart Little 2 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/vsrv1f3ikw1eg62/UP9000-SCUS94669_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/stuart2.jpg'/> </td>
<td> <h2 class="titulo_jogo">Stuart Little 2</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:137 fim: Stuart Little 2 | TCXS Project PS1 -->


<!-- id:138 inicio: Sunikoden | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/kqzyrisbqjs3n6d/UP9000-SLUS00292_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/suikoden1.jpg'/> </td>
<td> <h2 class="titulo_jogo">Sunikoden</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:138 fim: Sunikoden | TCXS Project PS1 -->


<!-- id:139 inicio: Super Shot Soccer | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/34ng9n7xnvtjf3q/UP9000-SLUS01464_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/superhot.jpg'/> </td>
<td> <h2 class="titulo_jogo">Super Shot Soccer</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:140 fim: Super Shot Soccer | TCXS Project PS1 -->


<!-- id:141 inicio: Syphon Filter | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/y7ssxq6h6l5sla9/UP9000-SCUS94240_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/syphonfilter.jpg'/> </td>
<td> <h2 class="titulo_jogo">Syphon Filter</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:141 fim: Syphon Filter | TCXS Project PS1 -->


<!-- id:142 inicio: Syphon Filter 3 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/s9tiwjuja2d2zwo/UP9000-SCUS94640_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/syphonphilter3.jpg'/> </td>
<td> <h2 class="titulo_jogo">Syphon Filter 3</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:142 fim: Syphon Filter 3 | TCXS Project PS1 -->


<!-- id:143 inicio: Tekken | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/f8t2r3xovacvff3/UP9000-SLUS00006_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/tekken.jpg'/> </td>
<td> <h2 class="titulo_jogo">Tekken</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:143 fim: Tekken | TCXS Project PS1 -->


<!-- id:144 inicio: TEKKEN 2 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/6bbvpdra7nbsysa/UP9000-SLPS00300_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/tekken2.jpg'/> </td>
<td> <h2 class="titulo_jogo">TEKKEN 2</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:144 fim: TEKKEN 2 | TCXS Project PS1 -->


<!-- id:145 inicio: TEKKEN 3 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/075sjqgwur91zd6/UP9000-SLPS01300_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/tekken3.jpg'/> </td>
<td> <h2 class="titulo_jogo">TEKKEN 3</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:145 fim: TEKKEN 3 | TCXS Project PS1 -->


<!-- id:146 inicio: Tenchu Stealth Assassins | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/0r9bof6923a7vfa/UP9000-SLUS00706_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/tenchu1.jpg'/> </td>
<td> <h2 class="titulo_jogo">Tenchu Stealth Assassins</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:146 fim: Tenchu Stealth Assassins | TCXS Project PS1 -->


<!-- id:147 inicio: Tenchu 2 Birth of the Stealth Assassins | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/987jzgbuel6sf7c/UP9000-SLUS00939_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/tenchu2.jpg'/> </td>
<td> <h2 class="titulo_jogo">Tenchu 2 Birth of the Stealth Assassins</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:147 fim: Tenchu 2 Birth of the Stealth Assassins | TCXS Project PS1 -->


<!-- id:148 inicio: Tony Hawk's Pro Skater | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/8cfzvrfrt7obrkq/UP9000-SLUS00860_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/thawk.jpg'/> </td>
<td> <h2 class="titulo_jogo">Tony Hawk's Pro Skater</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:148 fim: Tony Hawk's Pro Skater | TCXS Project PS1 -->


<!-- id:149 inicio: Tony Hawk's Pro Skater 2 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/qp6gyltnsscsj1c/UP9000-SLES02908_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/thawk2.jpg'/> </td>
<td> <h2 class="titulo_jogo">Tony Hawk's Pro Skater 2</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:149 fim: Tony Hawk's Pro Skater 2 | TCXS Project PS1 -->


<!-- id:150 inicio: Tony Hawk's Pro Skater 3 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/qwbuqh50yyqik2g/UP9000-SLES03645_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/thawk3.jpg'/> </td>
<td> <h2 class="titulo_jogo">Tony Hawk's Pro Skater 3</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:150 fim: Tony Hawk's Pro Skater 3 | TCXS Project PS1 -->


<!-- id:151 inicio: Tony Hawk's Pro Skater 4 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/qwbuqh50yyqik2g/UP9000-SLES03645_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/thawk4.jpg'/> </td>
<td> <h2 class="titulo_jogo">Tony Hawk's Pro Skater 4</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:151 fim: Tony Hawk's Pro Skater 4 | TCXS Project PS1 -->


<!-- id:152 inicio: The Legend of Dragon | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/9nxoyv7bkk4ahxk/UP9000-SLUS94491_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/thelegendofdragoon.jpg'/> </td>
<td> <h2 class="titulo_jogo">The Legend of Dragon</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:152 fim: The Legend of Dragon | TCXS Project PS1 -->


<!-- id:153 inicio: Tomba | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/8ejj01c5epmzovi/UP9000-SCES01331_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/tomba.jpg'/> </td>
<td> <h2 class="titulo_jogo">Tomba</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:153 fim: Tomba | TCXS Project PS1 -->


<!-- id:154 inicio: Tomba 2 The Evil Swine Returns | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/cfc4cn7iygy649m/UP9000-SCUS94454_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/tomba2.jpg'/> </td>
<td> <h2 class="titulo_jogo">Tomba 2 The Evil Swine Returns</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:154 fim: Tomba 2 The Evil Swine Returns | TCXS Project PS1 -->


<!-- id:155 inicio: Tomb Raider | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/62apz0yigw43z1s/UP9000-SLUS00152_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/tombraider1.jpg'/> </td>
<td> <h2 class="titulo_jogo">Tomb Raider</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:155 fim: Tomb Raider | TCXS Project PS1 -->


<!-- id:156 inicio: Tomb Raider 2 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/wcrzdzj24oc9gf9/UP9000-SLUS00437_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/tombraider2.jpg'/> </td>
<td> <h2 class="titulo_jogo">Tomb Raider 2</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:156 fim: Tomb Raider 2 | TCXS Project PS1 -->


<!-- id:157 inicio: Tomb Raider 3 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/r090wfxpqtdmw2c/UP9000-SLUS00691_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/tombraider3.jpg'/> </td>
<td> <h2 class="titulo_jogo">Tomb Raider 3</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:157 fim: Tomb Raider 3 | TCXS Project PS1 -->


<!-- id:158 inicio: Tomb Raider Chronicles | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/7wjggbn9dpknpxn/UP9000-SLUS01311_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/tombraiderchronicles.jpg'/> </td>
<td> <h2 class="titulo_jogo">Tomb Raider Chronicles</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:158 fim: Tomb Raider Chronicles | TCXS Project PS1 -->


<!-- id:159 inicio: Tomb Raider - The Last Revelation Croft | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/7qg2ehq79fr6hj5/UP9000-SLUS00885_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/tombraiderlastrevelation.jpg'/> </td>
<td> <h2 class="titulo_jogo">Tomb Raider - The Last Revelation Croft</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:159 fim: Tomb Raider - The Last Revelation Croft | TCXS Project PS1 -->


<!-- id:160 inicio: Twisted Metal | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/g9of7bd1ghymb1g/UP9000-SCES00061_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/twisted.jpg'/> </td>
<td> <h2 class="titulo_jogo">Twisted Metal</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:161 fim: Twisted Metal | TCXS Project PS1 -->


<!-- id:162 inicio: Twisted Metal 2 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/nmwc60qn0r53rsi/UP9000-SCUS94306_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/twisted2.jpg'/> </td>
<td> <h2 class="titulo_jogo">Twisted Metal 2</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:162 fim: Twisted Metal 2 | TCXS Project PS1 -->


<!-- id:163 inicio: Twisted Metal 3 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/k9s2ryq114ziwo3/UP9000-SCUS94249_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/twisted3.jpg'/> </td>
<td> <h2 class="titulo_jogo">Twisted Metal 3</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:163 fim: Twisted Metal 3 | TCXS Project PS1 -->


<!-- id:164 inicio: Twisted Metal 4 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/uasxsicytetftg2/UP9000-SCUS94560_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/twisted4.jpg'/> </td>
<td> <h2 class="titulo_jogo">Twisted Metal 4</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:164 fim: Twisted Metal 4 | TCXS Project PS1 -->


<!-- id:165 inicio: Twisted Metal Small Brawl | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/k2pb3ozjk7uf4uv/UP9000-SCUS94642_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/twistedsb.jpg'/> </td>
<td> <h2 class="titulo_jogo">Twisted Metal Small Brawl</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:165 fim: Twisted Metal Small Brawl | TCXS Project PS1 -->


<!-- id:166 inicio: Ultraman Fighting Evolution | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/j0xhzopqtzhoxdu/UP9000-SLPS01248_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/ultraman.jpg'/> </td>
<td> <h2 class="titulo_jogo">Ultraman Fighting Evolution</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:166 fim: Ultraman Fighting Evolution | TCXS Project PS1 -->


<!-- id:167 inicio: Vagrant Story | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/abhfdjvhekqmpe9/UP9000-SLUS01040_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/vagrant.jpg'/> </td>
<td> <h2 class="titulo_jogo">Vagrant Story</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:167 fim: Vagrant Story | TCXS Project PS1 -->


<!-- id:168 inicio: Valryrie Profile | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/ep55bfr120vc1w7/UP9000-SLUS01156_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/valkyrie.jpg'/> </td>
<td> <h2 class="titulo_jogo">Valryrie Profile</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:168 fim: Valryrie Profile | TCXS Project PS1 -->


<!-- id:169 inicio: Vigilante8 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/ccmy5ux8r7jd5uu/UP9000-SLUS00510_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/vigilante8.jpg'/> </td>
<td> <h2 class="titulo_jogo">Vigilante8</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:169 fim: Vigilante8 | TCXS Project PS1 -->


<!-- id:170 inicio: Vigilante8 2nd Offense | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/qfqdy8l8bnm67pp/UP9000-SLUS00868_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/vigilante82.jpg'/> </td>
<td> <h2 class="titulo_jogo">Vigilante8 2nd Offense</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:170 fim: Vigilante8 2nd Offense | TCXS Project PS1 -->


<!-- id:171 inicio: Warcraft 2 The Dark Saga | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/0e3i0z20a118cj3/UP9000-SLUS00480_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/warcraft2.jpg'/> </td>
<td> <h2 class="titulo_jogo">Warcraft 2 The Dark Saga</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:171 fim: Warcraft 2 The Dark Saga | TCXS Project PS1 -->


<!-- id:172 inicio: The Warriors | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/hflqpbzenu7tnsz/UP0000-SLUS21215_00-PS2CLASSICS00000.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/warriors.jpg'/> </td>
<td> <h2 class="titulo_jogo">The Warriors</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:172 fim: The Warriors | TCXS Project PS1 -->


<!-- id:173 inicio: Wild Arms | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/fgksjycvy0oxkvs/UP9000-SCUS94608_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/wildarms.jpg'/> </td>
<td> <h2 class="titulo_jogo">Wild Arms</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:173 fim: Wild Arms | TCXS Project PS1 -->


<!-- id:173 inicio: Winning Eleven World Soccer 2002| TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/gsso6ahe4b7bom3/UP9000-SLPM87056_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/win2002.jpg'/> </td>
<td> <h2 class="titulo_jogo">Winning Eleven World Soccer 2002</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:173 fim: Winning Eleven World Soccer 2002| TCXS Project PS1 -->


<!-- id:173 inicio: Winning Eleven World Soccer 4 | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/svj3h7ov9pi0gmn/UP9000-SLPM86291_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/win4.jpg'/> </td>
<td> <h2 class="titulo_jogo">Winning Eleven World Soccer 4</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:173 fim: Winning Eleven World Soccer 4| TCXS Project PS1 -->


<!-- id:174 inicio: World's Policies Chases | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/pra3moudr304gn5/UP9000-SLUS01165_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/wspolicechases.jpg'/> </td>
<td> <h2 class="titulo_jogo">World's Policies Chases</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:174 fim: World's Policies Chases | TCXS Project PS1 -->


<!-- id:175 inicio: X-Com - Terror from the Deep | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/va2jmftbmk6r7p3/UP9000-SLES00077_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/xcom.jpg'/> </td>
<td> <h2 class="titulo_jogo">X-Com - Terror from the Deep</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:175 fim: X-Com - Terror from the Deep | TCXS Project PS1 -->


<!-- id:176 inicio: X-Com - UFO Defense | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/vjkwleo963ml53q/UP9000-SLUS00141_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/xufo.jpg'/> </td>
<td> <h2 class="titulo_jogo">X-Com - UFO Defense</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:176 fim: X-Com - UFO Defense | TCXS Project PS1 -->


<!-- id:177 inicio: Xenogears | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"> <table> <tr> <td>
<div class="dropdown"> <img  class="caixa_imagem" class="dropbtn" src="imagens/ps1/xenogears.jpg" width="170" width="170"/>
<div class="dropdown-content">
<a href="https://www.dropbox.com/s/qc1qcnpc0i9s1dz/UP9000-SLUS00664_00-0000000000000001.pkg?dl=1">CD1<a/>
<a href="https://www.dropbox.com/s/rid42i5lsrg2z44/UP9000-SLUS00664_00-0000000000000001.pkg?dl=1">CD2<a/>
</div> </div> </td>  <td><h2 class="titulo_jogo">Xenogears</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:177 fim: Xenogears | TCXS Project PS1 -->


<!-- id:178 inicio: Yu-Gi-Oh! Forbidden Memories | TCXS Project PS1 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="https://www.dropbox.com/s/isw42ucnezzwntt/UP9000-SLUS01411_00-0000000000000001.pkg?dl=1">  
<img  class="caixa_imagem"  src='imagens/ps1/yugiohmemories.jpg'/> </td>
<td> <h2 class="titulo_jogo">Yu-Gi-Oh! Forbidden Memories</h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: PT-BR<br> Plataforma: PS1</p> </a>
</td> </tr> </table> </div> 
<!-- id:178 fim: Yu-Gi-Oh! Forbidden Memories | TCXS Project PS1 -->


<!-- final do container-fluid todo conteudo deve ficar antes desta div -->   
</div></div>
<footer class="tm-footer text-right" "><font color="#91060d" face="VT323" size="5"><font color="91060d"><b> TCXS Project PlayStation3 Store   |  2020   |   HAN HEN CFW   </b></font></footer> 
</div>
</body>
</html>