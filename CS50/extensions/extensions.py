def main():
    myInput = str(input(("File name: "))).lower()
    output = ""
    if ".gif" in myInput:
        output = "image/gif"
    elif ".jpg" in myInput or ".jpeg" in myInput:
        output = "image/jpeg"
    elif "png" in myInput:
        output = "image/png"
    elif "pdf" in myInput:
        output = "application/pdf"
    elif ".txt"in myInput:
        output = "text/plain"
    elif ".zip" in myInput: 
        output = "application/zip"
    else:
        output = "application/octet-stream"
    
    print(output)
    
main()