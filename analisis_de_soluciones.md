# Análisis de soluciones

## 1. Hello PyConES

Para resolver este problema solo hay que escribir en la salida estándar el texto
`Hello, PyConES!` usando `print`. No hay entrada que leer. La salida debe ser
exacta: respetar mayúsculas, la coma, el espacio y el signo de exclamación (15 caracteres).

## 2. PyRoom to Grow

Cada expansión duplica la capacidad de la sala, que empieza con 1 asiento, así que
después de `n` expansiones hay 2ⁿ asientos. El problema se reduce a calcular 2 elevado a `n`.

Como `0 ≤ n ≤ 30`, el resultado máximo es 2³⁰ = 1 073 741 824, un valor pequeño para Python, así que hay varias formas válidas:

1. **Ciclo:** empezar con `1` y multiplicar por 2, `n` veces. Es la más directa.
2. **Operador de potencia:** `2 ** n`.
3. **Desplazamiento de bits:** `1 << n`, que equivale a multiplicar por 2 `n` veces.

Caso borde: con `n = 0` no hay expansiones y la respuesta es `1`.

## 3. Pythonic Art

La entrada es una única línea con el nombre de la figura (`triangle` o `square`)
seguido de sus medidas. Hay que leerla, separarla en palabras y convertir las
medidas a enteros. Según el nombre de la figura se aplica la fórmula del perímetro:

- **`triangle a b c`:** el perímetro es la suma de los tres lados, `a + b + c`.
- **`square l`:** el perímetro es cuatro veces el lado, `4 * l`.

## 4. Python in the Air

Hay que contar cuántas veces aparece la subcadena `Python` en el string dado,
respetando las mayúsculas y minúsculas. Como el string tiene como máximo 100,000
caracteres y el patrón solo 6, la fuerza bruta es suficiente: no hace falta un
algoritmo más complejo como KMP o uno basado en hash.

Hay dos formas sencillas de hacerlo:

1. **Método `count`:** `s.count("Python")` devuelve directamente el número de
   apariciones.
2. **Ciclo por posiciones:** recorrer cada posición `i` del string y comprobar si
   la subcadena de 6 caracteres que empieza en `i` es igual a `Python`, sumando 1
   al contador cuando coincida.

`count` cuenta apariciones sin solapamiento, pero aquí da igual: `Python` no puede
solaparse consigo mismo, así que ambas opciones dan el mismo resultado.

## 5. PyCoffee

Hay que encontrar el nombre que más veces aparece en la lista y mostrarlo junto
con su número de apariciones. Si varios nombres empatan, gana el que va primero
en orden alfabético, comparando los nombres como texto simple (por eso `dev10`
va antes que `dev2`).

Como `n ≤ 100,000`, basta con una solución de O(n) o de O(n log n). Hay dos
formas sencillas de hacerlo:

1. **Diccionario de conteo:** recorrer la lista y guardar en un diccionario
   cuántas veces aparece cada nombre. Después se elige el nombre con más
   apariciones y, en caso de empate, el menor alfabéticamente.
2. **Ordenar la lista:** al ordenar los nombres, los iguales quedan juntos, así que
   solo hay que recorrer la lista llevando la cuenta de la racha actual de nombres
   iguales y guardar el nombre con la racha más larga. Como la lista está en orden
   alfabético, el desempate sale solo: basta con actualizar la respuesta únicamente
   cuando la racha sea **estrictamente mayor** que la mejor encontrada, de modo que
   ante un empate se conserva el nombre que va primero alfabéticamente.

## 6. Always in PySync

Los dos ciclos coinciden en los minutos que son múltiplos de `a` y de `b` a la vez,
así que el primer minuto mayor que 0 en el que se alinean es el **mínimo común
múltiplo** (mcm) de `a` y `b`.

Como `1 ≤ a, b ≤ 1000`, el resultado es como máximo 999 000 (cuando `a` y `b` son
coprimos), un valor pequeño para Python. Hay varias formas válidas de calcularlo:

1. **Fuerza bruta:** recorrer los múltiplos de `a` (`a`, `2a`, `3a`, ...) hasta
   encontrar el primero que sea divisible por `b`. Como a lo sumo hay que probar `b`
   múltiplos, son como mucho 1000 iteraciones, así que es más que suficiente.
2. **Fórmula con el mcd:** usar la relación `mcm(a, b) = a * b / mcd(a, b)`, donde el
   máximo común divisor se obtiene con `math.gcd` (o con el algoritmo de Euclides).
   Es la opción más corta y la más estándar. Conviene escribir `a * b // gcd(a, b)`,
   con división entera, para que el resultado sea un `int` y no un `float`.

## 7. The PyRate Radio

Es un cifrado César: cada letra inglesa se desplaza `k` posiciones en el alfabeto
y vuelve al principio al pasar de la `z`. Las mayúsculas siguen siendo mayúsculas,
las minúsculas siguen siendo minúsculas y cualquier otro carácter (dígitos,
espacios, signos de puntuación, tildes, `ñ`) se deja igual.

La clave es que `k` puede llegar a `10^6`, pero el alfabeto tiene solo 26 letras,
así que desplazar `k` posiciones es lo mismo que desplazar `k % 26`. Con `len(S) ≤ 500`
basta con recorrer el texto una vez, carácter por carácter, y transformar cada
letra. Hay varias formas de hacerlo:

1. **Alfabeto como cadena:** guardar `'abcdefghijklmnopqrstuvwxyz'` y su versión en
   mayúsculas. Para cada carácter `c`, si está en uno de los alfabetos se busca su
   posición `idx` con `find` y se toma la letra en `(idx + k) % 26`. El `% 26` se
   encarga del desbordamiento, así que no hace falta reducir `k` antes.
2. **Aritmética con `ord` y `chr`:** en lugar de buscar la posición en una cadena,
   se calcula con códigos de carácter. Para una letra minúscula `c`, su posición en
   el alfabeto es `ord(c) - ord('a')`; se le suma `k`, se aplica `% 26` y se
   reconstruye la letra con `chr(ord('a') + (ord(c) - ord('a') + k) % 26)`. Para las
   mayúsculas se hace lo mismo con `'A'`. Aquí hay que comprobar que `c` está en el
   rango `'a' <= c <= 'z'` o `'A' <= c <= 'Z'`. Es más corto que el método
   anterior y no necesita guardar los alfabetos.
