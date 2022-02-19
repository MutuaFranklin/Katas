array=[9,0,2,7,0,11,0,0,2,7,12,8,9]
def move_zeros(array):   
    
    return sorted(array, key=lambda x: x==0 and type(x) is not bool)

print(move_zeros(array))