id = int(input ("Digite o id do vendedor: "))
codpeca = int(input("Digite o código da peça: "))
preco = float(input ("Digite o preço unitario da peça: "))
qtd = int(input("Digite a quantidade de peças vendidas: "))

total = preco*qtd
comissao = total*0.05

print("O valor da comissão do vendedor de ID", id, "é de: R$", comissao, "\n código da peça:",codpeca, "\n valor total do produto:",total)