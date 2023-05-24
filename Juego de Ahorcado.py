"""
Tarea Corta 4 Juego de Ahorcado
""" 
import random


IntentosMax= 7

def ahorcado():
    """Subrutina pricipal del jeugo de ahorcado 
    Entradas: ninguna 
    Salidas: el juego de ahorcado"""
    
    global IntentosMax
    limpiarPantalla()
    imprimirEntrada()
    continuar= True
    while continuar:
        textoOriginal= leerTextoOriginal()
        texto= preparar(textoOriginal)
        intentadas=""
        intentos=["❤","❤","❤","❤","❤","❤","❤"] 
        ronda=1
        while intentos!=[] and\
            not adivino(texto, intentadas):
            #limpiarPantalla()
            imprimirRonda(texto, intentadas, intentos, ronda)
            letraIntento= leerIntento(intentadas)
            if aciertaIntento(texto, letraIntento):
                imprimirMensajeAcierto()
            else:
                imprimirMensajeNoAcierto()
                intentos.pop()
            intentadas += letraIntento
            ronda+=1
        if adivino(texto, intentadas):
            imprimirMensajeVictoria(textoOriginal)
        else:
            imprimirMensajeDerrota(textoOriginal)
        continuar= leerJugarNuevamente()
    imprimirMensajeDespedida()
def limpiarPantalla():
    """subrutina que imprime lineas en blanco
    para limpear la pantalla
    Entradas: ninguna
    Salidas: 40 lineas en blanco
    """
    print("\n"*40)
def imprimirEntrada():
    """Funcion que genera un rotulo de vienvenida 
    Entradas: ninguna
    Salidas: mensaje
    """
    print(" ")
    print("   _   _  vienvenido a               _       ")
    print("  /_\ | |__   ___  _ __ ___ __ _  __| | ___  ")
    print(" //_\\| '_ \ / _ \| '__/ __/ _` |/ _` |/ _ \ ")
    print("/  _  \ | | | (_) | | | (_| (_| | (_| | (_) |")
    print("\_/ \_/_| |_|\___/|_|  \___\__,_|\__,_|\___/ ")
    print("                              Por E.Costaguta")
    print("  __")
    print("  |  ""--.--.._                                             __..    ,--.")
    print("  |       `.   -.""\_...-----..._   ,--. .--..-----.._.""|   |   /   /")
    print("  |_   _    \__   ).  \           _/_ |   \|  ||  ..    >  `.  |  /   /")
    print("    | |_.'   |   / ""`  \  ===/  ..|..  \     ||      <   `.    |/__")
    print("    `.      .    \ ,--   \-..-\   /\   /     ||  |>   )--   |    /    |")
    print("    |__..-'__||__\   |___\ __.:-.._..-'_|\___||____..-/  |__|--""____/")
    print("                           _______________________")
    print("                          /                      ,'")
    print("                         /      ___            ,'")
    print("                       /   _.-'  ,'        ,-'   /")
    print("                      / ,-' ,--.'        ,'   .'/")
    print("                     /.'     `.         '.  ,' /")
    print("                    /      ,-'       ,--','  /")
    print("                         ,'        ,'  ,'    /")
    print("                        ,-'      ,' .-'     /")
    print("                     ,-'                   /")
    print("                  ,:______________________/")
    print("")
    print("")
def leerTextoOriginal():
    """Funcion que leer de la consola la palabra a se
    adivinada y retorna como el resultaod leido
    Entrada: texto de la lista de palabras
    Salidas: texto de la lista de palabras
    """
    texto= ["goku","gohan","trunks","vegeta","broly","Shenron","piccolo","cell","freezer","bulma","pan","Bills","whis","jiren"]
    texto=random.choice(texto)
    #while not esTextoValido(texto):
        #print("EL texto solo puede tener letras y espacios")
        #texto= input("Ingrese la palabra a adivinar: ")
    return texto
def esTextoValido(texto):
    """Funcion booleana que decide si un str es un testo valido para adivinar
        estradas:texto(str)
        Salidas: True o False
    """
    if type(texto)!= str:
        raise Exception("El texto debe de ser un str")
    if texto=="":
        return False
    for letra in texto:
        if letra.lower() not in "aábcdeéfghiíjklmnñoópqrstuúvwxyz":
            return False
    return True 
def preparar(texto):
    """Convierte el texto a minusculas, sustituye acentos y elimina 
    espacios a inicio y al final.
    Entradas: texto a procesar
    Salidas: texto sin mayusculas ni acentos 
    """
    if type(texto)!=str:
        raise Exception("El texto debe de ser un str")
    texto=texto.lower()
    texto=texto.strip()
    texto=texto.replace("á","a")
    texto=texto.replace("é","e")
    texto=texto.replace("í","i")
    texto=texto.replace("ó","o")
    texto=texto.replace("ú","u")
    return texto
def adivino(texto,intentadas):
    """Funcion booleana que dice si el usuario adivino o no la palabra 
        Entradas: el texto y las letras que el usuario ya probo
        salidas: Ture o False 
    """
    if type(texto)!=str or type(intentadas)!=str:
        raise Exception("El texto debe de ser un str")
    if not esTextoValido(texto):
        raise Exception("El texto contiene caracteres invalidos")
    for letra in texto:
        if letra!=" ":
            if letra not in intentadas:
                return False
    return True 
def imprimirRonda(texto,intentadas,intentos, ronda):
    """Esta funcion imprime cada ronda de juego, las letras utilizadas, cantidad 
    de intentos fallidos y escribe el texto "enmascarado" 
    entradas: texto sin tildes ni acentos, intentadas, intentos fallidos y las ronda
    por la que va el juego 
    salidas: informacion de la ronda
    """
    print("Numero de Ronda", ronda)
    print("Letras Utilizadas", intentadas)
    print("Cantidad de intentos fallidos", intentos)
    print(enmascarar(texto,intentadas))
    print()
def enmascarar(texto, intentadas):
    """Retorna un str con un guion bajo por cada letra que no
    ha sido adivinada. si una letra del texto aparece en las letras
    inentadas entonces agrega aesa letra en lugar del guion. 
    Entradas: texto y las letras intentasdas
    """
    listaPalabras=texto.split()
    resultado=""
    for palabra in listaPalabras:
        for letra in palabra:
            if letra in intentadas:
                resultado+=letra+" "
            else:
                resultado+="_ "
        resultado+="- "
    return resultado[:-2]
def leerIntento(intentadas):
    '''Funcion que pide al usuario que escriba una 
    letra para adivinar si ya esta en las adivinadas
    Entradas: letras intentadas
    Salidas: str con la aletra elegida por el usuario
    '''
    print()
    letra=input("Digite una letra: ")
    letra= letra.lower()
    while len(letra)!= 1 or letra not in "abcdefghijklmnñopqrstuvwxyz"\
         or letra in intentadas:
        print("Ingrese una letra que todavia no haya intentado.")
        print ("estas son las que ha intentado: ",intentadas)
        letra=input("Digite una letra: ")
        letra=letra.lower()
    print()
    return letra
def aciertaIntento(texto,letra):
    """Funcion booleana que dice si un intento es correcto
     o no 
     Entradas: texto y letra que acaba de intentar
     salida: true o false
    """        
    return letra in texto

def imprimirMensajeAcierto():
    print("Esta es la letra correcta")
def imprimirMensajeNoAcierto():
    print("No es la letra correcta")
def imprimirMensajeVictoria(textoOriginal):
    print("Felicidades ha adivinado la palabra", textoOriginal)
    print(" __      ___      _             _               _   _ ")
    print(" \ \    / (_)    | |           (_)             | | | |")
    print("  \ \  / / _  ___| |_ ___  _ __ _  __ _  __ _  | | | |")
    print("   \ \/ / | |/ __| __/ _ \| '__| |/ _` |/ _` | | | | |")
    print("    \  /  | | (__| || (_) | |  | | (_| | (_| | |_| |_|")
    print("     \/   |_|\___|\__\___/|_|  |_|\__,_|\__,_| (_) (_)")
    print("")
    print()
def imprimirMensajeDerrota(textoOriginal):
    print("Derrota. EL texto que tenia que adivina era", textoOriginal)

def leerJugarNuevamente():
    """Funcion booleana que pregunta al usuario si quiere jugar de nuevo
    solo acepta s o n como respuesta
    entradas: ninguna
    Salidas: true si es una s false si es una n
    """
    print()
    respuesta=input("¿Quiere jugar una nueva partida?(S/N)")
    respuesta=respuesta.lower()
    while respuesta not in ["s","n"]:
        respuesta=input("Responda con S o N ¿Desea jugar de  nuevo?")
        respuesta=respuesta.lower()
    return respuesta=="s"
def imprimirMensajeDespedida():
    print("Gracias por jugar ahorcado.")
ahorcado()