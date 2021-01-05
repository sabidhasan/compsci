//Required includes
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "dictionary.h"
#include <ctype.h>

//Defines
#define A_VAL 65
#define ALPHALEN 27

//Define node for trie structure
typedef struct node
{
    struct node *child[ALPHALEN];
    bool word_end;
} node;

//Function to give node for new node
node* create_node(void)
{
    //Allocate memory for new node
    node* ret = malloc(sizeof(node));
    
    if (ret != NULL)
    {
        //got the memory, time to initialize to NULL!
        (*ret).word_end = false;
        //Code below not needed; initially values are NULL and saves 0.02 sec in speed!
            //        for (int i = 0; i < 28; i++)
            //        {
            //            (*ret).child[i] = NULL;
            //        }
    }
    return ret;
}

//this will keep track of size of dictionary
int dict_size = 0;

//memory pointers list, used for unloading
node* pointers_list[1000000] = {};
int pointers_list_ctr = 1;
//To hold the root node! All others are referenced from this
node* root_node;

/**
 * Returns true if word is in dictionary else false.
 */
bool check(const char *word)
{
   //Curr node is for currently active node; ascii val is for value for ascii key
   int ascii_val;
   node* curr_node = root_node;
   
   //loop through word letter by letter checking
   for (int i = 0, len = strlen(word); i < len; i++)
   {
       //set ascii value (array is 27 long)
        if (word[i] == '\'') {
            //last position of array (A-Z are 0 to 25)
            ascii_val = ALPHALEN - 1;
        } else {
            ascii_val = (int) (toupper(word[i])) - A_VAL;
        }

       //check for invalid (non A-Z, non apostraphe)
       if ((*curr_node).child[ascii_val] != NULL) {
           //word exiustgs so far, follow its child
           curr_node = (*curr_node).child[ascii_val];
       } else {
           //word not found, return false
           return false;
       }
   }
   //now that we are at the end of the word, return the value of word_end at current node.
   //(it was initialized to FALSE by create_node function, but is true if word exists!)
   return (*curr_node).word_end;
}

/**
 * Loads dictionary into memory. Returns true if successful else false.
 */
bool load(const char *dictionary)
{
    //Temporary word 
    char tmp_word[LENGTH];
    //Create Root Node
    root_node = create_node();
    pointers_list[0] = root_node;
    //stores ascii value of current node
    int ascii_val;
    
    FILE *dict = fopen(dictionary, "r");
    while(fscanf(dict, "%s", tmp_word) != EOF)
    {
        //read a word so update dictionary size
        dict_size++;
        
        node *curr_node = root_node;
        //Loop through letter by letter to load it in
        for (int i = 0, len = strlen(tmp_word); i < len; i++)
        {
            //if curr_node at desired letter is NULL, then create a new node, point it to that place, set curr_node to new node
            //otherwise, ifg it exists, then curr_node = that existant.
            if (tmp_word[i] == '\'') {
                ascii_val = ALPHALEN - 1;
            } else {
                ascii_val = (int) (toupper(tmp_word[i])) - A_VAL;
            }
            
            if ((*curr_node).child[ascii_val] == NULL)
            {
                (*curr_node).child[ascii_val] = create_node();
                pointers_list[pointers_list_ctr] = (*curr_node).child[ascii_val];//(*curr_node).child[ascii_val];
                pointers_list_ctr++;
            }
            //upodate tge current node
            curr_node = (*curr_node).child[ascii_val];
        }
        (*curr_node).word_end = true;
    }
    return true;
}

/**
 * Returns number of words in dictionary if loaded else 0 if not yet loaded.
 */
unsigned int size(void)
{
    return dict_size;
}

/**
 * Unloads dictionary from memory. Returns true if successful else false.
 */
bool unload(void)
{
    for (int i = 0; i < 1000000; i++)
    {
        free(pointers_list[i]);
    }
    return true;
}
