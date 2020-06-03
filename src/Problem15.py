#Lattice paths problem 15
#Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#How many such routes are there through a 20×20 grid?

size=20
past=[[0 for i in range(size+1)] for i in range(size+1)] #initialize a blank 2D array

def main():
    #initialize top and left sides of grid to 1
    for x in range(len(past)):
        for y in range(len(past[0])):
            if (x==0 or y==0):
                past[x][y] = 1
    
    #DP: past[x][y]=past[x-1][y] + past[x][y-1]
    for x in range(1,len(past)):
        for y in range(len(past[0])):
            past[x][y] = past[x-1][y] + past[x][y-1]

    #print(past)
    print(past[size][size])


#function to get the idea behind the pattern of the grid
def do(x,y):
    print("curr: ",x,y,past)
    if (x>size or y>size):
        return;
    
    #the program got here: increment number of ways to get to this point by 1
    
    past[x][y] = past[x-1][y] + past[x][y-1]

    #go on to further iterations
    do(x+1,y)
    do(x,y+1)

if __name__=="__main__":
    main()   