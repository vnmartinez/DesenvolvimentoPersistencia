import pickle

# Função para adicionar um novo contato
def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o número de telefone do contato: ")
    email = input("Digite o e-mail do contato: ")

    contato = {
        'Nome': nome,
        'Telefone': telefone,
        'Email': email
    }

    # Abre o arquivo de contatos em modo de escrita binária
    with open('contatos.bin', 'ab') as arquivo:
        pickle.dump(contato, arquivo)
    print("Contato salvo com sucesso!")

# Função para listar todos os contatos
def listar_contatos():
    try:
        with open('contatos.bin', 'rb') as arquivo:
            while True:
                contato = pickle.load(arquivo)
                print("Nome:", contato['Nome'])
                print("Telefone:", contato['Telefone'])
                print("E-mail:", contato['Email'])
                print("-------------------------")
    except EOFError:
        pass

# Menu principal
while True:
    print("\n----- Menu de Contatos -----")
    print("1. Adicionar Contato")
    print("2. Listar Contatos")
    print("3. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        adicionar_contato()
    elif opcao == '2':
        listar_contatos()
    elif opcao == '3':
        break
    else:
        print("Opção inválida. Tente novamente.")
