aluno1 = input("Qual o primeiro aluno ?")
aluno2 = input("segundo aluno ?")
aluno3 = input("terceiro aluno ?")
aluno4 = input("quarto aluno ?")

alunos = [aluno1, aluno2, aluno3, aluno4]

import random
random.shuffle(alunos)
print(f"a ordem de apresentação será : {alunos}")

from flask import Flask

