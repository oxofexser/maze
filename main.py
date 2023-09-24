from maze_function import *
from data import *

mn = pygame.display.set_mode((setting_win['WIDTH'], setting_win['HEIGHT']))
pygame.display.set_caption('MAZE')
clock = pygame.time.Clock()

def run():
    game = True
    menu = False
    key_check = True
    lvl = 1

    hero = Hero(10, 10, 55, 60, image = hero_list)
    bot1 = Bot(180, 10, 64, 75, image = bot1_list, vertical = True)
    bot2 = Bot(900, 550, 64, 75, image = bot2_list)
    button_start = pygame.Rect(setting_win['WIDTH']//2 - 270, setting_win['HEIGHT'] // 2, 250, 60)
    button_end = pygame.Rect(setting_win['WIDTH']//2 + 20, setting_win['HEIGHT'] // 2, 250, 60)
    font_start_end =pygame.font.Font(None, 50)
    

    
    while game:
        events = pygame.event.get()
        mn.fill((164, 193, 222))

        x = 920
        for i in range(hero.XP):
            mn.blit(hp_image, (x, 10))
            x+= 25
        if hero.XP == 0:
            menu = True
            hero.SPEED = 0



        '''x, y = 20, 20
        for i in range(50):
            pygame.draw.line(mn, (255, 255, 255), (0, y), (setting_win['WIDTH'], y))
            pygame.draw.line(mn, (255, 255, 255), (x, 0), (x, setting_win['HEIGHT']))
            x += 20
            y += 20'''

        for wall in wall_list:
            pygame.draw.rect(mn, (255, 255, 255), wall)

        hero.move(mn)
        bot1.move(mn, hero)
        bot2.shoot(mn, hero)

        if key_check:
            mn.blit(key_image, (520, 30))
            if hero.colliderect(key_image.get_rect(topleft= (520, 30))):
                key_check = False
        else:
            mn.blit(door_image, (880, 350))
            if hero.colliderect(door_image.get_rect(topleft = (880, 350))):
                lvl += 1
                menu = True
                if menu:
                    winn = pygame.Rect(setting_win['WIDTH']//2 - 300, setting_win['HEIGHT'] // 2, 250, 60)
                    font_win = pygame.font.Font(None, 100)
                    pygame.draw.rect(mn, (108, 12, 255), winn)
                    mn.blit(font_win.render('WIN!!!', True, (0,0,0)), (winn.x, winn.y+100))
                    pygame.draw.rect(mn, (108, 12, 255), button_start)
                    pygame.draw.rect(mn, (108, 12, 255), button_end)
                    mn.blit(font_start_end.render('START', True, (0,0,0)), (button_start.x + 65, button_start.y + 15))
                    mn.blit(font_start_end.render('END', True, (0,0,0)), (button_end.x + 85, button_end.y + 15))
                    for event in events:
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            x, y = event.pos
                            if button_start.collidepoint(x,y):
                                menu = False
                                hero.SPEED = 5
                                hero.XP = 3
                            if button_end.collidepoint(x,y):
                                game = False
                    

        


        for event in events:
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    hero.MOVE['UP'] = True
                if event.key == pygame.K_s:
                    hero.MOVE['DOWN'] = True
                if event.key == pygame.K_d:
                    hero.MOVE['RIGHT'] = True
                if event.key == pygame.K_a:
                    hero.MOVE['LEFT'] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    hero.MOVE['UP'] = False
                if event.key == pygame.K_s:
                    hero.MOVE['DOWN'] = False
                if event.key == pygame.K_d:
                    hero.MOVE['RIGHT'] = False
                if event.key == pygame.K_a:
                    hero.MOVE['LEFT'] = False

        if menu:
            pygame.draw.rect(mn, (108, 12, 255), button_start)
            pygame.draw.rect(mn, (108, 12, 255), button_end)
            mn.blit(font_start_end.render('START', True, (0,0,0)), (button_start.x + 65, button_start.y + 15))
            mn.blit(font_start_end.render('END', True, (0,0,0)), (button_end.x + 85, button_end.y + 15))
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    if button_start.collidepoint(x,y):
                        menu = False
                        hero.SPEED = 5
                        hero.XP = 3
                    if button_end.collidepoint(x,y):
                        game = False
            


        clock.tick(60)
        pygame.display.flip()

run()