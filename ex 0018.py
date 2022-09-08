angulo = float(input("Qual o valor do angulo ?"))
import math
cos = math.cos(math.radians(angulo))
sen = math.sin(math.radians(angulo))
print(f"O coseno de {angulo} é igual a : {cos:.2f}")
print(f"O seno de {angulo} é : {sen:.2f}")
tan = math.tan(math.radians(angulo))
print(f"E a tangente de {angulo} é : {tan:.2f}")
