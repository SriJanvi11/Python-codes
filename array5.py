#n  times left shifting elements of an array
a = []
size = int(input("enter size:"))
for i in range(size):
    val = int(input("enter the values:"))
    a.append(val)
print("the original list is:",a)
n = int(input("enter the number of iteration:"))
for count in range(n):
    key = a[0]
    for i in range(1,size):
        a[i-1] =a[i]
    a[size-1]=key

print("the modified list is",a)