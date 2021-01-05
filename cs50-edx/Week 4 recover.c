#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    // Incorrect number of arguements were passed.
    if (argc != 2) {
        fprintf(stderr, "Usage: ./recover raw_file\n");
        return 1;
    }

    // Make mystery file and output
    char *raw = argv[1];

    // try to read input file (mystery) 
    FILE *ffile = fopen(raw, "r");
    if (ffile == NULL)
    {
        fprintf(stderr, "Couldn't open file %s.\n", raw);
        return 2;
    }
    
    //how many bytes I just read (for feterming the End Of File)
    size_t bytesRead = 0;
    //holds the current 512 bytes of buffer data
    unsigned char buffer[512];
    //string for filename for current jpg
    char filenames[8];
    //we need to only start writing once first file has been found, so start at 0. This is a boolean
    int something_open = 0;
    //filename counter for pictures
    int pic = 0;
    //actual file for writing
    FILE *img;
    
    //read 512 bytes at a time into buffer
    while ((bytesRead = fread(&buffer, 512, 1, ffile)) > 0) {
        //check for first four bytes of data using bitwise operator for the last one
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0) {
            //we've found a start of a JPG! Open a new one for sure
            sprintf(filenames, "%03d.jpg", pic);
            
            //if something is open, then lets close it (literally only DOESNT run before first pic is found)
            if (something_open == 1) 
            {
                fclose(img);
            }
            
            //increment counter for next time, open new image, set something_open to 1, write current buffer
            pic++;
            img = fopen(filenames, "w");
            something_open = 1;
			fwrite(buffer, sizeof(buffer), 1, img);
        
            
        } else if (something_open == 1) {
            //write buffer, because we are on an image
            fwrite(buffer, sizeof(buffer), 1, img);
        }
    }
    return 0;
}
