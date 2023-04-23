inp1 = int(input("enter a string: "))
inp2 = int(input("enter another string: "))

def getSmallest(a , b):
    if((a % 2 == 0) and (b % 2 == 0) ):
        return min(a , b)
    else:
        return False


print(getSmallest(inp1 , inp2))