
def operation_type(num1,num2,result):
    if(num1+num2)==result and (num1*num2)==result:
        operation ="addition and multiplication"
    elif(num1+num2)==result:
        operation = "addition"
    elif(num1-num2)==result:
        operation = "substraction" 
    elif(num1*num2)==result:
        operation = "multiplication"
    elif(num1/num2)==result:
        operation ="division"
    
    else:
        operation ="invalid operation"

    return operation

result =operation_type(2,2,4)
print(result)


def calc_type(a, b, res):
    dict = {a+b:'addition',a-b:'subtraction',a*b:'multiplication',a/b:'division'}
    return dict[res]

result = calc_type(2,2,4)
# print(result)


# def calc_type(a, b, res):
#     return next(
#         name for name in ['addition', 'subtraction', 'multiplication', 'division']
#         if globals()[name](a, b) == res
#     )

# result = calc_type(2,4,8)
# print(result)
    
               