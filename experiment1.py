def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
r=int(input("Enter first number:"))
s=int(input("Enter second number:"))
o=input("Enter operator:")
if o=="+":
    print("Sum:", add(r,s))
elif o=="-":
    print("Difference:",sub(r,s))
elif o=="*":
    print("Product:",mul(r,s))
else:
    print("Division:",div(a,b))
