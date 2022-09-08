from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)

print('Vamos brincar de jokenpô')
print('''Suas opções são:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')

player = int(input('Você escolhe:'))
if player >= 3:
 print('Opção inválida tente novamente')

print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Pô')
sleep(1)


print('\033[33m-~-' * 10)
print(f'Computador jogou {itens[pc]}')
print(f'Jogador jogou {itens[player]}')
print('\033[33m-~-' * 10)

if pc == 0:
 if player == 0:
  print('Ops Empatou')
 elif player == 1:
  print('Você ganhou')
 elif player == 2:
  print('Computador: Eu ganhei')
elif pc == 1:
 if player == 0:
  print('Você Perdeu')
 if player == 1:
  print('Ops Empatou')
 if player == 2:
  print('Computador: Eu Ganhei')
elif pc == 2:
 if player == 0:
  print('Você Ganhou')
 if player == 1:
  print('Computador: Eu ganhei')
 if player == 2:
  print('Ops Empatou')



