#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //get user's time
    printf("Minutes: ");
    int num_min = get_int();
    printf("Bottles: %i\n", num_min*12);
}
