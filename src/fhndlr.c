#include <stdio.h>
#include "fhndlr.h"

void grayscale(unsigned char* pixel)
{
    unsigned char blue  = pixel[0];
    unsigned char green = pixel[1];
    unsigned char red   = pixel[2];
    unsigned char gray;

    /* Convert to grayscale */
    gray = (unsigned char)((red + green + blue) / 3);

    /* Assign grayscale value */
    pixel[0] = gray;
    pixel[1] = gray;
    pixel[2] = gray;
}