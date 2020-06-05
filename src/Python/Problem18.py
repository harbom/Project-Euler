"""By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

graph = {}
class Node():
    def __init__(self,val):
        self.val = val

def assign_node_nodelist(lines,index,thisnode):
    if (index+1 >= len(lines)):
        graph[thisnode] = []
    else:
        nextline = [int(j) for j in lines[index+1].split(" ")] #the next line in the data file
        #print(nextline)

        nextnodelist = []
        for num in nextline:
            print(num)
            newnode = Node(int(num))
            nextnodelist.append(newnode)
            assign_node_nodelist(lines,index+1,newnode)
        
        graph[thisnode] = nextnodelist #assign the node 

nodeArray = []
def init_graph():
    r = open("Problem18Data.txt")
    lines = r.readlines()
    lines = [i[:-1] for i in lines] #remove the \n
    lines = [i.split(" ") for i in lines]

    #add all nodes to a huge nodeArray
    for currline in lines:
        newentry = []
        for val in currline:
            newentry.append(Node(int(val)))
        nodeArray.append(newentry)
    
    #for each line, add to the map: graph[val] = nextline
    for i in range(len(nodeArray)):
        currarray = nodeArray[i]
        for j in range(len(currarray)):
            currnode = currarray[j]
            if (i == len(nodeArray)-1):
                graph[currnode] = [] #put a blank array for 
            else:
                #have to make sure only adjacent members in the next line are added
                graph[currnode] = [nodeArray[i+1][j], nodeArray[i+1][j+1]]
    
    #print(lines)
    #printNodeArray(newNodeArray);
    #rootnode = Node(int(lines[0]))
    #assign_node_nodelist(lines,0,rootnode)
    
    #confirm its working ok
    #print_graph()

def printNodeArray(arr):
    for line in arr:
        for node in line:
            print(node.val)
        print()

def print_graph():
    for g in graph:
            print("key: ",g.val,"  nextlist: ",[i.val for i in graph[g]])

visited = set() #keeping track of nodes already visited

maxlist = [0]
def DFS(visited, graph, node, sum):
    if node not in visited:
        sum += node.val
        print("curr val: ",node.val,"  sum: ",sum)
        visited.add(node)
        nextnodelist = graph[node]
        if (len(nextnodelist) == 0): #the bottom most nodes
            maxlist.append(sum)
        for nextnode in nextnodelist:
            DFS(visited,graph,nextnode, sum)

def regularRecursion(node,sum):
    sum += node.val
    nextnodelist = graph[node]
    if len(nextnodelist) == 0: #bottom of the triangle
        if sum > maxlist[0]:
            maxlist[0] = sum
    else:
        regularRecursion(nextnodelist[0],sum) #only have 2 chilren: adjacent ones
        regularRecursion(nextnodelist[1],sum)    
def main():
    init_graph()
    root = nodeArray[0][0]
    #print(root.val) cool n good

    #do DFS
    #DFS(visited, graph, root, 0)
    
    #do regular recursion
    regularRecursion(root,0)
    print(max(maxlist))


if __name__ == '__main__':
    main()