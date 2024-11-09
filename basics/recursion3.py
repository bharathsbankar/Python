#graphs
#UN-Directed graph
#   Given "n" no.. of nodes in a undirected graph which does not have self loops and multi edges,
#   the no of maximaum edges that can present would be : (n-1)+edges(n-1) or (n*(n-1))/2
#*****************************
#Directed graph
#   Given "n" no.. of nodes in a directed graph which does not have self loops and multi edges,
#   the no of maximaum edges that can present would be : 2*(n-1)+edges(n-1) or n*(n-1)
#*****************************

def maxEdges_UnDirectedGraph(n):
    #without recursion:
    #return (n*(n-1))/2

    #with recursion:
    if n==2:
        return 1
    if n<=1:
        return 0

    return (n-1)+maxEdges_UnDirectedGraph(n-1)

def maxEdges_DirectedGraph(n):
    #without recursion :
    #return n*(n-1)

    #with recursion:
    if n==2:
        return 2
    if n<=1:
        return 0

    return 2*(n-1)+maxEdges_DirectedGraph(n-1)
if __name__=="__main__":
    nodes=int(input("enter the number of nodes : " ))
    print("undirected graph : ",maxEdges_UnDirectedGraph(nodes))
    print("directed graph : ",maxEdges_DirectedGraph(nodes))