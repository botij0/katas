# Problema: Asignación de alturas a rascacielos

Se te da un array `A` de `N` enteros, que representan las alturas máximas de `N` rascacielos a construir. Tu tarea es especificar las alturas reales de los rascacielos, cumpliendo con las siguientes condiciones:

-   La altura del rascacielos en la posición `K` debe ser positiva y no mayor que `A[K]`.
-   No puede haber dos rascacielos con la misma altura.
-   La suma total de las alturas de los rascacielos debe ser la máxima posible.

## Implementación

Debes escribir una función en Java:

```python
class Solution:
    def solution(self, A: List[int]) -> List[int]:
```

Dicha función, dado un array `A` de `N` enteros, debe retornar un array `B` de `N` enteros donde `B[K]` representa la altura asignada al rascacielos en la posición `K`, cumpliendo con las condiciones mencionadas.

Si hay múltiples soluciones posibles, la función puede devolver cualquiera de ellas. Se garantiza que siempre es posible construir todos los rascacielos cumpliendo con los requisitos.

## Ejemplos

Entrada: `A = [1, 2, 3]`

Salida: `[1, 2, 3] `

---

Entrada: `A = [9, 4, 3, 7, 7] `

Salida: `[9, 4, 3, 7, 6] `

---

Entrada: `A = [2, 5, 4, 5, 5]   `

Salida: `[1, 2, 3, 4, 5]  `

## Restricciones

-   `N` es un entero en el rango `[1..50,000]`.
-   Cada elemento de `A` es un entero en el rango `[1..1,000,000,000]`.
-   Siempre existe una solución válida para cada entrada dada.
