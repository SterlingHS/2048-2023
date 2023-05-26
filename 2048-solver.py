import random
import math

board = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

def print_board():
    global board
    for row in board:
        print(row)
    return True

def bubble(dir, simulation):
    bd = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]
    bd = Move(dir, simulation, bd)
    if dir == "a" or dir == "d":
        for row in bd:
            Merge(row, dir)
    else:
        for col in range(4):
            temp_list = []
            for row2 in bd:
                    temp_list.append(row2[col])
            
            temp_list = Merge(temp_list, dir)
            for row3 in range(4):
                bd[row3][col] = temp_list[row3]

    bd = Move(dir, simulation, bd)

    if not simulation:
        for row in range(4):
            for col in range(4):
                board[row][col] = bd[row][col]

    return bd
            

def Move(dir, simulation, bd):
    global board
    if bd == [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]:
        for row in range(4):
                for col in range(4):
                    bd[row][col] = board[row][col]
    # iterate through each row
    for row in bd:
        # reset vars for each row
        consecutive_zeros = 0

        # iterate through each value in the row
        if dir == "a":
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

        elif dir == "d":
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

        elif dir == "s":
            for col in range(4):
                temp_list = []
                consecutive_zeros = 0
                # create a temporary list of all the values in a column
                for row2 in bd:
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
                    bd[row3][col] = temp_list[row3]

            for col in range(4):
                temp_list = []
                consecutive_zeros = 0
                # create a temporary list of all the values in a column
                for row2 in bd:
                    temp_list.append(row2[col])

                temp_list = Merge(temp_list, "forward")

                for row3 in range(4):
                    bd[row3][col] = temp_list[row3]
                
            
        elif dir == "w":
            for col in range(4):
                col_index = 0
                temp_list = []
                consecutive_zeros = 0

                # create a temporary list of all the values in a column
                for row2 in bd:
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
                    bd[row3][col] = temp_list[row3]

    if simulation == False:
        for row in range(4):
            for col in range(4):
                board[row][col] = bd[row][col]
                
    return bd

def add_random():
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
    if dir == "a" or dir == "w":
        for val in range(3):
            if merge_list[val] == merge_list[val + 1]:
                merge_list[val] *= 2
                merge_list[val + 1] = 0
    elif dir == "d" or dir == "s":
        for val in range(3, 0 , -1):
            if merge_list[val] == merge_list[val - 1]:
                merge_list[val] *= 2
                merge_list[val - 1] = 0
    return merge_list

def check_moves():
    moves = []

    if bubble("w", True) != board:
        moves.append("w")
    if bubble("a", True) != board:
        moves.append("a")
    if bubble("d", True) != board:
        moves.append("d")
    if bubble("s", True) != board:
        moves.append("s")

    return moves

def game_over():
    global board
    global maxes

    max_value = 0
    for row in board:
        if max(row) > max_value:
            max_value = max(row)

    
    maxes[int(math.log2(max_value))] += 1

    board = [[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]
    add_random()

def get_percentages():
    max_sum = sum(maxes)
    ind = 0
    for val in maxes:
        if val != 0:
            print(val / max_sum * 100, "% - ", 2**ind)
        ind += 1

    
maxes = [0,0,0,0,0,0,0,0,0,0,0,0,0]

def random_strategy():
    return random.choice(possible_moves)

def manual_play():
    print_board()
    return input("Enter w, a, s, or d: ")

def left_down_strat():
    global last_move
    move_to_take = ""
    moves = check_moves()
    if last_move == "s" and "a" in moves and ("a" in moves or "s" in moves):
        move_to_take = "a"
        last_move = "a"
    elif "s" in moves and ("a" in moves or "s" in moves):
        move_to_take = "s"
        last_move = "s"
    elif "d" in moves:
        move_to_take = "d"
    else:
        move_to_take = "w"
    
    return move_to_take

def simulate_scores_strat():
    left_score = 0
    right_score = 0
    up_score = 0
    down_score = 0
    scores = [left_score, right_score, up_score, down_score]
    left_merges = 0
    right_merges = 0
    up_merges = 0
    down_merges = 0
    left_zeroes = 0
    right_zeroes = 0
    up_zeroes = 0
    down_zeroes = 0
    left_sum = 0
    right_sum = 0
    up_sum = 0
    down_sum = 0
    

    for row in range(4):
        last_match = 0
        for val in range(3,-1,-1):
            if board[row][val] == board[row][val - 1] and last_match == 0:
                right_merges += 1
                last_match = 1     
            elif last_match != 0:
                last_match = 0

        last_match = 0
        for val in range(3):
            if board[row][val] == board[row][val + 1] and last_match == 0:
                left_merges += 1
                last_match = 1     
            elif last_match != 0:
                last_match = 0 

        temp_list = []
        for row2 in range(4):
            temp_list.append(board[row][row2])

        last_match = 0
        for val in range(3,-1,-1):
            if temp_list[val] == temp_list[val - 1] and last_match == 0:
                down_merges += 1
                last_match = 1     
            elif last_match != 0:
                last_match = 0
        
        last_match = 0
        for val in range(3):
            if temp_list[val] == temp_list[val + 1] and last_match == 0:
                up_merges += 1
                last_match = 1     
            elif last_match != 0:
                last_match = 0
    
    for row in Move("d",True,board):
        right_corner = 0
        right_max_block = 0
        if max(row) > right_max_block:
            right_max_block = max(row)
        if row.index(right_max_block) == 3 or 0:
            right_corner = 1
        for val in range(4):
            if row[val] == 0:
                right_zeroes += 1
            right_sum += row[val]
        
    for row in Move("w",True,board):
        up_corner = 0
        up_max_block = 0
        if max(row) > up_max_block:
            up_max_block = max(row)
        if row.index(up_max_block) == 3 or 0:
            up_corner = 1

        for val in range(4):
            if row[val] == 0:
                up_zeroes += 1
            up_sum += row[val]
    for row in Move("s",True,board):
        down_corner = 0
        down_max_block = 0
        for row2 in range(4):
            if max(row) > down_max_block:
                down_max_block = max(row)
        if row.index(down_max_block) == 3 or 0:
            down_corner = 1

        for val in range(4):
            if row[val] == 0:
                down_zeroes += 1
            down_sum += row[val]

    for row in Move("a",True,board):
        left_corner = 0
        left_max_block = 0
        if max(row) > left_max_block:
            left_max_block = max(row)
        if row.index(left_max_block) == 3 or 0:
            left_corner = 1

        # temp_list = []
        # for val in range(4):
        #     if row[val] == row[val + 1]:
        #         future_merges_left += 1
            # temp_list.append(board[row][val])

            

        for val in range(4):
            if row[val] == 0:
                left_zeroes += 1
            left_sum += row[val]

    zeroes_weight = 0.5
    sum_weight = 0.1
    merge_weight = 1
    corner_weight = 10

    left_score = (left_merges * merge_weight) + (left_zeroes * zeroes_weight) + (left_sum * sum_weight) + (left_corner * corner_weight)
    right_score = (right_merges * merge_weight) + (right_zeroes * zeroes_weight) + (right_sum * sum_weight) + (right_corner * corner_weight)
    up_score = (up_merges * merge_weight) + (up_zeroes * zeroes_weight) + (up_sum * sum_weight) + (up_corner * corner_weight)
    down_score = (down_merges * merge_weight) + (down_zeroes * zeroes_weight) + (down_sum * sum_weight) + (down_corner * corner_weight)

    max_score = max(scores)
    ind = 0
    inputs = ["a","d","w","s"]
    actions = []
    
    for score in scores:
        if score == max_score:
            actions.append(inputs[ind])
        ind += 1
    if len(actions) != 4:
        to_return = random.choice(actions)
    else:
        to_return = left_down_strat()

    return to_return

def start_game():
    global board
    board = [[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]
    add_random()
    add_random()

last_move = "s"
times_to_play = int(input("how many times to play?"))
start_game()

while 1:
    
    possible_moves = check_moves()
    if len(possible_moves) == 0: 
        if times_to_play == 0:
            get_percentages()
            break
        game_over()
        times_to_play -= 1
    else:
        # print_board()
        # print("")
        dir = simulate_scores_strat()

    bubble(dir,False)

    add_random()
