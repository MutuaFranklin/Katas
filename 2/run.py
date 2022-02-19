list1 = [5, 10, 15, 20, 25]
list2 = [10, 30, 40, 70, 12]


def make_selection(list2):
    selected_list =[list2[0],list2[-1]]
    return selected_list

result = make_selection(list2)
print(result)


def manipulate_list(list1):
    new_list = [list1.pop(0), list1.pop()]

    return new_list

outcome = manipulate_list(list1)

print(outcome)
