string = "aa1bb2cc3d129d9"

def filter_string(string):
    splitted = list(string)
    

           
           
    string = ""
    for i in splitted:
        if i.isdigit():
            # result.append(i)
            string +=i
    output = int(string)       
    print(output)



        
        
   
    
            

    



    
output = filter_string(string)

