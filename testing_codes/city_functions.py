def city_country(city, country, population=0):
    """生成城市，国家"""
    if population:
        full_name = city + ', ' + country + ' - population ' + str(population)
    else:
        full_name = city + ', ' + country
    return full_name.title()