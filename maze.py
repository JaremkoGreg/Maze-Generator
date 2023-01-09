#This maze generator will be using the recursive backtrack algorithim.
import turtle
import random

#function which helps keep track of how many cells have been visited
def listsum(input):
    my_sum = 0
    for row in input:
        my_sum += sum(row)
    return my_sum

#function which generates the maze in a 3d array initially
def mazegenerate(sizex,sizey):
    #declaring needed variables
    Walls=[[[1,1,1,1] for a in range(sizex)] for b in range(sizey)]
    x=0
    y=0
    visitedsum=0
    currentcell=[x,y] 
    visited=[[0 for a in range(sizex)] for b in range(sizey)]
    visited[x][y]=1
    visitn=[[x,y]] #Stack keeps track of coordinates of cells visited
    n=0 #needed later on in the code to backtrack

    #while loop which stops running when all cells have been visited
    while visitedsum!=(sizex*sizey):
        options=[0,0,0,0] #start with no walls can be removed
        if y!=sizey-1:
            if visited[y+1][x]==0:
                options[1]=1
                #north wall can be removed
        if y!=0:
            if visited[y-1][x]==0:
                options[3]=1
                #south wall can be removed
        if x!=0:
            if visited[y][x-1]==0:
                options[0]=1
                #west wall can be removed
        if x!=sizex-1:
            if visited[y][x+1]==0:
                options[2]=1
                #east wall can be removed

        #if no wall can be broken down the program backtracks
        if options==[0,0,0,0]:
            currentcell=visitn[n-1]
            x=currentcell[0]
            y=currentcell[1]
            n=n-1
            
        else:
            cellfound=False
            while cellfound==False:
                randomint=random.randint(0,3)
                if options[randomint]==1:
                    if randomint==0:
                        oppisitecell=[currentcell[0]-1,currentcell[1]]#moves into west cell
                        Walls[currentcell[1]][currentcell[0]][0]=0#removes west wall
                        Walls[oppisitecell[1]][oppisitecell[0]][2]=0
                    elif randomint==1:
                        oppisitecell=[currentcell[0],currentcell[1]+1]#moves into north cell
                        Walls[currentcell[1]][currentcell[0]][1]=0#removes north wall
                        Walls[oppisitecell[1]][oppisitecell[0]][3]=0
                    elif randomint==2:
                        oppisitecell=[currentcell[0]+1,currentcell[1]]#moves into east cell
                        Walls[currentcell[1]][currentcell[0]][2]=0#removes east wall
                        Walls[oppisitecell[1]][oppisitecell[0]][0]=0
                    else:
                        oppisitecell=[currentcell[0],currentcell[1]-1]#moves into south cell
                        Walls[currentcell[1]][currentcell[0]][3]=0#removes south wall
                        Walls[oppisitecell[1]][oppisitecell[0]][1]=0
                    n=n+1
                    visitn.insert(n,oppisitecell)
                    currentcell=oppisitecell
                    visited[currentcell[1]][currentcell[0]]=1
                    x=currentcell[0]
                    y=currentcell[1]
                    cellfound=True
        visitedsum=listsum(visited)
    return(Walls)

#Displaying the maze using turtle
def printmaze(sizex,sizey,Walls):
    
    #setting up size of maze
    startx=250
    starty=-startx
    gridsize=(2*(-startx))/sizex

    #setting up how turtle will work
    turtle.color()
    turtle.clear()
    turtle.speed(0)
    
    #drawing the north walls edge and the west wall edge
    turtle.penup()
    turtle.goto(startx,starty)
    turtle.pendown()
    turtle.goto(-startx,starty)
    turtle.goto(-startx,-starty)
    turtle.setheading(0)

    #south wall of each cell
    for y in range(sizex):
        turtle.penup()
        turtle.goto(startx,-starty+gridsize*(y))
        for x in range(sizey):
            if Walls[y][x][3]==1:
                turtle.pendown()
            else:
                turtle.penup()
            turtle.forward(gridsize)
    turtle.left(90)
    
    #east wall of each cell
    for x in range(sizex):
        turtle.penup()
        turtle.goto(startx+gridsize*(x),-starty)
        for y in range(sizey):
            if Walls[y][x][0]==1:
                turtle.pendown()
            else:
                turtle.penup()
            turtle.forward(gridsize)

#-----------------Main--------------------------
#size of maze
sizex=3
sizey=3

#calling functions
walls=mazegenerate(sizex,sizey)
print(walls)
printmaze(sizex,sizey,walls)
quit = input("input any key to quit: ")