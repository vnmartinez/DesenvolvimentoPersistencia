import xml.etree.ElementTree as ET

# Função para adicionar um novo contato
def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o número de telefone do contato: ")
    email = input("Digite o e-mail do contato: ")

    # Cria um elemento de contato
    contato = ET.Element("Contato")
    ET.SubElement(contato, "Nome").text = nome
    ET.SubElement(contato, "Telefone").text = telefone
    ET.SubElement(contato, "Email").text = email

    # Abre o arquivo XML de contatos
    tree = ET.ElementTree(contato)
    with open('contatos.xml', 'ab') as arquivo:
        tree.write(arquivo, encoding='utf-8', xml_declaration=True)

    print("Contato salvo com sucesso!")

# Função para listar todos os contatos
def listar_contatos():
    try:
        tree = ET.parse('contatos.xml')
        root = tree.getroot()

        for contato in root:
            nome = contato.find('Nome').text
            telefone = contato.find('Telefone').text
            email = contato.find('Email').text

            print("Nome:", nome)
            print("Telefone:", telefone)
            print("E-mail:", email)
            print("-------------------------")
    except FileNotFoundError:
        print("Nenhum contato encontrado.")

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
