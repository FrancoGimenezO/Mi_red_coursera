############################################################
# Lo primero que haremos serÃ¡ escribir un mensaje de bienvenida al usuario
# con el nombre de la red. Puedes modificar este mensajes para que represente el nombre de tu propia red
# Considera que al escribir """ tambien estamos delimitado un string, pero al hacerlo de esta manera,
# cambios de li­nea que ocurran en el codigo se consideraran como parte del string.
# Si no estas convencido, prueba el funcionamiento reemplazando los delimitadores por "

print("Bienvenido a ... ")
print("""
              _                  __
   ____ ___  (_)  ________  ____/ /
  / __ `__ \/ /  / ___/ _ \/ __  /
 / / / / / / /  / /  /  __/ /_/ /
/_/ /_/ /_/_/  /_/   \___/\__,_/

""")

#Primera interaccion. Solicitamos al usuario que ingrese su nombre,
#y lo guardamos en una variable de tipo str
nombre = input("Para empezar, dime como te llamas. ")
print()
print("Hola ", nombre, ", bienvenido a Mi Red")
print()

#Segunda interaccion. Solicitamos el ingreso del año, y utilizamos este
#dato para estimar la edad de la persona. Por que decimos que solo estamos "estimando" su edad?
#¿Que ocurre si eliminamos la conversion a tipo de dato 'int' de la siguiente linea?
agno = int(input("Para preparar tu perfil, dime en que año naciste. "))
edad = 2023 - agno
print()

#Tercera interaccion. Solicitamos la estatura, medida en metros.
#Utilizamos la conversion a 'int', y una expresion para convertir esto
#a una medida en metros y centi­metros
estatura = float(input("Cuentame mas de ti, para agregarlo a tu perfil. ¿Cuanto mides? Damelo en metros. "))
estatura_m = int(estatura)
estatura_cm = int( (estatura - estatura_m)*100 )

#Cuarta interaccion. Consultamos cuantos amigos tiene el usuario.
num_amigos = int(input("Muy bien. Finalmente, cuentame cuantos amigos tienes. "))
tel = int(input ("Numero de telefono: "))
ciudad = input ("¿De que ciudad eres?: ")
genero = input ("Dime de que genero eres: ")


#Con los datos recolectados escribimos en pantalla un texto que resuma los datos que hemos obtenido
print()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
print("--------------------------------------------------")
print("Nombre:  ", nombre)
print("Edad:    ", edad, "años")
print("Estatura:", estatura_m, "metros y", estatura_cm, "centimetros")
print("Amigos:  ", num_amigos)
print("Telefono: ", tel)
print("Ciudad: ", ciudad)
print("Genero: " , genero)
print("--------------------------------------------------")
print("Gracias por la informacion. Esperamos que disfrutes con Mi Red")
print()

#Finalmente, solicitamos un mensaje de prueba que sirva para publicar un estado del usuario.
mensaje = input("Ahora vamos a publicar tu primer mensaje. ¿Que piensas hoy? ")
print()
print("--------------------------------------------------")
print(nombre, "dice:", mensaje)
print("--------------------------------------------------")

#Ahora puedes practicar solicitando mas datos al usuario. Solo tienes que usar apropiadamente input() y print()
#1. Escribe 3 solicitudes de datos al usuario, por ejemplo sexo, numero de telefono, ciudad donde vive,
#   pais de nacimiento, direccion, etc. Guarda esos datos en variables del tipo, y finalmente escrÃ­belos en pantalla
#   utilizando print. Puedes agregar todas las lÃ­neas que necesites.