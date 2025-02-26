# Enunciado del ejercicio

Se tienen dos palos de madera de longitudes `A` y `B`, respectivamente.  
Cada uno de ellos puede ser cortado en palos más cortos de longitudes enteras.

El objetivo es construir el cuadrado más grande posible.  
Para ello, debemos cortar los palos de manera que se obtengan **cuatro segmentos de la misma longitud** (se permiten sobras).

## Problema

Determinar la longitud del lado más largo del cuadrado que se puede formar con los palos dados.

Escribe una función en Python:

```python
def solution(A, B):
```

que, dados dos enteros A y B, devuelva la longitud del lado del cuadrado más grande que se puede obtener.
Si no es posible formar un cuadrado, la función debe retornar 0.

## Ejemplos

Entrada: `A = 10, B = 21`
Salida: `7`
Explicación: Podemos dividir el segundo palo en tres segmentos de longitud 7 y acortar el primero en 3 unidades.

Entrada: `A = 13, B = 11`
Salida: `5`
Explicación: Podemos cortar dos segmentos de longitud 5 de cada uno de los palos.

Entrada: `A = 2, B = 1`
Salida: `0`
Explicación: No es posible formar un cuadrado con los palos dados.

Entrada: `A = 1, B = 8`
Salida: `2`
Explicación: Podemos dividir el palo de longitud 8 en cuatro partes iguales.`

## Restricciones

-   A y B son enteros dentro del rango [1..1,000,000,000].
-   Se requiere un algoritmo eficiente.
