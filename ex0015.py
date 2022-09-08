d = int(input('Quantos dias alugados ?'))
km = float(input('Quantos kn rodados ?'))
preço = (d * 60) + (km * 0.15)
print('O preço total ficou em R${:.2f}'.format(preço))
