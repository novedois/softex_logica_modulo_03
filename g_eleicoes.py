"""
Desenvolva um código que simule uma eleição com três candidatos.
- candidato_X => 889
- candidato_Y => 847
- candidato_Z => 515
- branco => 0

O código deve perguntar se deseja finalizar a votação depois do voto. Caso
o número do voto não corresponda a nenhum candidato ou seja branco, ele deve
ser tratado como nulo. Se for inserido um texto ao invés de número, o código
deve retornar uma mensagem para votar novamente.

Quando a votação for finalizada, o código deverá mostrar o vencedor, aquele
com o maior número de votos e, também, a quantidade de votos de cada candidato,
os brancos e nulos 
"""

candidato_x = 0
candidato_y = 0
candidato_z = 0
nulos = 0
total_votos_validos = 0
vencedor = ""

print("\n* * * Votação * * *\n")

print("""
Códigos dos candidatos:

Candidato X -> 889
Candidato Y -> 847
Candidato Z -> 515
Branco      -> 0
""")

while True:
    try:
        voto = int(input("Digite o código do candidato: "))

        if voto == 889:
            print("Você votou no Candidato X!\n")
            candidato_x += 1
            total_votos_validos += 1
        elif voto == 847:
            print("Você votou no Candidato Y!\n")
            candidato_y += 1
            total_votos_validos += 1
        elif voto == 515:
            print("Você votou no Candidato Z!\n")
            candidato_z += 1
            total_votos_validos += 1
        else:
            print("Voto em branco!\n")
            nulos += 1

        continua = int(input("\nDigite 0 para sair ou 1 para continuar: "))

        if continua == 0:
            break
    except:
        print("Por favor digite um número válido!")

votos = [ candidato_x, candidato_y, candidato_z ]
vencedor = max(votos)
vencedor_nome = ""

if vencedor == votos[0]:
    vencedor_nome = "Candidato X"
elif vencedor == votos[1]:
    vencedor_nome = "Candidato Y"
elif vencedor == votos[2]:
    vencedor_nome = "Candidato Z"


print(f"""

* * * * RESULTADO * * * *

Vencedor: {vencedor_nome}


Candidato X: \t{candidato_x} votos
Candidato Y: \t{candidato_y} votos
Candidato Z: \t{candidato_z} votos

Votos válidos: \t{total_votos_validos}
Votos nulos: \t{nulos}
Votos totais: \t{total_votos_validos + nulos}


""")
