#shifting the elements of an array n times #right
a = []
size = int(input("enter size:"))
for i in range(size):
    val = int(input("enter the values:"))
    a.append(val)
print("the original list i7s:",a)
n = int(input("enter the number of iteration"))
for count in range(n):

    key = a[size - 1]
    for i in range(size - 2, -1, -1):
        a[i + 1] = a[i]
    a[0] = key
print("the modified list is:", a)