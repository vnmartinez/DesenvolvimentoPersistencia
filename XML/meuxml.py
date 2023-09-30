import xml.etree.ElementTree as ET

def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o número de telefone do contato: ")
    email = input("Digite o e-mail do contato: ")

    contato = ET.Element("Contato")
    ET.SubElement(contato, "Nome").text = nome
    ET.SubElement(contato, "Telefone").text = telefone
    ET.SubElement(contato, "Email").text = email

    tree = ET.ElementTree(contato)
    with open('contatos.xml', 'ab') as arquivo:
        tree.write(arquivo, encoding='utf-8', xml_declaration=True)

    print("Contato salvo com sucesso!")

def listar_contatos():
    try:
        tree = ET.parse('contatos.xml')
        root = tree.getroot()

        for Contato in root:
            nome_element = Contato.find('Nome')
            telefone_element = Contato.find('Telefone')
            email_element = Contato.find('Email')

            if nome_element is not None and telefone_element is not None and email_element is not None:
                nome = nome_element.text
                telefone = telefone_element.text
                email = email_element.text

                print("Nome:", nome)
                print("Telefone:", telefone)
                print("E-mail:", email)
                print("-------------------------")
            else:
                print("Contato mal formatado ou informações ausentes.")

    except FileNotFoundError:
        print("Nenhum contato encontrado.")

while True:
    print("\n----- Menu de Contatos -----")
    print("1. Adicionar Contato")
    print("2. Listar Contatos")
    print("3. Sair")
    
    opcao = input("Escolha uma opção: ")

    match opcao:
        case '1':
            adicionar_contato()
        case '2':
            listar_contatos()
        case '3':
            break
        case _:
            print("Opção inválida. Tente novamente.")
