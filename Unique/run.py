arr =[1,1,1,1,1,1,1,1,2,3,3,3]

def find_uniq(arr):
    # your code here
    for i in arr:
        if arr.count(i)==1:
            unique =i
            
    return unique

print(find_uniq(arr))