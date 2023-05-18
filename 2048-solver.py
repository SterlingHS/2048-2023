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

def Move(dir):
    global board
    # iterate through each row
    for row in board:
        # reset vars for each row
        consecutive_zeros = 0
        row_index = 0
        # iterate through each value in the row
        if dir == "left":
            for value in range(4):
                # count zeroes in a row
                if row[value] == 0:
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

        elif dir == "right":
            row_index = 3
            for value in range(3,-1,-1):
                # count zeroes in a row
                if row[value] == 0:
                    consecutive_zeros += 1
                # if the value is not equal to 0, and there have been zeroes before it
                elif consecutive_zeros != 0:
                    # shift the non-zero value to the left
                    row[row_index + consecutive_zeros] = row[row_index]
                    # replace the non-zero value with zero
                    row[row_index] = 0
                    # reset consecutive zeroes
                    consecutive_zeros = 0

                # to track which index it is checking
                row_index -= 1

        elif dir == "down":
            for col in range(4):
                col_index = 0
                temp_list = []
                consecutive_zeros = 0
                for row2 in board:
                    temp_list.append(row2[col])

                col_index = 3
                for value in range(3,-1,-1):
                    # count zeroes in a row
                    if temp_list[value] == 0:
                        consecutive_zeros += 1
                    # if the value is not equal to 0, and there have been zeroes before it
                    elif consecutive_zeros != 0:
                        # shift the non-zero value to the left
                        temp_list[col_index + consecutive_zeros] = temp_list[col_index]
                        # replace the non-zero value with zero
                        temp_list[col_index] = 0
                        # reset consecutive zeroes
                        consecutive_zeros = 0
                    
                    # to track which index it is checking
                    col_index -= 1

                
                for row3 in range(4):
                    board[row3][col] = temp_list[row3]
        
        elif dir == "up":
            for col in range(4):
                col_index = 0
                temp_list = []
                consecutive_zeros = 0

                for row2 in board:
                    temp_list.append(row2[col])

                for value in range(4):
                    # count zeroes in a row
                    if temp_list[value] == 0:
                        consecutive_zeros += 1
                    # if the value is not equal to 0, and there have been zeroes before it
                    elif consecutive_zeros != 0:
                        # shift the non-zero value to the left
                        temp_list[col_index - consecutive_zeros] = temp_list[col_index]
                        # replace the non-zero value with zero
                        temp_list[col_index] = 0
                        # reset consecutive zeroes
                        consecutive_zeros = 0
                    
                    # to track which index it is checking
                    col_index += 1

                
                for row3 in range(4):
                    board[row3][col] = temp_list[row3]
    
    return

def add_value():
    global board

    zeroes_pos = []

    for row in range(4):
        for col in range(4):
            if board[row][col] == 0:
                zeroes_pos.append((row,col))
    if len(zeroes_pos) == 0:
        return
    if(random.randint(0,9) < 9):
        value_to_add = 2
    else:
        value_to_add = 4

    pos_to_add = random.choice(zeroes_pos)
    board[pos_to_add[0]][pos_to_add[1]] = value_to_add

    return

Move("left")
Move("right")
print_board()