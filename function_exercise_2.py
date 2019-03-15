def show_magicians(magicians):
    """打印魔术师"""
    for magician in magicians:
        print(magician.title())


def make_great(magicians, great_magicians):
    """将magician名字改成magician the great"""
    for magician in magicians:
        great_magician = magician.title() + " the Great"
        great_magicians.append(great_magician)


magicians = ['a', 'b', 'c']
great_magicians = []
show_magicians(magicians)
make_great(magicians, great_magicians)
show_magicians(great_magicians)