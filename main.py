import pygame as pgm
# step by step membuat game

# init
pgm.init()

isRun = True
window_l = 500
window_p = 500 

window = pgm.display.set_mode((window_l,window_p))

# objek game

# posisi
x = 250
y = 250

# ukuran
panjang = 20
lebar = 20

# kecepatan
speed = 10

while isRun:
    pgm.time.delay(10)
    # input user, database input
    for event in pgm.event.get():
        if event.type == pgm.QUIT:
            isRun = False
    
    # input keyboard
    keys = pgm.key.get_pressed()    
    
    # left
    if keys[pgm.K_LEFT] and x > 0:
        x -= speed
    
    # right
    if keys[pgm.K_RIGHT] and x <window_l-lebar:
        x += speed
        
    # down
    if keys[pgm.K_DOWN] and y < window_p-panjang:
        y += speed
    
    # up
    if keys[pgm.K_UP] and y > 0:
        y -= speed
    
    # update asset
    window.fill((180,120,80))
    
    pgm.draw.rect(window,(220,200,0),(x,y,lebar,panjang))
    
    # render ke layar
    pgm.display.update()
    
pgm.quit()