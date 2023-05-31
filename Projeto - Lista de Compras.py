//Projeto: Lista de Compras

//Descrição: Um aplicativo de linha de comando que permite ao usuário criar e gerenciar uma lista de compras. O usuário pode adicionar itens à lista, remover itens e exibir a lista completa.

//Passos para o projeto:

//Criar uma interface de linha de comando que exibe um menu com as opções disponíveis para o usuário.
//Implementar a lógica para adicionar um item à lista de compras.
//Implementar a lógica para remover um item da lista de compras.
//Implementar a lógica para exibir a lista de compras completa.

//Aqui está um exemplo de código Python para este projeto:

def adicionar_item(lista):
    item = input("Digite o nome do item a ser adicionado: ")
    lista.append(item)
    print("Item adicionado com sucesso!")

def remover_item(lista):
    item = input("Digite o nome do item a ser removido: ")

    if item in lista:
        lista.remove(item)
        print("Item removido com sucesso!")
    else:
        print("Item não encontrado na lista!")

def exibir_lista(lista):
    print("Lista de Compras:")
    if lista:
        for item in lista:
            print("- " + item)
    else:
        print("A lista está vazia.")

def exibir_menu():
    print("Lista de Compras")
    print("Selecione a opção:")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Exibir lista")
    print("4. Sair")

def main():
    lista_compras = []

    while True:
        exibir_menu()
        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            adicionar_item(lista_compras)
        elif opcao == 2:
            remover_item(lista_compras)
        elif opcao == 3:
            exibir_lista(lista_compras)
        elif opcao == 4:
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
