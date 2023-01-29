import pygame
import sys
from config import *
from brick import Brick
from brickRow import BrickRow




def point_in_rect(pointx, pointy, rectx, recty , rect_width, rect_height):
    inx = rectx <= pointx <=rectx + rect_width
    iny = recty <=pointy <=recty + rect_height
    return inx and iny
# здесь происходит инициация,
# создание объектов
brick = Brick(50,50, RED)
brickRow = BrickRow
pygame.init()
sc = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
# радиус мяча
r = 20
# координаты мяча
ball_x = SCREEN_WIDTH//2
ball_y = SCREEN_HEIGHT // 2
# скорости мяча
ball_speed_x = 5
ball_speed_y = 4
#Кординаты ракетки
bat_x =BAT_HEIGHT // 2
bat_y =(SCREEN_WIDTH - BAT_HEIGHT) // 2
#скорость ракетки
bat_speed_y =0
# главный цикл
while True:
    # задержка
    clock.tick(FPS)
    # цикл обработки событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
 
    # --------
    # изменение объектов
    # --------
    # передвигаем мяч по экрану
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    # Выход за края экрана
    # левый
    if ball_x <= r:
        # летел налево - полетел направо
        ball_speed_x = -ball_speed_x
    # правый
    if ball_x >= SCREEN_WIDTH - r:
        # летел направо - полетел налево
        ball_speed_x = -ball_speed_x
    #Верхний
    if ball_y <=r:
        ball_speed_y = -ball_speed_y
    #Нижний
    if ball_y >= SCREEN_HEIGHT - r:
        ball_speed_y = -ball_speed_y
    #передвигаем ракетку по экрану
        
    bat_y +=bat_speed_y
    if bat_y <=0:
        bat_y =0
    elif bat_y >= SCREEN_HEIGHT - BAT_HEIGHT:
        bat_y = SCREEN_HEIGHT - BAT_HEIGHT
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        bat_x -= 15
    elif keys[pygame.K_RIGHT]:
        bat_x += 15
    #проверяем что мяч попал в ракетку
    #вычисляем середины сторон квадрата, описанного вокруг мяча
    mid_leftx=ball_x - r
    mid_lefty=ball_y
    
    mid_rightx=ball_x + r
    mid_righty=ball_y
    
    mid_topx= ball_x
    mid_topy= ball_y -r
    
    mid_bottomx = ball_x
    mid_bottomy = ball_y + r
    #правая граница ракетки
    if point_in_rect(mid_rightx, mid_righty , bat_x , bat_y , BAT_WIDTH, BAT_HEIGHT):
        ball_speed_x = -ball_speed_x
    # обновление экрана
    # заливаем фон
    sc.fill(BLACK)
    # рисуем круг
    for brickRow in Brick_Row.row:
        pygame.draw.rect(sc,BLACK,(brick.x,brick.y,BRICK_WIDTH,BRICK_HEIGHT),1)
        pygame.draw.rect(sc, brick.color,(brick.x+1,brick.y+1,BRICK_WIDTH-1,BRICK_HEIGHT-1))
    pygame.draw.circle(sc, ORANGE,(ball_x, ball_y), r)
    pygame.draw.rect(sc,ORANGE, (bat_x, bat_y, BAT_WIDTH, BAT_HEIGHT))
    pygame.display.update()
