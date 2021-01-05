#include <stdio.h>
#include <cs50.h>

void print_row(int num_signs, int height);

int main(void)
{
    //get height from user
    int height = -1;
    
    while (height < 0 || height > 23)
    {
        printf("Height: ");
        height = get_int();
    }
    
    //now lets run a for loop
    for (int i = 0; i < height; i++)
    {
        print_row(i+1, height);
    } 
 
}

void print_row(int num_signs, int height)
{
    for (int j = 0; j < height+2; j++)
    {
        if (j < height - num_signs || j == height + 1 || j == height)
        //|| j > num_signs + height + 1 ||
        {
            printf(" ");
        } else {
            printf("#");
        }
        
    }
    for (int j = 0; j < num_signs; j++)
    {
        printf("#");
    }
    printf("\n");
}