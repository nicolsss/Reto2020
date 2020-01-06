# Reto 1 - Vowel Square
En esto reto se debe determinar si dentro de una matriz existe una matriz cuadrada 2x2 de vocales.

## Funcionamiento
Se tiene la fución VowelSquare(strArr) donde el argumento recibido es una matriz 2D llena con letras del abecedario y la función determina si existe una amtriz cuadrada de 2x2. Por ejemplo si strArr es  ["abcd", "eikr", "oufj"] la matriz se verá así:
```
[[a b c d]
 [e i k r]
 [o u f j]]
```
Dentro de la matriz hay un cuadrado de vocales de 2x2 que comienza en la segunda fila y la primera columna, ei, ou. Por lo que el programa debería devolver la posición superior izquierda del cuadrado. Si no se encuentran un caudrado de vocales entonces la función debe retornar "Cuadrado no encontado".

## Ejemplos
```
Input: ["aqrst", "ukaei", "ffooo"]
Output: 1-2
```
```
Input: ["gg", "ff"]
Output: Cuadrado no encontado
```

### Información adicional
Lenguaje a utilizar:
```
Python
```

Link del Reto:
```
https://coderbyte.com/editor/Vowel%20Square:Python3
```