## Historia

La PyConES 2026 no es solo código. También es arte.

El equipo de diseño ha decorado todo el recinto con figuras geométricas gigantes inspiradas en los logos de las librerías más famosas de Python. Triángulos de NumPy. Cuadrados de Pandas. Por todas partes.

Pero justo antes de la inauguración, el equipo de impresión llama con malas noticias: han perdido las medidas exactas de cada figura y necesitan recalcular los **perímetros** para saber cuánto material de borde necesitan comprar.

Por suerte, alguien guardó un fichero con el nombre de cada figura y sus medidas. Solo falta el programa que lo procese.

El editor está abierto. El proveedor espera al teléfono.

## Enunciado

Dada una figura geométrica y sus medidas, calcula su **perímetro**.

Las figuras posibles son:

- `triangulo a b c` — triángulo con lados **a**, **b** y **c**
- `cuadrado l` — cuadrado con lado **l**

## Formato de entrada

Una única línea con el nombre de la figura seguido de sus medidas:

```
figura medida1 [medida2] [medida3]
```

## Constraints

- La figura será siempre una de: `triangulo`, `cuadrado`
- Todas las medidas son enteros positivos
- 1 ≤ medidas ≤ 1.000

## Formato de salida

Un único entero con el perímetro de la figura.

## Ejemplos

**Ejemplo 1**