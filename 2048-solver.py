import random

board = [[0,2,0,0],
         [0,0,2,0],
         [2,0,0,2],
         [0,0,0,2]]

def Move_Left():
    global board
    for row in board:
        consecutive_zeros = 0
        row_index = 0

        for value in row:
            if value == 0:
                consecutive_zeros += 1
            elif consecutive_zeros != 0:
                row[row_index - consecutive_zeros] = row[row_index]
                row[row_index] = 0
                consecutive_zeros = 0
            row_index += 1
        print(row)
    return board

Move_Left()
