"""
Desenvolva um programa que deve ler um arquivo csv intitulado “notas_alunos.csv”.
O arquivo deve ter a seguinte estrutura:

aluno: Nome do aluno;
nota_1: Primeira nota;
nota_2: Segunda nota;
faltas: Número de faltas;

O programa lerá esse arquivo e criará duas colunas. A primeira coluna será “media”,
que terá a média das duas notas do aluno. A segunda será “situacao”, com os valores:
APROVADO ou REPROVADO.

O aluno que tiver mais de 5 faltas ou possuir média menor que sete, será reprovado.
O programa deverá salvar esse novo dataframe com o nome “alunos_situacao.csv”.

Por fim, o programa deverá mostrar na tela:
- o maior número de faltas;
- a média geral das notas dos alunos;
- e a maior média.

Veja em anexo um exemplo do arquivo “notas_alunos.csv”.
"""

import pandas as pd

df = pd.read_csv("h_notas_alunos.csv")
df.head()

print(f"\n{df}\n")

alunos = df["aluno"]
media = (df["nota_1"] + df["nota_2"]) / 2

df["media"] = media
df["situacao"] = ""

mais_faltas = max(df["faltas"])
media_turma = df["media"].mean()
maior_media = max(df["media"])

df.loc[df["media"] >= 7, "situacao"] = "APROVADO"
df.loc[df["media"] < 7, "situacao"] = "REPROVADO"
df.loc[df["faltas"] > 5, "situacao"] = "REPROVADO"


print(df)

print(f"""
Mais faltas: {mais_faltas}
Média da turma: {media_turma}
Maior média: {maior_media}
""")

df.to_csv("h_alunos_situacao.csv")
