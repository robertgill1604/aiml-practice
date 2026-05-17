v=set()
def dfs(graph,s):
    v.add(s)
    print(s)
    for k in graph[s]:
        if(k not in v):
            dfs(graph,k)

graph={}
n=int(input())
for _ in range(n):
    data = input().split()
    graph[data[0]]=data[1:]
    
dfs(graph,'0')