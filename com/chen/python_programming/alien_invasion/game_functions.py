import sys
import pygame

def check_keydown_events(event,ship):
    '''响应按键'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
        print('right:',event.key)
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
        print('left:',event.key)
    elif event.key == pygame.K_UP:
        ship.moving_up = True
        print('up:',event.key)
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
        print('down:',event.key)


def check_keyup_events(event,ship):
    '''响应松开'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(ship):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)


def update_screen(ai_settings, screen, ship):
    '''更新屏幕上的图像,并切换到新屏幕'''

    # 每次循环时都重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()
