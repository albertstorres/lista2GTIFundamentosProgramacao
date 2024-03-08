# Um programa de vida saudável quer dar pontos para atividades físicas, os quais poderão ser trocados por dinheiro.
# O sistema funciona assim, cada hora de atividade física no mês vale pontos: 

# - até 10h de atividade no mês: ganha 2 pontos por hora;
# - de 11h até 20h de atividade no mês: ganha 5 pontos por hora;
# - acima de 20h de atividade no mês: ganha 10 pontos por hora.

# Faça um programa que leia quantas horas de atividade uma pessoa teve por mês, calcule e mostre quantos pontos
# ela obteve.

horas_de_atividade = float(input("Digite o total de horas de atividade física no mês: "))

while horas_de_atividade < 0 :
    horas_de_atividade = float(input("Digite um valor positivo para o total de horas: "))

if horas_de_atividade <= 10 :
    pontos = int(horas_de_atividade * 2)
elif horas_de_atividade == 11 and horas_de_atividade <= 20 :
    pontos = int(horas_de_atividade * 5)
else :
    pontos = int(horas_de_atividade * 10)
    
print(f"Total de pontos obtidos: {pontos}")