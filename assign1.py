# Randomly generate an n by m board.
# has spots 0-9, S, G, and #
import random
spots = ['0','1','2','3','4','5','6','7','8','9','#']

def gen_board(n, m):
    board = [[random.choice(spots) for i in range(n)] for i in range(m)]
    board[random.randint(0,n)][random.randint(0,m)] = 'S'
    board[random.randint(0,n)][random.randint(0,m)] = 'G'
    return board


def print_board(board):
    bstr= ""
    for row in board:
        rowStr = ""
        for spot in row:
            rowStr+= spot + "\t"
        bstr += rowStr
    print(bstr)
        #print(rowStr)

# Save board to file

def save_board(board, filename):
    f = open(filename,'w')
    for row in board:
        rowStr = ""
        for spot in row:
            rowStr+= spot + "\t"
        f.write(rowStr + '\n')
    f.close()

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

    board = []
    row = []
    for c in chars:
        if "\n" in c:
            board += [row]
            row = []
        else:
            row += c

    f.close()
    return board
            



    

class Space(object):
    def __init__(self, x, y, terrain, accessible):
        self.x = x
        self.y = y
        self.terrain = terrain
        self.accessible = accessible


