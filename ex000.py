nome = str(input("Qual o seu nome?")).strip().lower()
if 'gustavo' in nome:
    print('Seu nome é bonito')
else:
    print('Seu nome não é bonito')
print('\033[31;42mBom dia {}'.format(nome))

valor ='prova de python'
print(len(valor))




