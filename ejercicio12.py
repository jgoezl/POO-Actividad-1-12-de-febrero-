# 12. (Ejercicio Propuesto)
"""Un empleado trabaja 48 horas en la semana a razón de $5.000 hora. El porcentaje de
retención en la fuente es del 12,5% del salario bruto. Se desea saber cuál es el salario bruto,
la retención en la fuente y el salario neto del trabajador. """

#Clase

class Salarios:
  @staticmethod
  def calcular_salarioBruto(gananciaHora, horasTrabajadas):
    return gananciaHora * horasTrabajadas

  @staticmethod
  def calcular_loRetenido(salarioBruto, _retencion):
    return salarioBruto * _retencion
 
  @staticmethod
  def calcular_salarioNeto(salarioBruto, salarioNeto):
    return salario_bruto - salarioNeto


# Asignacion de variables

horas_trabajadasSemanalmente = 48
razon_hora = 5000
retencion = 12.5
porcentaje_retencion = retencion/100

salario_bruto = Salarios.calcular_salarioBruto(razon_hora, horas_trabajadasSemanalmente)
valor_retenido = Salarios.calcular_loRetenido(salario_bruto, porcentaje_retencion)
salario_neto = Salarios.calcular_salarioNeto(salario_bruto, valor_retenido)

print(f"""Salario bruto: {salario_bruto}; 
Retencion en la fuente: {valor_retenido}; 
Salario neto: {salario_neto}""")
