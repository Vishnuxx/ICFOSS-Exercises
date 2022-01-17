file1 = open("file1.txt" , "w")
for i in range(0,25):
    file1.writelines("Hello, welcome to the world of programming\n")

file1.close