# Randomly generate an n by m board.
# has spots 0-9, S, G, and #
import random
spots = ['1','2','3','4','5','6','7','8','9','#']

def h1(node):
    return 0

def getGoalPosition():
    for row_i, row in enumerate(b):
        for col_i, col in enumerate(b):
            if b[row_i][col_i] == 'G':
                return row_i, col_i
    return None

def getVerticalAndHorizontalDistance(node):
    vertical_distance = abs(goal_position[1] - node.col)  # get vertical distance
    horizontal_distance = abs(goal_position[0] - node.row)  # get horizontal distance

    return vertical_distance, horizontal_distance

def h2(node):
    vertical_distance, horizontal_distance = getVerticalAndHorizontalDistance(node)
    dist_to_use = min(vertical_distance, horizontal_distance)

    return dist_to_use

def h3(node):
    vertical_distance, horizontal_distance = getVerticalAndHorizontalDistance(node)

    dist_to_use = max(vertical_distance, horizontal_distance)

    return dist_to_use

# manhatten distance
def h4(node):
    vertical_distance, horizontal_distance = getVerticalAndHorizontalDistance(node)


    return vertical_distance + horizontal_distance

def h5(node):
    """
    If it has to turn once, its 1/3 the cost of the current node
    If it has to turn twice, its 2/3 the cost of the current node
    :param node:
    :return:
    """
    node_direction = node.direction
    node_col = node.col
    node_row = node.row
    node_cost = node.cost

    manhattan_distance = h4(node)


    if node_col == goal_position[1] or node_row == goal_position[1]:
        pass
    else:
        manhattan_distance += (1/3)*node_cost

    return manhattan_distance

def h6(node):
    return h5(node) * 3

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

def inBoard(spot, board):
    return ((spot[0] < len(board[0])) and (spot[0] >= 0) and (spot[1] < len(board)) and (spot[1] >= 0))
    
def tryMove(node, queue, board, h, direction, turns, jump, appendList):
    newActions = list(node.actions)
    if(jump):
        dist = 3
    else:
        dist = 1
    spot = [node.col + dist*direction[0], node.row + dist*direction[1]]; #col, row (x, y)
    if(inBoard(spot, board)):
        boardVal = board[spot[1]][spot[0]]
        if(boardVal != "#"):
            for string in appendList:
                newActions.append(string)
            cost = node.cost + (1/3) * turns * getCost(board[node.row][node.col])
            if(jump):
                cost += 20
            else:
                cost += getCost(boardVal)
            n = Node(spot[1], spot[0], direction, cost, 0, list(newActions))
            n.hCost = h(n)
            addToList(n, queue)
        

def expandNode(node, queue, board, h): 
    f = node.direction                     #        [0, -1]
    r = [-1*f[1], f[0]]                    #  [-1,0]       [1,0]
    l = [f[1], -1*f[0]]                    #        [0, 1]
    b = [-1*f[0], -1*f[1]]
    
    tryMove(node, queue, board, h, f, 0, 0, ["f"]) #forward
    tryMove(node, queue, board, h, f, 0, 1, ["j"]) #jump forward
    
    tryMove(node, queue, board, h, r, 1, 0, ["r", "f"]) #right
    tryMove(node, queue, board, h, r, 1, 1, ["r", "j"]) #jump right
    
    tryMove(node, queue, board, h, l, 1, 0, ["l", "f"]) #left
    tryMove(node, queue, board, h, l, 1, 1, ["l", "j"]) #jump left
    
    tryMove(node, queue, board, h, b, 2, 0, ["r", "r", "f"]) #back
    tryMove(node, queue, board, h, b, 2, 1, ["r", "r", "j"]) #jump back


# queue - A sorted list of nodes to expand. Sorted based on the cost to
#   get to the node plus the heuristic cost. (starts continaing only the start node)
# h - The heuristic function to use. 
def search_node(node, board, h):
    queue = [node]
    n = queue.pop()
    expanded = 0
    while(board[n.row][n.col][0] != 'G'):
        expandNode(n, queue, board, h);
        n = queue.pop()
        expanded += 1
    print(n.actions)
    print("Score: " + str(500-n.cost))
    print("Nodes expanded: " + str(expanded))
    return n

# Creates a node with the position of the s in the given board.
def get_initial_node(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'S':
                row, col = (i, j)
    return Node(row, col, [0,-1], 0, 0, []) #row, col
    
    
    

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

b = read_board("board1")
s = get_initial_node(b)

goal_position = getGoalPosition()

print("Heuristic Six:")
s.hCost = h6(s)
result = search_node(s, b, h6)
print("")

print("Heuristic Five:")
s.hCost = h5(s)
result = search_node(s, b, h5)
print("")

print("Heuristic four:")
s.hCost = h4(s)
result = search_node(s, b, h4)
print("")

print("Heuristic three:")
s.hCost = h3(s)
result = search_node(s, b, h3)
print("")

print("Heuristic two:")
s.hCost = h2(s)
result = search_node(s, b, h2)
print("")

print("Heuristic one:")
s.hCost = h1(s)
result = search_node(s, b, h1)
print("")

