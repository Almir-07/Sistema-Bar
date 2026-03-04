def verificar_entrada(idade_recebida):
    if idade_recebida == 18:
        return "Acabou de virar adulto, seja bem-vindo!"
    elif idade_recebida > 18:
        return "Entrada liberada."
    else:
        return "Entrada proibida para menores."

comandas = {}

while True:
    print("\n--- MENU DO BAR ---")
    print("1. Cadastrar Cliente")
    print("2. Lançar Bebidas")
    print("3. Fechar Conta (Remover do Bar)")
    print("4. Sair do Sistema")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        idade_usuario = int(input("Digite sua idade: "))
        mensagem = verificar_entrada(idade_usuario)
        print(mensagem)

        if "proibida" not in mensagem:
            nome = input("Digite o nome para abrir comanda: ").lower()
            comandas[nome] = 0
            print(f"Comanda de {nome.capitalize()} aberta!")

    elif opcao == "2":
        busca = input("Quem quer procurar? ").lower()
        if busca in comandas:
            bebidas = int(input(f"Quantas bebidas o {busca.capitalize()} consumiu agora? "))
            comandas[busca] += bebidas
            print(f"Total atual de {busca.capitalize()}: {comandas[busca]} bebidas.")
        else:
            print("Cliente não encontrado.")

    elif opcao == "3":
        busca = input("Quem vai fechar a conta e sair? ").lower()
        if busca in comandas:
            total_pago = comandas[busca]
            # O COMANDO MÁGICO:
            del comandas[busca] 
            
            print(f"💰 Conta de {busca.capitalize()} fechada!")
            print(f"O cliente pagou por {total_pago} bebidas e saiu do sistema.")
        else:
            print("Este cliente não está no bar.")

    elif opcao == "4":
        break
    

