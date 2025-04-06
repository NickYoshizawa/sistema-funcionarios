class Funcionario():
    def __init__(self,
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
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        self.cargo = cargo
        self.salario = salario
        self.cidade = cidade
        self.estado = estado
        self.escolaridade = escolaridade
        self.email = email
    
    def get_info(self):
        return (
            self.cpf,
            self.nome,
            self.idade,
            self.cargo,
            self.salario,
            self.cidade,
            self.estado,
            self.escolaridade,
            self.email
        )

    def __str__(self) -> str:
        return f"""
        ================================================
        CPF: {self.cpf}
        Funcionario {self.nome}:
        Idade: {self.idade}
        Cargo: {self.cargo}
        Salario: {self.salario:.2f}
        Cidade e Estado que reside: {self.cidade} - {self.estado}
        Escolaridade: {self.escolaridade}
        Email: {self.email}
        ================================================
        """