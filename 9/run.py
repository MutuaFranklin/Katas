def marks():
    marks1 = int(input('Enter marks1 \n'))
    marks2 = int(input('Enter marks2 \n'))
    marks3 = int(input('Enter marks3 \n'))
    marks4 = int(input('Enter marks4 \n'))
    marks5 = int(input('Enter marks5 \n'))
    if marks1 >=0 and marks1 <=100 and marks2>=0 and marks2<=100 and marks3 >=0 and marks3<=100 and marks4 >=0 and marks4<=100 and marks5 >=0 and marks5 <=100:
        avg =(marks1 +marks2 + marks3 +marks4 +marks5)/5
    else:
        print('Invalid entry!')
    if avg>79:
        print('Your grade is A')
    elif avg >=60 and avg <=79:
        print('Your grade is B')
    elif avg > 49 and avg <=59:
        print('Your grade is C')
    elif avg >=40 and avg <=49:
        print('Your grade is D')
    else:
        print('Your grade is E')
marks()