Ex15:def maiorIdade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"
idadeInput = int(input("Insira a sua idade: "))
print(maiorIdade(idadeInput))