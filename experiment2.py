a=[]
n=int(input("Enter number of order"))
print("Enter elements:")
for i in range(n):
    row=[]
    for j in range(n):
        row.append(int(input()))
    a.append(row)
print(a)
print("Matrix form:")
for i in range(n):
    for j in range(n):
        print(a[i][j],end=" ")
    print()
b=[]
n1=int(input("Enter number of order"))
print("Enter elements:")
for i in range(n1):
    row1=[]
    for j in range(n1):
        row1.append(int(input()))
    b.append(row1)
print(b)
print("Matrix form:")
for i in range(n1):
    for j in range(n1):
        print(b[i][j],end=" ")
    print()
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(n):
    for j in range(len(a[0])):
        result[i][j]=a[i][j]+b[i][j]
print("Sum of two matices is:")
for r in result:
    print(r)


    
