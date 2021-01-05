def get_int():
    while True:
        try:
            x = int(input("Height: "))
        except ValueError:
            continue
        return x
        
def main():
    #Get height
    height = -1
    while height < 0 or height > 23:
        height = get_int()
    
    for i in range(height):
        print_row(i+1, height)
        
def print_row(num_signs, height):
    for j in range(height+2):
        if (j < height - num_signs or j == height + 1 or j == height):
            print (" ", end="")
        else:
            print("#", end="")

    for j in range(num_signs):
        print("#", end="")
    print ("")
main()