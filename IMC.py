peso = float(input("Digite seu peso em kilos: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso /(altura ** 2)

print("O seu IMC é: ", imc)

if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc < 24.9:
    print("Peso normal")
elif imc >= 25 and imc < 29.9:
    print("excesso de peso")
elif imc >= 30 and imc < 34.9:
    print("Obesidade classe 1")
elif imc >= 35 and imc < 39.9:
    print("Obesidade classe 2")
elif imc >= 40:
    print("Obesidade classe 3")
    
