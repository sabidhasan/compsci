/**
 * Take out the red!
 */
       
#include <stdio.h>
#include <stdlib.h>
#include "bmp.h"

int main(int argc, char *argv[])
{
    // Incorrec tnumber of arguemtns passed
    if (argc != 3) {
        fprintf(stderr, "Usage: ./whodunit mystery-file output-file\n");
        return 1;
    }

    // make mystery file and output
    char *mystery_file = argv[1];
    char *output_file = argv[2];

    // try to read input file (mystery) 
    FILE *inptr = fopen(mystery_file, "r");
    if (inptr == NULL) {
        fprintf(stderr, "Couldn't open file %s.\n", mystery_file);
        return 2;
    }

    // open output file
    FILE *outptr = fopen(output_file, "w");
    if (outptr == NULL) {
        fclose(inptr);
        fprintf(stderr, "Couldn't create requested file %s.\n", output_file);
        return 3;
    }

    // read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bmphead;
    fread(&bmphead, sizeof(BITMAPFILEHEADER), 1, inptr);

    // read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bmpinfo;
    fread(&bmpinfo, sizeof(BITMAPINFOHEADER), 1, inptr);

    // ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bmphead.bfType != 0x4d42 || bmphead.bfOffBits != 54 || bmpinfo.biSize != 40 || 
        bmpinfo.biBitCount != 24 || bmpinfo.biCompression != 0) {
        //close the files, something is wrong!
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "File format was not as expected (24-bit BMP 4.0 file needed).\n");
        return 4;
    }

    // write outfile's BITMAPFILEHEADER
    fwrite(&bmphead, sizeof(BITMAPFILEHEADER), 1, outptr);

    // write outfile's BITMAPINFOHEADER
    fwrite(&bmpinfo, sizeof(BITMAPINFOHEADER), 1, outptr);

    //See how much padding is needed
    //Remember, total must be divisible by 4!
    int padding =  (4 - (bmpinfo.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;

    //iterate over rows of the input file
    //abs is needed to ensure compatibility with UPSIDE DOWN pictures!
    for (int i = 0, biHeight = abs(bmpinfo.biHeight); i < biHeight; i++)
    {
        //iterate over the pixel in current row
        for (int j = 0; j < bmpinfo.biWidth; j++)
        {
            // temporary storage
            RGBTRIPLE triple;

            // read RGB triple from infile
            fread(&triple, sizeof(RGBTRIPLE), 1, inptr);
            
            
            if ((triple.rgbtBlue == 0x00 && triple.rgbtRed == 0xff && triple.rgbtGreen == 0x00) || (triple.rgbtBlue == 0xff && triple.rgbtRed == 0xff && triple.rgbtGreen == 0xff)) {
                triple.rgbtRed = 0xff;
                triple.rgbtBlue = 0xff;
                triple.rgbtGreen = 0xff;
            } else {
                triple.rgbtRed = 0x00;
                triple.rgbtBlue = 0x00;
                triple.rgbtGreen = 0x00;
            }
            // write RGB triple to outfile
            fwrite(&triple, sizeof(RGBTRIPLE), 1, outptr);
        }

        // skip over padding, if any
        fseek(inptr, padding, SEEK_CUR);

        // then add it back (to demonstrate how)
        for (int k = 0; k < padding; k++)
        {
            fputc(0x00, outptr);
        }
    }

    // close infile
    fclose(inptr);

    // close outfile
    fclose(outptr);

    // success
    return 0;
}
