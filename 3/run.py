number = int(input("Enter a number: "))


def odd_or_even(number):
    if (number%2)==0:
        result = 'Even'
    else:
        result = 'Odd'

    return result 

outcome = odd_or_even(number)
print(outcome)