def main():
    history = []

    while True:
        action = input("Action: ").lower()

        if action == "undo":
            if len(history) > 0:
                undone = history.pop()
                print(f"Undone: {undone}")
            else:
                print("Nothing to undo.")

        elif action == "restart":
            history.clear()
            print("History cleared")

        else:
            history.append(action)

        print(history)


main()