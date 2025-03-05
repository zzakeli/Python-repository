
def main():
    myInput = str(input("Greetings: ")).lower().strip(  )
    if myInput.startswith("h") and not "hello" in myInput:
        print("$20")
    elif not "hello" in myInput:
        print("$100")
    else:
        print("$0")

main()