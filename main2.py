from personaje import personaje


nombre = input("ingrese el nombre:")
altura = float(input("ingrese su altura:"))
velocidad = float(input("ingrese su velocidad:"))
resistencia = float(input("ingrese su resistencaia:"))
fuerza = float(input("ingrese su fuerza:"))

personaje = personaje(nombre, altura, velocidad, resistencia, fuerza)

print("datos del personaje")
print(personaje.mostrar_datos())