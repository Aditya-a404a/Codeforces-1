n , m =  list(map(int,input().split()))
cats = list(map(int,input().split()))

from collections import defaultdict

graph= defaultdict(list)

for _ in range(n-1):
    x,y = list(map(int,input().split()))
    graph[x].append(y)
    graph[y].append(x)

count = 0 
q = [(1,0,0)]
# node,streakconsecutive not counting this one,prev

while q : 
    newq = [] 
    while q:
        node,streak, prev = q.pop()
        
        if len(graph[node])==1 and node!=1:
            if streak+cats[node-1]<=m:
                count+=1
        for nxt in graph[node]:
            if nxt!=prev:
                if cats[node-1]:
                    if streak+1 <=m:
                        newq.append((nxt,streak+1,node))
                else:
                    newq.append((nxt,0,node))
                
    q = newq 
print(count)






    

