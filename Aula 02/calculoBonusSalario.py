# 4. Cálculo de Bônus Salarial
# Peça ao usuário para inserir seu salário e o tempo de serviço. Se o tempo de serviço
# for superior a 5 anos, conceda um bônus de 5% ao salário. Ao final deve ser mostrado o salário atualizado.

tempoServico = int(input("Digite o tempo de serviço em anos: "))

salario = float(input("Digite o seu salário: "))

bonus = 0

if (tempoServico > 5):
    bonus = salario * 0.05
    salarioBonus = salario + bonus
    print(f"Você tem direito a um bônus de {bonus}, e vai receber de salário R$ {salarioBonus:.2f}")
else:
    print(f"O seu tempo de serviço é de {tempoServico} ano(s). Sendo assim você não tem direito ao bônus")