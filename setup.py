import sys
from cx_Freeze import setup, Executable

setup(
    name = "TCXS PROJECT STORE ADMIN",
    version = "1.0",
    description = "@GorpoOrko Development",
    executables = [Executable("main.py", base = "Win32GUI")])