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

  
// Verificar se foi enviando dados via POST
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $id = filter_input(INPUT_POST, 'id');
    $nome = filter_input(INPUT_POST, 'nome');
    $usuario = filter_input(INPUT_POST, 'usuario');
    $senha = filter_input(INPUT_POST, 'senha');
} else if (!isset($id)) {
// Se não se não foi setado nenhum valor para variável $id
    $id = (isset($_GET["id"]) && $_GET["id"] != null) ? $_GET["id"] : "";
    $usuario = (isset($_GET["usuario"]) && $_GET["usuario"] != null) ? $_GET["usuario"] : "";
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
              <img class="logo" src="../../assets/images/logo_cadastrouser.png"><br>
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
                          <li class="item-menu"> <a href="consulta_usuarios.php" class="link-menu">Verifica Usuarios</a></li>
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
  <h3 class="tituloRed">CADASTRO DE USUÁRIOS</h3>

  <?php
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




// Bloco If que Salva os dados no Banco - atua como Create e Update
if (isset($_REQUEST["act"]) && $_REQUEST["act"] == "save" && $nome != "") {
    try {
        if ($id != "") {
            $stmt = $conexao->prepare("UPDATE playstation_users SET nome=?, usuario=?,senha=?,cadastro=? WHERE id = ?");
            $stmt->bindParam(10, $id);
        } else {
            $stmt = $conexao->prepare("INSERT INTO playstation_users (nome, usuario, senha,cadastro,nivel) VALUES (?, ?, ?, NOW(),'user')");
        }
        $stmt->bindParam(1, $nome);
        $stmt->bindParam(2, $usuario);
        $stmt->bindParam(3, $senha);
        if ($stmt->execute()) {
            if ($stmt->rowCount() > 0) {
                echo "<p class=\"tituloBranco\">Usuário $nome adicionado para usar a loja!</p>";
                $id = null;
                $nome = null;
                $usuario = null;
                $senha = null;
            } else {
                echo "<p class=\"bg-danger\">Erro ao tentar efetivar cadastro</p>";
            }
        } else {
            echo "<p class=\"bg-danger\">Erro: Não foi possível executar a declaração sql</p>";
        }
    } catch (PDOException $erro) {
        echo "<p class=\"bg-danger\">Erro: " . $erro->getMessage() . "</p>";
    }
}





// Bloco if que recupera as informações no formulário, etapa utilizada pelo Update
if (isset($_REQUEST["act"]) && $_REQUEST["act"] == "upd" && $id != "") {
    try {
        $stmt = $conexao->prepare("SELECT * FROM playstation_users WHERE id = ?");
        $stmt->bindParam(1, $id, PDO::PARAM_INT);
        if ($stmt->execute()) {
            $rs = $stmt->fetch(PDO::FETCH_OBJ);
            $id = $rs->id;
            $nome = $rs->nome;
            $usuario = $rs->usuario;
            $senha = $rs->senha;
        } else {
            echo "<p class=\"bg-danger\">Erro: Não foi possível executar a declaração sql</p>";
        }
    } catch (PDOException $erro) {
        echo "<p class=\"bg-danger\">Erro: " . $erro->getMessage() . "</p>";
    }
}
   




// Bloco if utilizado pela etapa Delete
if (isset($_REQUEST["act"]) && $_REQUEST["act"] == "del" && $id != "" && $usuario != "") {
    try {
        $stmt = $conexao->prepare("DELETE FROM playstation_users WHERE id = ?");
        $stmt->bindParam(1, $id, PDO::PARAM_INT);
        $stmt2 = $conexao->prepare("DROP TABLE user_$usuario");
        $stmt2->bindParam(1, $usuario, PDO::PARAM_INT);
        if ($stmt->execute()) {
            echo "<p class=\"tituloBranco\">Usuário $usuario removido com exito do sistema.</p>";
            $id = null;
        } else {
            echo "<p class=\"bg-danger\">Erro: Não foi possível executar a declaração sql</p>";
        }
        if ($stmt2->execute()) {
            echo "<p class=\"tituloBranco\">Todos os dados de login e IP do usuário foram deletados.</p>";
            $usuario = null;
        } else {
            echo "<p class=\"tituloBranco\">Erro: Não foi possível executar a declaração sql</p>";
        }


    } catch (PDOException $erro) {
        echo "<p class=\"tituloBranco\">Usuário ainda não tinha logado no sistema, sem database de IP para deletar.</a>";
    }
}
?>


<form action="?act=save" method="POST" name="form1" class="form-horizontal" autocomplete="off">
    


          <!-- =====   NOME NA LOJA  ======   -->
          <div class="wrap-input100 validate-input m-b-16" >
            <div class="control-group  <?php echo !empty($tituloErro) ? 'error ' : ''; ?>">
            <label class="titulo">NOME EXIBIÇÃO</label>
             <div class="controls">
            <input class="input100" type="text" name="nome" value="<?php
                                        echo (isset($nome) && ($nome != null || $nome != "")) ? $nome : '';
                                        ?>" class="form-control"/>
            <span class="focus-input100"></span>
            </span>
          </div></div></div>

          <!-- =====   USUARIO ======   -->
          <div class="wrap-input100 validate-input m-b-16" >
            <div class="control-group  <?php echo !empty($tituloErro) ? 'error ' : ''; ?>">
            <label class="titulo">USUARIO</label>
             <div class="controls">
            <input class="input100" type="text" name="usuario" value="<?php
                                        echo (isset($usuario) && ($usuario != null || $usuario != "")) ? $usuario : '';
                                        ?>" class="form-control" />
            <span class="focus-input100"></span>
            </span>
          </div></div></div>

          <!-- =====   SENHA ======   -->
          <div class="wrap-input100 validate-input m-b-16" >
            <div class="control-group  <?php echo !empty($tituloErro) ? 'error ' : ''; ?>">
            <label class="titulo">SENHA</label>
             <div class="controls">
            <input class="input100" type="text" name="senha" value="<?php
                                        echo (isset($senha) && ($senha != null || $senha != "")) ? $senha : '';
                                        ?>" class="form-control" />
            <span class="focus-input100"></span>
            </span>
          </div></div></div>
                           

                    <div class="form-actions">
                        <button type="submit" class="login100-form-btn item-menu">Adicionar Usuário na TCXS Store</button>
                    </div><br><br>
                </form>
            


                
                    <div class="panel panel-default">
                        <table class="table table-striped">
                            <thead>
                                <tr>
                                	<td scope="col">ID</td>
                                    <td scope="col">NOME</td>
                                    <td scope="col">USUARIO</td>
                                    <td scope="col">SENHA</td>
                                    <td scope="col">CADASTRO</td>
                                    <td scope="col">NIVEL</td>
                                    <td scope="col">BANIR</td>
                                </tr>
                            </thead>
                            <tbody>
                                <?php
                                /**
                                 *  Bloco que realiza o papel do Read - recupera os dados e apresenta na tela
                                 */
                                try {
                                    $stmt = $conexao->prepare("SELECT * FROM playstation_users");
                                    if ($stmt->execute()) {
                                        while ($rs = $stmt->fetch(PDO::FETCH_OBJ)) {

                                            ?><tr>
                                            	<td data-label="ID:"><?php echo $rs->id; ?></td>
                                                <td data-label="Nome:"><?php echo $rs->nome; ?></td>
                                                <td data-label="Usuário:"><?php echo $rs->usuario; ?></td>
                                                <td data-label="Senha:"><?php echo $rs->senha; ?></td>
                                                <td data-label="Cadastro:"><?php echo $rs->cadastro; ?></td>
                                                <td data-label="Nivel:"><?php echo $rs->nivel; ?></td>
                                               

                                                <td  data-label="Banir:">
                                                 <a href="?act=del&id=<?php echo $rs->id; ?>&usuario=<?php echo $rs->usuario; ?>" class="botaoIcones" ><i class="fas fa-trash" aria-hidden="true"></i> Banir Usuário</a>
                                                </td>
                                        </tr>


                                        <?php
                                    }
                                } else {
                                    echo "Erro: Não foi possível recuperar os dados do banco de dados";
                                }
                            } catch (PDOException $erro) {
                                echo "Erro: " . $erro->getMessage();
                            }

                            ?>
                            </tbody>
                        </table>
                    </div>
                </div>


            </article>
        </div>

<script src="https://code.jquery.com/jquery-3.3.1.js" integrity="sha256-2Kok7MbOyxpgUVvAk/HJ2jigOSYS2auK4Pfzbm7uH60=" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <!-- Latest compiled and minified JavaScript -->
    <script src="../../../assets/js/bootstrap.min.js"></script>
</body>

</html>
