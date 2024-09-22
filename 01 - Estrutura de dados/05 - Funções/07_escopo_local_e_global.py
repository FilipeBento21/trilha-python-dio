salario = 2000


def salario_bonus(bonus, lista):
    global salario
    salario += bonus
    return salario

salario_com_bonus = salario_bonus(500)  # 2500
print(salario_com_bonus)

lista = [1]
salario_com_bonus = salario_bonus(500, lista)
print(salario_com_bonus)
print(lista)