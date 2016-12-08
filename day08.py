
def make_board(rows,cols):
    line=['.' for i in range(cols)]
    board = [line.copy() for i in range(rows)]
    return board
    

def rect(board,x,y):
    
    for row in range(y):
        for col in range(x):
            board[row][col]='#'
    return board

#list(map(list, zip(*l)))
def rotate_row(board,row,amt):
    board[row] = board[row][-amt:] + board[row][0:-amt]
    return board

def rotate_col(board,col,amt):
    board = list(map(list,zip(*board)))
    rotate_row(board,col,amt)
    board = list(map(list,zip(*board)))
    return board

def count(board):
    c=0
    for r in board:
        c=c+len([x for x in r if x =='#']) 
    return c

board = make_board(6,50)
input = open("day08.dat").readlines()
for line in input:
    c = line.split()[0]
    if c=="rect":
        rest=line.split()[1]
        (x,y)=rest.split("x")
        x = int(x)
        y=int(y)
        board= rect(board,x,y)
    else:
        (d1,c,loc,d,amt) = line.split()
        amt = int(amt)
        loc = int( loc.split("=")[1] )
        if c=='row':
            board = rotate_row(board,loc,amt)
        else:
            board = rotate_col(board,loc,amt)

print(board)
for r in board:
    s="".join(r)
    s=s.replace("."," ")
    print(s)

print(count(board))

