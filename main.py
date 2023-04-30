from pygame import *
from button import Button
from sprite import Player
from sprite import Wall
from random import randint


window = display.set_mode((800,700))


game = True
clock = time.Clock()
btn1 = Button('start_btn.png', 150,200,200, 50)
btn2 = Button('exit_btn.png', 400,200,200, 50)
player = Player('mario_standing.png','mario_right.png', 50,75 , 300,500)

bg = image.load("bg.png")
bg_width = bg.get_width()
bt_height = bg.get_height()

tiles = 2
scroll = 0

ground = Wall(800, 50,0, 700, color=(0,255,0))

bullets = []
walls = []
for i in range(3):
    wall = Wall(100,10, randint(400,600), randint(400,600), color=(255,0,0))
    walls.append(wall)



run = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                run = False
            if e.key == K_LEFT:
                scroll -= 5
            if e.key == K_SPACE:
                player.isJump = True  




    if run:
        for i in range(0, tiles):
            window.blit(bg, (i * bg_width + scroll, 0))
        scroll -= 5
        player.draw(window)
        player.move()
        player.jump()

        if abs(scroll) > bg_width:
            scroll = 0
         
        for w in walls:
            w.draw(window)
            if player.rect.colliderect(w.rect):
                game = False
                print('GAME OVER')
    

    else:
        window.fill((0,0,0))
        if btn1.draw(window):
            run = True
        if btn2.draw(window):
            game = False



    display.update()
    clock.tick(60)