# ## Greatest of Three Numbers

num1 = int(input("Enter Num1 :  "))
num2 = int(input("Enter Num2 :  "))
num3 = int(input("Enter Num3 :  "))

if((num1 > num2) and (num1 > num3)):
    print("Num1 is greatest")
elif((num2 > num1) and (num2 > num3)):
    print("Num2 is greatest")
else:
    print("Num3 is greatest")


### Second Way

num1 = int(input("Enter Num1 :  "))
num2 = int(input("Enter Num2 :  "))
num3 = int(input("Enter Num3 :  "))

if(num1 > num2 and num1 > num3):
    print("Num1 is greatest")
elif(num2 > num3):
    print("Num2 is greatest")
else:
    print("Num3 is greatest")


### Third Way

num1 = int(input("Enter Num1 :  "))
num2 = int(input("Enter Num2 :  "))
num3 = int(input("Enter Num3 :  "))

if(num1 > num2):
    if(num1 > num3):
        print("Num1 is greatest")
    else:
        print("Num3 is greatest")
else:
    if(num2 > num3):
        print("Num2 is greatest")
    else:
        print("Num3 is greatest")










