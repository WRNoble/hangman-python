def hangman(word):
    wrong = 0
    stage = ["",
            "___________        ",
            "|          |       ",
            "|          |       ",
            "|          O       ",
            "|          |       ",
            "|         /|\      ",
            "|         / \      ",
            "|                  "
            ]
    rletters = list(word)
    board = ["___"] * len(word)
    win = False
    print("Welcome to Hangman")