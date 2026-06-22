# Embedded Functions (Funciones Incorporadas y Estructuras de Control)

Guía de estructuras de control, funciones built-in y manejo de errores en Python.

---

## Contenido

### 1. Estructuras Condicionales: `if`, `elif`, `else`

```python
x = 10
if x > 5:
    print("x es mayor que 5")
elif x == 5:
    print("x es igual a 5")
else:
    print("x es menor que 5")
```

- No requiere paréntesis obligatorios.
- `elif` en lugar de `else if`.
- Indentación define los bloques.

### 2. Bucles

#### `for`

Itera sobre secuencias (listas, strings, rangos, etc.).

```python
for i in range(5):
    print(i)

for letra in "Python":
    print(letra)

frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)
```

#### `while`

Repite mientras una condición sea verdadera.

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

**Control de bucles:**
- `break` → sale del bucle.
- `continue` → salta a la siguiente iteración.
- `else` → se ejecuta si el bucle no fue interrumpido por `break`.

### 3. La sentencia `with` (Context Managers)

Manejo automático de recursos (archivos, conexiones, etc.).

```python
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
# El archivo se cierra automáticamente al salir del bloque
```

### 4. Funciones Built-in Comunes

Python incluye decenas de funciones incorporadas. Las más usadas:

| Función | Descripción |
|---------|-------------|
| `print()` | Imprime en consola |
| `input()` | Lee entrada del usuario |
| `len()` | Devuelve longitud de un objeto |
| `type()` | Devuelve el tipo de un objeto |
| `int()`, `float()`, `str()` | Casting entre tipos |
| `range()` | Genera secuencias numéricas |
| `enumerate()` | Itera con índice y valor |
| `zip()` | Combina múltiples iterables |
| `map()` | Aplica función a cada elemento |
| `filter()` | Filtra elementos según condición |
| `sorted()` | Ordena un iterable |
| `sum()`, `min()`, `max()` | Operaciones matemáticas básicas |
| `any()`, `all()` | Evaluación de condiciones en iterables |
| `isinstance()` | Verifica el tipo de un objeto |

#### Ejemplos

```python
# enumerate
for i, fruta in enumerate(["manzana", "banana", "cereza"]):
    print(f"{i}: {fruta}")

# zip
nombres = ["Ana", "Juan", "Luis"]
edades = [25, 30, 22]
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")

# map
numeros = [1, 2, 3, 4]
cuadrados = list(map(lambda x: x**2, numeros))

# filter
pares = list(filter(lambda x: x % 2 == 0, numeros))
```

### 5. Comprehensions

Forma concisa de crear secuencias.

```python
# List comprehension
cuadrados = [x**2 for x in range(10)]

# Dict comprehension
pares = {x: x**2 for x in range(5)}

# Set comprehension
impares = {x for x in range(10) if x % 2 != 0}
```

### 6. Manejo de Errores: `try`, `except`, `finally`

```python
try:
    x = int(input("Ingresa un número: "))
    resultado = 10 / x
    print(f"Resultado: {resultado}")
except ValueError:
    print("Eso no es un número válido")
except ZeroDivisionError:
    print("No se puede dividir entre cero")
except Exception as e:
    print(f"Error inesperado: {e}")
else:
    print("Todo salió bien")
finally:
    print("Esto se ejecuta siempre")
```

### 7. Funciones Lambda

Funciones anónimas de una sola línea.

```python
doble = lambda x: x * 2
print(doble(5))  # 10
```

### 8. Operador Ternario

```python
edad = 18
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
```
