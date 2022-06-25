"""

Faça uma função calculadora de dois números com três parâmetros: os dois
primeiros serão os números da operação e o terceiro será a entrada que
definirá a operação a ser executada. Considera a seguinte definição:
    1. Soma
    2. Subtração
    3. Multiplicação
    4. Divisão

Caso seja inserido um número de operação que não exista, o resultado deverá
ser 0.

"""


print("\n* * * * Calculadora * * * *\n")


def calculadora(numero_1, numero_2, operacao):
    if operacao == 1:
        return numero_1 + numero_2
    elif operacao == 2:
        return numero_1 - numero_2
    elif operacao == 3:
        return numero_1 * numero_2
    elif operacao == 4:
        return numero_1 / numero_2
    else:
        return 0

print("""
Operações:

1. Soma
2. Subtração
3. Multiplicação
5. Divisão
""")

print(f"Soma: {calculadora(5, 3, 1)}")
print(f"Subtração: {calculadora(5, 3, 2)}")
print(f"Multiplicação: {calculadora(5, 3, 3)}")
print(f"Divisão: {calculadora(5, 3, 4):.2f}")
print(f"Erro: {calculadora(5, 3, 5)}\n")
