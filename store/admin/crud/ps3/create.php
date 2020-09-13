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


require '../../../database.php';
//Acompanha os erros de validação
//id titulo descricao content_id imagem_db imagem link
// Processar so quando tenha uma chamada post
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $tituloErro = null;
    $descricaoErro = null;
    $content_idErro = null;
    $imagemErro = null;
    $link1Erro = null;  
    $link2Erro = null;  
    $link3Erro = null;  
    $link4Erro = null;  
    $link5Erro = null;  
    $link6Erro = null;  
    $link7Erro = null;  
    $link8Erro = null;  
    $link9Erro = null;  
    $link10Erro = null;  
    $link11Erro = null;  
    $link12Erro = null;  
    $link13Erro = null;  
    $link14Erro = null;  
    $link15Erro = null;
    $link16Erro = null; 
	$link17Erro = null; 
	$link18Erro = null; 
	$link19Erro = null; 
	$link20Erro = null; 
	$link21Erro = null; 
	$link22Erro = null; 
	$link23Erro = null; 
	$link24Erro = null; 
	$link25Erro = null; 
	$link26Erro = null; 
	$link27Erro = null; 
	$link28Erro = null; 
	$link29Erro = null; 
	$link30Erro = null;  


    if (!empty($_POST)) {
        $validacao = True;
        $novoUsuario = False;
        if (!empty($_POST['titulo'])) {
            $titulo = $_POST['titulo'];
        } else {
            $tituloErro = 'Por favor digite o seu titulo!';
            $validacao = False;
        }


        if (!empty($_POST['descricao'])) {
            $descricao = $_POST['descricao'];
        } else {
            $descricaoErro = 'Por favor digite a descricao!';
            $validacao = False;
        }


        if (!empty($_POST['content_id'])) {
            $content_id = $_POST['content_id'];
        } else {
            $content_idErro = 'Por favor digite o número do content_id!';
            $validacao = False;
        }


        if (!empty($_POST['imagem'])) {
            $imagem = $_POST['imagem'];
        } else {
            $imagemErro = 'Por favor digite o nome imagem!';
            $validacao = False;
        }


       
         
    
    

if (!empty($_POST['link1'])) {
            $link1 = $_POST['link1'];
        } else {
            //$link1 = '---';
            $link1Erro = 'O primeiro link é sempre obrigatório, é necessário que tenha ao menos este link cadastrado!';
            $validacao = False;
        }



if (!empty($_POST['link2'])) {
            $link2 = $_POST['link2'];
        } else {
            $link2Erro = 'O link 2 não é obrigatório, mantenha o nome "---" intalterado caso não vá inserir link!';
            $link2 = '---';
        }



if (!empty($_POST['link3'])) {
            $link3 = $_POST['link3'];
        } else {
            $link3Erro = 'O link 3 não é obrigatório, mantenha o nome "---" intalterado caso não vá inserir link!';
            $link3 = '---';
        }



if (!empty($_POST['link4'])) {
            $link4 = $_POST['link4'];
        } else {
            $link4Erro = 'O link 4 não é obrigatório, mantenha o nome "---" intalterado caso não vá inserir link!';
            $link4 = '---';
        }


if (!empty($_POST['link5'])) {
            $link5 = $_POST['link5'];
        } else {
            $link5Erro = 'O link5  não é obrigatório, mantenha o nome --- intalterado caso não vá inserir link5!';
            $link5 = '---';
        }
        
if (!empty($_POST['link6'])) {
            $link6 = $_POST['link6'];
        } else {
            $link6Erro = 'O link6  não é obrigatório, mantenha o nome --- intalterado caso não vá inserir link6!';
            $link6 = '---';
        }
        
if (!empty($_POST['link7'])) {
            $link7 = $_POST['link7'];
        } else {
            $link7Erro = 'O link7  não é obrigatório, mantenha o nome --- intalterado caso não vá inserir link7!';
            $link7 = '---';
        }
        
if (!empty($_POST['link8'])) {
            $link8 = $_POST['link8'];
        } else {
            $link8Erro = 'O link8  não é obrigatório, mantenha o nome --- intalterado caso não vá inserir link8!';
            $link8 = '---';
        }
        
if (!empty($_POST['link9'])) {
            $link9 = $_POST['link9'];
        } else {
            $link9Erro = 'O link9  não é obrigatório, mantenha o nome --- intalterado caso não vá inserir link9!';
            $link9 = '---';
        }
        
if (!empty($_POST['link10'])) {
            $link10 = $_POST['link10'];
        } else {
            $link10Erro = 'O link10  não é obrigatório, mantenha o nome --- intalterado caso não vá inserir link10!';
            $link10 = '---';
        }
        
if (!empty($_POST['link11'])) {
            $link11 = $_POST['link11'];
        } else {
            $link11Erro = 'O link11  não é obrigatório, mantenha o nome --- intalterado caso não vá inserir link11!';
            $link11 = '---';
        }
        
if (!empty($_POST['link12'])) {
            $link12 = $_POST['link12'];
        } else {
            $link12Erro = 'O link12  não é obrigatório, mantenha o nome --- intalterado caso não vá inserir link12!';
            $link12 = '---';
        }
        
if (!empty($_POST['link13'])) {
            $link13 = $_POST['link13'];
        } else {
            $link13Erro = 'O link13  não é obrigatório, mantenha o nome --- intalterado caso não vá inserir link13!';
            $link13 = '---';
        }
        
if (!empty($_POST['link14'])) {
            $link14 = $_POST['link14'];
        } else {
            $link14Erro = 'O link14  não é obrigatório, mantenha o nome --- intalterado caso não vá inserir link14!';
            $link14 = '---';
        }
        
if (!empty($_POST['link15'])) {
            $link15 = $_POST['link15'];
        } else {
            $link15Erro = 'O link15  não é obrigatório, mantenha o nome --- intalterado caso não vá inserir link15!';
            $link15 = '---';
        }
        
if (!empty($_POST['link16'])) {
            $link16 = $_POST['link16'];
        } else {
            $link16Erro = 'O link16  não é obrigatório, mantenha o nome --- intalterado caso não vá inserir link16!';
            $link16 = '---';
        }
        
if (!empty($_POST['link17'])) {
            $link17 = $_POST['link17'];
        } else {
            $link17Erro = 'O link17  não é obrigatório, mantenha o nome --- intalterado caso não vá inserir link17!';
            $link17 = '---';
        }
        
if (!empty($_POST['link18'])) {
            $link18 = $_POST['link18'];
        } else {
            $link18Erro = 'O link18  não é obrigatório, mantenha o nome --- intalterado caso não vá inserir link18!';
            $link18 = '---';
        }
        
if (!empty($_POST['link19'])) {
            $link19 = $_POST['link19'];
        } else {
            $link19Erro = 'O link19  não é obrigatório, mantenha o nome --- intalterado caso não vá inserir link19!';
            $link19 = '---';
        }
        
if (!empty($_POST['link20'])) {
            $link20 = $_POST['link20'];
        } else {
            $link20Erro = 'O link20  não é obrigatório, mantenha o nome --- intalterado caso não vá inserir link20!';
            $link20 = '---';
        }
        
if (!empty($_POST['link21'])) {
            $link21 = $_POST['link21'];
        } else {
            $link21Erro = 'O link21  não é obrigatório, mantenha o nome --- intalterado caso não vá inserir link21!';
            $link21 = '---';
        }
        
if (!empty($_POST['link22'])) {
            $link22 = $_POST['link22'];
        } else {
            $link22Erro = 'O link22  não é obrigatório, mantenha o nome --- intalterado caso não vá inserir link22!';
            $link22 = '---';
        }
        
if (!empty($_POST['link23'])) {
            $link23 = $_POST['link23'];
        } else {
            $link23Erro = 'O link23  não é obrigatório, mantenha o nome --- intalterado caso não vá inserir link23!';
            $link23 = '---';
        }
        
if (!empty($_POST['link24'])) {
            $link24 = $_POST['link24'];
        } else {
            $link24Erro = 'O link24  não é obrigatório, mantenha o nome --- intalterado caso não vá inserir link24!';
            $link24 = '---';
        }
        
if (!empty($_POST['link25'])) {
            $link25 = $_POST['link25'];
        } else {
            $link25Erro = 'O link25  não é obrigatório, mantenha o nome --- intalterado caso não vá inserir link25!';
            $link25 = '---';
        }
        
if (!empty($_POST['link26'])) {
            $link26 = $_POST['link26'];
        } else {
            $link26Erro = 'O link26  não é obrigatório, mantenha o nome --- intalterado caso não vá inserir link26!';
            $link26 = '---';
        }
        
if (!empty($_POST['link27'])) {
            $link27 = $_POST['link27'];
        } else {
            $link27Erro = 'O link27  não é obrigatório, mantenha o nome --- intalterado caso não vá inserir link27!';
            $link27 = '---';
        }
        
if (!empty($_POST['link28'])) {
            $link28 = $_POST['link28'];
        } else {
            $link28Erro = 'O link28  não é obrigatório, mantenha o nome --- intalterado caso não vá inserir link28!';
            $link28 = '---';
        }
        
if (!empty($_POST['link29'])) {
            $link29 = $_POST['link29'];
        } else {
            $link29Erro = 'O link29  não é obrigatório, mantenha o nome --- intalterado caso não vá inserir link29!';
            $link29 = '---';
        }
        
if (!empty($_POST['link30'])) {
            $link30 = $_POST['link30'];
        } else {
            $link30Erro = 'O link30  não é obrigatório, mantenha o nome --- intalterado caso não vá inserir link30!';
            $link30 = '---';
        }



    }

//Inserindo no database:
    if ($validacao) {
        $pdo = Database::conectar();
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        $sql = "INSERT INTO playstation_ps3 (titulo, descricao, content_id, imagem,cadastro, link1, link2, link3, link4, link5, link6, link7, link8, link9, link10, link11, link12, link13, link14, link15,link16,link17,link18,link19,link20,link21,link22,link23,link24,link25,link26,link27,link28,link29,link30) VALUES(?,?,?,?,NOW(),?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,? )";
        $q = $pdo->prepare($sql);
        $q->execute(array($titulo, $descricao, $content_id, $imagem, $link1, $link2, $link3, $link4, $link5, $link6, $link7, $link8, $link9, $link10, $link11, $link12, $link13, $link14, $link15, $link16, $link17, $link18, $link19, $link20, $link21, $link22, $link23, $link24, $link25, $link26, $link27, $link28, $link29, $link30));
        database::desconectar();
        header("Location: index.php");
    }
}



//---------------------------------------------------------------------------------------------------------------------
//================== FUNÇÃO UPLOAD DE IMAGEM | REDIMENSIONAMENTO | MARCA DAGUA TCXS ===================================
//--------------------------------------------------->>>
// CAMINHO PARA SALVAR A IMAGEM | CAMINHO DA MARCA DAGUA
$targetDir = "../../../assets/images/ps3/"; 
$watermarkImagePath = '../../../assets/images/watermark.png'; 
// FUNÇAO RESPONSAVEL PELO REDIMENSINAMENTO 
function resize_image($file, $w, $h, $crop=FALSE) {
    list($width, $height) = getimagesize($file);
    $r = $width / $height;
    //-----ATENÇÃO --- ATENÇÃO -----ATENÇÃO --- ATENÇÃO-----ATENÇÃO --- ATENÇÃO-----ATENÇÃO --- ATENÇÃO
    //REMOVER A LINHA ERRO REPORTING PARA VOLTAR VER ERROS DO PHP
    error_reporting(E_ALL & ~E_WARNING & ~E_NOTICE);
    //---------------------------------------------------------->>
    if ($crop) {
        if ($width > $height) {
            $width = ceil($width-($width*abs($r-$w/$h)));
        } else {
            $height = ceil($height-($height*abs($r-$w/$h)));
        }
        $newwidth = $w;
        $newheight = $h;
    } else {
        if ($w/$h > $r) {
            $newwidth = $h*$r;
            $newheight = $h;
        } else {
            $newheight = $w/$r;
            $newwidth = $w;
        }
    }

    $src = imagecreatefromjpeg($file);
    if (!$src){
           $src= imagecreatefromstring(file_get_contents($file));
        }




    $dst = imagecreatetruecolor($newwidth, $newheight);
    imagecopyresampled($dst, $src, 0, 0, 0, 0, $newwidth, $newheight, $width, $height);
    return $dst;
}
//SETA STATUS DA MENSAGEM PARA SABER SE SUBIU E RETORNA OS DADOS
$statusMsg = ''; 
if(isset($_POST["submit"])){ 
    if(!empty($_FILES["file"]["name"])){ 
        // Caminho de upload de arquivo
        $fileName = basename($_FILES["file"]["name"]); 
        $targetFilePath = $targetDir . $fileName; 
        $fileType = pathinfo($targetFilePath,PATHINFO_EXTENSION); 
        // Permitir certos formatos de arquivo
        $allowTypes = array('jpg','png','jpeg'); 
        if(in_array($fileType, $allowTypes)){ 
            // Upload file to the server 
            if(move_uploaded_file($_FILES["file"]["tmp_name"], $targetFilePath)){ 
                // Carregue o carimbo e a foto para aplicar a marca d'água
                //echo $targetFilePath;
                 $im = resize_image($targetFilePath, 200, 200); 
            
                $watermarkImg = imagecreatefrompng($watermarkImagePath); 
                switch($fileType){ 
                    case 'jpg': 
                        $im = imagecreatefromjpeg($targetFilePath); 
                    case 'jpeg': 
                        $im = imagecreatefromjpeg($targetFilePath); 
                        break; 
                    case 'png': 
                        $im = imagecreatefrompng($targetFilePath); 
                        break; 
                    default: 
                        $im = imagecreatefromjpeg($targetFilePath); 
                } 
                // SETA AS MARGENS PARA A MARCA DAGUA PODENDO REALINHAR ELA
                $marge_right = 00; 
                $marge_bottom = 00;                  
                // PEGA O WIDHT E HEIGHT DA MARCA DAGUA
                $sx = imagesx($watermarkImg); 
                $sy = imagesy($watermarkImg);                 
                // Copie a imagem da marca d'água em nossa foto usando os deslocamentos de margem e
                // a largura da foto para calcular o posicionamento da marca d'água.
                //redimensiona a imagem 
                $im = imagescale($im,250,250);
                imagecopy($im, $watermarkImg, imagesx($im) - $sx - $marge_right, imagesy($im) - $sy - $marge_bottom, 0, 0, imagesx($watermarkImg), imagesy($watermarkImg)); 
                // Salvar imagem e LIBERA A MEMORIA
                imagepng($im, $targetFilePath); 
                imagedestroy($im);      
                if(file_exists($targetFilePath)){ 
                    $statusMsg = "A imagem foi redimensionada e adicionada marca dagua com sucesso!"; 
                }else{ 
                    $statusMsg = "Upload da imagem falhou, tente novamete."; 
                }  
            }else{ 
                $statusMsg = "Desculpe, ocorreu um erro ao enviar seu arquivo."; 
            } 
        }else{ 
            $statusMsg = 'Desculpe, apenas arquivos JPG, JPEG e PNG podem fazer upload.'; 
        } 
    }else{ 
        $statusMsg = 'Selecione um arquivo para fazer upload.'; 
    } 
}
//---------------------------------------------------------------------------------------------------------------------

// MOSTRA O STATUS DA IMAGEM | NOME DA IMAGEM | CAMINHO COMPLETO DA IMAGEM ----->>
//echo $statusMsg;
//if ($statusMsg){
//  echo $fileName;
//echo "<br><br><img src='$targetFilePath'>";
//}



//---------------------------------------------------------------------------------------------------------------------

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
      <title>TCXS Project | ADD PS3 GAME</title>
</head>
<body>
<div class="container">

<!-- ============= MENUS PARA PC E CELULAR ======== --->
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
          </caption>



    

<div class="barraBase">
    <div class="blocoDadosInputs">
  <h3 class="tituloRed"> Cadastrar PlayStation PS3 na Database </h3>
        <form class="form-horizontal" action="create.php" method="post"  autocomplete="off" enctype="multipart/form-data">
        


          <!-- =====   TITULO ======   -->
          <div class="wrap-input100 validate-input m-b-16" >
            <div class="control-group  <?php echo !empty($tituloErro) ? 'error ' : ''; ?>">
            <label class="titulo">Titulo PS3</label>
             <div class="controls">
            <input class="input100" type="text" name="titulo" type="text" placeholder="Insira o titulo do jogo"
                                   value="<?php echo !empty($titulo) ? $titulo : ''; ?>">
                                   <?php if (!empty($tituloErro)): ?>
                                <span class="text-danger"><?php echo $tituloErro; ?></span>
                            <?php endif; ?>
            <span class="focus-input100"></span>
            </span>
          </div></div></div>

          <!-- =====   ~descricao ======   -->
          <div class="wrap-input100 validate-input m-b-16" >
             <div class="control-group <?php echo !empty($descricaoErro) ? 'error ' : ''; ?>">
                        <label class="titulo">descricao PS3</label>
                        <div class="controls">
                            <input class="input100" name="descricao" type="text" placeholder="Insira a descricao do jogo."
                                   value="<?php echo !empty($descricao) ? $descricao : ''; ?>">
                            <?php if (!empty($imagem_dbErro)): ?>
                                <span class="text-danger"><?php echo $descricaoErro; ?></span>
                            <?php endif; ?>
            <span class="focus-input100"></span>
            </span>
          </div></div></div>



          <!-- =====   CONTENT ID ======   -->
          <div class="wrap-input100 validate-input m-b-16" >
                    <div class="control-group <?php echo !empty($content_idErro) ? 'error ' : ''; ?>">
                        <label class="titulo">Content_id PS3</label>
                        <div class="controls">
                            <input class="input100" name="content_id" type="text" placeholder="Insira a content_id do jogo"
                                   value="<?php echo !empty($content_id) ? $content_id : ''; ?>">
                            <?php if (!empty($content_idErro)): ?>
                                <span class="text-danger"><?php echo $content_idErro; ?></span>
                            <?php endif; ?>
                        <span class="focus-input100"></span>
            </span>
          </div></div></div>


          <!-- =====   UPLOAD IMAGEM ======   -->
          <div class="wrap-input100 validate-input m-b-16" >
                    <div class="control-group ">
                        <label class="titulo">Upload de Imagem</label>
                        <div class="controls  ">

                          <?php 
                            if (!$statusMsg){
                             // exibiria a imagem da marca dagua 
                            //echo "<div class='inputUploadImagem'>";
                            //echo "<img src='../../../assets/images/watermark.png' >";
                            //echo "</div>";
                            }else{
                              echo "<div class='inputUploadImagem'>";
                              echo "<img src='$targetFilePath'>";
                              echo "</div>";
                            }
                            ?>
                            <div class="areaBotoesUpload">
                               <!-- GAMBIARRA PARA TIRAR O TEXTO DO BTN UPLOAD E ALICAR CSS  --->
                              <label  class="login100-form-btn m-b-16" for='selecao-arquivo' autofocus>Selecione uma imagem &#187;</label>
                              <input id='selecao-arquivo' type='file'  name="file" >

                            <input  class="login100-form-btn m-b-16" type="submit" name="submit" value="Upload" ></div>
                        <span class="focus-input100"></span></span></div></div></div>


<!-- =====   IMAGEM | pega as infos da função de upload e retorna se o status esta True o nome da imagem para por na DB======   -->
        <div class="wrap-input100 validate-input m-b-16" >
            <div class="control-group <?php echo !empty($imagemErro) ? 'error ' : ''; ?>">
                <label class="titulo">Imagem PS3</label>
                    <div class="controls">
                      <input class="input100" name="imagem" type="text" placeholder="Insira o nome da imagem"
                          value="<?php 
                          if ($statusMsg){
                                  echo $fileName;
                                }else{
                                  echo !empty($imagem) ? $imagem : '';
                                }
                           ?>">
                          <?php if (!empty($imagemErro)): ?>
                          <span class="text-danger"><?php echo $imagemErro; ?></span>
                          <?php endif; ?>
        <span class="focus-input100"></span></span></div></div></div>

                    


<!-- =====  LINK1  ======  LINK1 ===============  LINK1 ================ -->
<div class="wrap-input100 validate-input m-b-16" >
    <div class="control-group <?php echo !empty($link1Erro) ? 'error ' : ''; ?>">
        <label class="titulo">1º Link do jogo</label>
            <div class="controls">
                <input class="input100"  name="link1" type="text" placeholder="Insira o link 1"
                value="<?php echo !empty($link1) ? $link1 : ''; ?>" >
                <?php if (!empty($link1Erro)): ?>
                <span class="text-danger"><?php echo $link1Erro; ?></span>
                <?php endif; ?>
<span class="focus-input100"></span></span></div></div></div>   







<!-- =====  LINK2  ======  LINK2 ===============  LINK2 ================ -->
<div class="wrap-input100 validate-input m-b-16" >
    <div class="control-group <?php echo !empty($link2Erro) ? 'error ' : ''; ?>">
        <label class="titulo">2º Link do jogo</label>
            <div class="controls">
                <input class="input100"  name="link2" type="text" placeholder="Insira o link 2"
                value="<?php echo !empty($link2) ? $link2 : ''; ?>">
                <?php if (!empty($link2Erro)): ?>
                <span class="text-danger"><?php echo $link2Erro; ?></span>
                <?php endif; ?>
<span class="focus-input100"></span></span></div></div></div>   



<!-- =====  LINK3  ======  LINK3 ===============  LINK3 ================ -->
<div class="wrap-input100 validate-input m-b-16" >
    <div class="control-group <?php echo !empty($link3Erro) ? 'error ' : ''; ?>">
        <label class="titulo">3º Link do jogo</label>
            <div class="controls">
                <input class="input100"  name="link3" type="text" placeholder="Insira o link 3"
                value="<?php echo !empty($link3) ? $link3 : ''; ?>">
                <?php if (!empty($link3Erro)): ?>
                <span class="text-danger"><?php echo $link3Erro; ?></span>
                <?php endif; ?>
<span class="focus-input100"></span></span></div></div></div>   



<!-- =====  LINK4  ======  LINK4 ===============  LINK4 ================ -->
<div class="wrap-input100 validate-input m-b-16" >
    <div class="control-group <?php echo !empty($link4Erro) ? 'error ' : ''; ?>">
        <label class="titulo">4º Link do jogo</label>
            <div class="controls">
                <input class="input100"  name="link4" type="text" placeholder="Insira o link 4"
                value="<?php echo !empty($link4) ? $link4 : ''; ?>">
                <?php if (!empty($link4Erro)): ?>
                <span class="text-danger"><?php echo $link4Erro; ?></span>
                <?php endif; ?>
<span class="focus-input100"></span></span></div></div></div>   



<!-- =====  LINK5  ======  LINK5 ===============  LINK5 ================ -->
<div class="wrap-input100 validate-input m-b-16" >
    <div class="control-group <?php echo !empty($link5Erro) ? 'error ' : ''; ?>">
        <label class="titulo">5º Link do jogo</label>
            <div class="controls">
                <input class="input100"  name="link5" type="text" placeholder="Insira o link 5"
                value="<?php echo !empty($link5) ? $link5 : ''; ?>">
                <?php if (!empty($link5Erro)): ?>
                <span class="text-danger"><?php echo $link5Erro; ?></span>
                <?php endif; ?>
<span class="focus-input100"></span></span></div></div></div>   



<!-- =====  LINK6  ======  LINK6 ===============  LINK6 ================ -->
<div class="wrap-input100 validate-input m-b-16" >
    <div class="control-group <?php echo !empty($link6Erro) ? 'error ' : ''; ?>">
        <label class="titulo">6º Link do jogo</label>
            <div class="controls">
                <input class="input100"  name="link6" type="text" placeholder="Insira o link 6"
                value="<?php echo !empty($link6) ? $link6 : ''; ?>">
                <?php if (!empty($link6Erro)): ?>
                <span class="text-danger"><?php echo $link6Erro; ?></span>
                <?php endif; ?>
<span class="focus-input100"></span></span></div></div></div>   



<!-- =====  LINK7  ======  LINK7 ===============  LINK7 ================ -->
<div class="wrap-input100 validate-input m-b-16" >
    <div class="control-group <?php echo !empty($link7Erro) ? 'error ' : ''; ?>">
        <label class="titulo">7º Link do jogo</label>
            <div class="controls">
                <input class="input100"  name="link7" type="text" placeholder="Insira o link 7"
                value="<?php echo !empty($link7) ? $link7 : ''; ?>">
                <?php if (!empty($link7Erro)): ?>
                <span class="text-danger"><?php echo $link7Erro; ?></span>
                <?php endif; ?>
<span class="focus-input100"></span></span></div></div></div>   



<!-- =====  LINK8  ======  LINK8 ===============  LINK8 ================ -->
<div class="wrap-input100 validate-input m-b-16" >
    <div class="control-group <?php echo !empty($link8Erro) ? 'error ' : ''; ?>">
        <label class="titulo">8º Link do jogo</label>
            <div class="controls">
                <input class="input100"  name="link8" type="text" placeholder="Insira o link 8"
                value="<?php echo !empty($link8) ? $link8 : ''; ?>">
                <?php if (!empty($link8Erro)): ?>
                <span class="text-danger"><?php echo $link8Erro; ?></span>
                <?php endif; ?>
<span class="focus-input100"></span></span></div></div></div>   



<!-- =====  LINK9  ======  LINK9 ===============  LINK9 ================ -->
<div class="wrap-input100 validate-input m-b-16" >
    <div class="control-group <?php echo !empty($link9Erro) ? 'error ' : ''; ?>">
        <label class="titulo">9º Link do jogo</label>
            <div class="controls">
                <input class="input100"  name="link9" type="text" placeholder="Insira o link 9"
                value="<?php echo !empty($link9) ? $link9 : ''; ?>">
                <?php if (!empty($link9Erro)): ?>
                <span class="text-danger"><?php echo $link9Erro; ?></span>
                <?php endif; ?>
<span class="focus-input100"></span></span></div></div></div>   



<!-- =====  LINK10  ======  LINK10 ===============  LINK10 ================ -->
<div class="wrap-input100 validate-input m-b-16" >
    <div class="control-group <?php echo !empty($link10Erro) ? 'error ' : ''; ?>">
        <label class="titulo">10º Link do jogo</label>
            <div class="controls">
                <input class="input100"  name="link10" type="text" placeholder="Insira o link 10"
                value="<?php echo !empty($link10) ? $link10 : ''; ?>">
                <?php if (!empty($link10Erro)): ?>
                <span class="text-danger"><?php echo $link10Erro; ?></span>
                <?php endif; ?>
<span class="focus-input100"></span></span></div></div></div>   



<!-- =====  LINK11  ======  LINK11 ===============  LINK11 ================ -->
<div class="wrap-input100 validate-input m-b-16" >
    <div class="control-group <?php echo !empty($link11Erro) ? 'error ' : ''; ?>">
        <label class="titulo">11º Link do jogo</label>
            <div class="controls">
                <input class="input100"  name="link11" type="text" placeholder="Insira o link 11"
                value="<?php echo !empty($link11) ? $link11 : ''; ?>">
                <?php if (!empty($link11Erro)): ?>
                <span class="text-danger"><?php echo $link11Erro; ?></span>
                <?php endif; ?>
<span class="focus-input100"></span></span></div></div></div>   



<!-- =====  LINK12  ======  LINK12 ===============  LINK12 ================ -->
<div class="wrap-input100 validate-input m-b-16" >
    <div class="control-group <?php echo !empty($link12Erro) ? 'error ' : ''; ?>">
        <label class="titulo">12º Link do jogo</label>
            <div class="controls">
                <input class="input100"  name="link12" type="text" placeholder="Insira o link 12"
                value="<?php echo !empty($link12) ? $link12 : ''; ?>">
                <?php if (!empty($link12Erro)): ?>
                <span class="text-danger"><?php echo $link12Erro; ?></span>
                <?php endif; ?>
<span class="focus-input100"></span></span></div></div></div>   



<!-- =====  LINK13  ======  LINK13 ===============  LINK13 ================ -->
<div class="wrap-input100 validate-input m-b-16" >
    <div class="control-group <?php echo !empty($link13Erro) ? 'error ' : ''; ?>">
        <label class="titulo">13º Link do jogo</label>
            <div class="controls">
                <input class="input100"  name="link13" type="text" placeholder="Insira o link 13"
                value="<?php echo !empty($link13) ? $link13 : ''; ?>">
                <?php if (!empty($link13Erro)): ?>
                <span class="text-danger"><?php echo $link13Erro; ?></span>
                <?php endif; ?>
<span class="focus-input100"></span></span></div></div></div>   



<!-- =====  LINK14  ======  LINK14 ===============  LINK14 ================ -->
<div class="wrap-input100 validate-input m-b-16" >
    <div class="control-group <?php echo !empty($link14Erro) ? 'error ' : ''; ?>">
        <label class="titulo">14º Link do jogo</label>
            <div class="controls">
                <input class="input100"  name="link14" type="text" placeholder="Insira o link 14"
                value="<?php echo !empty($link14) ? $link14 : ''; ?>">
                <?php if (!empty($link14Erro)): ?>
                <span class="text-danger"><?php echo $link14Erro; ?></span>
                <?php endif; ?>
<span class="focus-input100"></span></span></div></div></div>   



<!-- =====  LINK15  ======  LINK15 ===============  LINK15 ================ -->
<div class="wrap-input100 validate-input m-b-16" >
    <div class="control-group <?php echo !empty($link15Erro) ? 'error ' : ''; ?>">
        <label class="titulo">15º Link do jogo</label>
            <div class="controls">
                <input class="input100"  name="link15" type="text" placeholder="Insira o link 15"
                value="<?php echo !empty($link15) ? $link15 : ''; ?>">
                <?php if (!empty($link15Erro)): ?>
                <span class="text-danger"><?php echo $link15Erro; ?></span>
                <?php endif; ?>
<span class="focus-input100"></span></span></div></div></div>   



<!-- =====  LINK16  ======  LINK16 ===============  LINK16 ================ -->
<div class="wrap-input100 validate-input m-b-16" >
    <div class="control-group <?php echo !empty($link16Erro) ? 'error ' : ''; ?>">
        <label class="titulo">16º Link do jogo</label>
            <div class="controls">
                <input class="input100"  name="link16" type="text" placeholder="Insira o link 16"
                value="<?php echo !empty($link16) ? $link16 : ''; ?>">
                <?php if (!empty($link16Erro)): ?>
                <span class="text-danger"><?php echo $link16Erro; ?></span>
                <?php endif; ?>
<span class="focus-input100"></span></span></div></div></div>  


<!-- =====  LINK17  ======  LINK17 ===============  LINK17 ================ -->
<div class="wrap-input100 validate-input m-b-16" >
    <div class="control-group <?php echo !empty($link17Erro) ? 'error ' : ''; ?>">
        <label class="titulo">17º Link do jogo</label>
            <div class="controls">
                <input class="input100"  name="link17" type="text" placeholder="Insira o link 17"
                value="<?php echo !empty($link17) ? $link17 : ''; ?>">
                <?php if (!empty($link17Erro)): ?>
                <span class="text-danger"><?php echo $link17Erro; ?></span>
                <?php endif; ?>
<span class="focus-input100"></span></span></div></div></div>  


<!-- =====  LINK18  ======  LINK18 ===============  LINK18 ================ -->
<div class="wrap-input100 validate-input m-b-16" >
    <div class="control-group <?php echo !empty($link18Erro) ? 'error ' : ''; ?>">
        <label class="titulo">18º Link do jogo</label>
            <div class="controls">
                <input class="input100"  name="link18" type="text" placeholder="Insira o link 18"
                value="<?php echo !empty($link18) ? $link18 : ''; ?>">
                <?php if (!empty($link18Erro)): ?>
                <span class="text-danger"><?php echo $link18Erro; ?></span>
                <?php endif; ?>
<span class="focus-input100"></span></span></div></div></div>  


<!-- =====  LINK19  ======  LINK19 ===============  LINK19 ================ -->
<div class="wrap-input100 validate-input m-b-16" >
    <div class="control-group <?php echo !empty($link19Erro) ? 'error ' : ''; ?>">
        <label class="titulo">19º Link do jogo</label>
            <div class="controls">
                <input class="input100"  name="link19" type="text" placeholder="Insira o link 19"
                value="<?php echo !empty($link19) ? $link19 : ''; ?>">
                <?php if (!empty($link19Erro)): ?>
                <span class="text-danger"><?php echo $link19Erro; ?></span>
                <?php endif; ?>
<span class="focus-input100"></span></span></div></div></div>  


<!-- =====  LINK20  ======  LINK20 ===============  LINK20 ================ -->
<div class="wrap-input100 validate-input m-b-16" >
    <div class="control-group <?php echo !empty($link20Erro) ? 'error ' : ''; ?>">
        <label class="titulo">20º Link do jogo</label>
            <div class="controls">
                <input class="input100"  name="link20" type="text" placeholder="Insira o link 20"
                value="<?php echo !empty($link20) ? $link20 : ''; ?>">
                <?php if (!empty($link20Erro)): ?>
                <span class="text-danger"><?php echo $link20Erro; ?></span>
                <?php endif; ?>
<span class="focus-input100"></span></span></div></div></div>  


<!-- =====  LINK21  ======  LINK21 ===============  LINK21 ================ -->
<div class="wrap-input100 validate-input m-b-16" >
    <div class="control-group <?php echo !empty($link21Erro) ? 'error ' : ''; ?>">
        <label class="titulo">21º Link do jogo</label>
            <div class="controls">
                <input class="input100"  name="link21" type="text" placeholder="Insira o link 21"
                value="<?php echo !empty($link21) ? $link21 : ''; ?>">
                <?php if (!empty($link21Erro)): ?>
                <span class="text-danger"><?php echo $link21Erro; ?></span>
                <?php endif; ?>
<span class="focus-input100"></span></span></div></div></div>  


<!-- =====  LINK22  ======  LINK22 ===============  LINK22 ================ -->
<div class="wrap-input100 validate-input m-b-16" >
    <div class="control-group <?php echo !empty($link22Erro) ? 'error ' : ''; ?>">
        <label class="titulo">22º Link do jogo</label>
            <div class="controls">
                <input class="input100"  name="link22" type="text" placeholder="Insira o link 22"
                value="<?php echo !empty($link22) ? $link22 : ''; ?>">
                <?php if (!empty($link22Erro)): ?>
                <span class="text-danger"><?php echo $link22Erro; ?></span>
                <?php endif; ?>
<span class="focus-input100"></span></span></div></div></div>  


<!-- =====  LINK23  ======  LINK23 ===============  LINK23 ================ -->
<div class="wrap-input100 validate-input m-b-16" >
    <div class="control-group <?php echo !empty($link23Erro) ? 'error ' : ''; ?>">
        <label class="titulo">23º Link do jogo</label>
            <div class="controls">
                <input class="input100"  name="link23" type="text" placeholder="Insira o link 23"
                value="<?php echo !empty($link23) ? $link23 : ''; ?>">
                <?php if (!empty($link23Erro)): ?>
                <span class="text-danger"><?php echo $link23Erro; ?></span>
                <?php endif; ?>
<span class="focus-input100"></span></span></div></div></div>  


<!-- =====  LINK24  ======  LINK24 ===============  LINK24 ================ -->
<div class="wrap-input100 validate-input m-b-16" >
    <div class="control-group <?php echo !empty($link24Erro) ? 'error ' : ''; ?>">
        <label class="titulo">24º Link do jogo</label>
            <div class="controls">
                <input class="input100"  name="link24" type="text" placeholder="Insira o link 24"
                value="<?php echo !empty($link24) ? $link24 : ''; ?>">
                <?php if (!empty($link24Erro)): ?>
                <span class="text-danger"><?php echo $link24Erro; ?></span>
                <?php endif; ?>
<span class="focus-input100"></span></span></div></div></div>  


<!-- =====  LINK25  ======  LINK25 ===============  LINK25 ================ -->
<div class="wrap-input100 validate-input m-b-16" >
    <div class="control-group <?php echo !empty($link25Erro) ? 'error ' : ''; ?>">
        <label class="titulo">25º Link do jogo</label>
            <div class="controls">
                <input class="input100"  name="link25" type="text" placeholder="Insira o link 25"
                value="<?php echo !empty($link25) ? $link25 : ''; ?>">
                <?php if (!empty($link25Erro)): ?>
                <span class="text-danger"><?php echo $link25Erro; ?></span>
                <?php endif; ?>
<span class="focus-input100"></span></span></div></div></div>  


<!-- =====  LINK26  ======  LINK26 ===============  LINK26 ================ -->
<div class="wrap-input100 validate-input m-b-16" >
    <div class="control-group <?php echo !empty($link26Erro) ? 'error ' : ''; ?>">
        <label class="titulo">26º Link do jogo</label>
            <div class="controls">
                <input class="input100"  name="link26" type="text" placeholder="Insira o link 26"
                value="<?php echo !empty($link26) ? $link26 : ''; ?>">
                <?php if (!empty($link26Erro)): ?>
                <span class="text-danger"><?php echo $link26Erro; ?></span>
                <?php endif; ?>
<span class="focus-input100"></span></span></div></div></div>  


<!-- =====  LINK27  ======  LINK27 ===============  LINK27 ================ -->
<div class="wrap-input100 validate-input m-b-16" >
    <div class="control-group <?php echo !empty($link27Erro) ? 'error ' : ''; ?>">
        <label class="titulo">27º Link do jogo</label>
            <div class="controls">
                <input class="input100"  name="link27" type="text" placeholder="Insira o link 27"
                value="<?php echo !empty($link27) ? $link27 : ''; ?>">
                <?php if (!empty($link27Erro)): ?>
                <span class="text-danger"><?php echo $link27Erro; ?></span>
                <?php endif; ?>
<span class="focus-input100"></span></span></div></div></div>  


<!-- =====  LINK28  ======  LINK28 ===============  LINK28 ================ -->
<div class="wrap-input100 validate-input m-b-16" >
    <div class="control-group <?php echo !empty($link28Erro) ? 'error ' : ''; ?>">
        <label class="titulo">28º Link do jogo</label>
            <div class="controls">
                <input class="input100"  name="link28" type="text" placeholder="Insira o link 28"
                value="<?php echo !empty($link28) ? $link28 : ''; ?>">
                <?php if (!empty($link28Erro)): ?>
                <span class="text-danger"><?php echo $link28Erro; ?></span>
                <?php endif; ?>
<span class="focus-input100"></span></span></div></div></div>  


<!-- =====  LINK29  ======  LINK29 ===============  LINK29 ================ -->
<div class="wrap-input100 validate-input m-b-16" >
    <div class="control-group <?php echo !empty($link29Erro) ? 'error ' : ''; ?>">
        <label class="titulo">29º Link do jogo</label>
            <div class="controls">
                <input class="input100"  name="link29" type="text" placeholder="Insira o link 29"
                value="<?php echo !empty($link29) ? $link29 : ''; ?>">
                <?php if (!empty($link29Erro)): ?>
                <span class="text-danger"><?php echo $link29Erro; ?></span>
                <?php endif; ?>
<span class="focus-input100"></span></span></div></div></div>  


<!-- =====  LINK30  ======  LINK30 ===============  LINK30 ================ -->
<div class="wrap-input100 validate-input m-b-16" >
    <div class="control-group <?php echo !empty($link30Erro) ? 'error ' : ''; ?>">
        <label class="titulo">30º Link do jogo</label>
            <div class="controls">
                <input class="input100"  name="link30" type="text" placeholder="Insira o link 30"
                value="<?php echo !empty($link30) ? $link30 : ''; ?>">
                <?php if (!empty($link30Erro)): ?>
                <span class="text-danger"><?php echo $link30Erro; ?></span>
                <?php endif; ?>
<span class="focus-input100"></span></span></div></div></div>  




                    <div class="form-actions">
                        <br/>
                        <button type="submit" class="login100-form-btn m-b-16">Adicionar</button>
                        <a href="index.php" type="btn" class="login100-form-btn m-b-16">Voltar</a>
                    </div>
                </form>
            </div></div>
        </div>
    </div>
</div>
</div>
<script src="https://code.jquery.com/jquery-3.3.1.js" integrity="sha256-2Kok7MbOyxpgUVvAk/HJ2jigOSYS2auK4Pfzbm7uH60="
        crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"
        integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49"
        crossorigin="anonymous"></script>
<!-- Latest compiled and minified JavaScript -->
<script src="../../../assets/js/bootstrap.min.js"></script>
</body>

</html>

