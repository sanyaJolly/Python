import random

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
    

turn = 0

while(not win(grid, 'X') and not win(grid, 'O')):
    if(turn == 9):
        print("It's a Draw ㄟ( ▔, ▔ )ㄏ")
        break

    # Human
    if turn%2==1:
        x,y=map(int,input().split())
        grid[x][y] = 'X'

    # AI 
    else:
        blank=[]
        for i in range(3):
            for j in range(3):
                if grid[i][j]==" ":
                    blank.append([i,j])
        x,y = blank[random.randint(0,len(blank)-1)]
        grid[x][y] = 'O'

    if win(grid,'X'):
        print("X Won!!😍😍")
    elif  win(grid,'O'):
        print("O Won!!👍.👌")

    show(grid)
    turn+=1

