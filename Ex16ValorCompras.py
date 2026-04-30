Ex16:def valorCompra(valor, qtde):
    return qtde * valor
valorInput = float(input("Insira o valor do produto: "))
qtdeInput = int(input("Insira a quantidade de produtos comprados: "))
print(valorCompra(valorInput, qtdeInput))