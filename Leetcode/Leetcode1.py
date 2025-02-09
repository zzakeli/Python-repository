def finalValueAfterOperations(self, operations):
    x = 0
    for char in operations:
        if("++" in char):
            x+=1
            continue
        x-=1
    return x

operations = ["X++","++X","--X","X--"]
self = 0
print(finalValueAfterOperations(self, operations))