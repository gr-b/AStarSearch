# Randomly generate an n by m board.
# has spots 0-9, S, G, and #
import random
spots = ['1','2','3','4','5','6','7','8','9','#']

def gen_board(n, m):
    board = [[random.choice(spots) for i in range(n)] for i in range(m)]
    board[random.randint(0,m-1)][random.randint(0,n-1)] = 'S'
    board[random.randint(0,m-1)][random.randint(0,n-1)] = 'G'
    return board


def print_board(board):
    bstr= ""
    for row in board:
        rowStr = ""
        for spot in row:
            rowStr+= spot + "\t"
        print(rowStr)
        #print(rowStr)

# Save board to file

def save_board(board, filename):
    f = open(filename,'w')
    for row in board:
        rowStr = ""
        for spot in row:
            rowStr+= spot + "\t"
        rowStr = rowStr.rstrip()
        f.write(rowStr + '\n')
    f.close()
    with open(filename, 'rb+') as f2:
        f2.seek(-1, os.SEEK_END)
        f2.truncate()
        f2.close()

##def read_board(filename):
##    f = open(filename, 'r')
##    boardStr = f.read(1000)
##    chars = boardStr.split('\t')
##
##    i = 0
##    newboard = []
##    j = 0
##    while i < len(chars):
##        char = '#'
##        tmp = []
##        
##        while char != '\n':
##            char = chars[j]
##            i += 1
##            j += 1
##            #print(char)
##            tmp += char
##        newboard += [tmp]
##        
##    return newboard

def read_board(filename):
    f = open(filename, 'r')
    boardStr = f.read(1000)
    chars = boardStr.split('\t')
    print(chars)

    board = []
    row = []
    for c in chars:
        if "\n" in c:
            board += [row]
            row = []
            if len(c)>1:
                row += c[1]
        else:
            row += c

    f.close()
    return board
            
b = read_board("board2")
print_board(b)


    

class Space(object):
    def __init__(self, x, y, terrain, accessible):
        self.x = x
        self.y = y
        self.terrain = terrain
        self.accessible = accessible


