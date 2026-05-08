alunos = []
# nota = ("nota")
def mostrarConceito(nota):
    if nota >= 7:
        return "Aprovado"
    elif nota >= 5:
        return "Recuperação"
    else:
        return "Reprovado"
def mediaSala():
    notas = 0.0
    for aluno in alunos:
        notas += aluno["nota"]
    media = notas / len(alunos)
    return media
def mostrarAlunos():
    aprovados = 0
    recuperacao = 0
    reprovados = 0
    melhor = None
    pior = None
    for aluno in alunos:
        conceito = mostrarConceito(aluno["nota"])
        print("\nNome do aluno: ", aluno["nome"])
        print("Nota final: ", aluno["nota"])
        print("Conceito: ", conceito)
        if conceito == "Aprovado":
            aprovados += 1
        elif conceito == "Recuperação":
            recuperacao += 1
        elif conceito == "Reprovado":
            reprovados += 1
        if melhor == None or aluno["nota"] > melhor["nota"]:
            melhor = aluno
        if pior == None or aluno["nota"] < pior["nota"]:
            pior = aluno
    print("\nMédia final da turma: ", mediaSala())
    print("Quantidade de aprovados: ", aprovados)
    print("Quantidade de alunos de recuperação: ", recuperacao)
    print("Quantidade de reprovados: ", reprovados)
    print("\nAluno com a maior nota: ", melhor["nome"])
    print("Nota: ", melhor["nota"])
    print("\nAluno com a menor nota: ", pior["nome"])
    print("Nota: ", pior["nota"])
def novoAlunoGen():
    while True:
        try:
            nome = input("Insira o nome do aluno: ")
            assert nome != "", "O nome não pode estar vazio!"
            idade = int(input("Insira a idade do aluno: "))
            assert idade >= 0, "A idade não pode ser negativa!"
            nota = float(input("Insira a nota do aluno: "))
            assert nota >= 0 and nota <= 10, "Insira uma nota entre 0 e 10!"
            registro = {
                "nome": nome,
                "idade": idade,
                "nota": nota
            }
            alunos.append(registro)
            yield registro
        except ValueError:
            print("Insira um valor válido!")
            yield "Valor inválido"
        except AssertionError as e:
            print(e)
            yield e
        except GeneratorExit:
            mostrarAlunos()
            raise

novoAluno = novoAlunoGen()
try:
    next(novoAluno)
    while True:
        continuar = input("Deseja cadastrar outro aluno? (S/N) ")
        if(continuar.lower() == "s"):
            next(novoAluno)
        else:
            novoAluno.close()
            break
except StopIteration:
    if len(alunos) > 0:
        mostrarAlunos()
except KeyboardInterrupt:
    print("\nFinalizando o programa...")