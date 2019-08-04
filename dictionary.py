learning = {'subject': 'python', 'time': '5h', 'status': 'freshman'}
print(learning['subject'])

# 添加键-值对
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
# ______________________________________________________________

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print('Original x-position: ' + str(alien_0['x_position']))

# 向右移动外星人
# 据外星人当前速度决定将其移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
elif alien_0['speed'] == 'fast':
    x_increment = 3

# 新位置等于老位置加上增量
alien_0['x_position'] += x_increment

print("New x-position: " + str(alien_0['x_position']))

# 删除键-值对
print(alien_0)
del alien_0['speed']
print(alien_0)

# 由类似对象组成的字典
favorite_avengers = {
    'Steven': 'iron man',
    'Henry': 'hulk',
    'Chris': 'hulk',
    'Alan': 'Black widow'
}
print(favorite_avengers)

# 遍历
print("We have different favorite avengers:")
for name, avenger in favorite_avengers.items():
    print(name + ': ' + avenger.title())

for name in favorite_avengers.keys():
    print(name)

# 按顺序遍历字典中的所有键,通常遍历顺序是不可预测的，所以要显示地写出要求
for name in sorted(favorite_avengers.keys()):
    print(name)

# 剔除重复
for avenger in set(favorite_avengers.values()):
    print(avenger)

# 嵌套：字典和列表可以互相嵌套
students = []

for student_number in range(1, 31):
    new_student = {'GPA': 4.0, 'IQ': 150, 'EQ': 20}
    students.append(new_student)

for student in students[:5]:
    print(student)

print("We have give offers to " + str(len(students)) + " students.")
