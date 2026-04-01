nome = str(input("Digite o nome do Jogador: "))
salarioAtual = int(input("Digite o salário atual: "))

if salarioAtual >= 0 and salarioAtual < 1000:
    novoSalario = salarioAtual * 1.20
elif salarioAtual >= 1000.1 and salarioAtual < 5000:
    novoSalario = salarioAtual * 1.10
elif salarioAtual >= 5000.1:
    novoSalario = salarioAtual * 1.05

print("O Jogador:", nome,"tem um salario atual de: ", salarioAtual,". \n O Jogador", nome,"agora tera um salário de: ",novoSalario)