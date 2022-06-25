import time


print("\n* * * * Bomba * * * *\n")

segundos = int(input("Digite o número de segundos: "))

print("\nIniciando contgem regressiva . . .\n")

for i in range(segundos, 0, -1):
    print(i)
    time.sleep(1)

print("\nBUM!\n")
