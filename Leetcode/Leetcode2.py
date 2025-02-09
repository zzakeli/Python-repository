def interpret(self, command):
    result = ""

    for i in range(len(command)):
        if(command[i] == "G"):
            result += "G"
            continue
        
        if(command[i : i + 2] == "()"):
            result += "o"
            i += 1
            continue
        
        if(command[i : i + 4] == "(al)"):
            result += "al"
            i += 3
    
    
    return result

command  = "G()()()()(al)"
self = 0
print(interpret(self, command))