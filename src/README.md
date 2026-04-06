# Remedial: Generación de Archivo de Texto

## 1. Objetivo

El objetivo de esta práctica es reforzar los siguientes conceptos fundamentales del lenguaje C:

* Manejo de archivos de texto.
* Uso de `fopen`, `fprintf` y `fclose`.
* Manipulación básica de salida formateada.
* Organización de código en un proyecto estructurado.
* Compilación mediante Makefile.

El alumno deberá generar un archivo de salida que contenga una pirámide de asteriscos con una base de 11 y altura de 6 a partir de la primer linea:

```sh
1|     *
2|    ***
3|   *****
4|  *******
5| *********
6|***********
7|
```

---

## 2. Estructura del Proyecto

```
project/
├── build/
│   └── out/
│       └── pyramid.txt
└── src/
    ├── makefile
    └── main.c
```

---

## 3. Descripción de la Asignación

El alumno deberá completar la implementación del archivo:

```
src/main.c
```

El programa deberá:

1. Crear o abrir un archivo de salida utilizando `fopen`.
2. Generar una pirámide de asteriscos (`*`) con una **base de 11 y altura de 6**.
3. Escribir el resultado en el archivo de salida.
4. Guardar el archivo en la siguiente ruta:

```
../build/out/pyramid.txt
```

---

## 4. Conceptos Teóricos

### 4.1 ¿Qué es fopen?

`fopen` es una función de la biblioteca estándar `<stdio.h>` que permite abrir archivos.

Sintaxis:

```c
FILE *fopen(const char *filename, const char *mode);
```

Modo utilizado en esta práctica:

* `"w"` → escritura en archivo de texto

Ejemplo:

```c
FILE *file = fopen("../build/out/pyramid.txt", "w");

if (file == NULL) {
    printf("Error al abrir el archivo.\n");
}
```

---

### 4.2 ¿Qué es fprintf?

`fprintf` permite escribir texto formateado en un archivo.

Sintaxis:

```c
int fprintf(FILE *stream, const char *format, ...);
```

Ejemplo:

```c
fprintf(file, "Hola mundo\n");
```

---

### 4.3 ¿Qué es fclose?

`fclose` se utiliza para cerrar un archivo abierto.

Sintaxis:

```c
int fclose(FILE *stream);
```

Ejemplo:

```c
fclose(file);
```

---

## 5. Requisitos Técnicos

* El archivo generado debe contener una pirámide con una **base de 11 y altura de 6**.
* El archivo debe guardarse en:

```
../build/out/pyramid.txt
```

* El programa debe compilar y ejecutarse sin errores ni advertencias con:

```bash
make clean all run
```

---

## 6. Pruebas de requerimientos

Usa las macros de Visual Studio Code:

```bash
CTRL + SHIFT + B
```

> **Nota:** Al completar los requerimientos, muestra al profesor tu entrega sin errores. No se requiere hacer commits.

---

**Autor:** Jesús Salvador López Ortega

[LinkedIn](https://www.linkedin.com/in/jesus-salvador-lopez-ortega/) | [GitHub](https://github.com/chucholoport) | [Correo Institucional](mailto:jlopez@upsrj.edu.mx)
