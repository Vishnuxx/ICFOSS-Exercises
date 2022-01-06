
mlist = [1,2,3,4,5,6]

string = ""
for i in mlist:
    if(i % 3 == 0):
        continue
    string += str(i) + ","

if(string[-1] == "," ):
    string = string[:-1]

print(string)