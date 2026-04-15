def calcular_total():
    try:
        preco1 = float(input("Digite o preço do primeiro produto: "))
        preco2 = float(input("Digite o preço do segundo produto: "))
    except:
        print("Erro: os preços devem ser numéricos!")
        return  # encerra o programa

    total = preco1 + preco2
    print(f"Valor total da compra: R$ {total:.2f}")


# chamando a função
calcular_total()