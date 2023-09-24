import pygame

setting_win = {
    'WIDTH' : 1000,
    'HEIGHT' : 700
}

maps = {
    'MAP1' : [
        '00000001000000000000000000000000100000000000000000',
        '00000000000000000000000000000000000000000000000000',
        '00000000000000000000000000000000000000000000000000',
        '00000000000000000000000000000000000000000000000000',
        '00000000000000000000000000000000000000000000000000',
        '00000000000000000000000000000000000000000000000000',
        '00000000000000000300000000000000200000000000000000',
        '00000000000000000000000000000000000000000000000000',
        '00000000000000000000000000000000000000000000000000',
        '00000000000000000000000000000000000000000010000000',
        '00000000000000000000000000000000000000000000000000',
        '00000000000000000000000000000000000000000000000000',
        '00000000000000000000000000000000000000000000000000',
        '00000000000000000000000000000000000000000000000000',
        '00000000000000000000000000000000000000000000000000',
        '00000000000000000000000000000000000000000000000000',
        '00000000000000000000000000000000000000000000000000',
        '00000000000000000000000000000000000000000000000000',
        '00000000000000000000000000000000000000000000000000',
        '000000000000013000000002100000000000000000000000000',
        '00000000000000000000000000000000000000000000000000',
        '00000000000000000000000000000000000000000000000000',
        '00000000000000000000000000000000000000000000000000',
        '00000000000000000000000000000000000000000000000000',
        '00000000000000000000000000000000000000000000000000',
        '00000000000000000000000000000000000000000020000000',
        '00000002300002000000000023000000000200000030000002',
        '00000000000000000000000000000000000000000000000000',
        '00000000000000000000000000000000000000000000000000',
        '00000000000000000000000000000000000000000000000000',
        '00000000000000000000000000000000000000000000000000',
        '00000000000000000000000000000000000000000000000000',
        '00000000000000000000000000000000000000000000000000',
        '00000000000000000000000000000000000000000000000000',
        '00000000000000000000000000000000000000000000000000'
    ]
}

wall_list = list()

hero_list = [
    pygame.transform.scale(pygame.image.load('image\\pin_0.png'), (63, 66)),
    pygame.transform.scale(pygame.image.load('image\\pin_1.png'), (63, 66)),
    pygame.transform.scale(pygame.image.load('image\\pin_0.png'), (63, 66)),
    pygame.transform.scale(pygame.image.load('image\\pin_2.png'), (63, 66))
]

bot1_list = [
    pygame.transform.scale(pygame.image.load('image\\walker.jpg'), (64, 75)),
    pygame.transform.scale(pygame.image.load('image\\walker_1.jpg'),(64, 75)),
    pygame.transform.scale(pygame.image.load('image\\walker_2.jpg'),(64, 75)),
    pygame.transform.scale(pygame.image.load('image\\walker_3..jpg'),(64, 75))
]

bot2_list = [
    pygame.transform.scale(pygame.image.load('image\\girl_2.jpg'), (64, 75)),
    pygame.transform.scale(pygame.image.load('image\\girl_1.jpg'), (64, 75))
]

bot2_list[0] = pygame.transform.flip(bot2_list[0], True, False)
bot2_list[1] = pygame.transform.flip(bot2_list[1], True, False)

hp_image = pygame.transform.scale(pygame.image.load('image\\hp.png'), (20, 20))
key_image = pygame.transform.scale(pygame.image.load('image\\key.jpg'), (64, 90))
door_image = pygame.transform.scale(pygame.image.load('image\\door_open.jpg'), (100, 150))

'''pygame.image.load('image\\enemy.png'),
    pygame.image.load('image\\enemy2.png')'''