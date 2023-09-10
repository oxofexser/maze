from maze_function import *
from data import *

mn = pygame.display.set_mode((setting_win['WIDTH'], setting_win['HEIGHT']))
pygame.display.set_caption('MAZE')
clock = pygame.time.Clock()

def run():
    game = True

    hero = Hero(10, 10, 55, 60, image = hero_list)
    bot1 = Bot(180, 10, 64, 64, image = bot1_list, vertical = True)

    
    while game:
        mn.fill((164, 193, 222))

        '''x, y = 20, 20
        for i in range(50):
            pygame.draw.line(mn, (255, 255, 255), (0, y), (setting_win['WIDTH'], y))
            pygame.draw.line(mn, (255, 255, 255), (x, 0), (x, setting_win['HEIGHT']))
            x += 20
            y += 20'''

        for wall in wall_list:
            pygame.draw.rect(mn, (255, 255, 255), wall)

        hero.move(mn)
        
        bot1.move(mn)


        for event in pygame.event.get():
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

        clock.tick(60)
        pygame.display.flip()

run()