[![Build](https://img.shields.io/badge/dev-gorpo-brightgreen.svg)]()
[![Stage](https://img.shields.io/badge/Release-Stable-brightgreen.svg)]()
[![Build](https://img.shields.io/badge/python-v3.7-blue.svg)]()
[![Build](https://img.shields.io/badge/windows-7%208%2010-blue.svg)]()
[![Build](https://img.shields.io/badge/Linux-Ubuntu%20Debian-orange.svg)]()
[![Build](https://img.shields.io/badge/arquiterura-64bits-blue.svg)]()
<h2 align="center">TCXS PROJECT STORE PAINEL ADMINISTRADOR PC</h2>
<h1 align="center">PlayStation3 Store | HAN | HEN | CFW</h1>
<img src="https://i.imgur.com/3Gmp3Ze.jpg" width="100%"></img><br>
<br>
<b>Programa Windows [PC]:</b><br>
<p>Sistema de administração para controle da TCXS Store PlayStation3, desenvolvido em python conta com sistema independente de arrasto, redimensionamento, minimização, ampliação e para fechar. Interface grafica(GUI) criada com auxilio do programa QtDesigner incluso no pacote PyQt5. Este programa necessita exclusivamente das versões PyQT5==5.12 pyqtwebengine==5.12. Imagens são enviadas via FTP ja redimensionadas e com marca d'agua.<br> Atenção:Este programa funciona no caminho "localhost/store/" ou seja https://tcxsproject.com.br/store/.<br>Confira outros extras do programa:</p>
<br>
<b>Dados necessários para funcionalidade do programa:</b><br>
- Nome da Database.<br>
- User da Database <br>
- Senha da Database <br>
- Endereço FTP<br>
- User FTP<br>
- Login FTP<br>
<br>

<b>Pacotes necessários:</b><br>
Pacotes necessários encontram-se no requirements.txt<br>
<code>pip install requirements.txt</code><br>

<b>Instalação manual dos pacotes:</b><br>
<code>pip install PyQT5==5.12</code><br>
<code>pyqtwebengine==5.12</code><br>
<code>pillow==6.2.2</code><br>
<code>....</code><br>
<code>.....</code><br>
<br>


<b>TELA INICIAL:</b><br>
- Sistema de menu Abre e Fecha com icones para identificação.<br>
- Sistema "MOUSE OVER" que quando mouse está sobre o botão ou item exibe informações.<br> 
- Sistema "MOUSE OVER" sobre o titulo do programa exibindo instruções de uso.<br>
- Necessária inserção dos dados de login Mysql e FTP do servidor que a loja está hospedada.<br>
- Dados de login salvos em banco de dados local SqLite3 sendo necessário inserir os dados apenas uma vez ou quando alterados no server.<br>
- [ATENÇÃO] deixe o mouse sobre o titulo do programa para receber instruções de uso!!!<br>
<img src="https://ia601501.us.archive.org/24/items/prints_programa_tcxs/home_menu_fechado.jpg" width="30%"></img>
<img src="https://ia801501.us.archive.org/24/items/prints_programa_tcxs/home_menu_aberto.jpg" width="30%"></img>
<img src="https://ia601501.us.archive.org/24/items/prints_programa_tcxs/mouse_overHOME.jpg" width="30%"></img><br>

<br>
<b>CADASTRO E CONSULTA DE USUÁRIOS:</b><br>
- Sistema de cadastro de usuários na database.<br>
- Para carregar a tabela clique inicialmente em adicionar, isto irá adicionar a tabela de usuários para visualização edição e exclusão.<br>
- Inserções Necessárias Nome para exibição na loja, user para logar e senha.<br>
- Botoes adiciona | atualiza | deleta<br>
- Para adicionar preencha todos os campos e clique em adicionar<br>
- Para atualizar preencha todos os dados, clique sobre o numero de uma linha na tabela e clique em atualizar, isto irá atualizar toda aquela linha.<br>
- Para deletar clique sobre a linha desejada e clique em deletar.<br>
- Sistema de consulta de acesso dos usuários exibe todos os dados do usuário, data e hora de acesso e o endereço de IP que acessou.<br>
- Para realizar uma consulta digite o user que o usuário entra na loja, e clique em pesquisar.<br>
- Caso não retorne algum dado é porque o usuário ainda não realizou nenhum login.<br>
- É necessário ao menos um login do usuario para que tenha algo a ser consultado!<br>
<img src="https://ia801501.us.archive.org/24/items/prints_programa_tcxs/cadastro_users.jpg" width="45%"></img>
<img src="https://ia801501.us.archive.org/24/items/prints_programa_tcxs/consulta_users.jpg" width="45%"></img><br>

<br>
<b>CADASTRO DE JOGOS E EXTRAS:</b><br>
- Sistema de cadastro de jogos e extras, tudo que tivermos com link direto irá funcionar neste sistema!<br>
- Para carregar as tabelas dos jogos clique inicialmente em adicionar!!!
- A tabela de PlayStation3 fica no final das abas.
- Jogos a serem cadastrados: PSP | PS1 | PS2 | PS3 | EMULADORES | EXTRAS<br>
- Extras para cadastrar qualquer coisa com link direto como filmes com player compativeis ou homebrew's.<br>
- Inserções necessárias Titulo | Descrição | Content ID | Imagem | Link<br>
- Titulo tente manter ele o menor e mais claro possivel.<br>
- Descrição necessário usar a tag < br > para pular linhas conforme exemplo:<br>
<code>Idioma: Ingles < br > Legenda: Ingles < br > Plataforma: Playstation3</code><br>
- [ATENÇÃO] Manter o padrão para descrição.<br>
- Content ID não necessário, porém o campo nunca poderá ficar vazio, preencha sempre com algo ou use ---.<br>
- Imagem, basta clicar e enviar, ela será automaticamente redimensionada e aplicada a marca d'agua, logo após upada via ftp, de um tempo até que isto aconteça para finalmente cadastrar (20 segundos??)!!!<br>
- Links de PSP, PS1 PS2, EMULADORES e EXTRAS são links unicos, portanto sempre necessários.<br>
- Links de PS3 é possivel cadastrar até 30 links por jogo, caso não va inserir um dos links é sempre necessário p uso de --- no campo de entrada.<br>
- [ATENÇÃO] Sempre mantenha os --- caso não vá usar os demais campos dos links de PS3!!!<br>
- Finalmente, para adicionar clique em adicionar.<br>
- Para atualizar, preencha normalmente todos os campos, suba a imagem e clique sobre a linha atualizar, é necessario subir uma nova imagem para que ela seja cadastrada seu caminho e nome junto a database, não se preocupe em lotar o servidor com imagens, elas ficam com apenas 15kb!!!<br>
- Para deletar um jogo basta clicar sobre a linha dele e clicar em deletar!<br>
<img src="https://ia801501.us.archive.org/24/items/prints_programa_tcxs/psp.jpg" width="30%"></img>
<img src="https://ia801501.us.archive.org/24/items/prints_programa_tcxs/Screenshot_2.jpg" width="30%"></img>
<img src="https://ia801501.us.archive.org/24/items/prints_programa_tcxs/ps2.jpg" width="30%"></img><br>
<img src="https://ia801501.us.archive.org/24/items/prints_programa_tcxs/ps3.jpg" width="30%"></img>
<img src="https://ia801501.us.archive.org/24/items/prints_programa_tcxs/emuladores.jpg" width="30%"></img>
<img src="https://ia801501.us.archive.org/24/items/prints_programa_tcxs/extras.jpg" width="30%"></img><br>

<br>
<b>Sistema de Verificação da Database:</b><br>
- Como demais adm's não tem acesso ao PHPMyAdmin foi criado um painel para visualização de todas as tabelas da database.<br>
<img src="https://ia601501.us.archive.org/24/items/prints_programa_tcxs/consulta_databases.jpg" width="50%"></img><br>

<br>
<b>Verificador de links com erro [404]</b><br>
- Sistema de verificação de links quebrados offline.<br>
- Sistema funciona somente para links dropbox cadastrados na database.<br>
- Demais links fora dropbox não irão funcionar neste sistema.<br>
<img src="https://ia801501.us.archive.org/24/items/prints_programa_tcxs/verifica404.jpg" width="50%"></img><br>


<br>
<b>Sistema de Backup da Database Mysql [loja web]:</b><br>
- Com apenas um clique todo a databse será salva.<br>
- O backup será feito em um banco de dados SqLite3.<br>
- O administrador será avisado quando o backup terminar, após isto salve sua versão de backup em local seguro!<br>
<img src="https://ia801501.us.archive.org/24/items/prints_programa_tcxs/sistema_backup.jpg" width="50%"></img><br>

<br>
<h1> Demonstração do Frontend [loja web]:</h1><br>
<a href="https://linkdogit.com">Link do Git em breve.</a><br>
<img src="https://i.imgur.com/XyakSdF.png" width="20%"></img>
<img src="https://i.imgur.com/7qmteHR.png" width="20%"></img>
<img src="https://i.imgur.com/8cI4rvm.png" width="20%"></img>
<img src="https://i.imgur.com/6wdkq4V.png" width="20%"></img><br>
<br><br><br>
Nosso site: <a href="https://tcxsproject.com.br">Manicomio TCXS Project</a> | Developers: <a href="https://github.com/gorpo">GorpoOrko</a> | Partnerships:» <a href="https://t.me/tcxsproject2">telegram</a> | ©2020 | <a href="https://t.me/tcxsproject2">TCXS Project Hacker Team™</a><br>
<img src="https://raw.githubusercontent.com/gorpo/Manicomio-Boot-Theme/master/manicomio/boot.png" width="50%"></img>










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

