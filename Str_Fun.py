# # .endswith(" ")
str = ("I am a Python Coder")

print(str.endswith("der")) #T

print(str.endswith("r")) #T

print(str.endswith("er")) #T

print(str.endswith("hon")) #F

print(str.endswith(" ")) #F


# # .capitalize()
str = ("i am a Python Coder")
print(str.capitalize()) #I

print(str) #original string does not get modified

str = str.capitalize()
print(str) #Now string will get modified


# # .replace(old,new)
str = ("I am a Python Coder")
print(str.replace("o","a"))

print(str.replace("Python","Java"))


# # .find(word)
str = ("I am a Python Coder")

print(str.find("a")) #2

print(str.find("P")) #7

print(str.find("o")) #11

print(str.find("Python")) #7

print(str.find("Q")) #-1


# .count("")
str = ("I am a Python coder. He is a Java coder")
print(str.count("o")) #3

print(str.count("a")) #5

print(str.count("coder")) #2




