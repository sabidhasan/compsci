#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    //create coins array
    int coins[] = {25, 10, 5, 1};
    
    float change = -1;
    while (! (change >= 0))
    {
        printf("O hai! How much change is owed?\n");
        change = get_float();
    }
    int change_cents = round(change*100);

    int count = 0;
    while (change_cents != 0)
    {
        for (int i = 0; i < 4; i++)
        {
            if (coins[i] <= change_cents) {
                change_cents -= coins[i];
                count++;
                break;
            }
        }
    }
    
    
    printf("%i\n", count);
    
}