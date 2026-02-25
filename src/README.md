# Conversión de texto a minúsculas

---

## Objetivo

Implementar una función llamada `lowercase` que reciba un string como entrada y retorne una nueva cadena donde todos los caracteres alfabéticos estén convertidos a minúsculas.

Este ejercicio tiene como finalidad reforzar los siguientes conceptos fundamentales:

* Tipos de datos (`char`, `string`)
* Arreglos de caracteres
* Bucles `for`
* Estructuras condicionales `if`
* Manipulación de ASCII
* Operaciones bitwise
* Diseño de funciones

---

## Planteamiento del Problema

Se requiere desarrollar una función que transforme únicamente los caracteres alfabéticos mayúsculos (`A-Z`) en su equivalente en minúscula (`a-z`).

La función **NO debe utilizar funciones de librería** como:

* `tolower()`
* `strlwr()`
* Funciones equivalentes del lenguaje

---

## Especificación de Entradas

La función deberá recibir:

```c
char* input
```

### Restricciones de entrada:

1. El parámetro puede contener:

   * Letras mayúsculas `A-Z`
   * Letras minúsculas `a-z`
   * Números `0-9`
   * Símbolos especiales
   * Espacios

2. El string:

   * Debe estar correctamente terminado en `'\0'`
   * Puede tener longitud variable
   * Puede estar vacío (`""`)

3. No se evaluarán caracteres extendidos (acentos, UTF-8, etc.).
   Solo se evaluará ASCII estándar.

---

## Especificación de Salida

La función deberá retornar:

```c
char* output
```

### Condiciones de salida:

1. Todos los caracteres `A-Z` deben convertirse a `a-z`
2. Los demás caracteres deben permanecer sin modificación
3. El string resultante debe estar correctamente terminado en `'\0'`
4. No debe modificar memoria fuera del rango del string

---

## Reglas de Implementación

Desarrolla una función que implemente la conversión de mayúsculas a minúsculas de carácteres de tipo ASCII.

Puedes utilizar:

* Operaciones aritméticas
* Operaciones bitwise

No puedes utilizar:

* Funciones de `<ctype.h>`
* Funciones externas que realicen la conversión
* IA (Copilot, ChatGPT, Claude, etc)
* Internet o celular

---

## Especificación para Unit Testing

La función debe cumplir estrictamente el contrato.

> **No modifiques nada de la infraestructura, solamente agrega el código necesario dentro de la función.**

### Casos mínimos que deberán pasar:

| Entrada      | Salida Esperada |
| ------------ | --------------- |
| `"HELLO"`    | `"hello"`       |
| `"Hello123"` | `"hello123"`    |
| `"already"`  | `"already"`     |
| `"PiZzA"`    | `"pizza"`       |
| `"12345"`    | `"12345"`       |

---

## Infraestructura Base Proporcionada

Recibes el siguiente archivo base, solo debes implementar la lógica dentro del bloque `TODO`:

```c
/**
 * @brief uppercase ASCII characters to lowercase.
 *
 * @param input: pointer to null-terminated string
 * @return pointer to transformed string
 */
char* lowercase(char* input)
{
    char* output = input;
    /** 
     * TODO:
     *  Implement the algorithm here.
     *  - Iterate over the string
     *  - Detect uppercase letters
     *  - Convert to lowercase manually
     */ 

    return output;
}
```