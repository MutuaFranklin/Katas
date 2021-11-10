# Given: Two positive integers a and b (a<b<10000, a<b<10000).
# Return: The sum of all odd integers from a through b, inclusively.


a = int(input('Enter the first integer: '))
b = int(input('Enter the second integer: '))

def sum_of_odd(a, b):
    try:
        #convert to integers

        if(a<b<10000):
            if(a%2)!=0 and (b%2)!=0:
                total = a + b
                print(total)
            elif(a%2)==0 or (b%2)==0:
                print('Input odd numbers')
            else:
                print('Input odd numbers')

        else:
            print('Not within the specified range')
        


    

    except ValueError:
        return 'Invalid input. Enter an integer value'

sum_of_odd(a,b)