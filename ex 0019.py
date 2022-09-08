aluno1 = input("Qual o primeiro aluno ?")
aluno2 = input("segundo aluno ?")
aluno3 = input("terceiro aluno ?")
aluno4 = input("quarto aluno ?")

alunos = aluno1, aluno2, aluno3, aluno4

import random
alunox = random.choice(alunos)
print(f"O aluno que deve apagar o quadro é : {alunox}")

