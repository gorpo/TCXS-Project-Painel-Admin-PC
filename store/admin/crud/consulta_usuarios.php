<?php
session_start();
include('../../conexao.php');
// para iniciar esta sessao é necessario usar o link https://tcxsproject.com.br/cadastro.php?act=tcxs
//if (!$_REQUEST["act"] && $_REQUEST["act"] != "tcxs"){
//  header('Location: nao_logado.php');
//  exit();
//}

//verifica se esta logado senao redireciona
if(!$_SESSION['nome']) {
    header('Location: ../../nao_logado.php');
  exit();  
}


if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $usuario = filter_input(INPUT_POST, 'usuario');
} 

// Cria a conexão com o banco de dados
try {
     include('../../database.php');
    $conexao = Database::conectar();
    //$conexao = new PDO("mysql:host=localhost;dbname=tcxs_store", "root", "");
    //$conexao = new PDO("mysql:host=localhost;dbname=u923273795_users", "u923273795_users", "Tcxsproject2020web");
    $conexao->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $conexao->exec("set names utf8");
} catch (PDOException $erro) {
    echo "<p class=\"bg-danger\">Erro na conexão:" . $erro->getMessage() . "</p>";
}

// Bloco if que recupera as informações no formulário, etapa utilizada pelo Update
if (isset($_REQUEST["act"]) && $_REQUEST["act"] == "save" && $usuario != "") {
    try {
        $stmt = $conexao->prepare("SELECT * FROM user_$usuario");
        //$stmt->bindParam(1, $id, PDO::PARAM_INT);
        if ($stmt->execute()) {
            $rs = $stmt->fetch(PDO::FETCH_OBJ);
            $usuario = $rs->usuario;
            $senha = $rs->senha;
            $ip = $rs->ip;
            $data_atual = $rs->data_atual;
        } else {
            echo "<p class=\"bg-danger\">Erro: Não foi possível executar a declaração sql</p>";
        }
    } catch (PDOException $erro) {
        echo "<p class=\"bg-danger\">Caso usuário ainda não tenha realizado o login não teremos dados para consultar, espere ate que o usuário logue e tente novamente!</p>";
    }
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
      <meta property="og:image" content="../../assets/images/logo.png"/>
      <link rel="shortcut icon" href="../../assets/images/icon.png" />
      <script src="https://kit.fontawesome.com/a80232805f.js" crossorigin="anonymous"></script>
      <link rel="stylesheet" type="text/css" href="../../assets/css/style.css" />
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
      <link href="https://fonts.googleapis.com/css?family=Rubik&display=swap" rel="stylesheet">
      <script src="https://kit.fontawesome.com/af562a2a63.js" crossorigin="anonymous"></script>
      <title>TCXS Project STORE</title>
</head>
<body>

<div class="container">

        <!-- inicio da tabela -->

          <caption>
            <div class="barraTopo">
              <img class="logo" src="../../assets/images/logo_consultaip.png"><br>
                <!-- BARRA DE NAVEGAÇÃO DOS MENUS -->
                <div class="menu-content"> <label class="open-menu-all" for="open-menu-all">
                     <input class="input-menu-all" id="open-menu-all" type="checkbox" name="menu-open" />
                        <div class="navegacao-mobile">
                          <span class="linha-menu"></span>
                          <span class="linha-menu"></span>
                          <span class="linha-menu"></span>
                        </div>
                <ul class="list-menu">
                          <li class="item-menu"> <a href="cadastro_usuarios.php" class="link-menu ">Cadastro Usuarios</a></li>
                          <li class="item-menu"> <a href="consulta_usuarios.php" class="link-menu ">Verifica Usuarios</a></li>
                          <li class="item-menu"> <a href="infos/index.php" class="link-menu">PlayStation Infos</a></li>
                         <li class="item-menu"> <a href="psp/index.php" class="link-menu">PlayStation PSP</a></li>
                         <li class="item-menu"> <a href="ps1/index.php" class="link-menu">PlayStation1</a></li>
                         <li class="item-menu"> <a href="ps2/index.php" class="link-menu">PlayStation2</a></li>
                         <li class="item-menu"> <a href="ps3/index.php" class="link-menu">PlayStation3</a></li>
                         <li class="item-menu"> <a href="emuladores/index.php" class="link-menu">Emuladores</a></li>
						 <li class="item-menu"> <a href="extras/index.php" class="link-menu">Extras</a></li>
                </ul></label></div>
            </div>
          </caption>

 <div class="barraCadastro">
  <div class="blocoDadosInputs">
  <h3 class="tituloRed">Sistema de consulta | Verificar Vazamentos | Insira Usuario.</h3>

                    <form action="?act=save" method="POST" name="form1" class="form-horizontal" autocomplete="off">
                      <input type="hidden" name="id" value="<?php
            // Preenche o id no campo id com um valor "value"
            echo (isset($id) && ($id != null || $id != "")) ? $id : '';
            ?>" />


          <!-- =====   NOME NA LOJA  ======   -->
          <div class="wrap-input100 validate-input m-b-16" >
            <div class="control-group  <?php echo !empty($tituloErro) ? 'error ' : ''; ?>">
            <label class="titulo">Pesquisar usuário</label>
             <div class="controls">
            <input class="input100" type="text" name="usuario" value="<?php
                                        echo (isset($usuario) && ($usuario != null || $usuario != "")) ? $usuario : '';
                                        ?>" class="form-control" />
            <span class="focus-input100"></span>
            </span>
          </div></div></div>

            <div class="form-actions">
                        <button type="submit" class="login100-form-btn ">Verificar Acessos e IP</button>
                    </div><br><br>
                </form>


                           
                <div class="row">
                    <div class="panel panel-default">
                        <table class="table table-striped">
                            <thead>
                                <tr>
                                    <td scope="col">ip</td>
                                    <td scope="col">usuario</td>
                                    <td scope="col">senha</td>
                                    <td scope="col">data</td>
                                </tr>
                            </thead>
                            <tbody>
                                <?php
                                //trata o erro nao exibingo a mensagem de erro do mysql por nao achar uma database.
                                error_reporting(E_ALL & ~E_NOTICE);
                                /**
                                 *  Bloco que realiza o papel do Read - recupera os dados e apresenta na tela
                                 */
                                try {
                                    $stmt = $conexao->prepare("SELECT * FROM user_$usuario");
                                    if ($stmt->execute()) {
                                        while ($rs = $stmt->fetch(PDO::FETCH_OBJ)) {

                                            ?><tr>
                                                <td data-label="Endereço IP:"><?php echo $rs->ip; ?></td>
                                                <td data-label="Usuário:"><?php echo $rs->usuario; ?></td>
                                                <td data-label="Senha:"><?php echo $rs->senha; ?></td>
                                                <td data-label="Acessado:"><?php echo $rs->data_atual; ?></td>
                                                
                                        </tr>
                                        <?php
                                    }
                                } else {
                                    echo "Erro: Não foi possível recuperar os dados do banco de dados";
                                }
                            } catch (PDOException $erro) {
                                

                                echo "Caso usuário ainda não tenha realizado o login não teremos dados para consultar, espere ate que o usuário logue e tente novamente!" ;
                            }

                            ?>


                            </tbody>
                        </table>
                    </div>
                </div>
            </article>
        </div>
        <!-- final do painel de consultas -->


<!-- final do painel de consultas -->
</html>
