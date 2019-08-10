# method 1
total=1
for i in range(9):
    total=(total+1)*2
print(total)

# method 2
def peach(n):
    if n==10:
        return 1
    else:
        return (peach(n+1)+1)*2

print(peach(1))