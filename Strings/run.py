l= [1,2,6,7,'euue']
def filter_list(l):
    r=[]
    for value in l:
        if (type(value) is int):
            r.append(value)

        
    return r


result = filter_list(l)
print(result)


     
            