# method 1
height = 100
times = 10
total = height
for i in range(1,times):
        total += height
        height /= 2
        print(height)
print('第十次反弹的高度：' + str(height / 2))
print('第十次落地时共经过'+str(total)+'m')

# method 2
def high(n):
    if n==0:
        return 100
    else:
        return high(n-1)/2

height=100
total=height
for i in range(1,times):
    total+=high(i)*2
print('第十次反弹的高度：' + str(high(10)))
print('第十次落地时共经过'+str(total)+'m')