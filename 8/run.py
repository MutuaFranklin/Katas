# (Method 1)
def large_number():
    l =[]
    for y in range(0,3):
        p=int(input('enter number \n'))
        l.append(p)
    numbers=sorted(l)
    for x in numbers:
        if x  % 4 ==0:
            a=x
            print(a,'Is a multiple of 4')
        
        
        
    print(numbers.pop(), 'Is the largest number')
large_number()


# (Method 2)
def large_number():
    first_number= int(input('Enter number \n'))
    second_number = int(input('Enter number \n'))
    third_number = int(input('Enter number \n'))
    list=[first_number,second_number,third_number]
    list.sort()
    print(list[-1],'Is the largest number in the list')
large_number()