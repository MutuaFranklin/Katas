def sum_str(a, b):
    # happy coding !
    
    if len(a) == 0 and  len(b) >0 : 
        sum =int(b)
    elif len(b) == 0 and  len(a) >0:
        sum =int(a)
    elif len(a) == 0 and len(b) == 0:
        sum = 0
    else:
        sum = int(a) + int(b)
    output = str(sum)
    
    return output

res = sum_str('' ,'6')

print(res)



