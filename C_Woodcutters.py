n = int(input())

tree =  [ ]
for x in range(n):
    tree.append(list(map(int,input().split())))

prev = -float("inf")
count = 0 
for x in range(len(tree)):
    if prev<tree[x][0]-tree[x][1]:
        count+=1
        prev = tree[x][0]
    else:
        if x+1 <len(tree):
            if tree[x][0]+tree[x][1] < tree[x+1][0] :
                count+=1
                prev = tree[x][0]+tree[x][1]
            else:
                prev = tree[x][0]
        else:
            count+=1
print(count)
