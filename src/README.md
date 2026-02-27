# Conversión de texto a mayúsculas

---

## Objetivo

Implementar una función llamada `uppercase` que reciba un string como entrada y retorne una nueva cadena donde todos los caracteres alfabéticos estén convertidos a mayúsculas.

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

Se requiere desarrollar una función que transforme únicamente los caracteres alfabéticos minúsculas (`a-z`) en su equivalente en mayúsculas (`A-Z`).

La función **NO debe utilizar funciones de librería** como:

* `toupper()`
* `strupr()`
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
return input
```

### Condiciones de salida:

1. Todos los caracteres `a-z` deben convertirse a `A-Z`
2. Los demás caracteres deben permanecer sin modificación
3. El string resultante debe estar correctamente terminado en `'\0'`
4. No debe modificar memoria fuera del rango del string

---

## Reglas de Implementación

Desarrolla una función que implemente la conversión de minúsculas a mayúsculas de carácteres de tipo ASCII.

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
| `"hello"`    | `"HELLO"`       |
| `"Hello123"` | `"HELLO123"`    |
| `"ALREADY"`  | `"ALREADY"`     |
| `"PiZzA"`    | `"PIZZA"`       |
| `"12345"`    | `"12345"`       |

---

## Infraestructura Base Proporcionada

Recibes el siguiente archivo base, solo debes implementar la lógica dentro del bloque `TODO`:

```c
/**
 * @brief lowercase ASCII characters to uppercase.
 *
 * @param input: pointer to null-terminated string
 * @return pointer to transformed string
 */
char* uppercase(char* input)
{
    /** 
     * TODO:
     *  Implement the algorithm here.
     *  - Iterate over the string
     *  - Detect lowercase letters
     *  - Convert to uppercase manually
     */ 

    return input;
}
```

---

# Tabla ASCII

| Dec | Hex  | Bin      | Char |
| --- | ---- | -------- | ---- |
| 65  | 0x41 | 01000001 | A    |
| 66  | 0x42 | 01000010 | B    |
| 67  | 0x43 | 01000011 | C    |
| 68  | 0x44 | 01000100 | D    |
| 69  | 0x45 | 01000101 | E    |
| 70  | 0x46 | 01000110 | F    |
| 71  | 0x47 | 01000111 | G    |
| 72  | 0x48 | 01001000 | H    |
| 73  | 0x49 | 01001001 | I    |
| 74  | 0x4A | 01001010 | J    |
| 75  | 0x4B | 01001011 | K    |
| 76  | 0x4C | 01001100 | L    |
| 77  | 0x4D | 01001101 | M    |
| 78  | 0x4E | 01001110 | N    |
| 79  | 0x4F | 01001111 | O    |
| 80  | 0x50 | 01010000 | P    |
| 81  | 0x51 | 01010001 | Q    |
| 82  | 0x52 | 01010010 | R    |
| 83  | 0x53 | 01010011 | S    |
| 84  | 0x54 | 01010100 | T    |
| 85  | 0x55 | 01010101 | U    |
| 86  | 0x56 | 01010110 | V    |
| 87  | 0x57 | 01010111 | W    |
| 88  | 0x58 | 01011000 | X    |
| 89  | 0x59 | 01011001 | Y    |
| 90  | 0x5A | 01011010 | Z    |
| 91  | 0x5B | 01011011 | [    |
| 92  | 0x5C | 01011100 | \    |
| 93  | 0x5D | 01011101 | ]    |
| 94  | 0x5E | 01011110 | ^    |
| 95  | 0x5F | 01011111 | _    |
| 96  | 0x60 | 01100000 | `    |
| 97  | 0x61 | 01100001 | a    |
| 98  | 0x62 | 01100010 | b    |
| 99  | 0x63 | 01100011 | c    |
| 100 | 0x64 | 01100100 | d    |
| 101 | 0x65 | 01100101 | e    |
| 102 | 0x66 | 01100110 | f    |
| 103 | 0x67 | 01100111 | g    |
| 104 | 0x68 | 01101000 | h    |
| 105 | 0x69 | 01101001 | i    |
| 106 | 0x6A | 01101010 | j    |
| 107 | 0x6B | 01101011 | k    |
| 108 | 0x6C | 01101100 | l    |
| 109 | 0x6D | 01101101 | m    |
| 110 | 0x6E | 01101110 | n    |
| 111 | 0x6F | 01101111 | o    |
| 112 | 0x70 | 01110000 | p    |
| 113 | 0x71 | 01110001 | q    |
| 114 | 0x72 | 01110010 | r    |
| 115 | 0x73 | 01110011 | s    |
| 116 | 0x74 | 01110100 | t    |
| 117 | 0x75 | 01110101 | u    |
| 118 | 0x76 | 01110110 | v    |
| 119 | 0x77 | 01110111 | w    |
| 120 | 0x78 | 01111000 | x    |
| 121 | 0x79 | 01111001 | y    |
| 122 | 0x7A | 01111010 | z    |
