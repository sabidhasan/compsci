#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#define VAL_CAP_A 65            //value of uppercase A
#define VAL_LOW_A 97            //value of lowercase A
#define ALPHA_LEN 26            //length of English Alphabet

//Get command line arguments
int main (int argc, string argv [])
{
    //key will store the user-read key
    string key;
    
    //if we give more or less than 2 arguments (first one is filename), error out
    if (argc != 2 ) {
        //show friendly help message
        printf("Usage: ./crack [hash]; only hash *must* be supplied.\n");
        return 1;
    } else {
        //Set key to Vigenere key, and loop through to determine it's validity
        key = argv[1];
        for (int i = 0, arg_len = strlen(key); i < arg_len; i++)
        {
            //If non alphabetic value found, then error out
            if (!(isalpha(key[i])))
            { 
                printf("Usage: hash must be entirely alphabetic; Character '%c' is not valid!\n", key[i]);
                return 1;
            }
        }
    }
    
    //Get the Plain text from user
    printf("plaintext: ");
    string plaintext = get_string();
    
    printf("ciphertext: ");
    //Vigenere counter holds incremented when vigenere key employed, curr_key is current letter
    int vignere = 0;
    char curr_key;
    //This will store what character will get printed at the end of each iteration
    int chr_to_print;
    
    //Loop through the string character by character
    for (int i = 0, str_len = strlen(plaintext); i < str_len; i++)
    {
        //the MOD ensures we loop around to 0 when it's too high
        curr_key = key[vignere % strlen(key)];
        
        //If we are dealing with a CAPITAL letter
        if (isupper(plaintext[i])) {
            //subtract the value of the first letter (A = 65), then add the key (subtract VAL_CAP_A to ensure A = 0, B = 1, etc.
            //mod with length of alphabet to account for turnaround (in case it's now greater than 26), and add back the value of CAP A.
            chr_to_print = (((int) plaintext[i] - VAL_CAP_A + (toupper( curr_key    ) - VAL_CAP_A)) % ALPHA_LEN) + VAL_CAP_A;
            //Increment vignere counter - we used the key
            vignere++;
        } else if (islower(plaintext[i])) {
            chr_to_print = (((int) plaintext[i] - VAL_LOW_A + (tolower(key[vignere % strlen(key)]) - VAL_LOW_A)) % ALPHA_LEN) + VAL_LOW_A;
            vignere++;
        } else {
            //non-alphabetic, so use as is
            chr_to_print = plaintext[i];
        }
        
        //print current letter
        printf("%c", chr_to_print);
    }
    printf("\n");
}