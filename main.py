from pygame import *
from button import Button


window = display.set_mode((700,500))


game = True
clock = time.Clock()
btn1 = Button('start_btn.png', 100,100,100, 50)
btn2 = Button('exit_btn.png', 200,200,200, 50)

bg = image.load("bg.png")
bg_width = bg.get_width()
bt_height = bg.get_height()
tiles = 2


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




    if run:
        for i in range(0, tiles):
            window.blit(bg, (0,0))
        scroll -= 5

    else:
        window.fill((0,0,0))
        if btn1.draw(window):
            run = True
        if btn2.draw(window):
            game = False



    display.update()
    clock.tick(60)