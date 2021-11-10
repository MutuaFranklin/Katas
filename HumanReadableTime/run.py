A = (1,2,3,4,6,7,8)

def find_missing(A):
    arr =[]

#     return [x for x in range (lst[0], lst[-1]+1) if x not in lst]
    
    for x in range (A[0], A[-1]+1):
      
        if x not in A:
            arr.append(x)
            output = min(arr)
        # else:
        #     output = "nONE"
            
        
    print(output)

res = (find_missing(A))

def solution(A):
    a=frozenset(sorted(A))
    m=max(a)
    if m>0:
        for i in range(1,m):
            if i not in a:
                return i
        else:
            return m+1
    else:
        return 1

res = solution(A)
print(res)







