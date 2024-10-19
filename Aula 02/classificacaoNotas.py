# 3. Classificação de Notas
# Peça ao usuário para inserir uma nota de 0 a 100 e, em seguida, classifique-a como
# "A" (90-100), "B" (80-89), "C" (70-79), "D" (60-69) ou "F" (abaixo de 60).

nota = float(input("Digite a sua nota (0/100): "))

if (nota >= 90 and nota <= 100):
    print("A sua classificação é A.")
elif (nota >= 80):
    print("A sua classificação é B.")
elif (nota >= 70):
    print("A sua classificação é C.")
elif (nota >= 60):
    print("A sua classificação 0é D.")
elif (nota < 60):
    print("A sua classificação é F.")
else:
    print(f"Você inseriu a nota {nota}, lembre-se que deve ser de 0 a 100")






    
    