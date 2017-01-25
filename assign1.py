# Randomly generate an n by m board.
# has spots 0-9, S, G, and #
import random
spots = ['1','2','3','4','5','6','7','8','9','#']

def h0(node):
    return 0

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
    #print(chars)

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
    while(i < len(queue) and cost < queue[i].cost + queue[i].hCost):
        i += 1
    queue.insert(i, node)
    
def getCost(str):
    if(str[0] == 'S' or str[0] == 'G'):
        return 1;
    else:
        return int(str);

def expandNode(node, queue, board, h):
    newActions = list(node.actions)
    
    f = node.direction
    r = [f[1],-1*f[0]]
    l = [-1*f[1], f[0]]
    b = [-1*f[0], -1*f[1]]
    
    spot = [node.row+f[0], node.col+f[1]] #forward
    if(spot[0] < len(board) and spot[1] < len(board[0])):     
        if(board[spot[0]][spot[1]] != '#'):
            newActions.append("f");
            n = Node(spot[0], spot[1], f, node.cost + getCost(board[spot[0]][spot[1]]), 0, newActions);
            n.hCost = h(n);
            addToList(n, queue);
            
    spot = [node.row+3*f[0], node.col+3*f[1]]; #jump forward
    if(spot[0] < len(board) and spot[1] < len(board[0])):
        if(board[spot[0]][spot[1]] != '#'):
            newActions.append("j");
            n = Node(spot[0], spot[1], f, node.cost + 20, 0, newActions);
            n.hCost = h(n);
            addToList(n, queue);
            
    spot = [node.row+r[0], node.col+r[1]]; #right
    if(spot[0] < len(board) and spot[1] < len(board[0])):
        if(board[spot[0]][spot[1]] != '#'):
            newActions.append("r");
            newActions.append("f");
            n = Node(spot[0], spot[1], r, node.cost + (1/3)*getCost(board[node.row][node.col]) + getCost(board[spot[0]][spot[1]]), 0, newActions);
            n.hCost = h(n);
            addToList(n, queue);
            
    spot = [node.row+3*r[0], node.col+3*r[1]]; #jump right
    if(spot[0] < len(board) and spot[1] < len(board[0])):
        if(board[spot[0]][spot[1]] != '#'):
            newActions.append("r");
            newActions.append("j");
            n = Node(spot[0], spot[1], r, node.cost + (1/3)*getCost(board[node.row][node.col]) + 20, 0, newActions);
            n.hCost = h(n);
            addToList(n, queue);
            
    spot = [node.row+l[0], node.col+l[1]]; #left
    if(spot[0] < len(board) and spot[1] < len(board[0])):
        if(board[spot[0]][spot[1]] != '#'):
            newActions.append("l");
            newActions.append("f");
            n = Node(spot[0], spot[1], l, node.cost + (1/3)*getCost(board[node.row][node.col]) + getCost(board[spot[0]][spot[1]]), 0, newActions);
            n.hCost = h(n);
            addToList(n, queue);
            
    spot = [node.row+3*l[0], node.col+3*l[1]]; #jump left
    if(spot[0] < len(board) and spot[1] < len(board[0])):
        if(board[spot[0]][spot[1]] != '#'):
            newActions.append("l");
            newActions.append("j");
            n = Node(spot[0], spot[1], l, node.cost + (1/3)*getCost(board[node.row][node.col]) + 20, 0, newActions);
            n.hCost = h(n);
            addToList(n, queue);
            
    spot = [node.row+b[0], node.col+b[1]]; #back
    if(spot[0] < len(board) and spot[1] < len(board[0])):
        if(board[spot[0]][spot[1]] != '#'):
            newActions.append("l");
            newActions.append("l");
            newActions.append("f");
            n = Node(spot[0], spot[1], b, node.cost + (2/3)*getCost(board[node.row][node.col]) + getCost(board[spot[0]][spot[1]]), 0, newActions);
            n.hCost = h(n);
            addToList(n, queue);
            
    spot = [node.row+3*b[0], node.col+3*b[1]]; #jump back
    if(spot[0] < len(board) and spot[1] < len(board[0])):
        if(board[spot[0]][spot[1]] != '#'):
            newActions.append("l");
            newActions.append("l");
            newActions.append("j");
            n = Node(spot[0], spot[1], b, node.cost + (2/3)*getCost(board[node.row][node.col]) + 20, 0, newActions);
            n.hCost = h(n);
            addToList(n, queue);

# queue - A sorted list of nodes to expand. Sorted based on the cost to
#   get to the node plus the heuristic cost. (starts continaing only the start node)
# h - The heuristic function to use. 
def search_node(queue, board, h):
    node = queue.pop()
    #print(node.actions)
    if(board[node.row][node.col][0] == 'G'):
        return node
    expandNode(node, queue, board, h);
    search_node(queue, board, h)
    
    

# Creates a node with the position of the s in the given board.
def get_initial_node(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'S':
                row, col = (i, j)
    return Node(row, col, [0,1], 0, 0, []) #row, col
    
    
    

class Space(object):
    def __init__(self, x, y, terrain, accessible):
        self.x = x
        self.y = y
        self.terrain = terrain
        self.accessible = accessible

class Node(object):
    def __init__(self, row, col, direction, cost, hCost, actions):
        self.col = col
        self.row = row
        self.direction = direction
        self.cost = cost
        self.hCost = hCost
        self.actions = actions

b = read_board("board2")
s = get_initial_node(b)
s.hCost = h0(s)
queue = [s]
result = search_node(queue, b, h0)  
