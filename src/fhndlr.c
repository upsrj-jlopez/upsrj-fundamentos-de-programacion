#include "fhndlr.h"

char* lowercase(char* input)
{
    int i = 0;
    while (input[i] != '\0')
    {
        if (input[i] >= 'A' && input[i] <= 'Z') 
            input[i] = input[i] + ('a' - 'A');
        i++;
    }
    return input;
}


char* uppercase(char* input)
{
    int i = 0;
    while (input[i] != '\0')
    {
        if (input[i] >= 'a' && input[i] <= 'z') 
            input[i] = input[i] - ('a' - 'A');
        i++;
    }
    return input;
}

char* capitalize(char* input)
{
    input = lowercase(input);

    int i = 0;
    int capitalize = 1;
    while (input[i] != '\0')
    {
        if (input[i] == ' ' || input[i] == '\n' || input[i] == '\t')
        {
            capitalize = 1;
        }    
        else
        {
            if (capitalize)
            {
                input[i] = input[i] - ('a' - 'A');
            }
            capitalize = 0;
        }
        i++;
    }
    return input;
}