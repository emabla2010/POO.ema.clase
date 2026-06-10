#En el archivo Personaje_clase.py desarrollar la clase Personaje  
# con #atributo de clase "estado = True" #vivo. Y el constructor y los atributos (nombre, altura, velocidad, resistencia, fuerza) y dos metodos, correr y recuperarse.
#Luego en el archivo carrera.py crear un menu:
#  "ingresar participantes"pedirle los datos al usuario para instanciar objetos e imprimirlos por pantalla, "correr carrera" "pedir distancia" y realizar la carrera, "salir"

class Personaje:
    estado = True #vivo

    def __init__(self, nombre, altura, velocidad, resistencia,fuerza):
        self.nombre = nombre
        self.altura = altura
        self.velocidad = velocidad
        self.resistencia = resistencia
        self.fuerza = fuerza

    def correr (self,estado):
        if estado == True:
            distancia = 1000
            tiempo = distancia / self.velocidad
            return tiempo

        else:
            print("El personaje no puede correr")
            
    def recuperarse (self): 
        pass  
    