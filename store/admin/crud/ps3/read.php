<?php
session_start();
if(!$_SESSION['nome']) {
  header('Location: ../../../nao_logado.php');
  exit();
}
require '../../../database.php';
$id = null;
if (!empty($_GET['id'])) {
    $id = $_REQUEST['id'];
}

if (null == $id) {
    header("Location: index.php");
} else {
    $pdo = Database::conectar();
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $sql = "SELECT * FROM playstation_ps3 where id = ?";
    $q = $pdo->prepare($sql);
    $q->execute(array($id));
    $data = $q->fetch(PDO::FETCH_ASSOC);
    database::desconectar();
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
      <title>TCXS Project | INFO PS3</title>
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
             <h3 class="tituloRed">[INFORMAÇÕES - APENAS LEITURA]<br>Jogo: <?php echo $data['titulo']; ?><br>PlayStation PS3<br>Data Cadastro: <?php echo $data['cadastro']; ?> </h3>
        <form class="form-horizontal">

            <!-- =====   TITULO ======   -->
          <div class="wrap-input100 validate-input m-b-16" >
            <div class="control-group  <?php echo !empty($tituloErro) ? 'error ' : ''; ?>">
            <label class="titulo">Titulo PS3</label>
                <div class="controls">
            <input class="input100" value="<?php echo $data['titulo']; ?>">
            <span class="focus-input100"></span></div></div></div>

            <!-- =====   descricao ======   -->
          <div class="wrap-input100 validate-input m-b-16" >
            <div class="control-group  <?php echo !empty($tituloErro) ? 'error ' : ''; ?>">
            <label class="titulo">descricao PS3</label>
                <div class="controls">
            <input class="input100" value="<?php echo $data['descricao']; ?>">
            <span class="focus-input100"></span></div></div></div>

            <!-- =====   CONTENT ID ======   -->
          <div class="wrap-input100 validate-input m-b-16" >
            <div class="control-group  <?php echo !empty($tituloErro) ? 'error ' : ''; ?>">
            <label class="titulo">CONTENT ID PS3</label>
                <div class="controls">
            <input class="input100" value="<?php echo $data['content_id']; ?>">
            <span class="focus-input100"></span></div></div></div>

            <!-- =====   IMAGEM ======   -->
          <div class="wrap-input100 validate-input m-b-16" >
            <div class="control-group  <?php echo !empty($tituloErro) ? 'error ' : ''; ?>">
            <label class="titulo">IMAGEM PS3</label>
                <div class="controls">
            <input class="input100" value="<?php echo $data['imagem']; ?>">
            <span class="focus-input100"></span></div></div></div>

            <!-- =====   Data ======   -->
          <div class="wrap-input100 validate-input m-b-16" >
            <div class="control-group  <?php echo !empty($tituloErro) ? 'error ' : ''; ?>">
            <label class="titulo">DATA PS3</label>
                <div class="controls">
            <input class="input100" value="<?php echo $data['cadastro']; ?>">
            <span class="focus-input100"></span></div></div></div>


            

<!-- =====   LINK1 ======  LINK1 ====== LINK1 ======  -->
          <div class="wrap-input100 validate-input m-b-16" >
            <label class="titulo">Link1 PS3</label>
                <div class="controls">
            <input class="input100" value="<?php echo $data['link1']; ?>">
            <span class="focus-input100"></span></div></div></div>

<!-- =====   LINK2 ======  LINK2 ====== LINK2 ======  -->
          <div class="wrap-input100 validate-input m-b-16" >
            <label class="titulo">Link2 PS3</label>
                <div class="controls">
            <input class="input100" value="<?php echo $data['link2']; ?>">
            <span class="focus-input100"></span></div></div></div>

<!-- =====   LINK3 ======  LINK3 ====== LINK3 ======  -->
          <div class="wrap-input100 validate-input m-b-16" >
            <label class="titulo">Link3 PS3</label>
                <div class="controls">
            <input class="input100" value="<?php echo $data['link3']; ?>">
            <span class="focus-input100"></span></div></div></div>

<!-- =====   LINK4 ======  LINK4 ====== LINK4 ======  -->
          <div class="wrap-input100 validate-input m-b-16" >
            <label class="titulo">Link4 PS3</label>
                <div class="controls">
            <input class="input100" value="<?php echo $data['link4']; ?>">
            <span class="focus-input100"></span></div></div></div>

<!-- =====   LINK5 ======  LINK5 ====== LINK5 ======  -->
          <div class="wrap-input100 validate-input m-b-16" >
            <label class="titulo">Link5 PS3</label>
                <div class="controls">
            <input class="input100" value="<?php echo $data['link5']; ?>">
            <span class="focus-input100"></span></div></div></div>

<!-- =====   LINK6 ======  LINK6 ====== LINK6 ======  -->
          <div class="wrap-input100 validate-input m-b-16" >
            <label class="titulo">Link6 PS3</label>
                <div class="controls">
            <input class="input100" value="<?php echo $data['link6']; ?>">
            <span class="focus-input100"></span></div></div></div>

<!-- =====   LINK7 ======  LINK7 ====== LINK7 ======  -->
          <div class="wrap-input100 validate-input m-b-16" >
            <label class="titulo">Link7 PS3</label>
                <div class="controls">
            <input class="input100" value="<?php echo $data['link7']; ?>">
            <span class="focus-input100"></span></div></div></div>

<!-- =====   LINK8 ======  LINK8 ====== LINK8 ======  -->
          <div class="wrap-input100 validate-input m-b-16" >
            <label class="titulo">Link8 PS3</label>
                <div class="controls">
            <input class="input100" value="<?php echo $data['link8']; ?>">
            <span class="focus-input100"></span></div></div></div>

<!-- =====   LINK9 ======  LINK9 ====== LINK9 ======  -->
          <div class="wrap-input100 validate-input m-b-16" >
            <label class="titulo">Link9 PS3</label>
                <div class="controls">
            <input class="input100" value="<?php echo $data['link9']; ?>">
            <span class="focus-input100"></span></div></div></div>

<!-- =====   LINK10 ======  LINK10 ====== LINK10 ======  -->
          <div class="wrap-input100 validate-input m-b-16" >
            <label class="titulo">Link10 PS3</label>
                <div class="controls">
            <input class="input100" value="<?php echo $data['link10']; ?>">
            <span class="focus-input100"></span></div></div></div>

<!-- =====   LINK11 ======  LINK11 ====== LINK11 ======  -->
          <div class="wrap-input100 validate-input m-b-16" >
            <label class="titulo">Link11 PS3</label>
                <div class="controls">
            <input class="input100" value="<?php echo $data['link11']; ?>">
            <span class="focus-input100"></span></div></div></div>

<!-- =====   LINK12 ======  LINK12 ====== LINK12 ======  -->
          <div class="wrap-input100 validate-input m-b-16" >
            <label class="titulo">Link12 PS3</label>
                <div class="controls">
            <input class="input100" value="<?php echo $data['link12']; ?>">
            <span class="focus-input100"></span></div></div></div>

<!-- =====   LINK13 ======  LINK13 ====== LINK13 ======  -->
          <div class="wrap-input100 validate-input m-b-16" >
            <label class="titulo">Link13 PS3</label>
                <div class="controls">
            <input class="input100" value="<?php echo $data['link13']; ?>">
            <span class="focus-input100"></span></div></div></div>

<!-- =====   LINK14 ======  LINK14 ====== LINK14 ======  -->
          <div class="wrap-input100 validate-input m-b-16" >
            <label class="titulo">Link14 PS3</label>
                <div class="controls">
            <input class="input100" value="<?php echo $data['link14']; ?>">
            <span class="focus-input100"></span></div></div></div>

<!-- =====   LINK15 ======  LINK15 ====== LINK15 ======  -->
          <div class="wrap-input100 validate-input m-b-16" >
            <label class="titulo">Link15 PS3</label>
                <div class="controls">
            <input class="input100" value="<?php echo $data['link15']; ?>">
            <span class="focus-input100"></span></div></div></div>


<!-- =====   LINK16 ======  LINK16 ====== LINK16 ======  -->
          <div class="wrap-input100 validate-input m-b-16" >
            <label class="titulo">Link16 PS3</label>
                <div class="controls">
            <input class="input100" value="<?php echo $data['link16']; ?>">
            <span class="focus-input100"></span></div></div></div>


<!-- =====   LINK17 ======  LINK17 ====== LINK17 ======  -->
          <div class="wrap-input100 validate-input m-b-16" >
            <label class="titulo">Link17 PS3</label>
                <div class="controls">
            <input class="input100" value="<?php echo $data['link17']; ?>">
            <span class="focus-input100"></span></div></div></div>


<!-- =====   LINK18 ======  LINK18 ====== LINK18 ======  -->
          <div class="wrap-input100 validate-input m-b-16" >
            <label class="titulo">Link18 PS3</label>
                <div class="controls">
            <input class="input100" value="<?php echo $data['link18']; ?>">
            <span class="focus-input100"></span></div></div></div>


<!-- =====   LINK19 ======  LINK19 ====== LINK19 ======  -->
          <div class="wrap-input100 validate-input m-b-16" >
            <label class="titulo">Link19 PS3</label>
                <div class="controls">
            <input class="input100" value="<?php echo $data['link19']; ?>">
            <span class="focus-input100"></span></div></div></div>


<!-- =====   LINK20 ======  LINK20 ====== LINK20 ======  -->
          <div class="wrap-input100 validate-input m-b-16" >
            <label class="titulo">Link20 PS3</label>
                <div class="controls">
            <input class="input100" value="<?php echo $data['link20']; ?>">
            <span class="focus-input100"></span></div></div></div>


<!-- =====   LINK21 ======  LINK21 ====== LINK21 ======  -->
          <div class="wrap-input100 validate-input m-b-16" >
            <label class="titulo">Link21 PS3</label>
                <div class="controls">
            <input class="input100" value="<?php echo $data['link21']; ?>">
            <span class="focus-input100"></span></div></div></div>


<!-- =====   LINK22 ======  LINK22 ====== LINK22 ======  -->
          <div class="wrap-input100 validate-input m-b-16" >
            <label class="titulo">Link22 PS3</label>
                <div class="controls">
            <input class="input100" value="<?php echo $data['link22']; ?>">
            <span class="focus-input100"></span></div></div></div>


<!-- =====   LINK23 ======  LINK23 ====== LINK23 ======  -->
          <div class="wrap-input100 validate-input m-b-16" >
            <label class="titulo">Link23 PS3</label>
                <div class="controls">
            <input class="input100" value="<?php echo $data['link23']; ?>">
            <span class="focus-input100"></span></div></div></div>


<!-- =====   LINK24 ======  LINK24 ====== LINK24 ======  -->
          <div class="wrap-input100 validate-input m-b-16" >
            <label class="titulo">Link24 PS3</label>
                <div class="controls">
            <input class="input100" value="<?php echo $data['link24']; ?>">
            <span class="focus-input100"></span></div></div></div>


<!-- =====   LINK25 ======  LINK25 ====== LINK25 ======  -->
          <div class="wrap-input100 validate-input m-b-16" >
            <label class="titulo">Link25 PS3</label>
                <div class="controls">
            <input class="input100" value="<?php echo $data['link25']; ?>">
            <span class="focus-input100"></span></div></div></div>


<!-- =====   LINK26 ======  LINK26 ====== LINK26 ======  -->
          <div class="wrap-input100 validate-input m-b-16" >
            <label class="titulo">Link26 PS3</label>
                <div class="controls">
            <input class="input100" value="<?php echo $data['link26']; ?>">
            <span class="focus-input100"></span></div></div></div>


<!-- =====   LINK27 ======  LINK27 ====== LINK27 ======  -->
          <div class="wrap-input100 validate-input m-b-16" >
            <label class="titulo">Link27 PS3</label>
                <div class="controls">
            <input class="input100" value="<?php echo $data['link27']; ?>">
            <span class="focus-input100"></span></div></div></div>


<!-- =====   LINK28 ======  LINK28 ====== LINK28 ======  -->
          <div class="wrap-input100 validate-input m-b-16" >
            <label class="titulo">Link28 PS3</label>
                <div class="controls">
            <input class="input100" value="<?php echo $data['link28']; ?>">
            <span class="focus-input100"></span></div></div></div>


<!-- =====   LINK29 ======  LINK29 ====== LINK29 ======  -->
          <div class="wrap-input100 validate-input m-b-16" >
            <label class="titulo">Link29 PS3</label>
                <div class="controls">
            <input class="input100" value="<?php echo $data['link29']; ?>">
            <span class="focus-input100"></span></div></div></div>


<!-- =====   LINK30 ======  LINK30 ====== LINK30 ======  -->
          <div class="wrap-input100 validate-input m-b-16" >
            <label class="titulo">Link30 PS3</label>
                <div class="controls">
            <input class="input100" value="<?php echo $data['link30']; ?>">
            <span class="focus-input100"></span></div></div></div>





                    <br/>
                    <div class="form-actions">
                        <a href="index.php" type="btn" class="login100-form-btn m-b-16">Voltar</a>
                    </div>
                </div>
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
