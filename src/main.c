#include <stdio.h>

/** @brief archivo de salida */
#define OUTPUT_FILE "../build/out/pyramid.txt"

/** @brief altura de la piramide */
#define HEIGHT 6
/** @brief ancho de la piramide */
#define WIDTH  11

int main()
{
    
    FILE* file = fopen(OUTPUT_FILE, "w");
    
    /** 
     * @brief buffer para capturar linea de texto.
     * @details ancho (11) + '\0' (1) 
     */
    char line[WIDTH + 1];

    /** @details iteramos por filas y columnas */
    for (int i = 0; i < HEIGHT; i++) {
        
        for (int j = 0; j < WIDTH; j++) {

            /** @details llenamos el buffer "line" con lo que corresponda */
            if (j <= WIDTH / 2 + i &&
                j >= WIDTH / 2 - i) 
                line[j] = '*';
            else 
                line[j] = ' ';

        }

        /** @details escribimos en el archivo de salida */
        fprintf(file, "%s\n", line);

    }

    fclose(file);

    return 0;
}