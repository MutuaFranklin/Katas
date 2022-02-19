# n=int(input("Enter a number: "))

# def occurrence(n):
#     count =0
#     for i in range(n+1):
#         if(i==3):
#             count = count + 1
#         else:
#             count=0
#     return count

# print(occurrence(n))




numbers =[2,4,7,8]

4+16+49+64


squared_numbers=[]

def function(numbers):
    for num in numbers:
        square= num*num

        squared_numbers.append(square)
    sum=0
    n = len(squared_numbers)
    for i in range(n):
        sum = sum + squared_numbers[i]
    return sum


print(function(numbers))








