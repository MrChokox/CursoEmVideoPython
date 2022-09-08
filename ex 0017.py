print("Vamos descobrir o valor da hipotenusa de um triangulo retangulo")
oposto = float(input("Digite o valor do cateto oposto :"))
adjacente = float(input("Digite o valor da adjacente : "))
import math
hipotenusa = math.hypot(oposto,adjacente)
print(f"O valor da hipotenusa do triangulo retangulo com lados iguais a : {oposto} e {adjacente} é : {hipotenusa:.2f}")
