
def operation_type(num1,num2,result):
    if(num1+num2)==result:
        operation = "addition"
    elif(num1-num2)==result:
        operation = "substraction" 
    elif(num1*num2)==result:
        operation = "multiplication"
    elif(num1/num2)==result:
        operation ="division"
    else:
        operation ="unknown"

    return operation

result =operation_type(2,5,7)
print(result)
    
               