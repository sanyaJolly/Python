

grid=[]

for i in range(3):
    temp=[]
    for j in range(3):
        temp.append(" ")
    grid.append(temp)

def win(grid,char):
    # Horizontal
    for i in range(3):
        j=0
        while( j!= 3 and grid[i][j]==char):
            j=j+1
        if(j==3):
            return True 
    
    # for i in range(3):
    #     bool = True
    #     for j in range(3):
    #         if grid[i][j]!=char:
    #             bool=False

    # Vertical
    for i in range(3):
        j=0
        while(j != 3 and grid[j][i]==char):
            j=j+1
        if(j==3):
            return True 

    # Diagnol 1
    bool=True
    for i in range(3):
        if grid[i][i]!=char:
            bool=False
    if bool==True:
        return True
    
    # Diagnol 2
    bool=True
    for i in range(3):
        if grid[i][2-i]!=char:
            bool=False
    if bool==True:
        return True

    return False

def show(grid):
    for i in grid:
        print(*i, sep=" | ")
        print("--------")
    print("")

    # for i in range(3):
    #     for j in range(3):
    #         print(grid[i][j],end=" | ")
    #     print("")  
    #     print("-------------")  

def minimax(grid, minmax):
    if win(grid,'X'):
        return 1
    if win(grid,'O'):
        return -1
    bool = False
    for i in range(3):
        for j in range(3):
            if grid[i][j] == " ":
                bool = True
                break
    if bool == False:
        return 0
    blanks=[]
    # Maximize
    if minmax == True:
        best = -2
        for i in range(3):
            for j in range(3):
                if grid[i][j]==" ":
                    blanks.append([i,j])

        for i in blanks:
            grid_cpy = [row[:] for row in grid]
            grid_cpy[i[0]][i[1]] = 'X'
            temp = minimax(grid_cpy, False)
            if(temp > best):
                best = temp
        return best
    # Minimize
    else:
        best = 2
        for i in range(3):
            for j in range(3):
                if grid[i][j]==" ":
                    blanks.append([i,j])

        for i in blanks:
            grid_cpy = [row[:] for row in grid]
            grid_cpy[i[0]][i[1]] = 'O'
            temp = minimax(grid_cpy, True)
            if(temp < best):
                best = temp
        return best

turn = 0 

while(not win(grid, 'X') and not win(grid, 'O')):
    if(turn == 9):
        print("It's a Draw ㄟ( ▔, ▔ )ㄏ")
        break

    # Human
    if turn%2==0:
        x,y=map(int,input().split())
        grid[x][y] = 'O'

    # AI 
    else:
        best = -2
        best_move = []
        for i in range(3):
            for j in range(3):
                if(grid[i][j] == " "):
                    grid_cpy = [row[:] for row in grid]
                    grid_cpy[i][j] = 'X'
                    temp = minimax(grid_cpy, False)
                    if(temp > best):
                        best = temp
                        best_move = [i,j]   
        grid[best_move[0]][best_move[1]] = 'X'

    show(grid)    

    if win(grid,'X'):
        print("X Won!!😍😍")
    elif  win(grid,'O'):
        print("O Won!!👍.👌")

    
    turn+=1

