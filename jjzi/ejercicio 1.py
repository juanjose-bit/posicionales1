nombre1 = input("Ingrese el nombre del primer trabajador: ")
salario_bruto1 = float(input("Ingrese el salario bruto del primer trabajador: "))
deducciones1 = float(input("Ingrese las deducciones del primer trabajador: "))
bonificaciones1 = float(input("Ingrese las bonificaciones del primer trabajador: "))

salario_neto1 = salario_bruto1 - deducciones1 + bonificaciones1

nombre2 = input("Ingrese el nombre del segundo trabajador: ")
salario_bruto2 = float(input("Ingrese el salario bruto del segundo trabajador: "))
deducciones2 = float(input("Ingrese las deducciones del segundo trabajador: "))
bonificaciones2 = float(input("Ingrese las bonificaciones del segundo trabajador: "))

salario_neto2 = salario_bruto2 - deducciones2 + bonificaciones2

if salario_neto1 > salario_neto2:
    print("El trabajador con más salario neto es:", nombre1)
elif salario_neto2 > salario_neto1:
    print("El trabajador con más salario neto es:", nombre2)
else:
    print("Ambos trabajadores tienen el mismo salario neto.")
