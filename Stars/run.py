number = input('Enter the number of rows: ')


def print_stars(number):
    #convert to integer
    try: 
        number = int(number)

        for i in range(1, number+1):
                print(i * '*')
       
    except ValueError:
        print('Input value should be an integer')


print_stars(number)