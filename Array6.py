#insertion in an array
a = []
size = int(input("enter size:"))
for i in range(size):
    val = int(input("enter the values:"))
    a.append(val)
print("the original list is:",a)
key = int(input("enter the number you want to insert:"))
pos = int(input("enter the position where you want to insert the number:"))
a.append(None)
for i in range(size-1,pos-2,-1):
    a[i+1] = a[i]
a[pos-1] = key
print("the modified list is",a)