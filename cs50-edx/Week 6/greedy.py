def get_float():
    while True:
        try:
            x = float(input(""))
        except ValueError:
            continue
        return x
        
def main():
    coins = [25, 10, 5, 1]
    change = -1    
    
    while not(change >= 0):
        print ("O hai! How much change is owed? ", end="")
        change = get_float();
        
    change_cents = round(change*100);

    count = 0;
    while change_cents != 0:
        for val in coins:
            if val <= change_cents:
                change_cents -= val
                count += 1
                break;

    print("{}".format(count))

main()