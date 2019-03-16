import json

import pygal.maps.world
from pygal.style import RotateStyle, LightColorizedStyle

from country_codes import get_country_code

#将数据加载到一个列表中
filename = 'data_visualization\population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# 创建一个包含人口数量的字典
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country)
        if code:
            cc_populations[code] = population

## 根据人口数量将所有的国家分成三组
pop_1, pop_2, pop_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        pop_1[cc] = pop
    elif pop < 1000000000:
        pop_2[cc] = pop
    else:
        pop_3[cc] = pop

wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', pop_1)
wm.add('10m-1bn', pop_2)
wm.add('>1bn', pop_3)

wm.render_to_file(r'data_visualization\world_population.svg')

# 打印每个国家2010年的人口数量
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            print(country_name + ": " + str(population))
        else:
            print('ERROR - ' + country_name)