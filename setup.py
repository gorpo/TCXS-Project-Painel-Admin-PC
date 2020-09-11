import sys
import requests
from cx_Freeze import setup, Executable

"""Instruções CX Freeze:
[INSTALL] pip install cx_Freeze==6.1
1. O CX Freeze cria programas windows executaveis, podemos passar alguns parametros como vistos abaixo:
2. name = nome do projeto.
3. version = versao do projeto.
4. options = 
4.1 "include_msvcr": True,   |  inclui a dll do windows para que o usuário não tenha que por ela manualmente.
4.2 "include_files": ['funcoes','images'],  |  inclui suas pastas e arquivos necessários para o programa. 
4.3  "zip_include_packages": ["*"],  |  zipa as lib' as compactando e economizando espaço.
4.4 "zip_exclude_packages": ["PyQt5","requests","importlib","certifi"]  |  exclui os pacotes que derem algum erro na compilaçao zipada
4.5 caso nao queira zipar os arquivos, oque torna o programa maior basta remover o 4.4.
5. description = descrição do seu projeto
6. executables = passa o programa e a base="Win32GUI" para interface grafica, icon="images/icon.ico" caminho do icone do programa

[COMANDO PARA COMPILAR] python setup.py build
"""

setup(
    name = "TCXS PROJECT STORE ADMIN",
    version = "1.0",
    options = {"build_exe": {"include_msvcr": True, "include_files": [],  "zip_include_packages": ["*"], "zip_exclude_packages": ["PyQt5","requests","importlib","certifi"]}},
    description = "@GorpoOrko Development",
    executables = [Executable("TCXSProject.py", base = "Win32GUI", icon="images/icon.ico")])


