def main():
    names = ["Alice", "Bob", "Charlie", "David"]

    for i in range(len(names)):
        print(write_letter(names[i], "Yassin"))


def write_letter(receiver, sender):
    return f"""
==========================
Dear {receiver},

You are invited to my birthday party! I hope you can come, 7:00 PM at my house.
Please let me know if you can make it.

Sincerely,
{sender}
==========================
"""


main()