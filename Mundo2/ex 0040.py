nota = float(input('Qual foi sua primeira nota?'))
nota2 = float(input('Qual foi sua segunda nota?'))
media = (nota + nota2) / 2

if media > 7.0:
    print("Prabens você passou")
elif media < 5.0:
    print("Você não passou, estude mais!")
else:
    print('Sua nota não foi suficiente, mas você tem direito a recuperação')
