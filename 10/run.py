import math
speed = (input('Enter speed: '))
def check_speed(speed):
    try:
        int_speed = int(speed)

        if (int_speed<=70):
            print('Ok')
        else:
            increment = ((int_speed)-70)
            points = math.floor(increment/5)

            print('Your current speed is: ', speed)
            print('awarded demerit points', points)

            if (points) >=12:
                print('License suspended')

            

    except ValueError: 
        print('Invalid input. Try an Integer')  

    
    
check_speed(speed)








