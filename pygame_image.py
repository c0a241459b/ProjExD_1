import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    tmr = 0

    bg_img2 = pg.transform.flip(bg_img, True, False)

    kt_img = pg.image.load("fig/3.png")
    kt_img = pg.transform.flip(kt_img, True, False)
        
    bg_x = 0
    bg_y = 0
    
    kt_rct = kt_img.get_rect()
    kt_rct.center = 300, 200


    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        key_lst = pg.key.get_pressed()

        kt_rct.move_ip((-1,0))
        
        if key_lst[pg.K_UP]:
            kt_rct.move_ip((0,-1))
        if key_lst[pg.K_DOWN]:
            kt_rct.move_ip((0,1))
        if key_lst[pg.K_RIGHT]:
            kt_rct.move_ip((2,0))


        bg_x -= 1
        if bg_x <= -3200:
            bg_x = 0
        if bg_x >= 1600:
            bg_x = -1600
        screen.blit(bg_img2, (bg_x - 1600, 0))
        screen.blit(bg_img, (bg_x, 0))
        screen.blit(bg_img2, (bg_x + 1600, 0))
        screen.blit(bg_img, (bg_x + 3200, 0))
        screen.blit(kt_img, kt_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(200)
        
        
        

        



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()