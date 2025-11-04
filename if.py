# # vote
age = int(input("Enter Your Age :"))

if (age>=18):

    print("Can Vote")
    print("Can Drive")


# #Traffic Light
light = "green"

if(light == "red"):
    print("Stop")
elif(light == "green"):
    print("Go")
elif(light == "yellow"):
    print("look")

print("end of code")


# # differcence between if & elif

## Only "if"
num = 5

if(num > 2):
    print("greater than 2")
if(num > 3):
    print("greater than 3")

# ## both statement will get executed due to the "if"




## "if" with "elif"
num = 5

if(num > 2):
    print("greater than 2")
elif(num > 3):
    print("greater than 3")

## only one statement get executed due to "elif"
## elif condition get checked only when the if conition get failed.  
## If the "if" condition is true then the elif condition never get executed.









