[![Build](https://img.shields.io/badge/dev-gorpo-brightgreen.svg)]()
[![Stage](https://img.shields.io/badge/Release-Stable-brightgreen.svg)]()
[![Build](https://img.shields.io/badge/python-v3.7-blue.svg)]()
[![Build](https://img.shields.io/badge/windows-7%208%2010-blue.svg)]()
[![Build](https://img.shields.io/badge/Linux-Ubuntu%20Debian-orange.svg)]()
[![Build](https://img.shields.io/badge/arquiterura-64bits-blue.svg)]()
<h2 align="center">TCXS PROJECT STORE PHP MYSQL WITH APP ANDROID E PAINEL ADMIN</h2>
<h1 align="center">PlayStation3 Store | HAN | HEN | CFW</h1>
<img src="https://i.imgur.com/3Gmp3Ze.jpg" width="100%"></img><br>

<b>Databases:</b><br>
- Editar os arquivos "database.php" e "conexao.php" com os dados do host.<br>
- Dump SQL limpo junto ao código apenas com admins cadastrados.
- Dump de testes adicionado.<br>

- Toda e qualquer alteraçao deve ser informada no changelog, favor informar sempre no documento que estiver editando que id parou de usar para quem for atualizar a proxima vez saiba de que id começar, se possivel informe neste documento a id que parou para melhor visualização, mantenha um backup desde mesmo material no dropbox, versionando sempre sua versão passada.<br>
- Fixes, patches e outros arquivos como o apk devem ficar em um branch separado neste git, manter apenas a versão MASTER intacta pronta para upload<br>
- Os dados de banco de dados desta versão são da minha maquina local, para hospedar é necessário trocar usuario, senha e nome do banco de dados nas configurações PHP<br>
- Para rodar em outra maquina local é necessário ter Apache e Mysql instalados, soluçoes como XAMPP para computador ou algum aplicativo android facilmente podem ser usados<br>
- Em caso de uso com o XAMPP basta jogar todos arquivos na pasta htdocs, criar um banco de dados e importar o dump.sql<br>
- O dump.sql contido na programaçao já contem os administradores cadastrados com uma data de assinatura infinita<br>
- O gerenciamento de usuarios pode ser feito via navegador ou via APK Android<br>
- Sistema de banimento automático ainda será desenvolvido, creio eu que vou gostar sentar de manha dar uma cagada, pegar o meu café, minha maconha e dando uma cagada sentar o ban em alguns users... @GorpoOrko<br>
- Todas e qualquer informaçoes adicionais devem ser inseridas neste documento e versionada neste git.<br>
- 09 de Agosto de 2020 <br>


<h1> Changelog:</h1><br>
<b>Sistema de proteção:</b><br>
- sistema com login e senha para usuários armazenando sua data de entrada<br>
- sistema que permite o download dos jogos somente via console PLAYSTATION3<br>
- controle de acesso dos usuários que cria uma tabela para cada usuário e armazena seu ip e data de ACESSOS<br>
- sistema para cadastro e banimento de usuários<br>
- sistema para consulta de visitas e conferência dos IP's dos usuários<br>
- aplicativo Android para facilitar o gerenciamento<br>
- sistema de proteção inserido em todas as paginas, por este motivo tivemos que mudar para PHP <br>
- sistema de login reconhece usuario, ip e aparelho conectado<br>
- caso links tentem ser acessados sem estar logado o usuario é levado para uma pagina de aviso<br>
- somente usuarios logados conseguem acessar os links da loja<br>
- somente pode ser feito download via console PLAYSTATION3, safa exceção do plugin gorpo.js desabilitado<br>
- sistema de banimento automatico apos 30 dias incluso no codigo<br>
<br>
<b>Parte para usuários:</b><br>
- pagina de login com login e senha que cria uma tabela para cada usuario armazenando a data de acesso e IP<br>
- pagina home informando o nome do usuário, IP e aparelho conectado<br>
- pagina home recebe o usuário mostrando menu do topo e em forma de banner<br>
- pagina de PlayStation PSP alimentada usando até id:34<br>
- pagina de PlayStation1 alimentada usando até id:1149<br>
- pagina de PlayStation2 alimentada usando até id:2147<br>
- pagina de PlayStation3 alimentada usando até id:3192<br>
- pagina de PlayStation Emuladores alimentada usando até id:emu7<br>
- pagina de PlayStation PSN Stuff alimentada usando até id:stuff_650<br>
<p>OBS: As id's seguem uma ordem lógica, elas devem ser inseridas sempre em ordem crescente 0,1,2,3.....23,2,25...., estas ids fazem ligação com o arquivo gorpo.js o qual habilita e desabilita os botões de download não permitindo download em outra plataforma que não seja o console PlayStation3.</p><br>
<br>
<b>Parte para administradors:</b><br>
- pagina de cadastro de usuarios<br>
- pagina para deletar/banir usuários<br>
- pagina para gerenciar acesso dos usuarios<br>
- aplicativo android para banimento dos usuários<br>
- acesso ao sistema de cadastro via link: <a href="https://tcxsproject.com.br/store/cadastro.php?act=tcxs">https://tcxsproject.com.br/store/cadastro.php?act=tcxs</a><br>
- acesso so sistema de consulta via link: <a href="https://tcxsproject.com.br/store/consulta.php?act=tcxs">https://tcxsproject.com.br/store/consulta.php?act=tcxs</a> <br>
- Tutorial para visualização/programação da loja em localhost: <a href="https://youtu.be/o3KJM1d4eHQ">Tutorial Hospedagem Local XAMPP</a> <br>
- Tutorial para colocar a loja no servidor: <a href="https://youtu.be/gTF19YUih2E">Demonstração de como hospedar Externamente | Deploy</a> <br>
<p>OBS: Este sistema via link é protegido pelo token "?act=tcxs", se alguem tentar acessar diretamente o arquivo cadastro.php não irá funcionar, este token não pode vazar. O aplicativo de celular ja tem o token inserido em sua programação. </p><br>
<br>
<h1> Codigos Utéis da programação:</h1><br>
<b>Sistema de proteção dos botões permindo download somente em consoles PlayStation3, para ativar ou desativar basta comentar/descomentar o codigo:</b><br>
	<code>
		writeEnvInfo();
		ps3chk();
</code><br>

<h1> Demonstração:</h1><br>
<img src="https://i.imgur.com/XyakSdF.png" width="100%"></img><br>
<img src="https://i.imgur.com/7qmteHR.png" width="100%"></img><br>
<img src="https://i.imgur.com/8cI4rvm.png" width="100%"></img><br>
<img src="https://i.imgur.com/6wdkq4V.png" width="100%"></img><br>

<code><script type="text/javascript">
var OSNome = "";
if (window.navigator.userAgent.indexOf("Windows NT 10.0")!= -1) OSNome="Windows 10";
if (window.navigator.userAgent.indexOf("Windows NT 6.2") != -1) OSNome="Windows 8";
if (window.navigator.userAgent.indexOf("Windows NT 6.1") != -1) OSNome="Windows 7";
if (window.navigator.userAgent.indexOf("Windows NT 6.0") != -1) OSNome="Windows Vista";
if (window.navigator.userAgent.indexOf("Windows NT 5.1") != -1) OSNome="Windows XP";
if (window.navigator.userAgent.indexOf("Windows NT 5.0") != -1) OSNome="Windows 2000";
if (window.navigator.userAgent.indexOf("Mac")            != -1) OSNome="Mac/iOS";
if (window.navigator.userAgent.indexOf("X11")            != -1) OSNome="UNIX";
if (window.navigator.userAgent.indexOf("Linux")          != -1) OSNome="Linux";
if (window.navigator.userAgent.indexOf("5.0 (") + 19, ua.indexOf(") Apple") != -1) OSNome="PlayStation3";
//var fwVersion = ua.substring(ua.indexOf("5.0 (") + 19, ua.indexOf(") Apple"));
document.write(' | Sistema: '+ OSNome);
</script> </code>


<h1> Comandos auxiliares Github - CLI </h1><br>
<b>email:</b><br>
	<code>git config --global user.email "gorpoorko@protonmail.com"</code><br>
<b>username:</b><br>
	<code>git config --global user.name "gorpoorko"</code><br>
	
<b>Adicionar um arquivo em específico</b><br>
	<code>git add meu_arquivo.txt</code><br>
<b>Adicionar um diretório em específico</b><br>
	<code>git add meu_diretorio</code><br>
<b>Adicionar todos os arquivos/diretórios</b><br>
	<code>git add .	</code><br>
<b>Adicionar um arquivo do gitignore -  git add -f arquivo_no_gitignore.txt</b><br>

<b>Comitar um arquivo</b><br>
	<code>git commit meu_arquivo.txt</code><br>
<b>Comitar vários arquivos</b><br>
	<code>git commit meu_arquivo.txt meu_outro_arquivo.txt</code><br>
<b>Comitar informando mensagem</b><br>
	<code>git commit meuarquivo.txt -m "minha mensagem de commit"</code><br>

<b>Remover arquivo</b><br>
	<code>git rm meu_arquivo.txt</code><br>
<b>Remover diretório</b><br>
	<code>git rm -r diretorio</code><br>

<b>O primeiro push de um repositório deve conter o nome do repositório remoto e o branch.</b><br>
	<code>git push -u origin master</code><br>
<b>Os demais pushes não precisam dessa informação</b><br>
	<code>git push</code><br>
<b>Atualizar repositório local de acordo com o repositório remoto</b><br>
<b>Atualizar os arquivos no branch atual</b><br>
	<code>git pull</code><br>
<b>Buscar as alterações, mas não aplica-las no branch atual</b><br>
	<code>git fetch</code><br>

<b>Criando um novo branch</b><br>
	<code>git branch bug-123</code><br>
	<code>git branch gh-pages    - para sites</code><br>
<b>Trocando para um branch existente</b><br>
	<code>git checkout bug-123</code><br>
<b>Neste caso, o ponteiro principal HEAD esta apontando para o branch chamado bug-123.</b><br>
<b>Criar um novo branch e trocar</b><br>
	<code>git checkout -b bug-456</code><br>
<b>Voltar para o branch principal (master)</b><br>
	<code>git checkout master</code><br>

<b>Upando algo para um branch ja existente</b><br>
	<code>git remote add origin <"link do git seja master ou branch"></code><br>
<b>Adicione os arquivos</b><br>
	<code>git add . ou nome do arquivo ou pasta</code><br>
<b>Comente oque foi adicionado</b><br>
	<code>git commit -m "comentario"</code><br>
<b>Fazer as atualizações no repositorio online</b><br>
	<code>git fetch</code><br>
<b>Adicionando a historia do repositorio online</b><br>
	<code>git pull origin master --allow-unrelated-histories</code><br>

<b>Resolver merge entre os branches</b><br>
	<code>git merge bug-123</code><br>
<b>Para realizar o merge, é necessário estar no branch que deverá receber as alterações. O merge pode automático ou manual. O merge automático será feito em arquivos textos que não sofreram alterações nas mesmas linhas, já o merge manual será feito em arquivos textos que sofreram alterações nas mesmas linhas. A mensagem indicando um merge manual será:<br>
Automerging meu_arquivo.txt<br>
CONFLICT (content): Merge conflict in meu_arquivo.txt<br>
Automatic merge failed; fix conflicts and then commit the result.</b><br>
<b>Apagando um branch</b><br>
	<code>git branch -d bug-123</code><br>
<b>Listar branches</b><br>
	<code>git branch</code><br>
<b>Listar branches com informações dos últimos commits</b><br>
	<code>git branch -v</code><br>
<b>Listar branches que já foram fundidos (merged) com o master</b><br>
	<code>git branch --merged</code><br>
<b>Listar branches que não foram fundidos (merged) com o master</b><br>
	<code>git branch --no-merged</code><br>

<b>Criando um branch remoto com o mesmo nome</b><br>
	<code>git push origin bug-123</code><br>
<b>Criando um branch remoto com nome diferente</b><br>
	<code>git push origin bug-123:new-branch</code><br>
<b>Baixar um branch remoto para edição</b><br>
	<code>git checkout -b bug-123 origin/bug-123</code><br>
<b>Apagar branch remoto</b><br>
	<code>git push origin:bug-123</code><br>
<b>Fazendo o rebase entre um o branch bug-123 e o master.</b><br>
	<code>git checkout experiment</code><br>
	<code>git rebase master</code><br>

Nosso site: <a href="https://tcxsproject.com.br">Manicomio TCXS Project</a> | Developers: <a href="https://github.com/gorpo">GorpoOrko</a> | Partnerships:» <a href="https://t.me/tcxsproject2">telegram</a> | ©2020 | <a href="https://t.me/tcxsproject2">TCXS Project Hacker Team™</a><br>
<img src="https://raw.githubusercontent.com/gorpo/Manicomio-Boot-Theme/master/manicomio/boot.png" width="50%"></img>
