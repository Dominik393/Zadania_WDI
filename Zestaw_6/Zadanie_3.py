def minimal_number_of_moves(t, k, pos_y = 0, cost = 0):
    if pos_y == 0:
        cost = t[0][k]
    if k == 0 and pos_y < 7:
        a = minimal_number_of_moves(t, k, pos_y + 1, cost + t[pos_y + 1][k])
        b = minimal_number_of_moves(t, k + 1, pos_y + 1, cost + t[pos_y + 1][k + 1])
        if a <= b:
            cost = a
        else:
            cost = b
    elif k == 7 and pos_y < 7:
        a = minimal_number_of_moves(t, k - 1, pos_y + 1, cost + t[pos_y + 1][k - 1])
        b = minimal_number_of_moves(t, k, pos_y + 1, cost + t[pos_y + 1][k])
        if a <= b:
            cost = a
        else:
            cost = b
    else:
        if pos_y < 7:
            a = minimal_number_of_moves(t, k - 1, pos_y + 1, cost + t[pos_y + 1][k - 1])
            b = minimal_number_of_moves(t, k, pos_y + 1, cost + t[pos_y + 1][k])
            c = minimal_number_of_moves(t, k + 1, pos_y + 1, cost + t[pos_y + 1][k + 1])
            if a <= b:
                if a <= c:
                    cost = a
                else:
                    cost = c
            else:
                if b <= c:
                    cost = b
                else:
                    cost = c

    return  cost

chessboard = [
    [1,2,13,1,5,1,2,8],
    [1,3,13,1,5,1,2,8],
    [1,2,13,1,5,1,2,8],
    [1,2,13,1,5,1,2,8],
    [1,2,13,1,5,1,2,8],
    [1,2,13,1,5,1,2,8],
    [1,2,13,1,5,1,2,8],
    [1,2,13,1,5,1,2,8]
]

print(minimal_number_of_moves(chessboard, 7))