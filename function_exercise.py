#城市名
def city_country(city, country):
    print(city + ', ' + country)


#专辑
def make_album(album_name, singer, songs_num=0):
    album = {}
    if songs_num:
        album['songs_num'] = songs_num
    album['album_name'] = album_name
    album['singer'] = singer.title()
    return album


album = make_album('22', 'adele')
print(album)
album = make_album('18', 'adele', 13)
print(album)

while True:
    print("Please create your own album:")
    print("(press q any time you want to quit.)")

    album_name = input("album name: ")
    if album_name == 'q':
        break

    singer = input("singer: ")
    if singer == 'q':
        break

    songs_num = input("songs number: ")
    if songs_num == 'q':
        break

    album = make_album(album_name, singer, songs_num)
    print(album)