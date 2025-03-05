def main():
    time = str(input("What time is it? ")).strip()
    total = convert(time)
    
    if total >= 7 and total <= 8:
        print("breakfast time")
    elif total >= 12 and total <= 13:
        print("lunch time")
    elif total >= 18 and total <= 19:
        print("dinner time")


def convert(time):
    hour = int(time[0:time.find(":")])
    minute = int(time[time.find(":") + 1:]) / 60
    
    return hour + minute
    
if __name__ == "__main__":
    main()
