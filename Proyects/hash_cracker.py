import hashlib

#Mada mada daze

hash_file = "b4f4a173aee29c49fbd8bcff45f7a7d7055f935bf8eee8397e771b42a32a8158"

dic_file = input("Ingrese la direccion del archivo, del diccionario: ")

with open (dic_file,"r") as file:

    diccionario = [line.strip for line in file]

    for password in diccionario:

        hash_calculado = hashlib.sha256(password.encode()).hexdigest()


        if hash_calculado == hash_file :

            print("La contrasenia origial es: " + password)
            break

        else:
            print("La contrasenia no se encuentra en el diccionario")
