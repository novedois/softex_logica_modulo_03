
print("\n* * * * NOTAS * * * *\n")

nome = input("Digite o nome do aluno: ")
faltas = int(input("Digite o número de faltas: "))
nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
media = (nota_1 + nota_2) / 2

print(f"""
Aluno: {nome}
Média: {media:.2f}
Faltas: {faltas}
""")

if media < 7 or faltas > 3:
    print("Aluno reprovado\n")
else:
    print("Aluno aprovado\n")