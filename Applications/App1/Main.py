import random
    
hands = ["rock","paper","scissor"]

def main():
    player = None
    while True:
        player = input("Enter sign: ").lower()
    
        if(player == hands[0] or player == hands[1] or player == hands[2]):
            break
        print("Invalid input.")

    computer = randomize()

    print("player: " + player)
    print("computer: " + computer)
    compete(player, computer)

    
def randomize():
    comp_choice = random.choice(hands)
    
    # dict = {
    #     1:"rock",
    #     2:"paper",
    #     3:"scissor"
    # }
    return comp_choice

def compete(player: str, computer: str):
    
    if((player == "rock" and computer == "paper") or (player == "paper" and computer == "scissor")or (player == "scissor" and computer == "rock")):
        print("You lose!")
    
    elif((player == "rock" and computer == "scissor") or (player == "paper" and computer == "rock") or (player == "scissor" and computer == "paper")):
        print("You won!")
    else:
        print("It's a draw.")
    
if(__name__ == "__main__"):
    main()