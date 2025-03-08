def main():
    myInput = str(input("Expression: ")).strip()
    y = ""
    if "+" in myInput:
        y = "+"
    elif "-" in myInput:
        y = "-"
    elif "*" in myInput:
        y = "*"
    elif "/" in myInput:
        y = "/"
        
    x = float(myInput[0:myInput.find(y) - 1])
    z = float(myInput[myInput.find(y) + 2:])
    output = 0
    
    if y == "+":
        output = x + z
    elif y == "-":
        output = x - z
    elif y == "*":
        output = x * z
    elif y == "/":
        output = x / z
        
    print(output)   
    
main()