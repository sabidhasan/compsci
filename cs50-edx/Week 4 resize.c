/**
 * Copies a BMP piece by piece, just because.
 */
       
#include <stdio.h>
#include <stdlib.h>
#include "bmp.h"

int main(int argc, char *argv[])
{
    // ensure proper usage
    if (argc != 4)
    {
        fprintf(stderr, "Usage: ./resize resize-factor infile outfile\n");
        return 1;
    }
    
    //get scaling factor
    int factor = atoi(argv[1]);
    if (factor > 100 || factor < 1) {
        fprintf(stderr, "Factor must be within 1 to 100.\n");
        return 1;
    }

    //get input and output file names
    char *infile = argv[2];
    char *outfile = argv[3];

    // open input file 
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 1;
    }

    // open output file
    FILE *outptr = fopen(outfile, "w");
    if (outptr == NULL)
    {
        fclose(inptr);
        fprintf(stderr, "Could not create %s.\n", outfile);
        return 1;
    }

    // read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);

    // read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);

    // ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 || 
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 1;
    }

    // determine padding for scanlines
    int padding = (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;
    int write_filepadding = (4 - (bi.biWidth * factor * sizeof(RGBTRIPLE)) % 4) % 4;
    
    int old_height = bi.biHeight;
    int old_width = bi.biWidth;

    //WORK ON THIS
    bi.biWidth = old_width * factor;
    bi.biHeight = old_height * factor;
    bi.biSizeImage = ((sizeof(RGBTRIPLE) * bi.biWidth) + write_filepadding) * abs(bi.biHeight);
    bf.bfSize = bi.biSizeImage + sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER);
    
    //printf("%i, %i, %i, %i, %lu", bi.biWidth, bi.biHeight, bi.biSizeImage, bf.bfSize, sizeof(RGBTRIPLE));
    
    fwrite(&bf, sizeof(BITMAPFILEHEADER), 1, outptr);

    // write outfile's BITMAPINFOHEADER
    fwrite(&bi, sizeof(BITMAPINFOHEADER), 1, outptr);


    //create row variable
    RGBTRIPLE trip[old_width];

    // iterate over infile's scanlines
    for (int i = 0; i < abs(old_height); i++)
    {
        
        // iterate over pixels in scanline
        for (int j = 0; j < old_width; j++)
        {
            // read RGB triple from infile
            fread(&trip[j], sizeof(RGBTRIPLE), 1, inptr);

        }
        int zero = 0x00;
        
        for (int m = 0; m < factor; m++)
        {
            for (int n = 0; n < old_width; n++)
            {
                for (int x = 0; x < factor; x++)
                {
                    fwrite(&trip[n], sizeof(RGBTRIPLE), 1, outptr);
                }
            }
            
            for (int k = 0; k < write_filepadding; k++)
            {
                
                fwrite(&zero, 1, 1, outptr);
            }
            
        }

        
        // skip over padding, if any
        fseek(inptr, padding, SEEK_CUR);

    }

    // close infile
    fclose(inptr);

    // close outfile
    fclose(outptr);

    // success
    return 0;
}
