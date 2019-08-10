def factor(num):
    res=set()
    for i in range(1,num):
        if num%i==0:
            res.add(i)
    return res

for i in range(2,1001):
    if i==sum(factor(i)):
        print(i)