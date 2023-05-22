import random

board = [[2,2,2,0],
         [2,2,2,0],
         [0,0,0,0],
         [0,0,0,0]]

def print_board():
    global board
    for row in board:
        print(row)
    return True

def bubble(dir):
    Move(dir)
    if dir == "left" or dir == "right":
        for row in board:
            Merge(row, dir)
    else:
        for col in range(4):
            temp_list = []
            for row2 in board:
                    temp_list.append(row2[col])
            
            Merge(temp_list, dir)
            for row3 in range(4):
                board[row3][col] = temp_list[row3]

    Move(dir)
            

def Move(dir):
    global board
    # iterate through each row
    for row in board:
        # reset vars for each row
        consecutive_zeros = 0

        # iterate through each value in the row
        if dir == "left":
            for row_index in range(4):
                # count zeroes in a row
                if row[row_index] == 0:
                    consecutive_zeros += 1
                # if the value is not equal to 0, and there have been zeroes before it
                elif consecutive_zeros != 0:
                    # shift the non-zero value to the left
                    row[row_index - consecutive_zeros] = row[row_index]
                    # replace the non-zero value with zero
                    row[row_index] = 0
                    
                    try:
                        for consecutive_test in range(4 - row_index):
                            if row[row_index + consecutive_test] != 0:
                                # shift the non-zero value to the left
                                row[row_index + consecutive_test - consecutive_zeros] = row[row_index + consecutive_test]
                                # replace the non-zero value with zero
                                row[row_index + consecutive_test] = 0
                            elif (row_index != 2):
                                break
                    except:
                        consecutive_zeros = 1
                    
                    # reset consecutive zeroes
                    consecutive_zeros = 1

        elif dir == "right":
            for row_index in range(3,-1,-1):
                # count zeroes in a row
                if row[row_index] == 0:
                    consecutive_zeros += 1
                # if the value is not equal to 0, and there have been zeroes before it
                elif consecutive_zeros != 0:
                    # shift the non-zero value to the right
                    row[row_index + consecutive_zeros] = row[row_index]
                    # replace the non-zero value with zero
                    row[row_index] = 0
                
                    try:
                        for consecutive_test in range(row_index + 1):
                            if row[row_index - consecutive_test] != 0:
                                # shift the non-zero value to the right
                                row[row_index - consecutive_test + consecutive_zeros] = row[row_index - consecutive_test]
                                # replace the non-zero value with zero
                                row[row_index - consecutive_test] = 0
                            elif (row_index != 1):
                                break
                    except:
                        consecutive_zeros = 1
                    
                    # reset consecutive zeroes
                    consecutive_zeros = 1
            row = Merge(row, "backward")

        elif dir == "down":
            for col in range(4):
                temp_list = []
                consecutive_zeros = 0
                # create a temporary list of all the values in a column
                for row2 in board:
                    temp_list.append(row2[col])

                for col_index in range(3,-1,-1):
                    # count zeroes in a row
                    if temp_list[col_index] == 0:
                        consecutive_zeros += 1
                    # if the value is not equal to 0, and there have been zeroes before it
                    elif consecutive_zeros != 0:
                        # shift the non-zero value to the right in temp list
                        temp_list[col_index + consecutive_zeros] = temp_list[col_index]
                        # replace the non-zero value with zero
                        temp_list[col_index] = 0

                        for consecutive_test in range(col_index - 1):
                            if temp_list[col_index - consecutive_test] != 0:
                                # shift the non-zero value to the right in temp list
                                temp_list[col_index - consecutive_test + consecutive_zeros] = temp_list[col_index - consecutive_test]
                                # replace the non-zero value with zero
                                temp_list[col_index - consecutive_test] = 0
                            else:
                                break

                        # reset consecutive zeroes
                        consecutive_zeros = 1
                
                
                for row3 in range(4):
                    board[row3][col] = temp_list[row3]

            for col in range(4):
                temp_list = []
                consecutive_zeros = 0
                # create a temporary list of all the values in a column
                for row2 in board:
                    temp_list.append(row2[col])

                temp_list = Merge(temp_list, "forward")

                for row3 in range(4):
                    board[row3][col] = temp_list[row3]
                
            
        elif dir == "up":
            for col in range(4):
                col_index = 0
                temp_list = []
                consecutive_zeros = 0

                # create a temporary list of all the values in a column
                for row2 in board:
                    temp_list.append(row2[col])

                for col_index in range(4):
                    # count zeroes in a row
                    if temp_list[col_index] == 0:
                        consecutive_zeros += 1
                    # if the value is not equal to 0, and there have been zeroes before it
                    elif consecutive_zeros != 0:
                        # shift the non-zero value to the left in temp list
                        temp_list[col_index - consecutive_zeros] = temp_list[col_index]
                        # replace the non-zero value with zero
                        temp_list[col_index] = 0
                        try:
                            for consecutive_test in range(4 - col_index):
                                if temp_list[col_index + consecutive_test] != 0:
                                    # shift the non-zero value to the left in temp list
                                    row[col_index + consecutive_test - consecutive_zeros] = row[col_index + consecutive_test]
                                    # replace the non-zero value with zero
                                    row[col_index + consecutive_test] = 0
                                else:
                                    break
                        except:
                            consecutive_zeros = 0

                        # reset consecutive zeroes
                        consecutive_zeros = 1
                    
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

def Merge(merge_list, dir):
    if dir == "left" or dir == "up":
        for val in range(4):
            if val != 3:
                if merge_list[val] == merge_list[val + 1]:
                    merge_list[val] *= 2
                    merge_list[val + 1] = 0
    elif dir == "right" or dir == "down":
        for val in range(3, -1 , -1):
            if val != 0:
                if merge_list[val] == merge_list[val - 1]:
                    merge_list[val] *= 2
                    merge_list[val - 1] = 0
    return merge_list

running = True

while True:

    dir = input("Enter w, a, s, or d: ")
    if dir == "w":
        bubble("up")
    elif dir == "a":
        bubble("left")
    elif dir == "d":
        bubble("right")
    else:
        bubble("down")

    print_board()