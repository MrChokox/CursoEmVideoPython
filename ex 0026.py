frase = str(input("Digite uma frase:")).strip().lower()
print('A letra a aparece {} vezes na frase'.format(frase.count('a')))
print('A primeira letra a apareceu na posição {} da frase'.format(frase.find('a')+1))
print('A ultima letra A aparece na posição {} da frase'.format(frase.rfind('a')+1))

