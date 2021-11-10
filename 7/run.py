def email():
    my_email=input("Enter email")
    if len(my_email.split("@")) > 1 and len(my_email.split(".")) >1:
        return "valid email"
    else:
        return "invalid email"
results=email()
print(results)