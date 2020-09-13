<!-- ████████╗ ██████╗██╗  ██╗███████╗    ██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗
    ╚══██╔══╝██╔════╝╚██╗██╔╝██╔════╝    ██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝
       ██║   ██║      ╚███╔╝ ███████╗    ██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║   
       ██║   ██║      ██╔██╗ ╚════██║    ██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║   
       ██║   ╚██████╗██╔╝ ██╗███████║    ██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║   
       ╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝   -->
<!-- @Gorpo Orko - 2020 -->
<?php
session_start();
if (!$_REQUEST["act"] && $_REQUEST["act"] != "mitsuky"){
  header('Location: nao_logado.php');
  exit();
}

?>
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
      <script src="../assets/js/gorpo.js"></script>

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
                    <li class="tm-nav-item"><a href="../nao_logado.php" class="tm-nav-item-link tm-button ">Informações</a></li>
                    <li class="tm-nav-item"><a href="../nao_logado.php" class="tm-nav-item-link tm-button ">PlayStation PSP</a></li>
                    <li class="tm-nav-item"><a href="../nao_logado.php" class="tm-nav-item-link tm-button ">PlayStation1</a></li>
                    <li class="tm-nav-item"><a href="../nao_logado.php" class="tm-nav-item-link tm-button ">PlayStation2</a></li>
                    <li class="tm-nav-item"><a href="../nao_logado.php" class="tm-nav-item-link tm-button active">PlayStation3</a></li>
                    <li class="tm-nav-item"><a href="../nao_logado.php" class="tm-nav-item-link tm-button">Emuladores</a></li>
                    <li class="tm-nav-item"><a href="doadores/index.html" class="tm-nav-item-link tm-button">Guia para Membros</a></li>
                    <li class="tm-nav-item"><a href="https://tcxsproject.com.br/dev/ps3xploit.com/" class="tm-nav-item-link tm-button">PS3Xploit</a></li>
                </ul>
            </nav>
            <div class="banner_infos"><div class="dados_user">
Seu IP: <?php echo $_SERVER['REMOTE_ADDR'];?><br>              
Bundle Atual: Resident Evil<br>
Próximo Bundle:  Rockstar
            </div></div>
        </section>
    </div>

<!-- ============================== INICIO DOS JOGOS PARA DOWNLOAD ABAIXO ==============================   -->
 <div class="tm-main-content">
<!-- ============================== INICIO DOS JOGOS PARA DOWNLOAD ABAIXO ==============================   -->





<!-- inicio: Resident Evil 6 LEGENDADO  | TCXS Project PS3 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a   href="#janela_Resident Evil 6 LEGENDADO">  
<img  class="caixa_imagem"  src="../assets/images/ps3/resevil6.jpg" width="170"/> </td>
<td> <h2 class="titulo_jogo">Resident Evil 6 LEGENDADO </h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PS3</p> </a>
</td> </tr> </table> </div> 
<!-- chama a pop-up pela id="janela_nome do jogo" -->
<div id="janela_Resident Evil 6 LEGENDADO" class="janelaDownloadPS3">
<div><a href="#" class="botao_fechar">X</a>
<div class="imagem_pequenaPS3"><img src="../assets/images/ps3/resevil6.jpg" width="170"  width="170" height="170"/></div>
<div ><p class='textoJogoPS3'>Jogo: Resident Evil 6 LEGENDADO<br>
Idioma: Ingles<br>
Legenda: Ingles<br>
Plataforma: PlayStation3</p></div>
<button id="btn1001" class="botaoDownloadPS3" type="button" onclick="window.location.href='https://www.dropbox.com/s/mgy97ggxnlwfaq2/1DGAME-NPUB30855_00-NPUB308550000000.pkg?dl=1';" autofocus>Parte 1</button>
<button id="btn1002" class="botaoDownloadPS3" type="button" onclick="window.location.href='https://www.dropbox.com/s/l5xwyu4eddb720i/2DGAME-NPUB30855_00-NPUB308550000000.pkg?dl=1';" autofocus>Parte 2</button>
<button id="btn1003" class="botaoDownloadPS3" type="button" onclick="window.location.href='https://www.dropbox.com/s/we1uolh648a3fhj/3DGAME-NPUB30855_00-NPUB308550000000.pkg?dl=1';" autofocus>Parte 3</button>
<button id="btn1004" class="botaoDownloadPS3" type="button" onclick="window.location.href='https://www.dropbox.com/s/rmppuzs4cep8ajl/2PATCH-BLUS30855_00-BLUS308550000000.pkg?dl=1';" autofocus>Parte 4</button>
</div></div>
<!-- fim:  Resident Evil 6 LEGENDADO  | TCXS Project PS3 -->


<!-- inicio: Resident Evil Revelations 2  | TCXS Project PS3 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="#janela_Resident Evil Revelations 2">  
<img  class="caixa_imagem"  src="../assets/images/ps3/resevilrvl2.jpg" width="170"/> </td>
<td> <h2 class="titulo_jogo">Resident Evil Revelations 2 </h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PS3</p> </a>
</td> </tr> </table> </div> 
<!-- chama a pop-up pela id="janela_nome do jogo" -->
<div id="janela_Resident Evil Revelations 2" class="janelaDownloadPS3">
<div><a href="#" class="botao_fechar">X</a>
<div class="imagem_pequenaPS3"><img src="../assets/images/ps3/resevilrvl2.jpg" width="170"  width="170" height="170"/></div>
<div ><p class='textoJogoPS3'>Jogo: Resident Evil Revelations 2<br>
Idioma: Ingles<br>
Legenda: Ingles<br>
Plataforma: PlayStation3</p></div>
<button  id="btn1005" class="botaoDownloadPS3" type="button" onclick="window.location.href='https://www.dropbox.com/s/matuzka7pwymi3d/1DGAME-NPUB31444_00-NPUB314440000000.pkg?dl=1';" autofocus>Parte 1</button>
<button  id="btn1006" class="botaoDownloadPS3" type="button" onclick="window.location.href='https://www.dropbox.com/s/9egjfce01vti8fj/2DGAME-NPUB31444_00-NPUB314440000000.pkg?dl=1';" autofocus>Parte 2</button>
<button id="btn1007" class="botaoDownloadPS3" type="button" onclick="window.location.href='https://www.dropbox.com/s/etjxl1m8x4pehhp/3DGAME-NPUB31444_00-NPUB314440000000.pkg?dl=1';" autofocus>Parte 3</button>
<button id="btn1008"  class="botaoDownloadPS3" type="button" onclick="window.location.href='https://www.dropbox.com/s/w6xs04ojx6mat6j/2PATCH-BLUS31444_00-BLUS314440000000.pkg?dl=1';" autofocus>Parte 4</button>
<button  id="btn1009" class="botaoDownloadPS3" type="button" onclick="window.location.href='https://www.dropbox.com/s/z4e414dh8vlecjf/Resident%20Evil%20Revelations%202%20-%20Episode%202.pkg?dl=1';" autofocus>Parte 5</button>
<button id="btn1010" class="botaoDownloadPS3" type="button" onclick="window.location.href='https://www.dropbox.com/s/3hkvcitssr77x5x/Resident%20Evil%20Revelations%202%20-%20Raid%20Mode%20-%20Weapon%20Storage%20C.pkg?dl=1';" autofocus>Parte 6</button>
<button id="btn1011" class="botaoDownloadPS3" type="button" onclick="window.location.href='https://www.dropbox.com/s/y0mokh69utyqbhf/Resident%20Evil%20Revelations%202%20dlc%20Barry%27s%20Commandant%20Costume.pkg?dl=1';" autofocus>Parte 7</button>
<button  id="btn1012" class="botaoDownloadPS3" type="button" onclick="window.location.href='https://www.dropbox.com/s/8bnm7egeaqh9utk/Resident%20Evil%20Revelations%202%20dlc%20Claire%27s%20Rodeo%20Costume.pkg?dl=1';" autofocus>Parte 8</button>
<button  id="btn1013" class="botaoDownloadPS3" type="button" onclick="window.location.href='https://www.dropbox.com/s/rfw8lmpy8fdbv1g/Resident%20Evil%20Revelations%202%20dlc%20Moira%27s%20Urban%20Ninja%20Costume.pkg?dl=1';" autofocus>Parte 9</button>
<button  id="btn1014" class="botaoDownloadPS3" type="button" onclick="window.location.href='https://www.dropbox.com/s/b8paq8xf4mrz3x1/Resident%20Evil%20Revelations%202%20dlc%20Natalia%27s%20Lottie%20Suit%20Costume.pkg?dl=1';" autofocus>Parte 10</button>
<button  id="btn1015" class="botaoDownloadPS3" type="button" onclick="window.location.href='https://www.dropbox.com/s/0un81tgctz5gqst/Resident%20Evil%20Revelations%202%20dlc%20Raid%20Mode%20-%20Album%20Storage%20A.pkg?dl=1';" autofocus>Parte 11</button>
<button  id="btn1016" class="botaoDownloadPS3" type="button" onclick="window.location.href='https://www.dropbox.com/s/w2wy8j3hzrv6keg/Resident%20Evil%20Revelations%202%20dlc%20Raid%20Mode%20Character%20-%20Hunk.pkg?dl=1';" autofocus>Parte 12</button>
<button  id="btn1017" class="botaoDownloadPS3" type="button" onclick="window.location.href='https://www.dropbox.com/s/obejvst97qquwon/Resident%20Evil%20Revelations%202%20dlc%20Raid%20Mode%20Character%20-%20Albert%20Wesker.pkg?dl=1';" autofocus>Parte 13</button>
<button  id="btn1018" class="botaoDownloadPS3" type="button" onclick="window.location.href='https://www.dropbox.com/s/jbzd02xxcrc2lei/Resident%20Evil%20Revelations%202%20dlc%20Raid%20Mode%20-%20Weapon%20Storage%20A.pkg?dl=1';" autofocus>Parte 14</button>
<button  id="btn1019" class="botaoDownloadPS3" type="button" onclick="window.location.href='https://www.dropbox.com/s/cd603mekfv70xib/Resident%20Evil%20Revelations%202%20dlc%20Raid%20Mode%20-%20Throwback%20Map%20Pack%20%28Mission%20IX%29.pkg?dl=1';" autofocus>Parte 15</button>
<button  id="btn1020" class="botaoDownloadPS3" type="button" onclick="window.location.href='https://www.dropbox.com/s/b9q4rsvgve5krsh/Resident%20Evil%20Revelations%202%20dlc%20Raid%20Mode%20-%20Parts%20Storage%20A.pkg?dl=1';" autofocus>Parte 16</button>
<button  id="btn1021" class="botaoDownloadPS3" type="button" onclick="window.location.href='https://www.dropbox.com/s/2lx0ouh6ene115y/Resident%20Evil%20Revelations%202%20Free%20Compatibility%20Pack.pkg?dl=1';" autofocus>Parte 17</button>
<button  id="btn1022" class="botaoDownloadPS3" type="button" onclick="window.location.href='https://www.dropbox.com/s/2uk1bgayw0kgjj4/Resident%20Evil%20Revelations%202%20Extra%20Episode%20-%20The%20Struggle.pkg?dl=1';" autofocus>Parte 18</button>
<button  id="btn1023" class="botaoDownloadPS3" type="button" onclick="window.location.href='https://www.dropbox.com/s/524kk93y862rn36/Resident%20Evil%20Revelations%202%20Extra%20Episode%20-%20Little%20Miss.pkg?dl=1';" autofocus>Parte 19</button>
<button  id="btn1024" class="botaoDownloadPS3" type="button" onclick="window.location.href='https://www.dropbox.com/s/1yxdy6yz1t4y3rn/Resident%20Evil%20Revelations%202%20Episode%204%20-%20Metamorphosis.pkg?dl=1';" autofocus>Parte 20</button>
<button  id="btn1025" class="botaoDownloadPS3" type="button" onclick="window.location.href='https://www.dropbox.com/s/uhpyhdr50veoaqb/Resident%20Evil%20Revelations%202%20Episode%203%20-%20Judgment.pkg?dl=1';" autofocus>Parte 21</button>
</div></div>
<!-- fim:  Resident Evil Revelations 2  | TCXS Project PS3 -->


<!-- inicio: Resident Evil Revelations HD   | TCXS Project PS3 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="#janela_Resident Evil Revelations HD ">  
<img  class="caixa_imagem"  src="../assets/images/ps3/rerhd.jpg" width="170"/> </td>
<td> <h2 class="titulo_jogo">Resident Evil Revelations HD  </h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PS3</p> </a>
</td> </tr> </table> </div> 
<!-- chama a pop-up pela id="janela_nome do jogo" -->
<div id="janela_Resident Evil Revelations HD " class="janelaDownloadPS3">
<div><a href="#" class="botao_fechar">X</a>
<div class="imagem_pequenaPS3"><img src="../assets/images/ps3/rerhd.jpg" width="170"  width="170" height="170"/></div>
<div ><p class='textoJogoPS3'>Jogo: Resident Evil Revelations HD <br>
Idioma: Ingles<br>
Legenda: Ingles<br>
Plataforma: PlayStation3</p></div>
<button id="btn1026"  class="botaoDownloadPS3" type="button" onclick="window.location.href='https://www.dropbox.com/s/xnhz3qj05jotdml/1DGAME-NPEB01773_00-NPEB017730000000.pkg?dl=1';" autofocus>Parte 1</button>
<button id="btn1027"  class="botaoDownloadPS3" type="button" onclick="window.location.href='https://www.dropbox.com/s/l03ljtb6b7z55ah/2DGAME-NPEB01773_00-NPEB017730000000.pkg?dl=1';" autofocus>Parte 2</button>
<button  id="btn1028" class="botaoDownloadPS3" type="button" onclick="window.location.href='https://www.dropbox.com/s/te5t9vdrsgmx27m/3DGAME-NPEB01773_00-NPEB017730000000.pkg?dl=1';" autofocus>Parte 3</button>
<button id="btn1029" class="botaoDownloadPS3" type="button" onclick="window.location.href='https://www.dropbox.com/s/uoga28ybwhvltgx/2PATCH-BLES01773_00-BLES017730000000.pkg?dl=1';" autofocus>Parte 4</button>
</div></div>
<!-- fim:  Resident Evil Revelations HD   | TCXS Project PS3 -->


<!-- inicio: ResidentEvil 5 Gold  | TCXS Project PS3 -->
<div class="media-body  tm-bg-light-gray"><table> <tr> <td>
<a href="#janela_ResidentEvil 5 Gold">  
<img  class="caixa_imagem"  src="../assets/images/ps3/re5.jpg" width="170"/> </td>
<td> <h2 class="titulo_jogo">ResidentEvil 5 Gold </h2>
<p class='textoJogo'>Idioma: Ingles<br> Legenda: Ingles<br> Plataforma: PlayStation PS3</p> </a>
</td> </tr> </table> </div> 
<!-- chama a pop-up pela id="janela_nome do jogo" -->
<div id="janela_ResidentEvil 5 Gold" class="janelaDownloadPS3">
<div><a href="#" class="botao_fechar">X</a>
<div class="imagem_pequenaPS3"><img src="../assets/images/ps3/re5.jpg" width="170"  width="170" height="170"/></div>
<div ><p class='textoJogoPS3'>Jogo: ResidentEvil 5 Gold<br>
Idioma: Ingles<br>
Legenda: Ingles<br>
Plataforma: PlayStation3</p></div>
<button  id="btn1030" class="botaoDownloadPS3" type="button" onclick="window.location.href='https://www.dropbox.com/s/suzlirxsmbrbe5l/1DGAME-NPUB30491_00-NPUB304910000000.pkg?dl=1';" autofocus>Parte 1</button>
<button id="btn1031" class="botaoDownloadPS3" type="button" onclick="window.location.href='https://www.dropbox.com/s/gkqz9alk6lu6z21/2DGAME-NPUB30491_00-NPUB304910000000.pkg?dl=1';" autofocus>Parte 2</button>
<button  id="btn1032" class="botaoDownloadPS3" type="button" onclick="window.location.href='https://www.dropbox.com/s/pjk6y25gzc9lnud/3DGAME-NPUB30491_00-NPUB304910000000.pkg?dl=1';" autofocus>Parte 3</button>
<button id="btn1033" class="botaoDownloadPS3" type="button" onclick="window.location.href='https://www.dropbox.com/s/xby01syhabn1z9a/4DGAME-NPUB30491_00-NPUB304910000000.pkg?dl=1';" autofocus>Parte 4</button>
<button id="btn1034" class="botaoDownloadPS3" type="button" onclick="window.location.href='https://www.dropbox.com/s/aaqeulyh8t11e45/2PATCH-BLUS30491_00-BLUS304910000000.pkg?dl=1';" autofocus>Parte 5</button>
</div></div>
<!-- fim:  ResidentEvil 5 Gold  | TCXS Project PS3 -->

<script>
    writeEnvInfo();
    ps3chk();
</script> 

<!-- final do container-fluid todo conteudo deve ficar antes desta div -->   
</div></div>
<footer class="tm-footer text-right" "><font color="#91060d" face="VT323" size="5"><font color="91060d"><b> TCXS Project PlayStation3 Store   |  2020   |   HAN HEN CFW   </b></font></footer> 
</div>
</body>
</html>