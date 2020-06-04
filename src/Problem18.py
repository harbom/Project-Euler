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

def init_graph():
    r = open("Problem18Data.txt")
    lines = r.readlines()
    lines = [i[:-1] for i in lines] #remove the \n
    #print(lines)

    rootnode = Node(int(lines[0]))
    assign_node_nodelist(lines,0,rootnode)
    
    #confirm its working ok
    #print_graph()

def print_graph():
    for g in graph:
        if graph[g]:
            print("key: ",g.val,"  nextlist: ",[i.val for i in graph[g]])
        else:
            print("key: ",g.val,"  nextlist: None")

visited = set() #keeping track of nodes already visited

def DFS(visited, graph, node):
    if node not in visited:
        print(node.val)
        visited.add(node)
        nextnodelist = graph[node]
        for nextnode in nextnodelist:
            DFS(visited,graph,nextnode)

def main():
    init_graph()

    #do DFS
    #print([k.val for k in graph.keys()])
    
    #python graphs maintain the order that they were inserted
    #root = list(graph.keys())[0]
    #print(root in graph) --> True
    #DFS(visited, graph, root)


if __name__ == '__main__':
    main()