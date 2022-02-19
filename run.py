number = int(input("Enter a number: "))

def solution(number):
    results=[]
    for x in range(number):
        if(x%3==0) or (x%5==0):
            results.append(x)
    print(results)
    total =sum(results)
    return total

print(solution(number))
    


    