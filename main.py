def add (p,q):
    return p + q
def subtract (p,q):
    return p - q
def multiply (p,q):
    return p * q
def divide (p,q):
    return p / q

print("Please select the operation")
print("a.addition")
print("b.subtraction")
print("c.multiplication")
print("d.division")

choice = input("Please enter your choice a,b,c,d - ")
n1 = int(input("Enter the first number - "))
n2 = int(input("Enter the second number - "))

if choice == 'a':
    print(n1,"+",n2,"=",add(n1,n2))
elif choice == 'b':
    print(n1,"-",n2,"=",subtract(n1,n2))
elif choice == 'c':
    print(n1,"*",n2,"=",multiply(n1,n2))
elif choice == 'd':
    print(n1,"/",n2,"=",divide(n1,n2))
else:
    print("invalid choice")