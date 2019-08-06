# method 1
target = int(input())
Fibs = [1, 1]
i = 2
while i < target:
    Fibs.append(Fibs[i - 1] + Fibs[i - 2])
    i += 1
print(Fibs[target-1])

# method 2
target = int(input())
res = 0
a, b = 1, 1
for i in range(target-1):
    a,b=b,a+b
print(a)

# method 3  递归实现
def Fib(n):
    return 1 if n<=2 else Fib(n-1)+Fib(n-2)
print(Fib(int(input())))