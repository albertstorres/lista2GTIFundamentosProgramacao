# Uma loja de roupas está em promoção. Acima de 2 peças de roupas compradas e fazendo o pagamento à vista, 
# o cliente tem 20% de desconto no valor total. Faça um algoritmo que receba:

# - A quantidade de peças compradas;
# - O valor total da compra;
# - O código referente a condição de pagamento:
#   i. 1 - Á vista;
#  ii. 2 - Crédito;
# iii. 3 - Crédito parcelado.

# Por fim, o algoritmo deverá apresentar uma mensagem informando se o desconto foi aplicado, e em caso positivo,
# o novo valor da compra.

quantidade_pecas_compradas = int(input("Digite a quantidade de peças compradas: "))
total_compra = float(input("Digite o valor total da compra: "))

print("1 - Á vista")
print("2 - Crédito")
print("3 - Crédito parcelado")

codigo_pagamento = int(input("Digite a opção de pagamento: "))

if quantidade_pecas_compradas > 2 and codigo_pagamento == 1 :
    desconto = total_compra * 0.2
    print(f"O desconto de R$ {desconto} foi aplicado")
    print(f"Valor da compra: R$ {total_compra - desconto}")
else :
    print("Desconto não aplicado.")
    print(f"Valor da compra: R$ {total_compra}")
