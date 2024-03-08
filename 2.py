# Precisa-se desenvolver um sistema para verificar se um aluno foi aprovado na disciplina. Pede-se que o professor
# insira as duas notas do aluno e sua frequência em porcentagem.
# Primeiro verifica-se se o aluno possui no mínimo 75% de frequência, caso seja verdadeiro, verifica-se a média 
# do aluno é maior ou igual a 7, mostrando a mensagem "Aprovado por média". Se não, mostrar a mensagem 
# "Reporvado por média".
# Mas, se a frequência for abaixo de 75%, apresenta a mensagem "Reprovado por falta"

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
frequencia = float(input("Digite a frequência do aluno: "))

if frequencia >= 75 :
    media = (nota1 + nota2) / 2
    if media >= 7 :
        print("Aprovado por média")
    else :
        print("Reprovado por média")
else :
    print("Reprovado por falta")