import math

print("Calculadora de Áreas")
print("---------------------")

shape = input("Ingrese la forma para calcular el área (cuadrado, rectángulo, triángulo, círculo, hexágono): ")

if shape.lower() == "cuadrado":
    side = float(input("Ingrese la longitud del lado del cuadrado: "))
    area = side**2
    print("El área del cuadrado es:", area)

elif shape.lower() == "rectángulo":
    base = float(input("Ingrese la base del rectángulo: "))
    height = float(input("Ingrese la altura del rectángulo: "))
    area = base * height
    print("El área del rectángulo es:", area)

elif shape.lower() == "triángulo":
    base = float(input("Ingrese la base del triángulo: "))
    height = float(input("Ingrese la altura del triángulo: "))
    area = (base * height) / 2
    print("El área del triángulo es:", area)
    
elif shape.lower() == "círculo":
    radius = float(input("Ingrese el radio del círculo: "))
    area = math.pi * (radius**2) 
    print("El área del círculo es:", area)
    
elif shape.lower() == "hexágono":
    apothem = float(input("Ingrese el apotema del hexágono: ")) 
    side = float(input("Ingrese la longitud del lado del hexágono: "))
    perimeter = 6 * side
    area = (perimeter * apothem) / 2
    print("El área del hexágono es:", area)

else:
    print("Forma no válida")