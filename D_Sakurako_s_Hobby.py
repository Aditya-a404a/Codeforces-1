
T = int(input())

def solve(nums,color):

    # print(nums,color)


    seen = [-1]*len(nums)

    for x in range(len(nums)):
        if seen[x] == -1:
            seen[x] = x
            i = nums[x]-1
            while seen[i] == -1:
                seen[i] = x
                i = nums[i]-1
    count =[0]*len(nums)
    for x in range(len(nums)):
        if color[x]=="0":
            count[seen[x]] += 1
    ans = [0]*len(nums)
    
    for x in range(len(nums)):
        
        ans[x]=count[seen[x]]
    return ans 
    # print(seen)
    

    
    



    pass

for _ in range(T):
    n = int(input())
    nums = list(map(int, input().split()))
    color =  input()
    T = solve(nums,color)
    for x in T:
        print(x,end=" ")
    print()