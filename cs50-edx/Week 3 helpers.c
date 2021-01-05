/**
 * helpers.c
 *
 * Helper functions for Problem Set 3.
 */
 
#include <cs50.h>
#include <math.h>
#include "helpers.h"
#include <stdio.h>

/**
 * Returns true if value is in array of n values, else false.
 */
bool search(int value, int values[], int n)
{
    if (n <= 0) {
        return false;
    }

//    sort(values, n);

    //do binary search
    int start = 0;
    int end = n;
    
    do
    {
        int mid = floor((start + end)/2);
        
        //printf("Checking mid %i\n", mid);
        
        if (values[mid] > value) {
            end = mid - 1;
        } else if (values[mid] < value){
            start = mid + 1;
        } else {
            return true;
        }
        
        //printf ("Start now is %i and end is %i.\n\n\n", start, end);
    } while ( start <= end );
    
    return false;
}

/**
 * Sorts array of n values.
 */
void sort(int values[], int n)
{
    // TODO: implement an O(n^2) sorting algorithm
    //printf("Enteringf sort fdunciton.");
    int sorted[65536];
    int temp_sort[65536];
    
    for (int i = 0; i < n; i++)
    {
        int curr_val = values[i];
        temp_sort[curr_val] += 1;
        //printf("Tempsort of currval %i is %i\n", curr_val, temp_sort[curr_val]);
    }
    //loop through created array and return
    int counter = 0;
    for (int i = 0; i < 65536; i++)
    {
        if (temp_sort[i] == 0) {
            continue;
        }
        //printf ("Currnet i is %i current tempsort is %i (looping this many times)\n", i, temp_sort[i]);
        
        for (int j = 0; j < temp_sort[i]; j++)
        {
            sorted[counter] = i;
            counter++;
           // printf("sorted of counter %i is %i\n", counter, sorted[counter-1]);

        }
        //printf("\n\n\n");
    }
    
    for (int i = 0; i < n; i++) {
      values[i] = sorted[i];
    }

}
