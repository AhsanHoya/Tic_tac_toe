
"""
Tic Tac Toe 

Tasks:
-print board
-take turn
-check win


"""
#d = [[2,1,0,1],[0,3,0,1],[0,0,5,1],[1,2,1,1]]

grid = [[0,0,0],[0,0,0],[0,0,0]]


def print_board(board):
    for i in board:
        for j in i:
            print (j, end=" ")
        print ("")

def take_turn(turn):
    print("Player", turn, "turn:")
    x = int(input("choose your column: "))
    y = int(input("choose your row: "))
    """
    Range Check: If user input column and row is out of range 0-2
    print error message and retry.
    """
    if (x < 0 or x > 2) or (y < 0 or y > 2):
        print("Out of Range. Select 0-2. Are ya crazy?")
        take_turn(turn)
        return
    """
    If the cell is taken, print error message and retry. If the number is anything over 0
    """
    if grid[x][y] > 0:
        print("What ya doin'?")
        take_turn(turn)
        return
    grid[x][y] = turn

def check_win(turn):
    """
    if one cell and the one under it and the one under it are the same, then the player wins.
    And...if the cell im talking about and the one under the on enext to it
    if (x,y) (x+1,y) (x+2,y) are the same, or (x,y) (x,y+1), (x,y+2) are the same, or (x,y) (x+1,y+1) (x+2,y+2) are the same
    The player wins (?)
    """
    #if grid[x][y] [x][y] == x+1==x+2

    for x in range(3): # vert
        if grid[x][0] == turn:
            if grid[x][1] == turn:
                if grid[x][2] == turn:
                    # WIN
                    pass


    for y in range(3): # horz
        if grid[0][y] == turn:
            if grid[1][y] == turn:
                if grid[2][y] == turn:
                    # WIN
                    pass
    #diagonals
    if 
def main():
    print_board(grid)
    for _ in range(9):
        take_turn(1)
        print_board(grid)
        check_win()
        
        take_turn(2)
        print_board(grid)
        check_win()
    


main(