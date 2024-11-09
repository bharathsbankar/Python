#graphs
#Given "n" no.. of nodes in a undirected graph which does not have self loops and multi edges,
# the no of maximaum edges that can present would be : (n-1)+edges(n-1)
def edges(n):
    if n==2:
        return 1
    if n<=1:
        return 0

    return (n-1)+edges(n-1)
if __name__=="__main__":
    nodes=int(input("enter the number of nodes : " ))
    print(edges(nodes))