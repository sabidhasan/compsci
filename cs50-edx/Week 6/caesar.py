import sys
VAL_CAP_A =  65
VAL_LOWER_A = 97
ALPHA_LEN = 26

def get_float():
    while True:
        try:
            x = float(input(""))
        except ValueError:
            continue
        return x
        
def main():
    if len(sys.argv) != 2:
        print("Usage: ./caesar [integer]")
        exit(1)
    key = int(sys.argv[1]) % ALPHA_LEN
    plaintext = input("plaintext: ")
    
    print("Ciphertext: ", end="")
    
    for char in plaintext:
        if char.isupper():
            print(chr(((ord(char) - VAL_CAP_A + key) % ALPHA_LEN) + VAL_CAP_A).upper(), end="")
        elif char.islower():
            print(chr(((ord(char) - VAL_LOWER_A + key) % ALPHA_LEN) + VAL_CAP_A).lower(), end="")
        else:
            print(char, end="")
    print("")
    return 0

if __name__ == "__main__":
    main()
