base = input('Enter the base value: ')
height = input('Enter the height value: ')


def calculate_area(base, height):
    #convert to float
    try: 
        base = float(base)
        height = float(height)

        area = 1/2*base*height

        print ('Area: ', area)
    except ValueError:
        print('Input values should be a float')


calculate_area(base, height)