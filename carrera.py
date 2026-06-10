from personaje_clase import Personaje

menu = '''
1-crear personaje
2-Mostrar participantes
3-corer carrera 
4-recuperar participantes
5-salir
'''
participantes = []

while True:
    print (menu)
    opcion = int(input("ingrese una opcion:"))

    if opcion == 1:
        nombre = input("ingrese el nombre del personaje: ")
        altura = float(input("ingese la altura del personaje: "))
        velocidad = int(input("ingrese la velocidad del personaje: "))
        resistencia = int(input("ingrese el valor de la resistencia"))
        fuerza = int(input("ingrese la fuerza del personaje"))

        personaje1 = Personaje(nombre,altura,velocidad,resistencia,fuerza)
        print(personaje1.nombre)


    elif opcion == 2: 
        tiempo = personaje1.correr(True)
        print("el personaje demoro",tiempo)


    elif opcion == 3:  
        break     

