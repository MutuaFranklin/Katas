age = input('How old are you in years?: ')

def years_to_days(age):
    try:
        age = int(age)
        if (age>0):
            age_in_days = age*365
            print(f'You are { age_in_days } days old.')

        else:
            print('Please input a valid age above 0')
    except ValueError:
        print('Your age value should be an integer')


years_to_days(age)


