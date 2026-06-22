# Fundamentos de Python

Guía de conceptos básicos para empezar con Python.

---

## Contenido

### 1. Hello World

El punto de partida clásico. Usamos `print()` para mostrar mensajes en consola.

```python
print("Hello, World!")
```

- `\n` para saltos de línea.
- `;` para múltiples statements en una línea (poco usado).
- Comentarios con `#` (una línea) o `""" """` (multi-línea).

### 2. Variables

Las variables se crean al asignarles un valor. No requieren declaración de tipo.

```python
x = 5
y = "John"
```

**Tipado dinámico:** Python infiere el tipo automáticamente.

**Casting:** Forzar un tipo con `str()`, `int()`, `float()`.

**Case sensitive:** `a` y `A` son variables distintas.

**Asignación múltiple:**
```python
x, y, z = "Orange", "Banana", "Cherry"
x = y = z = "Orange"
```

**Unpacking:** Desempaquetar colecciones en variables.
```python
fruits = ["Apple", "Banana", "Cherry"]
x, y, z = fruits
```

**Scope:** Variables globales (fuera de funciones) y locales (dentro de funciones).

### 3. Tipos de Datos

| Tipo | Clase | Ejemplo |
|------|-------|---------|
| int | `int` | `5` |
| float | `float` | `3.14` |
| complex | `complex` | `1 + 2j` |
| str | `str` | `"Hola"` |
| bool | `bool` | `True` / `False` |

**Operaciones con booleanos:** `and`, `or`, `not`.

**Strings:** Soportan indexación, slicing (`[::-1]` para invertir) y métodos como `.join()`.

### 4. Operadores

- **Aritméticos:** `+`, `-`, `*`, `/`, `//`, `%`, `**`
- **Comparación:** `==`, `!=`, `>`, `<`, `>=`, `<=`
- **Lógicos:** `and`, `or`, `not`
- **Asignación:** `=`, `+=`, `-=`, `*=`, `/=`
- **Pertenencia:** `in`, `not in`
- **Identidad:** `is`, `is not`

### 5. Entrada y Salida

```python
nombre = input("Ingresa tu nombre: ")
print(f"Hola, {nombre}!")
```

### 6. Convenciones

- Nombres de variables en `snake_case`.
- Constantes en `UPPER_CASE`.
- Indentación de 4 espacios (obligatoria).
- PEP 8 como guía de estilo.
