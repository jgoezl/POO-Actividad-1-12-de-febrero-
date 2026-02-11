# 4 (Ejercicio resuelto)
"""A la mamá de Juan le preguntan su edad, y contesta: tengo 3 hijos, pregúntele a Juan su
edad. Alberto tiene 2/3 de la edad de Juan, Ana tiene 4/3 de la edad de Juan y mi edad es
la suma de las tres. Hacer un algoritmo que muestre la edad de los cuatro."""

# Clase

class Edades:
  @staticmethod
  def calcular_edadAlberto(edad_juan):
    return int(2/3 * edad_juan)

  @staticmethod
  def calcular_edadAna(edad_juan):
    return int(4/3 * edad_juan)

  @staticmethod
  def calcular_edadMadre(edad_juan, edad_alberto, edad_ana):
    return edad_juan + edad_alberto + edad_ana

# Asignacion de variables    

edad_juan = int(input("¿Cuál es la edad de Juan?: "))
edad_alberto = Edades.calcular_edadAlberto(edad_juan)
edad_ana = Edades.calcular_edadAna(edad_juan)
edad_madre = Edades.calcular_edadMadre(edad_juan, edad_alberto, edad_ana)

print(f"""Las edades son:
Alberto:{edad_alberto}, Juan:{edad_juan}, Ana:{edad_ana}, Mamá:{edad_madre}""")
