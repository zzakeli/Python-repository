def main():
    camelCase = str(input("camelCase: ")).strip()
    snakeCase = ""
    
    for i in range(len(camelCase)):
        if i != len(camelCase) - 1 and camelCase[i + 1].isupper():
            snakeCase += camelCase[i]
            snakeCase += "_"
            continue
        
        if camelCase[i].isupper():
            snakeCase += camelCase[i].lower()
            continue
        
        snakeCase += camelCase[i]
    
    print("snake_case: ",snakeCase)

main()