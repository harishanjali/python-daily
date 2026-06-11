#fibinocci range

c = 1
x = 0
y = 1
while c<=10:
    print(x)
    x = x+y
    x,y = y,x
    c+=1


def fib(n):
    if n==0:
        return 0
    return fib(n-1)+fib(n-2)

res = fib(5)
print(res)