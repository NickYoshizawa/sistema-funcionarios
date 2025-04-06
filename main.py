from Funcionario.Funcionario import Funcionario
from Utils.inputs import *
from Utils.dbFunctions import *

class App():
    def __init__(self) -> None:
        self.lista_func: Funcionario = []
        
        criar_tabela()
        
        funcoes = (self.adicionar_novo_func, self.atualizar_func, self.mostrar_func, self.mostrar_lista_func, self.remover_func)

        # Adicionando diretamente os funcionarios Nicolas e Lucas apenas para teste

        func_nicolas = Funcionario(
            nome = "Nicolas",
            cidade = "Bragança Paulista",
            estado = "São Paulo",
            idade = 20,
            escolaridade = "Cursando Ensino Superior",
            cargo = "Analista de Suporte I",
            salario = 2500.00,
            email = "nicolas@gmail.com",
            cpf = 12345678910
            )

        func_lucas = Funcionario(
            nome = "Lucas",
            cidade = "Bragança Paulista",
            estado = "São Paulo",
            idade = 24,
            escolaridade = "Ensino Superior Completo",
            cargo = "Dev Pleno",
            salario = 8000.00,
            email = "lucas@gmail.com",
            cpf = 43563212345
            )
        self._adicionar_func_diretamente(func_nicolas)
        self._adicionar_func_diretamente(func_lucas)
        
        # ====================================================

        while True:
            print("""
            ========== Menu de Opcões ==========
            [1] Adicionar Funcionário
            [2] Editar Funcionário
            [3] Buscar Funcionário
            [4] Listar Funcionários
            [5] Excluir Funcionários
            [6] Sair
            """)
            while True:
                opcao = input_int("Digite uma opção: ")
                if opcao < 1 or opcao > 6:
                    print("Opção inválida. Tente Novamente!")
                else:
                    break

            if opcao == 6:
                print("========== Programa encerrado! ==========")
                break
            funcoes[opcao-1]()
        
    def _adicionar_func_diretamente(self, funcionario: Funcionario) -> None:
        """
        Adiciona diretamente um objeto de classe "Funcionario" à lista
        """
        self.lista_func.append(funcionario)
    
    def __criar_func(self) -> tuple:
        """
        Gera um formulário para que o usuário preencha com os dados do funcionário que deseja adicionar à lista
        """
        print("="*15 + " Formulário do Funcionario " + "="*15)
        nome = input_str("Nome do funcionario: ").strip().title()
        cidade = input_str("Cidade do funcionario: ").strip().title()
        estado = input_str("Estado do funcionario: ").strip().title()
        idade = input_idade("Idade do funcionario: ")
        escolaridade = input_str("Escolaridade do funcionario: ").strip().title()
        cargo = input_str("Cargo do funcionario: ").strip().title()
        salario = input_float("Salário do funcionario: R$")
        email = input_gmail("Email Google do funcionario: ")
        while True:
            try:
                cpf = input_cpf("CPF do funcionario: ")
                for func in self.lista_func:
                    if func.cpf == cpf:
                        raise Exception("Já existe um funcionario com esse CPF. Tente Novamente!")
                break
            except Exception as e:
                print(e)

        print("="*15 + " Fim do Formulário " + "="*15)

        return (nome, cidade, estado, idade, escolaridade, cargo, salario, email, cpf)
    
    def adicionar_novo_func(self, _msg: bool = True) -> None:
        """
        Adiciona um novo funcionário á lista
        """
        dados = self.__criar_func()
        adicionar_funcionario(dados[0], dados[1], dados[2], dados[3], dados[4], dados[5], dados[6], dados[7], dados[8])
        self.lista_func.append(funcionario)
        if(_msg):
            print("\nFuncionário adicionado com sucesso!\n")
            print("="*20 + " Fim " + "="*20 + "\n")
    
    def remover_func(self) -> None:
        """
        Remove um funcionário existente da lista
        """
        print("="*10 + " Removendo um Funcionário " + "="*10 + "\n")
        cpf = input_cpf("Digite o CPF do funcionario que deseja remover: ")
        for func in self.lista_func:
            if func.cpf == cpf:
                print(func)
                r = str(input('Digite "S" para confirmar a exclusão do funcionário acima: ')).strip().upper()[0]
                if r == "S":
                    self.lista_func.remove(func)
                    print("Funcionário removido com sucesso!")
                else:
                    print("Operação cancelada!")
                    print("="*20 + " Fim " + "="*20 + "\n")
        print(f"Nenhum funcionário com CPF: {cpf} foi encontrado!\n")
        print("="*20 + " Fim " + "="*20 + "\n")
    
    def atualizar_func(self) -> None:
        """
        Atualiza um funcionário existente na lista
        """
        print("="*10 + " Atualizando Funcionário " + "="*10 + "\n")
        cpf = input_cpf("Digite o CPF do funcionario que deseja atualizar: ")
        
        for func in self.lista_func:
            if func.cpf == cpf:
                print(func)
                r = str(input('Digite "S" para confirmar a edição do funcionário acima: ')).strip().upper()[0]
                if r == "S":
                    print("Deixe o campo em branco caso não deseje editar.")
                    nome = input_str(f"Nome do funcionario ({func.nome}): ", True).strip().title()
                    cidade = input_str(f"Cidade do funcionario ({func.cidade}): ", True).strip().title()
                    estado = input_str(f"Estado do funcionario ({func.estado}): ", True).strip().title()
                    idade = input_idade(f"Idade do funcionario ({func.idade}): ", True)
                    escolaridade = input_str(f"Escolaridade do funcionario ({func.escolaridade}): ", True).strip().title()
                    cargo = input_str(f"Cargo do funcionario ({func.cargo}): ", True).strip().title()
                    salario = input_float(f"Salário do funcionario ({func.salario}): R$", True)
                    email = input_gmail(f"Email Google do funcionario ({func.email}): ", True)
                else:
                    print("="*20 + " Fim " + "="*20 + "\n")
                    return
        print(f"Nenhum funcionário com CPF: {cpf} foi encontrado!\n")
        print("="*20 + " Fim " + "="*20 + "\n")
    
    def mostrar_func(self) -> None:
        """
        Mostra um funcionário específico através do identificador "CPF"
        """
        cpf = input_cpf("Digite o CPF do funcionario que deseja procurar: ")
        for func in self.lista_func:
            if func.cpf == cpf:
                print(func)
                return None
        print(f"Nenhum funcionário com CPF: {cpf} foi encontrado!")
    
    def mostrar_lista_func(self) -> None:
        """
        Mostra todos os funcionários da lista
        """
        print("="*15 + " Lista de Funcionários " + "="*15 + "=")
        for func in self.lista_func:
            print(func)
        print("="*20 + " Fim da lista " + "="*20)
    
if __name__ == '__main__':
    App()
