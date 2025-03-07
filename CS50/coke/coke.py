def main():
    cents = 50
    while cents >  0:
        print("Amount Due:", cents)
        insert = int(input("Insert Coin: "))
        
        if insert == 25 or insert == 10 or insert == 5:
            cents -= insert

    print("Change Owed:", abs(cents))
main()
