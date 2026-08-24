def main():
    difficulty = input("Difficulty or Casual? ")
    player = input("Multiplayer or Singleplayer? ")

    if difficulty == "Difficulty":
        if player == "Multiplayer":
            recommend("Pocker")
        elif player == "Singleplayer":
            recommend("Chess")
        else:
            print("Invalid input for player type.")

    elif difficulty == "Casual":
        if player == "Multiplayer":
            recommend("Hearts")
        elif player == "Singleplayer":
            recommend("clock")
        else:
            print("Invalid input for player type.")

    else:
        print("Enter a valid difficulty")        


def recommend(game):
    print("You might like", game)            

main()

