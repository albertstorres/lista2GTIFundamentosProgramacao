# Desenvolva um programa que leia a área em m² de um terreno retangular. Ao final, o programa deverá mostrar a 
# classificação desse terreno, de acordo com a lista abaixo:
# - Abaixo de 100 m² = Terreno Popular;
# - Entre 100 e 500 m² = Terreno Master;
# - Acima de 500 m² = Terreno Vip.

area = float(input("Digite a área do terreno: "))

while area <= 0 :
    area = float(input("Digite uma área positiva e maior que zero: "))

if area < 100 :
    print("Terreno Popular")
elif area == 100 and area <= 500 :
    print("Terreno Master")
else :
    print("Terreno Vip")
