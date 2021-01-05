#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
//Value of capital letter A
#define VAL_CAP_A 65
//Value of lowercase A
#define VAL_LOWER_A 97
//length of alphabet (English alphabet!)
#define ALPHA_LEN 26

//Note, we get argument count and argument vectors here
int main(int argc, string argv[])
{
    //if we give mroe than 2 arguments (first one is filename), or less than 2 (no real arguements)
    if (argc != 2 ) {
        //show friendly help message
        printf("Usage: ./caesar [integer]\n");
        //error code
        return 1;
    }

    //key is a number from 1 to length of alphabet that represents the shift of the Ceasar cipher.
    int key = atoi(argv[1]) % ALPHA_LEN;
    printf("plaintext: ");
    //plaintext stores user entered text
    string plaintext = get_string();

    printf("ciphertext: ");
    //Loop through the string character by character
    for (int i = 0, str_len = strlen(plaintext); i < str_len; i++)
    {
        //This will store what character will get printed at the end of this iteration of the loop
        int chr_to_print;
        
        //If we are dealing with a CAPITAL letter
        if (isupper(plaintext[i])) {
            //subtract the value of the first letter (A = 65), then add the key, mod it with length of alphabet to account for 
            //turnaround (in case it's now greater than 26), and add back the value of CAP A.
            chr_to_print = (((int) plaintext[i] - VAL_CAP_A + key) % ALPHA_LEN) + VAL_CAP_A;
        } else if (islower(plaintext[i]))       {
            //same for lower case
            chr_to_print = (((int) plaintext[i] - VAL_LOWER_A + key) % ALPHA_LEN) + VAL_LOWER_A;
        } else {
            //if not A-Z or a-z, then just use as is
            chr_to_print = plaintext[i];
        }
        
        //print to console
        printf("%c", chr_to_print);
    }
    
    //return 0 error code - it worked!
    printf("\n");
    return 0;
}