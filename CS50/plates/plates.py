def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    hasNumeric = False
    firstNumeric = 0
    if len(s) < 2 or len(s) > 6:
        return False
    
    for i in range(len(s)):
        if str(s[i]).isnumeric():
            hasNumeric = True
            firstNumeric = s[i]
            break
    
    if int(firstNumeric) == 0:
        return False
        
    if  (hasNumeric and (str(s[len(s) - 1]).isalpha() and str(s[0]).isalpha())):
        return False
        
    for i in range(len(s)):
        if not(str(s[i]).isalpha() or str(s[i]).isnumeric()):
            return False
    
    return True

main()
