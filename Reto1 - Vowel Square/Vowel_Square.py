vocales =["a","A","e","E","i","I","o","O","u","U"]

def VowelSquare(strArr):
    for i, fila in enumerate(strArr):
        for j, letra in enumerate(fila):
            if letra in vocales:
                #Verficar que la ´posicion siguiente exista
                if ((i+1< len(strArr)) and (j+1<len(strArr[0]))):
                    #Verificacion de que se forme un vowel square
                    if((fila[j+1] in vocales) and (strArr[i+1][j] in vocales) and (strArr[i+1][j+1] in vocales)):
                        #Retorno de la posicion izquierda superior del vowel square
                        return str(i)+"-"+str(j)
    return "cuadrado no encontrado"

#Programa Principal
entrada = eval(input())
print(VowelSquare(entrada))