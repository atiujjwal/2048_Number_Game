import random

def start_the_game():
    mat = [[0]*4 for i in range(4)]
    return mat

def add_new2(mat):
    while(1):
        row = random.randint(0, 3)
        col = random.randint(0, 3)

        if mat[row][col] == 0:
            mat[row][col] = 2
            return mat
        

        
                
def is_game_over(mat):
    zero_present = False
    for i in range(4):
        if 0 in mat[i]:
            zero_present = True
    return not(zero_present)


def get_current_state(mat):
    zero_present, equal_present = False, False
    #anywhere if 2048 is present or zero is present
    for i in range(4): 
        if 2048 in mat[i]:
            return "won"
        if 0 in mat[i]:
            zero_present = True
            
    #if it there exist consecutive equal multiple of 2
    for i in range(4):
        for j in range(4):
            if (i+1 < 4 and mat[i][j] == mat[i+1][j]) or (j+1 < 4 and mat[i][j] == mat[i][j+1]):
                   equal_present = True
    
    #if either equal_present or zero_present is True, we continue the game
    if equal_present or zero_present:
        return "continue"
    #if both return value false, the game is lost
    return "lost"




def transpose(mat):
    trans = [[0] * 4 for i in range(4)]
    for i in range(4):
        for j in range(4):
            trans[i][j] = mat[j][i]
    return trans


def compress(mat):
    changed = False
    for i in range(4):
        idx = 0
        for j in range(4):
            if mat[i][j] != 0:
                mat[i][idx] = mat[i][j]
                if idx != j:
                    changed = True
                    mat[i][j] = 0
                idx += 1
    return mat, changed
                    
def merge(mat):
    changed = False
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:
                changed = True
                mat[i][j] = mat[i][j] * 2
                mat[i][j + 1] = 0
    return mat, changed


def reverse(mat):
    new_mat = []
    for i in range(4):
        new_mat.append(mat[i][::-1])
    for i in range(4):
        for j in range(4):
            mat[i][j] = new_mat[i][j]
    return mat
      
    
def move_up(mat): 
    mat = transpose(mat)
    mat, change1 = compress(mat)
    mat, change2 = merge(mat)
    mat, temp = compress(mat)
    mat = transpose(mat)
    return mat, change1 or change2

def move_down(mat):
    mat = transpose(mat)
    mat = reverse(mat)
    mat, change1 = compress(mat)
    mat, change2 = merge(mat)
    mat, temp = compress(mat)
    mat =  reverse(mat)
    mat = transpose(mat)
    return mat, change1 or change2
 
    
def move_right(mat):
    mat = reverse(mat)
    mat, change1 = compress(mat)
    mat, change2 = merge(mat)
    mat, temp = compress(mat)
    mat = reverse(mat) 
    return mat, change1 or change2



def move_left(mat):
    mat, change1 = compress(mat)
    mat, change2 = merge(mat)
    mat, temp = compress(mat)
    return mat, change1 or change2


