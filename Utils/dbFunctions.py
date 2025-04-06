import sqlite3

DB_NAME = 'Data/empresa.db'

def conectar() -> None:
    """
    Conecta no banco de dados dado pela variavel: DB_NAME
    """
    return sqlite3.connect(DB_NAME)

def criar_tabela() -> None:
    """
    Cria a tabela tbFuncionario se não existir ou se conecta a ela se existir
    """
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
    ) -> None:
    """
    Adiciona um funcionário à tabela tbFuncionario
    """
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO tbFuncionario (cpf, nome, idade, cargo, salario, cidade, estado, escolaridade, email)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (cpf, nome, idade, cargo, salario, cidade, estado, escolaridade, email))
    conexao.commit()
    conexao.close()

def mostrar_funcionario(info_funcionario: tuple) -> None:
    print(f"""
            ================================================
            CPF: {info_funcionario[0]}
            Funcionario {info_funcionario[1]}:
            Idade: {info_funcionario[2]}
            Cargo: {info_funcionario[3]}
            Salario: {info_funcionario[4]:.2f}
            Cidade e Estado que reside: {info_funcionario[5]} - {info_funcionario[6]}
            Escolaridade: {info_funcionario[7]}
            Email: {info_funcionario[8]}
            ================================================
        """)

def buscar_funcionario(cpf: int) -> str:
    """
    Busca um funcionário da tabela tbFuncionario
    """
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM tbFuncionario WHERE cpf = ?', (cpf,))
    funcionario = cursor.fetchone()
    conexao.close()
    return funcionario if funcionario else None

def listar_funcionarios() -> tuple:
    """
    Lista os funcionários da tabela tbFuncionario
    """
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM tbFuncionario')
    funcionarios = cursor.fetchall()
    conexao.close()
    return funcionarios

def editar_funcionario(cpfOriginal, cpfNovo="", nome="", idade="", cargo="", salario="", cidade="", estado="", escolaridade="", email="") -> None:
    """
    Edita um funcionário da tabela tbFuncionario
    """
    conexao = conectar()
    cursor = conexao.cursor()

    atualizacoes = []
    valores = []
    
    
    if cpfNovo != "":
        atualizacoes.append("cpf = ?")
        valores.append(cpfNovo)
    if nome != "":
        atualizacoes.append("nome = ?")
        valores.append(nome)
    if idade != "":
        atualizacoes.append("idade = ?")
        valores.append(idade)
    if cargo != "":
        atualizacoes.append("cargo = ?")
        valores.append(cargo)
    if salario != "":
        atualizacoes.append("salario = ?")
        valores.append(salario)
    if cidade != "":
        atualizacoes.append("cidade = ?")
        valores.append(cidade)
    if estado != "":
        atualizacoes.append("estado = ?")
        valores.append(estado)
    if escolaridade != "":
        atualizacoes.append("escolaridade = ?")
        valores.append(escolaridade)
    if email != "":
        atualizacoes.append("email = ?")
        valores.append(email)

    valores.append(cpfOriginal)

    if atualizacoes:
        comando = f'UPDATE tbFuncionario SET {", ".join(atualizacoes)} WHERE cpf = ?'
        cursor.execute(comando, valores)
        conexao.commit()

    conexao.close()
    
def excluir_funcionario(cpf) -> None:
    """
    Exclui um funcionário da tabela tbFuncionario
    """
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM tbFuncionario WHERE cpf = ?', (cpf,))
    conexao.commit()
    conexao.close()

