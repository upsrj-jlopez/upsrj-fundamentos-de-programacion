#include <stdio.h>
#include <stdlib.h>
#include "fhndlr.h"

#define INPUT_FILE        "../inputs/lorem.txt"
#define LOWER_OUTPUT_FILE "../inputs/lower.txt"
#define UPPER_OUTPUT_FILE "../inputs/upper.txt"
#define CAPTL_OUTPUT_FILE "../inputs/capitalize.txt"

int main(void) {

    /* Reads input file content */
    FILE* input = fopen(INPUT_FILE, "r");
    
    if (input == NULL) {
        perror("unable to read file.");
        return 1;
    }

    /* Reads lower output file content */
    FILE* lower_output = fopen(LOWER_OUTPUT_FILE, "w");

    if (lower_output == NULL) {
        perror("unable to open lower output file");
        fclose(input);
        return 1;
    }

    /* Reads upper output file content */
    FILE* upper_output = fopen(UPPER_OUTPUT_FILE, "w");

    if (upper_output == NULL) {
        perror("unable to open upper output file");
        fclose(input);
        fclose(lower_output);
        return 1;
    }

    /* Reads capitalized output file content */
    FILE* captl_output = fopen(CAPTL_OUTPUT_FILE, "w");

    if (captl_output == NULL) {
        perror("unable to open capitalize output file");
        fclose(input);
        fclose(lower_output);
        fclose(upper_output);
        return 1;
    }

    /* Data buffer for file content manipulation */
    char buffer[1024];  

    while (fgets(buffer, sizeof(buffer), input) != NULL) {
        
        lowercase(buffer);
        fputs(buffer, lower_output);

        uppercase(buffer);
        fputs(buffer, upper_output);

        capitalize(buffer);
        fputs(buffer, captl_output);
    }

    /* Close files (Important to avoid memory leaks) */
    fclose(input);
    fclose(lower_output);
    fclose(upper_output);
    fclose(captl_output);

    return 0;
}