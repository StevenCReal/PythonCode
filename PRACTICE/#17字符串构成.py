string = input('Enter a line of string: ')
alp=0
spa=0
num=0
oth=0

for s in string:
    if s.isspace():
        spa+=1
    elif s.isalpha():
        alp+=1
    elif s.isdigit():
        num+=1
    else:
        oth+=1

print('space: ',spa)
print('digit: ',num)
print('alpha: ',alp)
print('other: ',oth)
