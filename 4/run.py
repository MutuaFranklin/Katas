list = [20, 10, 20, 1, 100]


def smallest(list):
    smallest_number =min(list)

    return smallest_number

result = smallest(list)
print(result)



def minimum(list):
    current_min = list[0]  # Start by assuming the first number is smallest
    for num in list:       # Loop through each number in the list
        if num < current_min:
            current_min = num  # Update current_min if current number is less
    return current_min

print (minimum(list))

def smallest_value(list):
    list.sort()
    result =list[0]
    return result

print(smallest_value(list))

