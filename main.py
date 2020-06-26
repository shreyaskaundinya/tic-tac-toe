import hard
import easy
import random


def easy_game(rowboard, colboard):
    w = easy.play(rowboard, colboard)
    if w != "TIE":
        print("\n\nWINNER WINNER :\n", w, " WINS!!!!!!!")
    else:
        print("TIE")
    easy.reset()


def hard_game(rowboard, colboard):
    w = hard.play(rowboard, colboard)
    if w != "TIE":
        print("\n\nWINNER WINNER :\n", w, " WINS!!!!!!!")
    else:
        print("TIE")
    hard.reset()


def main():
    c = True
    while c == True:
        row1 = ["", "", ""]
        row2 = ["", "", ""]
        row3 = ["", "", ""]
        col1 = ["", "", ""]
        col2 = ["", "", ""]
        col3 = ["", "", ""]

        rowboard = [row1, row2, row3]
        colboard = [col1, col2, col3]
        intro = "HELLO WELCOME TO THE GAME OF TIC TAC TOE....\n\n"
        print(intro)
        game_mode = input(
            """
            Enter
            1 for easy mode
            2 for hard mode
            3 for random : """)
        print("\n\n")
        if game_mode == "1":
            easy_game(rowboard, colboard)
        elif game_mode == "2":
            hard_game(rowboard, colboard)
        elif game_mode == "3":
            r = random.randint(1, 1000)
            if r <= 500:
                easy_game(rowboard, colboard)
            if r > 500:
                hard_game(rowboard, colboard)

        print("\n\n")
        c = not bool(input("Click enter to play again, type q to quit"))


main()
