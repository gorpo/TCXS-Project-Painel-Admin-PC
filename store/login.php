<!-- ████████╗ ██████╗██╗  ██╗███████╗    ██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗
     ╚══██╔══╝██╔════╝╚██╗██╔╝██╔════╝    ██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝
        ██║   ██║      ╚███╔╝ ███████╗    ██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║   
        ██║   ██║      ██╔██╗ ╚════██║    ██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║   
        ██║   ╚██████╗██╔╝ ██╗███████║    ██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║   
        ╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝   -->
<!-- @Gorpo Orko - 2020 -->

<?php
session_start();
//inclui o arquivo de conexao com banco de dados
include('conexao.php');
//se usuario e senha estiverem vazios leva o usuario para o login novamente
if(empty($_POST['usuario']) || empty($_POST['senha'])) {
	header('Location: index.php');
	exit();
}

//-------------------------------------------------------------------------
//data de hoje
$datahoje = date('Y-m-d H:i:s'); 
// data de hoje +   . ' -33 days'
$dataatual = strtotime($datahoje);    
//pega a entrada do usuario no input
$usuario = mysqli_real_escape_string($conexao, $_POST['usuario']);
//pega senha do usuario no input
$senha = mysqli_real_escape_string($conexao, $_POST['senha']);
//pega o ip do usuario 
$ip = $_SERVER['REMOTE_ADDR']; 
//seleciona tudo da tabela usuario e confere o nome e senha
$query = "select nome from playstation_users where usuario = '{$usuario}' and senha = '{$senha}'";
$result = mysqli_query($conexao, $query);
$row = mysqli_num_rows($result);


//------------------------------------------------------------------------
//verifica os dados de login, se estiverem certos redireciona para a página
if($row == 1) {
	$sql= "SELECT (cadastro) from playstation_users where usuario = '$usuario'"; //pega o usuario no banco de dados
	$sqldata = mysqli_query($conexao, $sql); //conexao com a query
	$rowdata = mysqli_fetch_array($sqldata); //array da variavel
	$datacadastrada = $rowdata['cadastro']; //seleciona a data do usuario
	$datacadastro = strtotime($datacadastrada. '+33 days'); //converte a data de cadastro e seta quantos dias usuário pode ficar
	
	//cria a tabela com nome do usuario para guardar seu ip e data de acesso
	$sql = "CREATE TABLE IF NOT EXISTS user_$usuario (usuario VARCHAR(300), senha VARCHAR(300), ip VARCHAR(70), data_atual datetime)";
	if($conexao->query($sql) === TRUE) {
		$_SESSION['cadastro'] = true;
	}//$conexao->close();
	
	//insere na tabela do usuario o ip de acesso e a data de acesso
	$sqla = "INSERT INTO user_$usuario (usuario, senha, ip, data_atual) VALUES ('$usuario','$senha','$ip',NOW())";
	if($conexao->query($sqla) === TRUE) {
		$_SESSION['cadastro'] = true;
	}
	
	//------------------------------------------------------------
	//se o login do usuario ocorrer ele vai para a pagina Location:
	$usuario_bd = mysqli_fetch_assoc($result);
	$_SESSION['nome'] = $usuario_bd['nome'];

	//-------------------------------------------------------------
	//verifica se o prazo de uso do usuario ainda é valido
	if ($datacadastro > $dataatual){   
	//abre a sessão pro usuario		
     $_SESSION['usuario'] = $usuario;   
	//se o login ocorrer o usuario é levado para a pagina Location:
	header('Location: loja/index.php');
exit();} else {
	//apaga o usuario do sistema de login
	$delUser = "DELETE FROM playstation_users WHERE usuario = '$usuario'";
	if($conexao->query($delUser) === TRUE) {
	}

	//----------------------------------------------------------------
	// se o login tiver expirado, deleta a tabela e os dados do usuario 
	$sqlo = "DROP TABLE  user_$usuario";
	if($conexao->query($sqlo) === TRUE) {
	}
	//se o prazo do usuario tiver expirado ele volta para home
	header('Location: ./index.php');
}
	$conexao->close();

//------------------------------------------	
//se o login estiver errado volta para a home
} else {
	$_SESSION['nao_autenticado'] = true;
	header('Location: ./index.php');
	exit();
}