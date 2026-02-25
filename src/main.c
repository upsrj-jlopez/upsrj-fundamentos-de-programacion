#include <stdio.h>
#include <string.h>

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

int main(void)
{
#ifdef UNIT_TEST

    /* Test mode: read input from stdin */
    char buffer[256];

    if (fgets(buffer, sizeof(buffer), stdin) == NULL)
    {
        return 1;
    }

    /* Remove trailing newline if present */
    buffer[strcspn(buffer, "\n")] = '\0';

    char* result = lowercase(buffer);

    printf("%s", result);

#else

    /* Normal execution mode */
    char text[] = "HELLO World 123!";

    char* result = lowercase(text);

    printf("Result: %s\n", result);

#endif

    return 0;
}