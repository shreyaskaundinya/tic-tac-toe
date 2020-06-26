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

center = (2, 2)
corner = None
corner_co_ords = [(1, 1), (3, 1), (3, 3), (1, 3)]
adjacent_corners = {
    (1, 1): [2, 4],
    (3, 1): [1, 3],
    (3, 3): [2, 4],
    (1, 3): [1, 3]
}
coordinate_matrix = [
    [(1, 1), (1, 2), (1, 3)],
    [(2, 1), (2, 2), (2, 3)],
    [(3, 1), (3, 2), (3, 3)]
]

all_coor = [
    (1, 1), (1, 2), (1, 3),
    (2, 1), (2, 2), (2, 3),
    (3, 1), (3, 2), (3, 3)
]

turns = {
    X: {

    },
    O: {

    }

}


def reset():
    global all_coor, corner
    x = [
        (1, 1), (1, 2), (1, 3),
        (2, 1), (2, 2), (2, 3),
        (3, 1), (3, 2), (3, 3)
    ]
    for i in x:
        all_coor.append(i)

    corner = None

    turns = {
        X: {},
        O: {}
    }


def adjacent_coordinates(corner):
    global corner_co_ords
    if corner == corner_co_ords[0]:
        return (1, 2), (2, 1)
    if corner == corner_co_ords[1]:
        return (1, 2), (2, 3)
    if corner == corner_co_ords[2]:
        return (2, 3), (2, 3)
    if corner == corner_co_ords[3]:
        return (2, 1), (3, 2)


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


def mid_point_check(turn, adj_corner_to_1, adj_corner_to_3, rowboard, col_to_1, col_to_3):
    global all_coor, turns, X, O
    turn1 = turns[X][1]
    turn3 = turns[X][3]


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3[0]


def play(rowboard, colboard):
    global X, O, all_coor, corner_co_ords, turns, adjacent_corners
    row1 = rowboard[0]
    row2 = rowboard[1]
    row3 = rowboard[2]
    col1 = colboard[0]
    col2 = colboard[1]
    col3 = colboard[2]
    x, y = (None, None)
    turn = 1
    while board_check(rowboard) != False:
        if turn % 2 == 1:
            print("Turn : ", turn, "(COMPUTERS TURN) \n")
        else:
            print("Turn : ", turn, "(PLAYERS TURN) \n")
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
            if turn == 1:
                # random corner
                coordinates = random.sample(corner_co_ords, 1)[0]
                all_coor.remove(coordinates)
                turns[X][turn] = coordinates
                cx, cy = coordinates
                row1, row2, row3, col1, col2, col3 = place(turn,
                                                           cx, cy, row1, row2, row3, col1, col2, col3)
                rowboard = rowb_make(row1, row2, row3)
                colboard = rowb_make(col1, col2, col3)
            elif turn == 3:
                # get the adjacent corners of the previously placed X
                get_adj_corner = [corner_co_ords[i-1]
                                  for i in adjacent_corners[turns[X][1]]]
                best = None
                # if O is placed at center, X must be placed at the opposite corner of the previously placed X to get an advantage
                if turns[O][2] == (2, 2):
                    if turns[X][1] == (1, 1):
                        best = (3, 3)
                    if turns[X][1] == (3, 1):
                        best = (1, 3)
                    if turns[X][1] == (3, 3):
                        best = (1, 1)
                    if turns[X][1] == (1, 3):
                        best = (3, 1)
                else:
                    # check for available adjacent corner to TURN 1 X and place it there
                    for i in get_adj_corner:
                        if turns[O][2] == i:
                            pass
                        else:
                            best = i
                    # If both are occupied place in opposite corner of the TURN 1 X
                    if best == None:
                        if turns[X][1] == (1, 1):
                            best = (3, 3)
                        if turns[X][1] == (3, 1):
                            best = (1, 3)
                        if turns[X][1] == (3, 3):
                            best = (1, 1)
                        if turns[X][1] == (1, 3):
                            best = (3, 1)
                all_coor.remove(best)
                turns[X][turn] = best
                cx, cy = best
                row1, row2, row3, col1, col2, col3 = place(turn,
                                                           cx, cy, row1, row2, row3, col1, col2, col3)
                rowboard = rowb_make(row1, row2, row3)
                colboard = rowb_make(col1, col2, col3)
            elif turn == 5:
                best = None
                if turns[O][2] == (2, 2):
                    '''
                    - this means the X is placed in the opposite corners of the diagonal
                    - next X must be placed in the relative corner of the two corners X is already placed in
                    '''
                    get_adj_corner = [corner_co_ords[i-1]
                                      for i in adjacent_corners[turns[X][3]]]
                    for i in get_adj_corner:
                        if turns[O][2] == i:
                            pass
                        else:
                            best = i
                    all_coor.remove(best)
                    turns[X][turn] = best
                    cx, cy = best
                    row1, row2, row3, col1, col2, col3 = place(turn,
                                                               cx, cy, row1, row2, row3, col1, col2, col3)
                    rowboard = rowb_make(row1, row2, row3)
                    colboard = rowb_make(col1, col2, col3)
                else:
                    # check if O is put between the Adjacent corner X
                    betweenx, betweeny = (
                        turns[X][1][0]+turns[X][3][0])//2, (turns[X][1][1]+turns[X][3][1])//2
                    if element(betweenx, betweeny, rowboard) != O:
                        all_coor.remove((betweenx, betweeny))
                        turns[X][turn] = (betweenx, betweeny)
                        row1, row2, row3, col1, col2, col3 = place(turn,
                                                                   betweenx, betweeny, row1, row2, row3, col1, col2, col3)
                        rowboard = rowb_make(row1, row2, row3)
                        colboard = rowb_make(col1, col2, col3)

                    else:
                        # get the adjacent corners of the X in turn 1 and 3
                        get_adj_corner_to_1 = [corner_co_ords[i-1] for i in adjacent_corners[turns[X][1]] if element(
                            corner_co_ords[i-1][0], corner_co_ords[i-1][1], rowboard) != X][0]
                        get_adj_corner_to_3 = [corner_co_ords[i-1] for i in adjacent_corners[turns[X][3]] if element(
                            corner_co_ords[i-1][0], corner_co_ords[i-1][1], rowboard) != X][0]
                        # to check if there is obstruction to either corner
                        for i in (get_adj_corner_to_1, get_adj_corner_to_3):
                            x, y = i

                            if element(x, y, rowboard) != O:
                                if i == get_adj_corner_to_1:
                                    betweenx, betweeny = (
                                        turns[X][1][0]+i[0])//2, (turns[X][1][1]+i[1])//2
                                else:
                                    betweenx, betweeny = (
                                        turns[X][3][0]+i[0])//2, (turns[X][3][1]+i[1])//2

                                if element(betweenx, betweeny, rowboard) != O:
                                    all_coor.remove((x, y))
                                    turns[X][turn] = (x, y)
                                    row1, row2, row3, col1, col2, col3 = place(turn,
                                                                               x, y, row1, row2, row3, col1, col2, col3)
                                    rowboard = rowb_make(row1, row2, row3)
                                    colboard = rowb_make(col1, col2, col3)
                                    break
                                else:
                                    continue
                                all_coor.remove(i)
                                turns[X][turn] = (x, y)
                                row1, row2, row3, col1, col2, col3 = place(turn,
                                                                           x, y, row1, row2, row3, col1, col2, col3)
                                rowboard = rowb_make(row1, row2, row3)
                                colboard = rowb_make(col1, col2, col3)
                                break
                            else:
                                continue
                        else:
                            # to check if the O is in between the X in turn 5 and turn 1 or turn 3 to check best corner
                            for i in (get_adj_corner_to_1, get_adj_corner_to_3):
                                betweenx, betweeny = (
                                    turns[X][1][0]+i[0])//2, (turns[X][1][1]+i[1])//2
                                if element(betweenx, betweeny, rowboard) != O:
                                    all_coor.remove((x, y))
                                    turns[X][turn] = (x, y)
                                    row1, row2, row3, col1, col2, col3 = place(turn,
                                                                               x, y, row1, row2, row3, col1, col2, col3)
                                    rowboard = rowb_make(row1, row2, row3)
                                    colboard = rowb_make(col1, col2, col3)
                                else:
                                    continue
            elif turn == 7:
                for i in all_coor:
                    x, y = i
                    row1, row2, row3, col1, col2, col3 = place(turn,
                                                               x, y, row1, row2, row3, col1, col2, col3)
                    rowboard = rowb_make(row1, row2, row3)
                    colboard = rowb_make(col1, col2, col3)
                    w = winners_check(row1, row2, row3, col1,
                                      col2, col3, rowboard)
                    if w[0] == X:
                        break
                    else:
                        if x == 1:
                            col1[y-1] = ""
                        elif x == 2:
                            col2[y-1] = ""
                        elif x == 3:
                            col3[y-1] = ""

                        if y == 1:
                            row1[x-1] = ""
                        elif y == 2:
                            row2[x-1] = ""
                        elif y == 3:
                            row3[x-1] = ""

        else:
            # players turn
            while True:
                print()
                co_ordinate = tuple(
                    eval(input("Enter coordinate of placing O : ")))
                turns[O][turn] = co_ordinate
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
