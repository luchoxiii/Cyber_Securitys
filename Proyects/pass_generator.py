import random
import string

#Un jugador que tiene dudas, es una carga para el equipo. Lucho      

longitud = int(input("Ingrese el tamanio de la password: "))

carateres = string.ascii_letters + string.digits + string.punctuation

password = "".join(random.choice(carateres) for i in range (longitud))

print("El password generado es: " + password)

