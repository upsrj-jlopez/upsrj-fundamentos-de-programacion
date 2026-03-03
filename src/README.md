# Práctica: Manejo de Archivos, Apuntadores y Modularidad

---

## 1. Objetivo

El objetivo de esta práctica es reforzar los siguientes conceptos fundamentales del lenguaje C:

* Uso de apuntadores.
* Manejo de cadenas de caracteres (strings) terminadas en `\0`.
* Uso de arreglos.
* Apertura y lectura de archivos con `fopen`.
* Programación modular mediante archivos `.c` y `.h`.
* Compilación separada con Makefile.

El alumno deberá implementar funciones de transformación de texto y utilizarlas para procesar el contenido de un archivo.

---

## 2. Estructura del Proyecto

```
project/
├── inputs/
│   └── lorem.txt
└── src/
    ├── makefile
    ├── main.c
    ├── fhndlr.c
    └── fhndlr.h
```

---

## 3. Descripción de la Asignación

El alumno deberá completar la implementación del archivo:

```
src/fhndlr.c
```

Las funciones a implementar son:

```c
/**
 * @brief uppercase ASCII characters to lowercase.
 *
 * @param input: pointer to null-terminated string
 * @return pointer to transformed string
 */
char* lowercase(char* input); 

/**
 * @brief lowercase ASCII characters to uppercase.
 *
 * @param input: pointer to null-terminated string
 * @return pointer to transformed string
 */
char* uppercase(char* input);

/**
 * @brief ASCII characters capitalization.
 *
 * @param input: pointer to null-terminated string
 * @return pointer to transformed string
 */
char* capitalize(char* input);
```

Posteriormente, en:

```
src/main.c
```

El programa deberá:

1. Abrir el archivo `../inputs/lorem.txt` utilizando `fopen`.
2. Leer su contenido.
3. Procesarlo utilizando las funciones declaradas en `fhndlr.h`.
4. Generar un archivo con el texto de entrada modificado por cada función.

---

## 4. Conceptos Teóricos

### 4.1 ¿Qué es un Array en C?

Un array (arreglo) es una colección de elementos del mismo tipo almacenados en posiciones contiguas de memoria.

Ejemplo:

```c
int numeros[5] = {1, 2, 3, 4, 5};
```

En memoria:

```
numeros[0]
numeros[1]
numeros[2]
numeros[3]
numeros[4]
```

Cada elemento puede accederse mediante su índice.

En el caso de las cadenas en C, un string es un arreglo de caracteres terminado en el carácter nulo `\0`.

Ejemplo:

```c
char texto[] = "Hola";
```

En memoria realmente se almacena como:

```
'H' 'o' 'l' 'a' '\0'
```

Por esta razón, las funciones que reciben `char*` trabajan directamente sobre un arreglo de caracteres mediante apuntadores.

---

### 4.2 ¿Qué es fopen?

`fopen` es una función de la biblioteca estándar `<stdio.h>` que permite abrir archivos.

Sintaxis general:

```c
FILE *fopen(const char *filename, const char *mode);
```

Parámetros:

* `filename`: ruta del archivo.
* `mode`: modo de apertura.

Modos comunes:

* `"r"`  → lectura.
* `"w"`  → escritura (sobrescribe).
* `"a"`  → escritura al final.
* `"r+"` → lectura y escritura.

Ejemplo:

```c
FILE *file = fopen("../inputs/lorem.txt", "r");

if (file == NULL) {
    printf("Error al abrir el archivo.\n");
}
```

`fopen` devuelve un apuntador a tipo `FILE`.
Si ocurre un error, devuelve `NULL`.

Es responsabilidad del programador cerrar el archivo con:

```c
fclose(file);
```

---

## 5. Requisitos Técnicos

* No usar funciones de transformación como `toupper()` o `tolower()`.
* Trabajar únicamente con valores ASCII.
* Las funciones deben modificar la cadena usando apuntadores.
* El programa debe compilar y correr sin errores ni advertencias con:

```bash
make clean all run
```

## 6. Pruebas de requerimientos

Usa las macros de Visual Studio Code.

```bash
CTRL + SHIFT + B
```

---

**Autor:** Jesús Salvador López Ortega
[LinkedIn](https://www.linkedin.com/in/jesus-salvador-lopez-ortega/) | [GitHub](https://github.com/chucholoport) | [Correo Institucional](mailto:jlopez@upsrj.edu.mx)