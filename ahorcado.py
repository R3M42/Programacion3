def jugar():
    print ("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
    print ("Bienvenido al juego del ahorcado")
    print ("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
    
    palabra_secreta = "mandarina"
    letras_acertadas = ["_" for elemento in palabra_secreta]
    
    ahorcado = False
    acerto = False
    errores = 0 #Contador de errores
    
    print(letras_acertadas)
    while(not ahorcado and not acerto):
        entrada = input ("Ingrese una letra...")
        entrada = entrada.strip()                # elimina el espacion en blanco a la izquierda
        entrada = entrada.lower()                # convierte a letras minusculas
        
        if entrada in palabra_secreta:
            indice = 0
            for letra in palabra_secreta:
                if(entrada==letra):
                    letras_acertadas[indice] = letra

                indice = indice + 1
        else:
            errores += 1
            
        ahorcado = errores == 9
        acerto = "_" not in letras_acertadas
        print(letras_acertadas)
        
    if(acerto):
        print("Felicitaciones, ganaste!!")
    else:
        print("Lo siento, perdiste!!")
        

    print("Fin del juego")
    
if(__name__ == "__main__"):
    jugar()