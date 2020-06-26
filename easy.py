'''
[
    [X, O, X]
    [X, O, X]
    [X, O, X]
]

[
     1  2  3
    [X, X, X]
    [O, O, O]
    [X, X, X]
]

'''

import random

X = "X"
O = "O"


all_coor = [
    (1, 1), (1, 2), (1, 3),
    (2, 1), (2, 2), (2, 3),
    (3, 1), (3, 2), (3, 3)
]


def reset():
    global all_coor
    x = [
        (1, 1), (1, 2), (1, 3),
        (2, 1), (2, 2), (2, 3),
        (3, 1), (3, 2), (3, 3)
    ]
    for i in x:
        all_coor.append(i)


def board_check(rowboard):
    # to check if board is empty
    for row in rowboard:
        check = None
        for cell in row:
            if row == "":
                check = False
                return check
        else:
            check = True


def element(x, y, rowboard):
    return rowboard[y-1][x-1]


def winners_check(r1, r2, r3, c1, c2, c3, rowboard):
    global X, O
    for i in (r1, r2, r3, c1, c2, c3):
        # rows and cols
        if i.count(X) == 3:
            return X, True
        elif i.count(O) == 3:
            return O, True
    else:
        # diagonals
        if element(1, 1, rowboard) == element(2, 2, rowboard) and element(1, 1, rowboard) == element(3, 3, rowboard) and element(1, 1, rowboard) in (X, O):
            return element(1, 1, rowboard), True
        elif element(3, 1, rowboard) == element(2, 2, rowboard) and element(3, 1, rowboard) == element(1, 3, rowboard) and element(1, 3, rowboard) in (X, O):
            return element(1, 3, rowboard), True
        else:
            return None, False


def board_print(board):
    print(" ", end="")
    for i in range(3):
        print(" ", i+1, end=" ")
    print()
    for i in range(len(board)):
        print(i+1, board[i])
    print()


def rowb_make(row1, row2, row3):
    rowboard = [row1, row2, row3]
    return rowboard


def colb_make(col1, col2, col3):
    colboard = [row1, row2, row3]
    return colboard


def place(turn, cx, cy, row1, row2, row3, col1, col2, col3):
    global X, O
    if turn % 2 == 1:
        unit = X
    else:
        unit = O
    if cx == 1:
        col1[cy-1] = unit
    elif cx == 2:
        col2[cy-1] = unit
    elif cx == 3:
        col3[cy-1] = unit

    if cy == 1:
        row1[cx-1] = unit
    elif cy == 2:
        row2[cx-1] = unit
    elif cy == 3:
        row3[cx-1] = unit

    return row1, row2, row3, col1, col2, col3


def play(rowboard, colboard):
    global X, O, all_coor
    print(all_coor)
    row1 = rowboard[0]
    row2 = rowboard[1]
    row3 = rowboard[2]
    col1 = colboard[0]
    col2 = colboard[1]
    col3 = colboard[2]
    x, y = (None, None)
    turn = 1
    while board_check(rowboard) != False:
        print("Turn : ", turn, "\n")
        board_print(rowboard)
        w, b = winners_check(row1, row2, row3, col1, col2, col3, rowboard)
        if b == True:
            return w
        else:
            pass
        if len(all_coor) == 0:
            return "TIE"
        if turn % 2 == 1:
            # computers turn
            coordinates = random.sample(all_coor, 1)[0]
            all_coor.remove(coordinates)
            cx, cy = coordinates
            row1, row2, row3, col1, col2, col3 = place(turn,
                                                       cx, cy, row1, row2, row3, col1, col2, col3)
            rowboard = rowb_make(row1, row2, row3)
            colboard = rowb_make(col1, col2, col3)

        else:
            # players turn
            while True:
                print()
                co_ordinate = tuple(
                    eval(input("Enter coordinate of placing O : ")))
                print(co_ordinate)
                cx, cy = co_ordinate
                if cx not in (1, 2, 3) or cy not in (1, 2, 3):
                    print("Enter the correct coordinates.")
                    continue
                elif co_ordinate not in all_coor:
                    print("Coordinates already occupied.")
                    continue
                else:
                    break
            # x is column and y is row
            previous_turn = co_ordinate
            # place the O in the board
            all_coor.remove(co_ordinate)
            row1, row2, row3, col1, col2, col3 = place(turn,
                                                       cx, cy, row1, row2, row3, col1, col2, col3)
            rowboard = rowb_make(row1, row2, row3)
            colboard = rowb_make(col1, col2, col3)

        turn += 1
