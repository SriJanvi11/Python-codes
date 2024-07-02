#shifting all the element of array to one step left
a = []
size = int(input("enter size:"))
for i in range(size):
    val = int(input("enter the values:"))
    a.append(val)
print("the original list is:",a)
key = a[0]
for i in range(1,size):
    a[i-1] =a[i]
a[size-1]=key
print("the modified list is:",a)