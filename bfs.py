from collections import deque
def bfs(graph,n,s):
    v=set()
    q=deque([s])
    v.add(s)
    while q:
        u=q.popleft()
        print(u)
        for k in graph[u]:
            if(k not in v):
                v.add(k)
                q.append(k)
graph={}
n=int(input())
for _ in range(n):
    data = input().split()
    graph[data[0]]=data[1:]
    
bfs(graph,n,'0')