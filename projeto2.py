class Cliente:
    def __init__(self, id:int, nome:str, cpf:int, idade:int, telefone:int) -> None:
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.telefone = telefone
        


class Quarto:
    def __init__(self, id:int, nome:str, valor:float, disponibilidade:bool) -> None:
        self.id = id
        self.nome = nome
        self.valor = valor
        self.disponibilidade = disponibilidade
        self.lista_quarto = []
        


class Reserva:
    def __init__(self, id: int, data_entrada: str, data_saida: str, quarto: Quarto, cliente: Cliente, status: str) -> None:
        self.id = id
        self.data_entrada = data_entrada
        self.data_saida = data_saida
        self.quarto = quarto
        self.cliente = cliente
        self.status = status


class Hotel_gerencia:
    def __init__(self) -> None:
        self.lista_de_reserva = []    
        self.lista_de_quartos = []
        self.lista_de_clientes = []
        self.id_count_reserva = 1
        self.id_count_quarto = 1
        self.id_count_cliente = 1

    
    def cadastrarQuartos(self):
        nome = input("Digite o nome do quarto : ")
        valor = float(input("Digite o preço do quarto: "))
        disponibilidade = input("Está disponível? (s/n): ").lower() == 's'
        
        quarto = Quarto(id=self.id_count_quarto, nome=nome, valor=valor, disponibilidade=disponibilidade)
        self.id_count_quarto += 1
        self.lista_de_quartos.append(quarto)
        print("Quarto cadastrado com sucesso!")


    
    def verQuartos(self):
        for quarto_da_vez in self.lista_de_quartos:
            print(f"""
            ID: {quarto_da_vez.id}
            Nome: {quarto_da_vez.nome}
            Valor: R${quarto_da_vez.valor: .2f}
            Disponibilidade: {'Disponível' if quarto_da_vez.disponibilidade else 'Indisponível'}
            """)

    def editarQuarto(self):
        id_quarto = int(input("Digite o ID do quarto que você deseja editar: "))
        quarto_encontrado = False
        for quarto_da_vez in self.lista_de_quartos:
           if quarto_da_vez.id == id_quarto:
              quarto_encontrado = True
              nome = input(f"Digite o novo nome do quarto (atualmente {quarto_da_vez.nome}): ")
              valor = float(input(f"Digite o novo valor do quarto (atualmente R${quarto_da_vez.valor:.2f}): "))

              quarto_da_vez.nome = nome
              quarto_da_vez.valor = valor
              print("Quarto atualizado com sucesso!")
              return

    if not quarto_encontrado:
        print("Quarto não encontrado.")
 




while True:

    menu = input("""
    Escolha uma opção:
    1 - Cadastrar Quartos
    2 - Ver Todos os Quartos
    3 - Editar Quartos
    4 - Excluir Quartos
    0 - Sair
    """)

    match menu:
        case "1":
            
        case "2":
          