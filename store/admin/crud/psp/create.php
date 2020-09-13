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
    $linkErro = null;

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
            $imagemErro = 'Por favor digite o imagem!';
            $validacao = False;
        }


       
        if (!empty($_POST['link'])) {
            $link = $_POST['link'];
        } else {
            $linkErro = 'Por favor digite link!';
            $validacao = False;
        }



    }
//---------------------------------------------------------------------------------------------------------------------
//Inserindo o jogo na database:
    if ($validacao) {
        $pdo = Database::conectar();
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        $sql = "INSERT INTO playstation_psp (titulo, descricao, content_id, imagem,cadastro, link) VALUES(?,?,?,?,NOW(),? )";
        $q = $pdo->prepare($sql);
        $q->execute(array($titulo, $descricao, $content_id, $imagem, $link));
        database::desconectar();
        header("Location: index.php");
    }
}


//---------------------------------------------------------------------------------------------------------------------
//================== FUNÇÃO UPLOAD DE IMAGEM | REDIMENSIONAMENTO | MARCA DAGUA TCXS ===================================
//--------------------------------------------------->>>
// CAMINHO PARA SALVAR A IMAGEM | CAMINHO DA MARCA DAGUA
$targetDir = "../../../assets/images/psp/"; 
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


<!-- ============= TEMPLATE HTML ======== --->
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
      <title>TCXS Project | ADD PSP GAME</title>
</head>
<body>
<div class="container">

<!-- ============= MENUS PARA PC E CELULAR ======== --->
    <caption>
            <div class="barraTopo">
              <img class="logo" src="../../../assets/images/logo_psp.png"><br>
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
                         <li class="item-menu"> <a href="index.php" class="link-menu">PlayStation PSP</a></li>
                         <li class="item-menu"> <a href="../ps1/index.php" class="link-menu">PlayStation1</a></li>
                         <li class="item-menu"> <a href="../ps2/index.php" class="link-menu">PlayStation2</a></li>
                         <li class="item-menu"> <a href="../ps3/index.php" class="link-menu">PlayStation3</a></li>
                         <li class="item-menu"> <a href="../emuladores/index.php" class="link-menu">Emuladores</a></li>
						 <li class="item-menu"> <a href="../extras/index.php" class="link-menu">Extras</a></li>
                </ul></label></div>
            </div>
          </caption>




<div class="barraBase ">
	<div class="blocoDadosInputs">
  <h3 class="tituloRed"> Cadastrar PlayStation PSP</h3>
        <form class="form-horizontal" action="create.php" method="post"  autocomplete="off" enctype="multipart/form-data">


          <!-- =====   TITULO ======   -->
          <div class="wrap-input100 validate-input m-b-16" >
            <div class="control-group  <?php echo !empty($tituloErro) ? 'error ' : ''; ?>">
            <label class="titulo">Titulo PSP</label>
             <div class="controls">
            <input class="input100" type="text" name="titulo" type="text" placeholder="Insira o titulo do jogo"
                                   value="<?php echo !empty($titulo) ? $titulo : ''; ?>">
                                   <?php if (!empty($tituloErro)): ?>
                                <span class="text-danger"><?php echo $tituloErro; ?></span>
                            <?php endif; ?>
            <span class="focus-input100"></span>
            </span>
          </div></div></div>

          <!-- =====   descricao ======   -->
          <div class="wrap-input100 validate-input m-b-16" >
             <div class="control-group <?php echo !empty($descricaoErro) ? 'error ' : ''; ?>">
                        <label class="titulo">descricao PSP</label>
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
                        <label class="titulo">Content_id PSP</label>
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
                <label class="titulo">Imagem PSP</label>
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



                    

          <!-- =====  LINK  ======   -->
          <div class="wrap-input100 validate-input m-b-16" >
                    <div class="control-group <?php echo !empty($linkErro) ? 'error ' : ''; ?>">
                        <label class="titulo">Link do jogo</label>
                        <div class="controls">
                            <input class="input100"  name="link" type="text" placeholder="Insira o link"
                                   value="<?php echo !empty($link) ? $link : ''; ?>" >
                            <?php if (!empty($linkErro)): ?>
                                <span class="text-danger"><?php echo $linkErro; ?></span>
                            <?php endif; ?>
                        <span class="focus-input100"></span>
            </span>
          </div></div></div>
                  


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

