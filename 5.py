# Ler o nome de dois times e a quantodade de gols marcados na partida (para cada time). Escrever o nome do vencedor.
# Caso não haja vencedor deverá ser impressa a palavra EMPATE.

time1 = input("Digite o nome do time mandante: ")
time2 = input("Digite o nome do time visitante: ")
gols_time1 = int(input(f"Digite o número de gols {time1}: "))
while gols_time1 < 0 :
    gols_time1 = int(input(f"Digite o número de gols do {time1}: "))
gols_time2 = int(input(f"Digite o número de gols do {time2}: "))
while gols_time2 < 0 :
    gols_time2 = int(input(f"Digite o número de gols do {time2}: "))

if gols_time1 > gols_time2 :
    print(f"Vencedor: {time1}")
elif gols_time2 > gols_time1 :
    print(f"Vencedor: {time2}")
else :
    print("EMPATE")

