"""

Desenvolva um programa que recebe do usuário nome completo e ano de nascimento
que seja entre 1922 e 2021. A partir dessas informações, o sistema mostrará o
nome do usuário e a idade que completou, ou completará, no ano atual (2022).

Caso o usuário não digite um número ou apareça um inválido no campo do ano,
o sistema informará o erro e continuará perguntando até que um valor correto
seja preenchido.

"""

print("\n* * * * Ano de Nascimento * * * *\n")

def recebe_nome():
    nome = input("Digite o seu nome: ")
    if len(nome) > 0:
        return nome
    else:
        raise Exception("Nome não pode estar vazio")

def recebe_ano():
    
    ano = int(input("Digite o ano de nascimento: "))
    if ano >= 1922 and ano <= 2022:
        idade = 2022 - ano
        return idade

    else:
        raise Exception("Ano de nascimento fora do aceito (1922-2022)")

def recebe_dados():
    nome = recebe_nome()
    if len(nome) > 0:
        idade = recebe_ano()
        print(f"\nSeu nome é {nome}, você tem {idade} anos\n")

while True:
    try:
        recebe_dados()
        break
    except Exception as err:
        print(f"\nOcorreu um erro\n{err}\n")
