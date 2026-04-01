precoCarro = float(input ("Digite o valor do carro: "))
imposto = precoCarro * 0.45
lucroVendededor = precoCarro *0.12
valorTotal = precoCarro + imposto + lucroVendededor

print ("O carro com o valor de fabrica de: R$", precoCarro, "haverá um imposto de 45% e um lucro para o vendedor de 12% a mais em seu valor.\nO valor total: R$", valorTotal)
print("O valor do imposto é: R$", imposto)
print("O lucro do vendedor sobre o Carro é: ",lucroVendededor)