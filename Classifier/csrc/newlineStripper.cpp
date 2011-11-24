#include <stdio.h>


int main()
{
    char currentChar;
    while (!feof(stdin))
    {
        currentChar = (char) fgetc(stdin);
        if (currentChar == '\n')
            printf(" ");
        else
            printf("%c", currentChar);
    }
}