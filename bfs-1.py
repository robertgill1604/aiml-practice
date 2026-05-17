graph = {}

n=int(input("Enter number of nodes: "))
for i in range(n):
    node=input("Enter node: ")
    neighbours=input(
        f"Enter neighbours of {node}: "
    ).split()
    graph[node]=neighbours
start=input("Enter starting node: ")
vd=set()
print(graph)

def bfs(graph,s):
    q=[]
    v=set()
    q.append(s)
    v.add(s)
    # print(len(q))
    while(len(q)!=0):
        u=q.pop(0)
        print(u,end=" ")
        neighbours=graph[u]
        for i in neighbours:
            if(i not in v):
                q.append(i)
                v.add(i)
def dfs(graph,s):
    if(s not in vd):
        vd.add(s)
        print(s,end=" ")
        neighbours=graph[s]
        for i in neighbours:
            dfs(graph,i)

print("BFS : ",end="")
bfs(graph,start)
print("\nDFS : ",end="")
dfs(graph,start)
