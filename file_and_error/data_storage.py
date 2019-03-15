import json

numbers = [1, 2, 3, 4, 5, 6]

file_name = r'file_and_error\number.json'
with open(file_name, 'w') as f_obj:
    json.dump(numbers, f_obj)

with open(file_name) as f_obj:
    numbers_read = json.load(f_obj)

print(numbers_read)