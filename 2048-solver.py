import random

board = [[0,2,0,0],
         [0,0,2,0],
         [2,0,0,2],
         [0,0,0,2]]

def print_board():
    global board
    for row in board:
        print(row)
    return True

def Move_Left():
    global board
    # iterate through each row
    for row in board:
        # reset vars for each row
        consecutive_zeros = 0
        row_index = 0
        # iterate through each value in the row
        for value in row:
            # count zeroes in a row
            if value == 0:
                consecutive_zeros += 1
            # if the value is not equal to 0, and there have been zeroes before it
            elif consecutive_zeros != 0:
                # shift the non-zero value to the left
                row[row_index - consecutive_zeros] = row[row_index]
                # replace the non-zero value with zero
                row[row_index] = 0
                # reset consecutive zeroes
                consecutive_zeros = 0
            # to track which index it is checking
            row_index += 1
    print_board()
    
    return

Move_Left()
