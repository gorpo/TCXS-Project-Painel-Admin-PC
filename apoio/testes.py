import sqlite3

conexao = sqlite3.connect('database.db')
# self.conexao.row_factory = self.sqlite3.Row
cursor = conexao.cursor()
cursor.execute("""  CREATE TABLE IF NOT EXISTS dados_mysql  (id integer not null primary key autoincrement, 
nome_database varchar(5000), user_database varchar(5000), senha_database varchar(5000), host_database varchar(
500), endereco_ftp varchar(500), user_ftp varchar(500), senha_ftp varchar(500));  """)
conexao.commit()
conexao.close()