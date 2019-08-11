def age(n):
    return age(n - 1) + 2 if n > 1 else 10


print(age(5))
