my_name = "Ahmet Atar"
my_id = "161024045"
my_email = "ahmet.atar2016@gtu.edu.tr"

import random
def generate(row,column):
    b = list(range(0,(row*column)))
    board = f1(b,column)
    return board
def f1(liste,n):
        x = len(liste)/float(n)
        y = []
        last = 0.0
        while last < len(liste):
            y.append(liste[int(last):int(last + x)])
            last += x
        return y
    

    
def shuffle(board,times=20):
    a = 0
    output = []
    while a < times:
        k = move_random(board)
        if k == None:
            pass
        else:
            output.append(k)
        a += 1
    return str(output)

#    
    
def is_valid(board):
    if 1 < len(board) <= 10 :
        return True
    else:
        return False
    
def is_solved(board):
    row = len(board)
    column = len(board[0])
    b_solved = list(range(0,(row*column)))
    b_solved = f1(b_solved,column)
    if board == b_solved:
        return True
    else:
        return False

def move_right(board):
    c = len(board[0])
    for i in range(0,len(board)):
        if 0 in board[i]:
            a = board[i].index(0)
            if a == c-1:
                return 0
            else:
                board[i][a],board[i][a+1] = board[i][a+1],board[i][a] 
            return 1
    
def move_left(board):
    for i in range(0,len(board)):
        if 0 in board[i]:
            a = board[i].index(0)
            if a == 0:
                return 0
            else:
                board[i][a],board[i][a-1] = board[i][a-1],board[i][a] 
            return 1

def move_up(board):
     for i in range(0,len(board)):
         if 0 in board[i]:
             a = board[i].index(0)
             if i == 0:
                return 0
             else:
                board[i][a],board[i-1][a] = board[i-1][a],board[i][a] 
             return 1

def move_down(board):
     r = len(board)
     for i in range(0,len(board)):
         if 0 in board[i]:
             a = board[i].index(0)
             if i == r-1:
                return 0
             else:
                board[i][a],board[i+1][a] = board[i+1][a],board[i][a] 
             return 1
    
def move_random(board):
    r = len(board)
    c = len(board[0])
    move_list = ["right","left","up","down"]
    b = random.sample(move_list,1)
    for i in range(0,r):
        if 0 in board[i]:
            a = board[i].index(0)
            k = i
            break
    if b == ["right"]:
        if a == c-1:
            move_list.remove("right")
            b = random.sample(move_list,1)
            if b == ["up"]:
                if k == 0:
                    move_list.remove("up")
                    b = random.sample(move_list,1)
                    if b == ["left"]:
                        board = move_left(board)
                        return "L"
                    else:
                        board = move_down(board)
                        return "D"
                else:
                    board = move_up(board)
                    return "U"
        else:
            board = move_right(board)
            return "R"
    elif b == ["left"]:
        if a == 0:
            move_list.remove("left")
            b = random.sample(move_list,1)
            if b == ["up"]:
                if k == 0:
                    move_list.remove("up")
                    b = random.sample(move_list,1)
                    if b == ["right"]:
                        board = move_right(board)
                        return "L"
                    else:
                        board = move_down(board)
                        return "D"
                else:
                    board = move_up(board)
                    return "U"
        else:
            board = move_left(board)
            return "L"
    elif b == ["up"]:
        if k == 0:
            move_list.remove("up")
            b = random.sample(move_list,1)
            if b == ["left"]:
                if a == 0:
                    move_list.remove("left")
                    b = random.sample(move_list,1)
                    if b == ["right"]:
                        board = move_right(board)
                        return "R"
                    else:
                        board = move_down(board)
                        return "D"
                else:
                    board = move_left(board)
        else:
            board = move_up(board)
            return "U"
    elif b == ["down"]:
        if k == r-1:
            move_list.remove("down")
            b = random.sample(move_list,1)
            if b == ["right"]:
                if a == c-1:
                    move_list.remove("right")
                    b = random.sample(board,1)
                    if b == ["down"]:
                        board = move_down(board)
                        return "D"
                    else:
                        board = move_left(board)
                        return "L"
                else:
                    board = move_right(board)
                    return "R"
        else:
            board = move_down(board)
            return "D"
        
def print_board(board):
    r = len(board)
    c = len(board[0])
    print("="*c*2)
    for i in range(0,r):
        for j in range(0,c):
            print(board[i][j],end = "  ")
        print("||")
    print("="*c*2)
    
def reset(board):
    row = len(board)
    column = len(board[0])
    b_solved = list(range(0,(row*column)))
    b_solved = f1(b_solved,column)
    if board == b_solved:
        return None
    else:
        board = b_solved
        return None

def rotate(board):
#    r = len(board)
#    c = len(board[0])
#    for i in range(0,r-1):
#        for j in range(0,c-1):
#            board[i][j],board
    pass

                
def get_board_size(board):
    r = len(board)
    c = len(board[0])
    return (c,r)


if __name__ == "__main__":
    print(f"My name is {my_name}.")
    print(f"My number is {my_id}.")
    print(f"My email is {my_email}.")
          
            
            
            
            
            
    

        
        
        
    