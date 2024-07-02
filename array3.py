a = []
size = int(input("enter size:"))
for i in range(size):
    val = int(input("enter the values:"))
    a.append(val)
print("the original list is:",a)
key1 = a[0]
key2 = a[1]
for i in range(2,size):
    a[i-2]=a[i]

a[size-2]=key1
a[size-1]=key2
print("the modified list is:",a)

