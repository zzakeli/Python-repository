def scoreOfString(self, s):
    total = 0
    for i in range(len(s) - 1):
        total += abs(ord(s[i]) - ord(s[i + 1]))
        
    return total
self = 0
print(scoreOfString(self,"zaz"))