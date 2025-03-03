
def main():
    myInput = str(input("What is the Answer to the Great Question of life, the Universe, and Everything? ")).lower().strip()
    if myInput == "42" or myInput == "forty-two" or myInput == "forty two":
        print("yes")
    else:
        print("no")
main()