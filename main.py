from Utils.inputs import *
from Utils.dbFunctions import *

class App():
    def __init__(self) -> None:
        criar_tabela()
        funcoes = (self.adicionar_novo_func, self.atualizar_func, self.mostrar_func, self.mostrar_lista_func, self.remover_func)
        
        """# Adicionando diretamente os funcionarios Nicolas e Lucas apenas para teste
        # (Usar só se nao existir esses funcionarios no banco de dados)
        
        adicionar_funcionario(
            cpf = 12345678910,
            nome = "Nicolas",
            idade = 20,
            cargo = "Analista de Suporte I",
            salario = 2500.00,
            cidade = "Bragança Paulista",
            estado = "São Paulo",
            escolaridade = "Cursando Ensino Superior",
            email = "nicolas@gmail.com",
        )
        
        adicionar_funcionario(
            cpf = 43563212345,
            nome = "Lucas",
            idade = 24,
            cargo = "Dev Pleno",
            salario = 8000.00,
            cidade = "Bragança Paulista",
            estado = "São Paulo",
            escolaridade = "Ensino Superior Completo",
            email = "lucas@gmail.com",
        )
        
        # ===================================================="""

        while True:
            print("""
            ========== Menu de Opcões ==========
            [1] Adicionar Funcionário
            [2] Editar Funcionário
            [3] Buscar Funcionário
            [4] Listar Funcionários
            [5] Excluir Funcionário
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
    
    def __criar_func(self) -> tuple:
        """
        Gera um formulário para que o usuário preencha com os dados do funcionário que deseja adicionar à lista
        """
        print("\n" + "="*15 + " Formulário do Funcionario " + "="*15 + "\n")
        while True:
            try:
                cpf = input_cpf("CPF do funcionario: ")
                if(buscar_funcionario(cpf)):
                    raise Exception("Já existe um funcionario com esse CPF. Tente Novamente!")
                else:
                    break
            except Exception as e:
                print(e)
        nome = input_str("Nome do funcionario: ").strip().title()
        idade = input_idade("Idade do funcionario: ")
        cargo = input_str("Cargo do funcionario: ").strip().title()
        salario = input_float("Salário do funcionario: R$")
        cidade = input_str("Cidade do funcionario: ").strip().title()
        estado = input_str("Estado do funcionario: ").strip().title()
        escolaridade = input_str("Escolaridade do funcionario: ").strip().title()
        email = input_gmail("Email Google do funcionario: ")
        print("="*15 + " Fim do Formulário " + "="*15)

        return (cpf, nome, idade, cargo, salario, cidade, estado, escolaridade, email)
    
    def adicionar_novo_func(self) -> None:
        """
        Adiciona um novo funcionário á lista
        """
        dados = self.__criar_func()
        adicionar_funcionario(dados[0], dados[1], dados[2], dados[3], dados[4], dados[5], dados[6], dados[7], dados[8])
        print("\nFuncionário adicionado com sucesso!\n")
        print("="*20 + " Fim " + "="*20 + "\n")
    
    def remover_func(self) -> None:
        """
        Remove um funcionário existente da lista
        """
        print("="*10 + " Removendo um Funcionário " + "="*10 + "\n")
        while True:
            cpf = input_cpf("Digite o CPF do funcionario que deseja remover: ")
            funcionario = buscar_funcionario(cpf)
            if funcionario:
                print(funcionario)
                r = str(input('Digite "S" para confirmar a exclusão do funcionário acima: ')).strip().upper()[0]
                if r == "S":
                    excluir_funcionario(cpf)
                    print("Funcionário removido com sucesso!")
                    break
                else:
                    print("Operação cancelada!")
                    break
            else:
                print(f"Nenhum funcionário com CPF: {cpf} foi encontrado.")
                print("Tente novamente!")
        print("="*20 + " Fim " + "="*20 + "\n")
    
    def atualizar_func(self) -> None:
        """
        Atualiza um funcionário existente na lista
        """
        print("="*10 + " Atualizando Funcionário " + "="*10 + "\n")
        cpfOriginal = input_cpf("Digite o CPF do funcionario que deseja atualizar: ")
        funcionario = info_funcionario(cpfOriginal)
        if(funcionario):
            print(buscar_funcionario(cpfNovo))
            r = str(input('Digite "S" para confirmar a edição do funcionário acima: ')).strip().upper()[0]
            if r == "S":
                print("Deixe o campo em branco caso não deseje editar.")
                while True:
                    try:
                        cpfNovo = input_cpf(f"CPF do funcionario ({funcionario[0]}): ", True)
                        if(buscar_funcionario(cpfNovo)):
                            raise Exception("Já existe um funcionario com esse CPF. Tente Novamente!")
                        else:
                            break
                    except Exception as e:
                        print(e)
                nome = input_str(f"Nome do funcionario ({funcionario[0]}): ", True).strip().title()
                idade = input_idade(f"Idade do funcionario ({funcionario[2]}): ", True)
                cargo = input_str(f"Cargo do funcionario ({funcionario[3]}): ", True).strip().title()
                salario = input_float(f"Salário do funcionario ({funcionario[4]}): R$", True)
                cidade = input_str(f"Cidade do funcionario ({funcionario[5]}): ", True).strip().title()
                estado = input_str(f"Estado do funcionario ({funcionario[6]}): ", True).strip().title()
                escolaridade = input_str(f"Escolaridade do funcionario ({funcionario[7]}): ", True).strip().title()
                email = input_gmail(f"Email Google do funcionario ({funcionario[8]}): ", True)
                editar_funcionario(cpfOriginal, cpfNovo, nome, idade, cargo, salario, cidade, estado, escolaridade, email)
            else:
                print("="*20 + " Fim " + "="*20 + "\n")
                return
        else:
            print(f"Nenhum funcionário com CPF: {cpfOriginal} foi encontrado!\n")
            print("="*20 + " Fim " + "="*20 + "\n")
    
    def mostrar_func(self) -> None:
        """
        Mostra um funcionário específico através do identificador "CPF"
        """
        while True:
            cpf = input_cpf("Digite o CPF do funcionario que deseja procurar: ")
            funcionario = buscar_funcionario(cpf)
            if funcionario:
                print("\n" + "="*20 + " Funcionário " + "="*20)
                print(funcionario)
                break
            else:
                print(f"Nenhum funcionário com CPF: {cpf} foi encontrado.")
                print("Tente novamente!")
        print("="*20 + " Fim " + "="*20 + "\n")
        
    def mostrar_lista_func(self) -> None:
        """
        Mostra todos os funcionários da lista
        """
        print("="*15 + " Lista de Funcionários " + "="*15 + "=")
        funcionarios = listar_funcionarios()
        for funcionario in funcionarios:
            print(f"""
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
        """)
        print("="*20 + " Fim da lista " + "="*20)
    
if __name__ == '__main__':
    App()
