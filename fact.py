#factorial
n=int(input("enter value:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)


#fact using def
def num(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
print("the factorial is :",num(5))
