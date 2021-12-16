
def readm():
    file = open("adjMat.txt", "r")
    lines = file.readlines()
    a=[]
    for line in lines:
        b=[]
        for x in line.strip('\n').split(' '):
            b.append(int(x))
        a.append(b)
    return a


def dijkstraAlgApply(source, adjMat):

    distance = []
    N = len(adjMat)

    #initialize element in array with infinity
    distance = [float('Inf')] * N

    #initialize element in visited node with 0
    visited_node =[0] * N

    distance[source] = 0        #source is the start node at 0

    next_node = 0

    # apply algorithm dijkstra
    for i in range(N):
        min = float('Inf')
        for j in range(N):
            if(distance[j]< min and visited_node[j] != 1):
                min = distance[j]
                next_node = j

    # mark process when the node is visited, mark with 1
        visited_node[next_node] = 1

        for k in range(N):
            # if the node not connect each other
            if adjMat[next_node][k] == 0:
                continue
            if(min + adjMat[next_node][k]) < distance[k]:
                distance[k] = min + adjMat[next_node][k]

    for i in range(len(visited_node)):
        print("For Vertex", i, ", the minimum distance to vertex", source ,"is ", distance[i])


def main():
    adjMat = readm()
    print(adjMat)
    row = len(adjMat)

    source = int(input("please enter the input from node 0 to node n-1: "))
    if source < row:
        print ('Showing the Dijskstra result for the node', source)
        dijkstraAlgApply(source, adjMat)
    else:
        print("Error! Input only works from node 0 to node n -1")


main()
