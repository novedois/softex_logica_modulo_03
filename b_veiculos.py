print("\n* * * * Veículos * * * *\n")

quantidade_rodas = int(input("Digite a quantidade de rodas: "))
peso_bruto = float(input("Digite o peso (em KG): "))
quantidade_pessoas = int(input("Digite a quantidade de pessoas no veículo: "))

habilitacao = ""
erro = False

if quantidade_rodas == 3 or quantidade_rodas == 2:
    habilitacao = "A"
elif quantidade_rodas == 4 and quantidade_pessoas <= 8 and peso_bruto <= 3500:
    habilitacao = "B"
elif quantidade_rodas >= 4 and peso_bruto > 3500 and peso_bruto <= 6000:
    habilitacao = "C"
elif quantidade_rodas >= 4 and quantidade_pessoas> 8:
    habilitacao = "D"
elif quantidade_rodas >= 4 and peso_bruto > 6000:
    habilitacao = "E"
else:
    erro = True

if erro:
    print("\n* * ERRO * *\n")
else:
    print(f"\nHabilitação indicada: {habilitacao}\n")
    