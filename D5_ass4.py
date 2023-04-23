arr = []

for i in range(0,7):
    arr.append(input("Enter a string: "))

#usiing len function 
largest = ""
smallest = ""

max = 0
min = len(arr[0])

for i in arr:
    if(len(i) > max):
        max = len(i)
        largest = i
    
    if(len(i) < min):
        min = len(i)
        smallest = i

print("Largest is : " + largest)
print("smallest is : " + smallest)
