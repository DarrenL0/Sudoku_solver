






sudoku_board = [
    [0,0,0,2,6,0,7,0,1],
    [6,8,0,0,7,0,0,9,0],
    [1,9,0,0,0,4,5,0,0],
    [8,2,0,1,0,0,0,4,0],
    [0,0,4,6,0,2,9,0,0],
    [0,5,0,0,0,3,0,2,8],
    [0,0,9,3,0,0,0,7,4],
    [0,4,0,0,5,0,0,3,6],
    [7,0,3,0,1,8,0,0,0],
]

def display_board(board):
    for i in range(len(board)):
        if i != 0 and i % 3 == 0:
            print("========================")
            
        for j in range(len(board[0])):
            if j != 0 and j % 3 == 0:
                print(" | ", end="")
                
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")
                
def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                #returning the row and column of a blank space
                return (i,j)
    return None

def valid(board, number, position):
    #check row
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False
    #check column 
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False
    
    #check space
    space_x = position[1] // 3
    space_y = position[0] // 3
    
    for i in range(space_y*3, space_y*3 + 3):
        for j in range(space_x * 3, space_x*3 + 3):
            if board[i][j] == number and (i,j) != position:
                return False
    return True

def solve(board):
    finder = find_blank(board)
    
    if not finder:
        return True
    else:
        row, column = finder
        
    for i in range(1,10):
        if(valid(board,i,(row,column))):
            board[row][column] = i
            
            if solve(board):
                return True
            
            board[row][column] = 0
    return False
    



display_board(sudoku_board)
solve(sudoku_board)


print("\n===========================\n")
display_board(sudoku_board)