def main():
    n = int(input("Enter mass: "))
    
    print(convert(n))

def convert(n):
    speedOfLight = 300000000
    return n * pow(speedOfLight, 2)

main()