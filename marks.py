## Marks

marks = int(input("Enter your Marks:"))

if(marks >= 90 ):
    print("Grade : A")

elif((marks >= 80) and (marks < 90) ):
    print("Grade : B")

elif((marks >= 70) and (marks < 80) ):
    print("Grade : C")

else:
    print("Grade : D")




# # Another Way

marks = int(input("Enter Your Marks :"))

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"

print("Your Grade :" , grade)



# ## Nesting

age = int(input("Enter Your age : "))

if(age >= 18):
    if(age >= 80):
        print("Cannot Drive")
    else:
        print("Can Drive")
else:
    print("Cannot Drive")



## another way

age = int(input("Enter Your age : "))

if(age >= 18):
    if(age <= 80):
        print("Can Drive")
    else:
        print("Cannot Drive")
else:
    print("Cannot Drive")









