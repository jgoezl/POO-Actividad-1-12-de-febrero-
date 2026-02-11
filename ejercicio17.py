# 17. (Ejercicio Propuesto)
"""Dado el radio de un circulo. Haga un algoritmo que obtenga el area del circulo y la longitud de la circunferencia"""

import math

# Clase

class Circulo:

  @staticmethod
  def area(r):
    return math.pi * r**2

  @staticmethod
  def longitud(r):
    return 2 * math.pi * r

# Trabajar con variables

radio = float(input("Ingresa el radio del circulo: "))
area = Circulo.area(radio)
longitud = Circulo.longitud(radio)

print(f"El area del circulo es {area} y la longitud de la circunferencia es {longitud}")
