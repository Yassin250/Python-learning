def main():
    player = input("Multiplayer or Singleplayer? ")
    if not (player == "Multiplayer" or player == "Singleplayer"):
        print("Enter a valid number of player")
        return

    difficulty = input("Difficulty (Difficult/Casual)? ")
    if not (difficulty == "Difficult" or difficulty == "Casual"):
        print("Enter a valid difficulty")
        return

    if difficulty == "Difficult" and player == "Multiplayer":
        recommend("Pocker")

    elif difficulty == "Difficult" and player == "Singleplayer":
        recommend("Chess")
    elif difficulty == "Casual" and player == "Multiplayer":
        recommend("Hearts")
    else:
        recommend("clock")        





def recommend(game):
    print("You might like", game)



main()