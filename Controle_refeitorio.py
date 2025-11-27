#Controle de refeitório
PRECO_REFEICAO = 2.0
nomes = []
contas = []
def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ").title()
    nomes.append(nome)
    conta = float(0)
    contas.append(conta)
    print(f"Usuário {nome} cadastrado com sucesso!")

def listar_usuarios():
    if not nomes:
        print("Nenhum usuário cadastrado.")
    else:
        print("Usuários cadastrados:")
        for i, nome in enumerate(nomes):
            print(f"{i + 1}. {nome} - Conta: R$ {contas[i]}")

def adicionar_credito():
    codigo = int(input("Digite o código do usuário (1 para primeiro, 2 para segundo, etc.): "))-1
    valor = float(input("Digite o valor a ser creditado: "))
    if 0 <= codigo < len(nomes):
        contas[codigo] += valor
        print(f"R$ {valor} creditados na conta de {nomes[codigo]}.")
    else:
        print("Código de usuário inválido.")  

def verificar_saldo():
    codigo = int(input("Digite o código do usuário (1 para primeiro, 2 para segundo, etc.): "))-1
    if 0 <= codigo < len(nomes):
        print(f"Saldo de {nomes[codigo]}: R$ {contas[codigo]}")
    else:
        print("Código de usuário inválido.")
        
def acessar_refeitorio():
    codigo = int(input("Digite o código do usuário (1 para primeiro, 2 para segundo, etc.): "))-1
    if 0 <= codigo < len(nomes):
        if contas[codigo] >= 2:
            contas[codigo] -= PRECO_REFEICAO
            print("Acesso liberado")
            print(f"{nomes[codigo]} acessou o refeitório. Saldo restante: R$ {contas[codigo]}")
        else:
            print("Acesso negado.")
            print(f"{nomes[codigo]} não tem saldo suficiente para acessar o refeitório.")
    else:
        print("Código de usuário inválido.")

while True:
    print("\nControle de Refeitório")
    print("1. Cadastrar usuário")
    print("2. Listar usuários") 
    print("3. Adicionar crédito")
    print("4. Verificar saldo") 
    print("5. Acessar refeitório")
    print("6. Sair")
    opcao = input("\nEscolha uma opção: ")
    if opcao == '1':
        cadastrar_usuario()
    elif opcao == '2':
        listar_usuarios()
    elif opcao == '3':
        adicionar_credito()
    elif opcao == '4':
        verificar_saldo()
    elif opcao == '5':
        acessar_refeitorio()
    elif opcao == '6':
        print("Sistema encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")