import pygame
import time
import random

print('Blue chases Red, white means sticky glue.')

pygame.font.init()

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
BLUE_VEL = 7
PLAYER_VEL = 5

WHITE = 255, 255, 255
BROWN = 173, 82, 12
GRAY = 102, 100, 99

FONT = pygame.font.SysFont('comicsans', 30)

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('BlueChaseRed')

def draw(Red, Blue, elapsed_time, Wall1, Wall2):
    WIN.fill(GRAY)

    time_text = FONT.render(f'Time: {round(elapsed_time)}s', 1, 'white')
    WIN.blit(time_text, (10, 10))

    pygame.draw.rect(WIN, 'red', Red)
    pygame.draw.rect(WIN, 'blue', Blue)

    pygame.draw.rect(WIN, WHITE, Wall1)
    pygame.draw.rect(WIN, WHITE, Wall2)

    pygame.display.update()

def move_ai(Blue, Red, Wall1, Wall2):
    if Red.x > Blue.x:
        new_x = Blue.x + BLUE_VEL
    elif Red.x < Blue.x:
        new_x = Blue.x - BLUE_VEL
    else:
        new_x = Blue.x


def main():
    start_time = time.time()
    run = True

    Red = pygame.Rect(300, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    Blue = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    random_x1 = random.randint(100, WIDTH - PLAYER_WIDTH - 100)
    random_y1 = random.randint(100, HEIGHT - PLAYER_HEIGHT - 100)

    random_x2 = random.randint(100, WIDTH - PLAYER_WIDTH - 100)
    random_y2 = random.randint(100, HEIGHT - PLAYER_HEIGHT - 100)

    Wall1 = pygame.Rect(random_x1, random_y1, PLAYER_WIDTH + 10, PLAYER_HEIGHT)
    Wall2 = pygame.Rect(random_x2, random_y2, PLAYER_WIDTH + 10, PLAYER_HEIGHT)

    clock = pygame.time.Clock()

    pygame.init()
    pygame.mixer.init()

    while run:
        elapsed_time = time.time() - start_time

        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and Red.x - PLAYER_VEL >= 0 and not Red.colliderect(Wall1) and not Red.colliderect(Wall2):
            Red.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and Red.x + PLAYER_VEL + Red.width <= WIDTH and not Red.colliderect(Wall1) and not Red.colliderect(Wall2):
            Red.x += PLAYER_VEL
        if keys[pygame.K_UP] and Red.y - PLAYER_VEL >= 0 and not Red.colliderect(Wall1) and not Red.colliderect(Wall2):
            Red.y -= PLAYER_VEL
        if keys[pygame.K_DOWN] and Red.y + PLAYER_VEL + Red.height <= HEIGHT and not Red.colliderect(Wall1) and not Red.colliderect(Wall2):
            Red.y += PLAYER_VEL

        move_ai(Blue, Red, Wall1, Wall2)

        if keys[pygame.K_r]:  # restart
            Red.x = 300
            Red.y = HEIGHT - PLAYER_HEIGHT
            Blue.x = 200
            Blue.y = HEIGHT - PLAYER_HEIGHT
            start_time = time.time()

        if Blue.colliderect(Red):
            pygame.mixer.music.load('tf_nemesis.mp3')
            pygame.mixer.music.play(-1)
            pygame.time.delay(4000)

            lost_text = FONT.render('Red Lost!', 1, 'white')
            WIN.blit(lost_text, (WIDTH / 2 - lost_text.get_width() / 2, HEIGHT / 2 - lost_text.get_height() / 2))
            pygame.display.update()
            pygame.time.delay(5000)
            break

        if Blue.colliderect(Wall1) or Blue.colliderect(Wall2):
            lost_text1 = FONT.render('Blue Lost!', 1, 'white')
            WIN.blit(lost_text1, (WIDTH / 2 - lost_text1.get_width() / 2, HEIGHT / 2 - lost_text1.get_height() / 2))
            pygame.display.update()
            pygame.mixer.music.load('tf_nemesis.mp3')
            pygame.mixer.music.play(-1)
            pygame.time.delay(5000)
            break

        draw(Red, Blue, elapsed_time, Wall1, Wall2)

    pygame.quit()

if __name__ == '__main__':
    main()



