valor_compra = float(input("Informe o total da compra: "))

forma_pagamento = int(input("Informe a forma de pagamento (|1 para A vista| ou |2 para A prazo|): "))

parcelas = 0

# 1 – A vista – 10% de desconto, caso o valor da venda seja maior que 500 15%, caso seja maior que 1000, 20% de desconto
if (forma_pagamento == 1):
    if (valor_compra > 1000):
        desconto = valor_compra * 0.20        
    elif (valor_compra > 500):
        desconto = valor_compra * 0.15
    else:
        desconto = valor_compra * 0.10

    print(f"O valor da compra é: R$ {valor_compra}, com desconto de R$ {desconto}. Com total a pagar de {valor_compra - desconto}")

# 2 – A prazo – A venda pode ser parcelada em até 18x. Caso seja parcelado em mais do que 10x possui juros:
# Apenas compras com mais de 800 reais podem ser parceladas acima de 5x;
# Juros:
#           1 – 11 vezes: 5% de juros ao mês.
#           2 – 12 vezes: 6.5% de juros ao mês.
#           3 – 13 vezes: 7% de juros ao mês.
#           4 – 14 vezes: 9% de juros ao mês.
#           5 – 15 vezes: 9.5% de juros ao mês.
#           6 – 16 vezes: 10% de juros ao mês.
#           7 – 17 vezes: 11.3% de juros ao mês.
#           8 – 18 vezes: 12% de juros ao mês.

elif (forma_pagamento == 2):
    parcelas = int(input("Informe em quantas parcelas deseja pagar: "))

    if (valor_compra < 800 and parcelas > 5):
            print("A quantidades de parcelas não pode ser maior de 5")
    else:
        if (parcelas > 18):
             print("A quantidades de parcelas não pode ser maior que 18")
        else:
             if (parcelas > 10):
                  if (parcelas == 11):
                    #    acrescimo = (valor_compra * 0.05) * 11
                    #    valor_compra = valor_compra + acrescimo
                    # valor_compra += valor_compra * 0.05 * 11  
                    valor_compra = (valor_compra * 0.05 * 11) + valor_compra
                  elif (parcelas == 12):
                    valor_compra = (valor_compra * 0.065 * 12) + valor_compra
                  elif (parcelas == 13):
                    valor_compra = (valor_compra * 0.07 * 13) + valor_compra
                  elif (parcelas == 14):
                    valor_compra = (valor_compra * 0.09 * 14) + valor_compra
                  elif (parcelas == 15):
                    valor_compra = (valor_compra * 0.095 * 15) + valor_compra
                  elif (parcelas == 16):
                    valor_compra = (valor_compra * 0.10 * 16) + valor_compra
                  elif (parcelas == 17):
                    valor_compra = (valor_compra * 0.113 * 17) + valor_compra
                  elif (parcelas == 18):
                    valor_compra = (valor_compra * 0.12 * 18) + valor_compra                
             
             print(f"O valor da compra é: R$ {valor_compra}")
else:
    print("Forma de pagamento inválida, tente novamente!")