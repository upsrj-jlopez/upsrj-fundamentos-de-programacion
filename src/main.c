#include <stdio.h>
#include "fhndlr.h"

#define HEADER 54
#define PIXEL 3

#define INPUT_BMP "../inputs/lena.bmp"
#define OUTPUT_BMP "../build/out/lena.bmp"

int main()
{
    FILE *input = NULL;
    FILE *output = NULL;

    unsigned char header[HEADER];
    unsigned char pixel[PIXEL];

    /* Open files */
    input = fopen(INPUT_BMP, "rb");
    if (input == NULL)
    {
        printf("Error opening input file\n");
        return -1;
    }

    output = fopen(OUTPUT_BMP, "wb");
    if (output == NULL)
    {
        printf("Error opening output file\n");
        fclose(input);
        return -1;
    }

    /* Read and copy header */
    fread(header, sizeof(unsigned char), 54, input);

    if (header[0] != 'B' || header[1] != 'M')
    {
        printf("Not a valid BMP file\n");
        fclose(input);
        fclose(output);
        return -1;
    }

    fwrite(header, sizeof(unsigned char), 54, output);

    /* Process pixel data using while */
    while (fread(pixel, sizeof(unsigned char), 3, input) == 3)
    {
        grayscale(pixel);
        /* Write pixel */
        fwrite(pixel, sizeof(unsigned char), 3, output);
    }

    fclose(input);
    fclose(output);

    printf("Conversion completed successfully\n");

    return 0;
}