def greet_user(username):
    """Say Hello to the user"""
    print("Hello, " + username.title() + ".")


greet_user('Steven')


# 位置实参 与 关键字实参: 位置实参是指实参位置和形参保持一致，按形参声明的先后顺序一一赋值；
# 关键字实参是指调用函数的时候以 “形参=实参” 的方式来传参, 这个时候实参的顺序无所谓
def describe_pet(pet_name,
                 animal_type='dog'):  # 在实参这里设置个默认值，当用户不赋予animal_type时，默认为dog
    """显示宠物的信息"""  # 同时注意，没有给默认值的形参必须放在前面，给了默认值的就放在后面
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('cat', 'Niko')
describe_pet(pet_name='Bobby', animal_type='dog')
describe_pet(pet_name='Wong Choi')
describe_pet('willie')


# 有返回值的参数 与 可选实参
def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的名字"""
    if middle_name:
        full_name = first_name + '·' + middle_name + '·' + last_name
    else:
        full_name = first_name + '·' + last_name
    return full_name.title()


musician = get_formatted_name('Michael', 'Jackson')
print(musician)
musician = get_formatted_name('samuel', 'jackson', 'j')
print(musician)

# ————————————————————————————————————————————————————————————————


def build_person(first_name, last_name, age=''):
    """返回一个字典， 其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix', age=27)
print(musician)

# ——————————————————————————————————————————————————————————


# 在函数中修改列表
def print_models(unprinted_designs, completed_models):  # 这里是将原件传入，可对原件修改
    # print_models(unprinted_designs[:], completed_models)
    # 上面通过切片的方式，表示只将副本传入，不修改原件
    """                                                
    模拟打印每个设计， 直到没有未打印的设计为止
    打印每个设计后， 都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

    #  模拟根据设计制作3D打印模型的过程
    print("Printing model: " + current_design)
    completed_models.append(current_design)


def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# ——————————————————————————————————————————————————————————————————————————


# 传递任意数量的实参
def make_pizza(*toppings):  # 形参名*toppings 中的星号让Python创建一个名为toppings 的空元组
    """概述要制作的比萨"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# 结合使用位置实参和任意数量实参
def make_pizza_2(size,
                 *toppings):  # 形参名*toppings 中的星号让Python创建一个名为toppings 的空元组
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza_2(16, 'pepperoni')
make_pizza_2(12, 'mushrooms', 'green peppers', 'extra cheese')


# 使用任意数量的关键字实参
def build_profile(
        first_name, last_name,
        **user_info):  # 形参**user_info 中的两个星号让Python创建一个名为user_info 的空字典
    """创建一个字典， 其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first_name
    profile['last_name'] = last_name

    for key, value in user_info.items():
        profile[key] = value

    return profile


student = build_profile(
    'Steven',
    'Chan',
    major='Environmental Engineering',
    age=20,
    idol='Jay Chou')
print(student)

jackie_chan = {'major': 'actor', 'age': 60, 'Idol': 'himself'}
student2 = build_profile('Jackie', 'Chan', **jackie_chan)  # 若已有包含额外信息的dict，可用**来直接将dict中的键-值对导入到可变参数中
print(student2)
