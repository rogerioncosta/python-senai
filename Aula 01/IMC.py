nome = input("Digite o seu nome: ")
altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso: "))

resultado = peso / (altura * altura)
# resultado = peso / altura ** 2

print(f"Olá, {nome}, o seu IMC é de: {resultado:.2f}")

'''
if(resultado <= 24.9 and resultado >= 18.6):
    print("Você está no peso normal")
elif(resultado < 18.5):
    print("Você está com o peso abaixo do normal")
elif(resultado <= 29.9 and resultado >= 25.0):
    print("Você está no sobrepeso")
elif(resultado >= 30.0):
    print("Você está com obesidade")
elif(resultado > 40):
    print("Obesidade Mórbida")
else:
    print("Valor inválido")
'''



