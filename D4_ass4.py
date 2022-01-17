#1
import re


file4 = open("file4.txt" , "w+")
file4.write("You are not reading this book because a teacher assigned it to you, you are reading it because you have a desire to learn, and wanting to learn is the biggest advantage you can have.")
file4.close()

#2
file4 = open("file4.txt" , "r")
sentence = file4.readline()
file4.seek(127)
print(file4.readline())

#3
print(sentence.replace("e" , "z"))

#4
print(sentence.count("a"))