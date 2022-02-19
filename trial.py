names=input("Enter the three names: ")
counts= input("Enter the three counts: ")
grades = input("Enter the three grades: ")

def alert(names, counts, grades):
    for name in names:
        if name == names[0]:
            count =counts[0]
            grade =grades[0]
            final_grade = int(grade) +int(count)*2
        elif name == names[1]:
            count =counts[1]
            grade =grades[1]
            final_grade = int(grade) +int(count)*2
        else:
            count =counts[2]
            grade =grades[2]
            final_grade = int(grade) +int(count)*2

        

        message =f"Hi {name}"
    return final_grade

print(alert(names, counts, grades))
        
