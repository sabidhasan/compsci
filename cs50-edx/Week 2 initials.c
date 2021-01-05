//ASCII value for space character, to avoid having constants
#define SPACE 32

#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    //get string from user
    string s = get_string();
    
    //needed in case of null string (?)
    if (s != NULL)
    {
        //Loop through the entire string, minus 1 (to avoid the \0 character at the end from being checked!)
        for (int i = 0, str_len = strlen(s); i < str_len - 1; i++)
        {
            //if we are at a NON space character s[i], and the prev one was a space --OR--
            //we are at the beginning (meaning i == 0) then let's print the current character (upper case)
            if (s[i] != SPACE && ((s[i-1] == SPACE) || i == 0))
            {
                printf("%c", toupper(s[i]));
            }
            
        }
        //per spec, need new line at the end
        printf("\n");
    }
}