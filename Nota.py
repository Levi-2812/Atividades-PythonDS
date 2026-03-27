n1 = int(input ("Digite a primeira nota do aluno: "))
n2 = int(input ("Digite a segunda nota do aluno: "))
n3 = int(input ("Digite a terceira nota do aluno: "))

Media = (n1+n2+n3) /3

if Media >= 8:
    print ("O aluno de média", Media, "tem o Conceito A")
elif Media >= 5 and Media < 8:
    print ("O aluno de média", Media, "tem o Conceito B")
elif Media <5:
    print ("O aluno de média", Media, "tem o Conceito C")