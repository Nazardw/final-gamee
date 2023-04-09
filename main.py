from pygame import *
from button import Button


window = display.set_mode((700,500))


game = True
clock = time.Clock()
btn1 = Button('start_btn.png', 100,100,100, 50)
btn2 = Button('exit_btn.png', 200,200,200, 50)


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False


    
    if btn1.draw(window):
        print("pressed")
    display.update()
    clock.tick(60)