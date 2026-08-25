WORDS = {"PAIR": 4, "HAIR": 4, "FAIR": 4, "AIR": 3, "CHAIR": 5}

def main():
    print("Welcom to the spelling Bee!")
    print ("Your letter are: A,I,P,C,R,H,G")

    score =0
    mistakes = 0

    while len(WORDS) > 0:
        word = input("Enter a word: ").upper()

        if word in WORDS:
            print("correct")
            score = WORDS[word]
            del WORDS[word]

        else:
            print("not a valid word.")
            score -= 1
            mistakes += 1
    print()
    print("Game over! Your score is: ", score)
    print("You made ", mistakes, "mistakes.")
main()
                