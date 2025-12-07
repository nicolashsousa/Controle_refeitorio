#Controle de refeitório
PRECO_REFEICAO = 2.0
usuarios = []

def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ").title()
    for usuario in usuarios:
        if usuario['nome'] == nome:
            print(f"O usuário '{nome}' já está cadastrado.")
            return

    usuarios.append({'nome': nome, 'conta': 0.0})
    print(f"Usuário {nome} cadastrado com sucesso!")

def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        print("Usuários cadastrados:")
        for i, usuario in enumerate(usuarios):
            print(f"{i + 1}. {usuario['nome']} - Conta: R$ {usuario['conta']:.2f}")

def selecionar_usuario():
    listar_usuarios()
    if not usuarios:
        return None

    try:
        codigo = int(input("Digite o código do usuário (ex: 1 para o primeiro): ")) - 1
        if 0 <= codigo < len(usuarios):
            return usuarios[codigo]
        else:
            print("Código de usuário inválido.")
            return None
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
        return None

def adicionar_credito():
    usuario_selecionado = selecionar_usuario()
    if usuario_selecionado:
        try:
            valor = float(input("Digite o valor a ser creditado: "))
            if valor > 0:
                usuario_selecionado['conta'] += valor
                print(f"R$ {valor:.2f} creditados na conta de {usuario_selecionado['nome']}.")
                print(f"Novo saldo: R$ {usuario_selecionado['conta']:.2f}")
            else:
                print("O valor do crédito deve ser positivo.")
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")

def verificar_saldo():
    usuario_selecionado = selecionar_usuario()
    if usuario_selecionado:
        print(f"Saldo de {usuario_selecionado['nome']}: R$ {usuario_selecionado['conta']:.2f}")
        
def acessar_refeitorio():
    usuario_selecionado = selecionar_usuario()
    if usuario_selecionado:
        if usuario_selecionado['conta'] >= PRECO_REFEICAO:
            usuario_selecionado['conta'] -= PRECO_REFEICAO
            print("Acesso liberado")
            print(f"{usuario_selecionado['nome']} acessou o refeitório. Saldo restante: R$ {usuario_selecionado['conta']:.2f}")
        else:
            print("Acesso negado.")
            print(f"{usuario_selecionado['nome']} não tem saldo suficiente para acessar o refeitório.")

def main():
    while True:
        print("\n--- Controle de Refeitório ---")
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

if __name__ == "__main__":
    main()