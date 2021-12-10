import random
#vamos a realizar una version 2.0.1
#aqui vamos a trabajar en la linea de cabecera

# a la par se agrega una linea en master

# se pone un comentario adicional a linea cabecera
#aqui se intenta una cabecera 2

#se intenta un nuevo comentario desde master para hacer un merge con conflicto

#un nuevo intento de conflicto se genera en este momento

#aqui se intenta genera un conflicto con la version master

# la idea es generar conflicto en las diferentes lineas

#se cambia los numero aleatorios para generar conflictos

# en esta version se realiza una nueva cabecera donde no se tendra sistema de vidas

def run():
    numero_aleatorio = random.randint(1,120)
    numero_elegido = int(input("elige un numero del 1 al 120: "))

    contador = 1
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print ('busca un numero más grande')
            numero_elegido =int(input('elige otro numero: '))

        else:
            print ('Busca un numero más pequeño')
            numero_elegido =int(input('elige otro numero: '))
    print ('ganste')
    print ("el juego terminó")

if __name__=='__main__':
    run()