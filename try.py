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

row1 = ["", "", ""]
row2 = ["", "", ""]
row3 = ["", "", ""]
col1 = ["", "", ""]
col2 = ["", "", ""]
col3 = ["", "", ""]

rowboard = [row1, row2, row3]
colboard = [col1, col2, col3]

previous_turn = ()
center = (2, 2)
corner = None
corner_co_ords = [(1, 1), (3, 1), (3, 3), (1, 3)]
corner_coord = ()


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


def side_cor(center):
    global previous_turn, corner_coord
    if corner == 1 or corner == 3:
        if previous_turn == (3, 1):
            x, y = (1, 3)
            corner_coord = (1, 3)
        else:
            x, y = (3, 1)
            corner_coord = (3, 1)
    elif corner == 2 or corner == 4:
        if previous_turn == (1, 1):
            x, y = (3, 3)
            corner_coord = (3, 3)
        else:
            x, y = (1, 1)
            corner_coord = (1, 1)
    return x, y


def fifth_strat(rowboard):
    global corner_coord, corner_co_ords, corner
    if corner_coord in (corner_co_ords[0], corner_co_ords[2]) and corner == 2:
        best = corner_co_ords[3]
        if element(best[0], best[1], rowboard) == "O":
            if corner_coord == corner_co_ords[0]:
                return corner_co_ords[2]
            else:
                return corner_co_ords[0]
    elif corner_coord in (corner_co_ords[0], corner_co_ords[2]) and corner == 4:
        best = corner_co_ords[1]
        if element(best[0], best[1], rowboard) == "O":
            if corner_coord == corner_co_ords[0]:
                return corner_co_ords[2]
            else:
                return corner_co_ords[0]
    if corner_coord in (corner_co_ords[1], corner_co_ords[3]) and corner == 1:
        best = corner_co_ords[2]
        if element(best[0], best[1], rowboard) == "O":
            if corner_coord == corner_co_ords[3]:
                return corner_co_ords[1]
            else:
                return corner_co_ords[3]
    elif corner_coord in (corner_co_ords[1], corner_co_ords[3]) and corner == 3:
        best = corner_co_ords[0]
        if element(best[0], best[1], rowboard) == "O":
            if corner_coord == corner_co_ords[3]:
                return corner_co_ords[1]
            else:
                return corner_co_ords[3]


def seventh_strat(r1, r2, r3, c1, c2, c3, rowboard):
    global corner_coord, corner, corner_co_ords
    if element(2, 2, rowboard) != "O":
        return 2, 2
    if corner_coord == corner_co_ords[0]:
        pass
    elif corner_coord == corner_co_ords[1]:
        pass
    elif corner_coord == corner_co_ords[2]:
        pass
    elif corner_coord == corner_co_ords[3]:
        pass


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
    global X, O, previous_turn, corner, corner_co_ords, corner_coord
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
        print(w, b)

        # breakpoint
        if turn == 7:
            break
        if b is True:
            return w
        else:
            pass
        if turn == 10:
            return "TIE"

        if turn % 2 == 1:
            # computers turn
            if turn == 1:
                corner = random.randint(1, 4)
                '''
                [1 0 2]
                [0 0 0]
                [4 0 3]
                '''
                print(corner)
                if corner == 1:
                    row1[0] = X
                    col1[0] = X
                    rowboard = rowb_make(row1, row2, row3)
                    colboard = rowb_make(col1, col2, col3)
                elif corner == 2:
                    row1[2] = X
                    col3[0] = X
                    rowboard = rowb_make(row1, row2, row3)
                    colboard = rowb_make(col1, col2, col3)
                elif corner == 3:
                    row3[2] = X
                    col3[2] = X
                    rowboard = rowb_make(row1, row2, row3)
                    colboard = rowb_make(col1, col2, col3)
                elif corner == 4:
                    row3[0] = X
                    col1[2] = X
                    rowboard = rowb_make(row1, row2, row3)
                    colboard = rowb_make(col1, col2, col3)
            else:
                if turn == 3:
                    x, y = side_cor(center)
                    row1, row2, row3, col1, col2, col3 = place(turn,
                                                               x, y, row1, row2, row3, col1, col2, col3)
                    rowboard = rowb_make(row1, row2, row3)
                    colboard = rowb_make(col1, col2, col3)

                if turn == 5:
                    x, y = fifth_strat(rowboard)
                    row1, row2, row3, col1, col2, col3 = place(turn,
                                                               x, y, row1, row2, row3, col1, col2, col3)
                    rowboard = rowb_make(row1, row2, row3)
                    colboard = rowb_make(col1, col2, col3)
                if turn == 7:
                    x, y = seventh_strat()
                    row1, row2, row3, col1, col2, col3 = place(turn,
                                                               x, y, row1, row2, row3, col1, col2, col3)
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
                else:
                    break
            # x is column and y is row
            previous_turn = co_ordinate
            # place the O in the board
            row1, row2, row3, col1, col2, col3 = place(turn,
                                                       cx, cy, row1, row2, row3, col1, col2, col3)
            rowboard = rowb_make(row1, row2, row3)
            colboard = rowb_make(col1, col2, col3)

        turn += 1


w = play(rowboard, colboard)
if w != "TIE":
    print("\n\n!!!!!!!!!!!!!!!!!!!!!!", w, " WINS!!!!!!!")
else:
    print("TIE")
