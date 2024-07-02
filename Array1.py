#shifting elements to one shift right in an array
a = []
size = int(input("enter size:"))
for i in range(size):
    val = int(input("enter the values:"))
    a.append(val)
print("the original list is:",a)
key = a[size-1]
for i in range(size-2,-1,-1):
    a[i+1] = a[i]
a[0] = key
print("the modified list is:",a)