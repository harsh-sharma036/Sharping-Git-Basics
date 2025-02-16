age = int(input("enter the age of a person: "))

if(age >= 18):
    print("you can vote now")

elif(age < 0):
    print("your age is invalid")

else:
    print("You are under-age")