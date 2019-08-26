fib = lambda n: n if n <= 2 else fib(n - 1) + fib(n - 2)
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))
print(fib(7))

def fib2(n):
    if n <=2:
        return n
    else:
        return fib2(n-1)+fib2(n-2)

print(fib2(6))

def exfib(x=5):
    if x==1 or x==0:
        return 1
    else:
        return fib(5-1)+fib(5-2)+fib(5-3)+fib(5-4)+fib(5-5)

print(exfib(5))
