#8 wide 10 tall
row = ['#',' ',' ',' ',' ',' ',' ','#']
bot = ['#','#','#','#','#','#','#','#']

board = [] #creates the list of the areas of the board
for r in range(9): 
    board.append(row.copy()) #9 rows of the list row, but copies it so it doesn't do the same commands for all of the rows (so they can all have their set x and y values)
board.append(bot) #1 row at the bottom with the bot list

def display_board(b): #creates a display for the board
    for r in b:
        s = ''
        for c in r:
            s += c
        print (s)
        
x = 3
y = 4
rotation = 0
piece = (((-1,0),(0,0),(0,-1),(1,0)),((0,0),(0,-1),(0,1),(1,0)))

shape=piece[0]
    
for spot in shape:
            nx = x + spot[0]
            ny = y + spot[1]
            board[ny][nx]='%' #draw piece in new location
board[y][x] = '*' #sets where the piece is with the asterisk
display_board(board)

def rotate(x, y, b, piece, rot):
    pass
    rot += 1
    rot %= len(piece)
    #need to see if it fits
    #need to return new rotation
    
def check_move (x, y, b, shape):
    #can the piece be moved to have its center at x, y?
    for spot in shape:
        nx = x + spot[0]
        ny = y + spot[1]
        if b[ny][nx] == '#': #spot is filled
            return False
    return True
    

#move_right notes from 4-4 class: this is how to move a SINGLE block to the right
#def move_right(x, y, b): #gives the pieces the ability to move to the right by increments of 1
#    if b[y][x+1] == ' ': #if space to the right is empty, move right
#        b[y][x+1] = '*'
#        b[y][x] = ' '
#        x += 1
#    return x

def move_right(x, y, b, shape):
    cx = x + 1
    cy = y
    if check_move(cx, cy, b, shape): #If space to right empty move right
        for spot in shape:
            nx = x + spot[0]
            ny = y + spot[1]
            b[ny][nx] =' ' #erase piece from old location
        x += 1
        for spot in shape:
            nx = x + spot[0]
            ny = y + spot[1]
            b[ny][nx]='%' #draw piece in new location
        b[y][x] = '*' #mark center location
        
    return x
            
