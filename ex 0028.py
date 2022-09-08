from random import randint
from time import sleep
numero = randint(0,5)
print('Estou pensando em um número de 0 a 5')
resposta = int(input('Qual foi o número que eu pensei:'))
print('Processando...')
sleep(3)
if resposta == numero:
    print('Parabéns você acertou o número')
else:
    print(f'Você errou, o número não é esse, a resposta era {numero}')




