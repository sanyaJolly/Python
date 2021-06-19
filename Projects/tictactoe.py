grid = []
for i in range(3):
    temp = []
    for j in range(3):
        temp.append(0)
    grid.append(temp)             
def win(grid, char):
    for i in range(3):
        b = True
        for j in range(3):
            if(grid[i][j]!= char):
                b=False
        if(b == True):
            return True
    
    for i in range(3):
        b=True
        for j in range(3):
           if  grid[j][i]!=char:
               b=False
        if b==True:
            return True

    b=True
    for i in range(3): 
        if(grid[i][i] != char):
            b=False
            break
    if b==True:
        return True
    
    b=True
    for i in range(3): 
        if(grid[i][2-i] != char):
            b=False
            break
    if b==True:
        return True
    return False
turn = 0
while(not win(grid, 'o') and not win(grid,'x')):
    if(turn == 9):
        print("its a draw!")
        break
    y=int(input(f'enter the row:'))
    x=int(input(f'enter the column:'))
    turn+=1
    if turn%2==0:
        grid[y][x] = 'o'
    else:
        grid[y][x]='x'

    for i in range(3):
        for j in range(3):
            print(grid[i][j], end=" ")
        print("")
    if(win(grid, 'o') == True):
        print("player 2 wins!!")
    if(win(grid, 'x') == True):
        print("player 1 wins!!")



