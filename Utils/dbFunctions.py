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
    
def info_funcionario(cpf: int) -> tuple:
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM tbFuncionario WHERE cpf = ?', (cpf,))
    funcionario = cursor.fetchone()
    conexao.close()
    return (funcionario[0], funcionario[1], funcionario[2], funcionario[3], funcionario[4], funcionario[5], funcionario[6], funcionario[7], funcionario[8])
    
def buscar_funcionario(cpf: int) -> str:
    """
    Busca um funcionário da tabela tbFuncionario
    """
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM tbFuncionario WHERE cpf = ?', (cpf,))
    funcionario = cursor.fetchone()
    conexao.close()
    if funcionario:
        return f"""
            ================================================
            CPF: {funcionario[0]}
            Funcionario {funcionario[1]}:
            Idade: {funcionario[2]}
            Cargo: {funcionario[3]}
            Salario: {funcionario[4]}
            Cidade e Estado que reside: {funcionario[5]} - {funcionario[6]}
            Escolaridade: {funcionario[7]}
            Email: {funcionario[8]}
            ================================================
        """
    else:
        return None

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

def editar_funcionario(cpfOriginal, cpfNovo=None, nome=None, idade=None, cargo=None, salario=None, cidade=None, estado=None, escolaridade=None, email=None) -> None:
    """
    Edita um funcionário da tabela tbFuncionario
    """
    conexao = conectar()
    cursor = conexao.cursor()

    atualizacoes = []
    valores = []
    
    
    if cpfNovo is not None:
        atualizacoes.append("cpf = ?")
        valores.append(cpfNovo)
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

