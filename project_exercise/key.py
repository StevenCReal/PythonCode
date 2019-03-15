import sys

import pygame

def key_test():
    #初始化并创建一个窗口
    pygame.init()
    pygame.display.set_mode((500,500))
    pygame.display.set_caption("Key Test")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(str(event.key))

key_test()