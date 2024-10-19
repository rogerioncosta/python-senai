# Atividades Listas e Laços de Repetição

# 1- Crie um programa que simule um sistema básico de reserva de voos. O programa deve permitir que o usuário adicione reservas de voos enquanto desejar. Cada reserva deve incluir o nome do passageiro e o destino. Ao final, o programa deve listar todas as reservas feitas.
import os

numeroReserva = 0
reservas = []
continuar = "s"

while (continuar.upper() == "s"):
    nome = input("Digite o seu nome: ")
    destino = input("Digite o destino: ")

    numeroReserva += 1    

    reservas.append([numeroReserva, nome, destino])
    # reservas.append({"Nr. Reserva: " , numeroReserva, "Nome: ", nome, "Destino: ", destino}) 
    
    continuar = input("Deseja continuar? (s/n): \n")

    os.system("cls") # Limpa a tela

print("Reservas feitas")
print("=" * 14)
print("")
    
for i in range(len(reservas)):
    print(f"Nr. Reserva: {reservas[i][0]} - Nome: {reservas[i][1]} - Destino: {reservas[i][2]}")

# listaNomes = []
# listaDestinos = []
# continuar = "s"

# while (continuar.upper() == "s"):
#     nome = input("Seu nome: ")
#     listaNomes.append(nome)

#     destino = input("Seu destino: ")
#     listaDestinos.append(destino)

#     continuar = input("Deseja continuar? (s/n): \n")

#     os.system("cls") # Limpa a tela

# print("Reservas feitas")
# print("=" * 14)
# print("")

# for i in range(len(listaNomes)):
#      print(f"Nome: {listaNomes[i]} - Destino: {listaDestinos[i]}")