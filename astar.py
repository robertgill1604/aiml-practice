import heapq
gp = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('G', 1)],
    'D': [('E', 1)],
    'E': [('G', 1)],
    'G': []
}
h = {
    'A': 5,
    'B': 4,
    'C': 1,
    'D': 2,
    'E': 1,
    'G': 0
}

def a_star(s,g):
    pq=[]
    heapq.heappush(pq,(0,s))
    v=set()
    while pq:
        f,node=heapq.heappop(pq)
        
        if node in v:
            continue
        
        v.add(node)
        print(node,end=" ") 
        
        if node==g:
            return
        
        for neg,cost in gp[node]:
            newf=cost+h[neg]
            heapq.heappush(pq,(newf,neg))
            
a_star('A','G')        
    
    