frase = str(input('Digite umas frase:')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
contrario = ''
for letra in range(len(junto) - 1, -1, -1):
    contrario += junto[letra]
print(junto,' essa frase ao contrario é:',contrario)
if junto == contrario:
    print('Essa frase é um palindromo')
else:
    print('Essa frase não é um palindromo')