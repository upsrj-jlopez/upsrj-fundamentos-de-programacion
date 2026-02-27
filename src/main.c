#include <stdio.h>
#include <string.h>

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

    char* result = uppercase(buffer);

    printf("%s", result);

#else

    /* Normal execution mode */
    char text[] = "HELLO World 123!";

    char* result = uppercase(text);

    printf("Result: %s\n", result);

#endif

    return 0;
}