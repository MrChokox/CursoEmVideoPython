nome = str(input('Digite aqui seu nome completo:')).strip()
dividido = nome.split()
print('Seu primeiro nome é {}'.format(dividido[0]))
print('Seu ultimo nome é {}'.format(dividido[len(dividido)-1]))

