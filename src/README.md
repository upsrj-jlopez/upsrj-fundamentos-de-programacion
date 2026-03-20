# Práctica: Manejo de Archivos Binarios, Apuntadores y Modularidad

---

## 1. Objetivo

El objetivo de esta práctica es reforzar los siguientes conceptos fundamentales del lenguaje C:

* Uso de apuntadores.
* Manipulación de arreglos de bytes.
* Manejo de archivos binarios.
* Lectura y escritura de archivos con `fopen`, `fread` y `fwrite`.
* Procesamiento de datos a bajo nivel.
* Programación modular mediante archivos `.c` y `.h`.
* Compilación separada con Makefile.

El alumno deberá implementar una función que procese datos binarios correspondientes a una imagen y los transforme a escala de grises.

---

## 2. Estructura del Proyecto

```id="9ad2n8"
project/
├── inputs/
│   └── lena.bmp
├── build/
│   └── out/
│       └── lena.bmp
└── src/
    ├── makefile
    ├── main.c
    ├── fhndlr.c
    └── fhndlr.h
```

---

## 3. Descripción de la Asignación

El alumno deberá completar la implementación del archivo:

```id="r2x7il"
src/fhndlr.c
```

La función a implementar es:

```c id="2c4i9v"
/**
 * @brief Converts a BGR pixel to grayscale.
 *
 * @param pixel: pointer to 3-byte pixel (Blue, Green, Red)
 * @return void
 */
void grayscale(unsigned char* pixel);
```

Posteriormente, en:

```id="qbnk9y"
src/main.c
```

El programa deberá:

1. Abrir el archivo `../inputs/lena.bmp` utilizando `fopen` en modo binario.
2. Leer los primeros 54 bytes correspondientes al header de la imagen.
3. Validar que el archivo sea un BMP (caracteres `'B'` y `'M'`).
4. Copiar el header al archivo de salida.
5. Leer los datos de la imagen en bloques de 3 bytes (un píxel).
6. Procesar cada píxel utilizando la función `grayscale`.
7. Escribir los píxeles procesados en el archivo de salida.
8. Generar una nueva imagen en:

```id="1y0ozc"
../build/out/lena.bmp
```

---

## 4. Conceptos Teóricos

### 4.1 ¿Qué es un Array en C?

Un array (arreglo) es una colección de elementos del mismo tipo almacenados en posiciones contiguas de memoria.

Ejemplo:

```c id="3r81hf"
unsigned char pixel[3];
```

En este caso, el arreglo representa un píxel en formato BMP:

```id="z0yg8g"
pixel[0] → Blue
pixel[1] → Green
pixel[2] → Red
```

Los arreglos permiten manipular directamente los datos de la imagen byte por byte.

---

### 4.2 ¿Qué es fopen?

`fopen` es una función de la biblioteca estándar `<stdio.h>` que permite abrir archivos.

Sintaxis general:

```c id="f0t6ny"
FILE *fopen(const char *filename, const char *mode);
```

Parámetros:

* `filename`: ruta del archivo.
* `mode`: modo de apertura.

Modos utilizados en esta práctica:

* `"rb"` → lectura en binario.
* `"wb"` → escritura en binario.

Ejemplo:

```c id="r9whf1"
FILE *file = fopen("../inputs/lena.bmp", "rb");

if (file == NULL) {
    printf("Error al abrir el archivo.\n");
}
```

Es responsabilidad del programador cerrar el archivo con:

```c id="y1knl7"
fclose(file);
```

---

### 4.3 ¿Qué es fread?

`fread` es una función de `<stdio.h>` que permite leer bloques de datos desde un archivo.

Sintaxis:

```c id="u6exey"
size_t fread(void *ptr, size_t size, size_t count, FILE *stream);
```

Parámetros:

* `ptr`: apuntador al buffer donde se almacenarán los datos.
* `size`: tamaño de cada elemento en bytes.
* `count`: número de elementos a leer.
* `stream`: archivo de entrada.

Ejemplo:

```c id="1b6v6o"
fread(header, sizeof(char), 54, input);
```

Esto lee 54 bytes del archivo y los guarda en `header`.

También puede usarse para leer píxeles:

```c id="1b67w5"
fread(pixel, sizeof(char), 3, input);
```

---

### 4.4 ¿Qué es fwrite?

`fwrite` es una función de `<stdio.h>` que permite escribir bloques de datos en un archivo.

Sintaxis:

```c id="zlfq3q"
size_t fwrite(const void *ptr, size_t size, size_t count, FILE *stream);
```

Parámetros:

* `ptr`: apuntador a los datos a escribir.
* `size`: tamaño de cada elemento en bytes.
* `count`: número de elementos a escribir.
* `stream`: archivo de salida.

Ejemplo:

```c id="8e3e6g"
fwrite(header, sizeof(char), 54, output);
```

Para píxeles:

```c id="h5a9z5"
fwrite(pixel, sizeof(char), 3, output);
```

---

### 4.5 ¿Cuál es la diferencia entre `char` y `unsigned char`?

En C, el tipo `char` puede comportarse como **signed** o **unsigned**, dependiendo del compilador.

#### 🔹 `char` (signed en muchos sistemas)

* Rango típico: **-128 a 127**
* Puede representar valores negativos
* No es adecuado para datos binarios puros

Ejemplo:

```c id="h0pj9m"
char value = 200;  /* Puede interpretarse como un número negativo */
```

---

#### 🔹 `unsigned char`

* Rango: **0 a 255**
* Representa correctamente valores de bytes
* Es el tipo recomendado para manejo de archivos binarios

Ejemplo:

```c id="p9f3l8"
unsigned char value = 200;  /* Se mantiene como 200 */
```

---

#### ⚠️ Importancia en esta práctica

Los píxeles de una imagen BMP están definidos en el rango **0–255**.

Si se utiliza `char`:

* Los valores pueden volverse negativos
* Se generan errores en los cálculos
* La imagen puede verse incorrecta (invertida o distorsionada)

Por esta razón, en esta práctica se debe utilizar:

```c id="z0v1s9"
unsigned char pixel[3];
```

---

### 4.6 Estructura básica de un archivo BMP

Un archivo BMP de 24 bits está compuesto por:

1. **Header (54 bytes)**
   Contiene metadatos como tamaño, ancho y alto.

2. **Datos de píxeles**
   Cada píxel se representa con 3 bytes en formato:

```id="2ztj5b"
[Blue][Green][Red]
```

En esta práctica:

* El header se copia sin modificaciones.
* Solo se procesan los datos de píxeles.

---

## 5. Requisitos Técnicos

* No usar `struct`.
* No usar memoria dinámica (`malloc`).
* Trabajar únicamente con arreglos y apuntadores.
* Usar exclusivamente:

  * `fopen`
  * `fread`
  * `fwrite`
* Utilizar tipo `unsigned char` para el manejo de píxeles.
* El programa debe compilar y ejecutarse sin errores ni advertencias con:

```bash id="k0wrnl"
make clean all run
```

---

## 6. Pruebas de requerimientos

Usa las macros de Visual Studio Code.

```bash id="a9l2h6"
CTRL + SHIFT + B
```

---

**Autor:** Jesús Salvador López Ortega
[LinkedIn](https://www.linkedin.com/in/jesus-salvador-lopez-ortega/) | [GitHub](https://github.com/chucholoport) | [Correo Institucional](mailto:jlopez@upsrj.edu.mx)