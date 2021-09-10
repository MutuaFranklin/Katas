phone = input("Enter the number to validate: ")

def validate_number(phone):

    
    
    if (phone.startswith('07')):
        newNumber = phone.replace('07','+2547',1)

    elif (phone.startswith('71')):
         newNumber = phone.replace('71','+2547',1)
      
    elif (phone.startswith('254')):
        newNumber = phone.replace('254','+2547',1)

    elif (phone.startswith('01')):
        newNumber = phone.replace('01','+2547',1)

    else:
        newNumber =phone


      
    return newNumber

    

result =  validate_number(phone)
print(result)
    

# 07.. or 71… or 254.. or 01





