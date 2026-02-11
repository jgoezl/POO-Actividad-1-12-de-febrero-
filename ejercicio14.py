# 14. (Ejercicio Propuesto)
"""Elabore un algoritmo que lea un numero y obtenga su cuadrado y su cubo"""

# clase

class Numero:
  @staticmethod
  def square(n):
    return n**2

  @staticmethod
  def cubic(n):
    return n**3

# trabajar con las variables

numero = int(input("Ingresa un numero: "))
cuadrado = Numero.square(numero)
cubo = Numero.cubic(numero)

print(f"El cuadrado de {numero} es {cuadrado} y el cubo es {cubo}")
