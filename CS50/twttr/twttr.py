def main():
    word = str(input("Input: "))
    output = ""
    for i in word:
        if i.lower() in ["a","e","i","o","u"]:
            continue
        output += i
    print(output)
main()