"""
Faça uma função calculadora que os números e as operações serão feitas pelo
usuário. O código deve ficar rodando infinitamente até que o usuário escolha
a opção de sair. No início, o programa mostrará a seguinte lista de operações:
    1: Soma
    2: Subtração
    3: Multiplicação
    4: Divisão
    0: Sair

Digite o número para a operação correspondente e caso o usuário introduza
qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e
voltar ao menu de opções.

Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e
segundo valor, um de cada. Depois precisa executar a operação e mostrar o
resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá
parar. 

É necessário que o sistema mostre as opções sempre que finalizar uma operação
e mostrar o resultado. 
"""

print("\n* * * * Calculadora * * * *\n")

while True:
    print("""
Opções:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão
5. Sair
""")
    escolha = int(input("Selecione uma opção: "))
    if escolha > 0 and escolha < 5:
        numero_1 = int(input("Digite o primeiro número: "))
        numero_2 = int(input("Digite o segundo número: "))

        if escolha == 1:
            print(f"\nSoma: {numero_1 + numero_2}\n")
        elif escolha == 2:
            print(f"\nSubtração: {numero_1 - numero_2}\n")
        elif escolha == 3:
            print(f"\nMultiplicação: {numero_1 * numero_2}\n")
        elif escolha == 4:
            print(f"\nDivisão: {numero_1 / numero_2}\n")

    elif escolha <= 0 or escolha > 5:
        print("\nEsta opção não existe, tente novamente!\n")

    else:
        print("\nFinalizando programa....\n")
        break
