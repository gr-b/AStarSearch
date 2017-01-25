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
        f.write(rowStr + '\n')
    f.close()

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

def addToList(node, queue):
    i = 0
    cost = node.cost + node.hCost
    while(cost < queue[i].cost + queue[i].hCost):
        i++
    insert(i, node)
    

# queue - A sorted list of nodes to expand. Sorted based on the cost to
#   get to the node plus the heuristic cost. (starts continaing oonly the start node)
# h - The heuristic function to use. 
def search_node(queue, h):
    node = queue.pop()
    #forward n -> node.col + n*direction[0], node.row + n*direction[1] 
    #backward direction = [-1*direction[0], -1*direction[1]]
    #right direction = [direction[1],-1*direction[0]]
    #left direction = [-1*direction[1], direction[0]]

# Creates a node with the position of the s in the given board.
def get_initial_node(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'S':
                row, col = (i, j)
    return Node(col, row, [0,1], 0, 0, [], []) #col,row
    
    
    

class Space(object):
    def __init__(self, x, y, terrain, accessible):
        self.x = x
        self.y = y
        self.terrain = terrain
        self.accessible = accessible

class Node(object):
    def __init__(self, col, row, direction, cost, hCost, actions, children):
        self.col = col
        self.row = row
        self.direction = direction
        self.cost = cost
        self.hCost = hCost
        self.actions = actions
        self.children = children
        
