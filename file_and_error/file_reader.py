#打开文件
with open(r'file_and_exception\pi_digits.txt') as file_object:      #前面务必加上r
    contents = file_object.read()
    print(contents)

#逐行读取
path_name = r'file_and_exception\pi_digits.txt'
with open(path_name) as file_object:
    for line in file_object:
        print(line.rstrip())    #rstrip()用于删除多出的空行

#将文件逐行储存在列表中
with open(path_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

#使用文件的内容
pi_string = ''
for line in lines:
    pi_string += line.strip()   #strip()可以删除空格

print(pi_string)
print(len(pi_string))

#写入空文件
file_name =r"file_and_exception\programming_message.txt"

with open(file_name, 'w') as file_object:       #w是写入模式
    file_object.write("I love programming!\n")

#附加到文件
with open(file_name,'a') as file_object:        #a是附加模式
    file_object.write("I love reading!")