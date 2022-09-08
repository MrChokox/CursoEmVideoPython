nome = str(input("Qual o seu nome ? ")).strip()
print(nome.upper())
print(nome.lower())
print('Seu nome possui {} Letras'.format(len(nome) - nome.count(" ")))
sep = nome.split()
print('E seu primeiro nome é {} e ele possui {} letras'.format(sep[0],len(sep[0])))

