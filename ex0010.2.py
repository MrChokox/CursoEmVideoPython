real = float(input('Quanto voce tem na carteira ? R$'))
dolar = real / 5.52
iene = real / 0.051
print('com R${:.2f} voce pode comprar US${:.2f} e {:.2f}ienes'.format(real, dolar, iene))
