import sqlite3

DB_NAME = 'Data/empresa.db'

def conectar():
    return sqlite3.connect(DB_NAME)

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tbFuncionario (
            cpf INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            idade INTEGER,
            cargo TEXT,
            salario REAL,
            cidade TEXT,
            estado TEXT,
            escolaridade TEXT,
            email TEXT
        )
    ''')
    conexao.commit()
    conexao.close()

def adicionar_funcionario(
        cpf: int,
        nome: str,
        idade: int,
        cargo: str,
        salario: float,
        cidade: str,
        estado: str,
        escolaridade: str,
        email: str,
    ):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO tbFuncionario (cpf, nome, idade, cargo, salario, cidade, estado, escolaridade, email)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (cpf, nome, idade, cargo, salario, cidade, estado, escolaridade, email))
    conexao.commit()
    conexao.close()
    
def buscar_funcionario(cpf: int):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM tbFuncionario WHERE cpf = ?', (cpf,))
    funcionario = cursor.fetchone()
    conexao.close()
    return funcionario

def listar_funcionarios():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM tbFuncionario')
    funcionarios = cursor.fetchall()
    conexao.close()
    return funcionarios

def editar_funcionario(cpf, nome=None, idade=None, cargo=None, salario=None, cidade=None, estado=None, escolaridade=None, email=None):
    conexao = conectar()
    cursor = conexao.cursor()

    atualizacoes = []
    valores = []

    if nome is not None:
        atualizacoes.append("nome = ?")
        valores.append(nome)
    if idade is not None:
        atualizacoes.append("idade = ?")
        valores.append(idade)
    if cargo is not None:
        atualizacoes.append("cargo = ?")
        valores.append(cargo)
    if salario is not None:
        atualizacoes.append("salario = ?")
        valores.append(salario)
    if cidade is not None:
        atualizacoes.append("cidade = ?")
        valores.append(cidade)
    if estado is not None:
        atualizacoes.append("estado = ?")
        valores.append(estado)
    if escolaridade is not None:
        atualizacoes.append("escolaridade = ?")
        valores.append(escolaridade)
    if email is not None:
        atualizacoes.append("email = ?")
        valores.append(email)

    valores.append(cpf)

    if atualizacoes:
        comando = f'UPDATE tbFuncionario SET {", ".join(atualizacoes)} WHERE cpf = ?'
        cursor.execute(comando, valores)
        conexao.commit()

    conexao.close()
    
def excluir_funcionario(cpf):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM tbFuncionario WHERE cpf = ?', (cpf,))
    conexao.commit()
    conexao.close()

