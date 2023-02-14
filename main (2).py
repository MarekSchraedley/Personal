
import pygame, sys
from pygame.locals import QUIT
from time import sleep
pygame.init()
global colorvar
colorvar = 0
white = (255, 255, 255)
yellow = (255,255, 100)
black = (0, 0, 0)
red = (210, 50, 80)
green = (0, 255, 0)
blue = (50, 150, 210)
dis_width = 600
dis_height = 400
progstart = True
global dis
dis = pygame.display.set_mode((dis_width, dis_height))
global flash
flash = 0
level = 1
rvar = 1
svar = 0
levelpassed = 0
#LVL1
winover = 1
winup = 2
playover = 1
playup = 0
Lvl1reset = [[1, 3, 2], [1, 1, 1], [2, 4, 1]]
Lvl1 = [[1, 3, 2], [1, 1, 1], [2, 4, 1]]
Lvl1wid = [[280, 300, 320], [280, 300, 320], [280, 300, 320]]
Lvl1hei = [[220, 220, 220], [200,200,200], [180, 180, 180]]
#LVL2
winover2 = 4
winup2 = 6
playover2 = 3
playup2 = 0
Lvl2reset = [[1, 1, 1, 3, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 2, 2, 2, 1, 1], [1, 1, 2, 2, 2, 1, 1], [1, 1, 2, 2, 2, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 4, 1, 1]]

Lvl2 = [[1, 1, 1, 3, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 2, 2, 2, 1, 1], [1, 1, 2, 2, 2, 1, 1], [1, 1, 2, 2, 2, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 4, 1, 1]]
Lvl2wid = [[240, 260, 280, 300, 320, 340, 360], [240, 260, 280, 300, 320, 340, 360], [240, 260, 280, 300, 320, 340, 360], [240, 260, 280, 300, 320, 340, 360], [240, 260, 280, 300, 320, 340, 360], [240, 260, 280, 300, 320, 340, 360], [240, 260, 280, 300, 320, 340, 360]]
Lvl2hei = [[260, 260, 260, 260, 260, 260, 260], [240, 240, 240, 240, 240, 240, 240], [220, 220, 220, 220, 220, 220, 220], [200, 200, 200, 200, 200, 200, 200], [180, 180, 180, 180, 180, 180, 180], [160, 160, 160, 160, 160, 160, 160], [140, 140, 140, 140, 140, 140, 140]]
#lvl3
winover3 = 2
winup3 = 4
playover3 = 2
playup3 = 0
Lvl3reset = [[1, 1, 3, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 4, 1, 1]]

Lvl3 = [[1, 1, 3, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 4, 1, 1]]
Lvl3wid = [[260, 280, 300, 320, 340], [260, 280, 300, 320, 340], [260, 280, 300, 320, 340], [260, 280, 300, 320, 340], [260, 280, 300, 320, 340]]
Lvl3hei = [[240, 240, 240, 240, 240], [220, 220, 220, 220, 220], [200, 200, 200, 200, 200], [180, 180, 180, 180, 180], [160, 160, 160, 160, 160]]
#lvl4
winover4 = 3
winup4 = 2
playover4 = 3
playup4 = 0
Lvl4reset = [[1, 1, 1, 3, 1, 1, 1], [1, 2, 1, 1, 1, 2, 1], [1, 1, 1, 4, 1, 1, 1]]

Lvl4 = [[1, 1, 1, 3, 1, 1, 1], [1, 2, 1, 1, 1, 2, 1], [1, 1, 1, 4, 1, 1, 1]]
Lvl4wid = [[240, 260, 280, 300, 320, 340, 360], [240, 260, 280, 300, 320, 340, 360], [240, 260, 280, 300, 320, 340, 360]]
Lvl4hei = [[220, 220, 220, 220, 220, 220, 220], [200, 200, 200, 200, 200, 200, 200], [180, 180, 180, 180, 180, 180, 180]]
#lvl5
winover5 = 5
winup5 = 3
playover5 = 5
playup5 = 0
Lvl5reset = [[2, 1, 1, 1, 1, 3, 1, 1, 2, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1], [1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1]]

Lvl5 = [[2, 1, 1, 1, 1, 3, 1, 1, 2, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1], [1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1]]
Lvl5wid = [[200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400], [200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400], [200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400], [200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400]]
Lvl5hei = [[220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220], [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200], [180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180], [160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160]]
#def blink(x,y):
  #global flash, colorvar, dis
  #sleep(1)
  #if flash == 0:
    #print(flash)
    #colorvar = yellow
    #flash = 1
  #if flash == 1:
    #print(flash)
    #colorvar = white
    #flash = 0
  #pygame.draw.rect(dis, colorvar, pygame.Rect(x, y, 10, 10))   
  #pygame.display.update()
def message(msg, color, size, width, height):
  font_style = pygame.font.SysFont("sans-serif", size)
  mesg = font_style.render(msg, True, color)
  dis.blit(mesg, [width, height])
DISPLAYSURF = pygame.display.set_mode((600, 400), 0, 32)
pygame.display.set_caption('Tiptoe')
while True:
    DISPLAYSURF.fill(blue)
    
    if progstart == True:
      message("Tiptoe", red, 100, 175, 50)
      message("Press P To Play", red, 60, 140, 200)
    if progstart == False:
      message("Use arrow keys to move and do not go out of bounds", red, 30, 10, 10)
      message("Blocks dissapear once touched", red, 27, 10, 40)
      message("You must trace over every block before you go to the green ending zone", red, 25, 10, 60)
      message("Level: " + str(level), red, 25, 10, 80)
      ###############################
      if level == 1:
        for h in range(len(Lvl1)):
          for l in range(len(Lvl1[h])):
            if Lvl1[h][l] == 1:
              colorvar = black
            elif Lvl1[h][l] == 2:
              colorvar = blue
            elif Lvl1[h][l] == 4:
              colorvar = green
            elif Lvl1[h][l] == 3:
              colorvar = yellow
              
              #blink(Lvl1wid[h][l], Lvl1hei[h][l])
            elif Lvl1[h][l] == 0:
              colorvar = blue
            pygame.draw.rect(dis, colorvar, pygame.Rect(Lvl1wid[h][l], Lvl1hei[h][l], 10, 10))     
            #end of lvl1
        for event in pygame.event.get():
         if event.type == QUIT:
           pygame.quit()
           sys.exit()
         if event.type == pygame.KEYDOWN:
           print(playup, playover)
           if event.key == pygame.K_UP:
              try:
                if Lvl1[playup+1][playover] == 2:
                  Lvl1 = [[1, 3, 2], [1, 1, 1], [2, 4, 1]]
                  playover = 1
                  playup = 0
                else:
                  Lvl1[playup][playover] = 2
                  playup = playup + 1
                  Lvl1[playup][playover] = 3
                
                pass
              except:
                Lvl1 = [[1, 3, 2], [1, 1, 1], [2, 4, 1]]
                playover = 1
                playup = 0
                pass
           if event.key == pygame.K_DOWN:
              try:
                if Lvl1[playup-1][playover] == 2:
                  Lvl1 = [[1, 3, 2], [1, 1, 1], [2, 4, 1]]
                  playover = 1
                  playup = 0
                elif playup - 1 < 0:
                  Lvl1 = [[1, 3, 2], [1, 1, 1], [2, 4, 1]]
                  playover = 1
                  playup = 0
                else:
                  Lvl1[playup][playover] = 2
                  playup = playup - 1
                  Lvl1[playup][playover] = 3
                  #get rid of negative index accessability
                pass
              except:
                Lvl1 = [[1, 3, 2], [1, 1, 1], [2, 4, 1]]
                playover = 1
                playup = 0
                pass
           if event.key == pygame.K_LEFT:
              try:
                if Lvl1[playup][playover-1] == 2:
                  Lvl1 = [[1, 3, 2], [1, 1, 1], [2, 4, 1]]
                  playover = 1
                  playup = 0
                elif playover - 1 < 0:
                  Lvl1 = [[1, 3, 2], [1, 1, 1], [2, 4, 1]]
                  playover = 1
                  playup = 0
                else:
                  Lvl1[playup][playover] = 2
                  playover = playover - 1
                  Lvl1[playup][playover] = 3
                  #get rid of negative index accesability
                pass
              except:
                Lvl1 = [[1, 3, 2], [1, 1, 1], [2, 4, 1]]
                playover = 1
                playup = 0
                pass
           if event.key == pygame.K_RIGHT:
              try:
                if Lvl1[playup][playover+1] == 2:
                  Lvl1 = [[1, 3, 2], [1, 1, 1], [2, 4, 1]]
                  playover = 1
                  playup = 0
                else:
                  Lvl1[playup][playover] = 2
                  playover = playover + 1
                  Lvl1[playup][playover] = 3
                  #get rid of negative index accesability
                pass
              except:
                Lvl1 = [[1, 3, 2], [1, 1, 1], [2, 4, 1]]
                playover = 1
                playup = 0
        if winover == playover and winup == playup:      
          levelpassed = True
          for h in range(len(Lvl1)):
             for l in range(len(Lvl1[h])):
                if Lvl1[h][l] == 1:
                  levelpassed = False
                  
          if levelpassed == True:
            level = level + 1
            winover = 10
          else:
            Lvl1 = [[1, 3, 2], [1, 1, 1], [2, 4, 1]]
            playover = 1
            playup = 0      
                
      if level == 4:
        for h in range(len(Lvl2)):
          for l in range(len(Lvl2[h])):
            if Lvl2[h][l] == 1:
              colorvar = black
            elif Lvl2[h][l] == 2:
              colorvar = blue
            elif Lvl2[h][l] == 4:
              colorvar = green
            elif Lvl2[h][l] == 3:
              colorvar = yellow
              
              #blink(Lvl1wid[h][l], Lvl1hei[h][l])
            elif Lvl2[h][l] == 0:
              colorvar = blue
            pygame.draw.rect(dis, colorvar, pygame.Rect(Lvl2wid[h][l], Lvl2hei[h][l], 10, 10))     
            #end of lvl1
        for event in pygame.event.get():
         if event.type == QUIT:
           pygame.quit()
           sys.exit()
         if event.type == pygame.KEYDOWN:
           print(playup2, playover2)
           if event.key == pygame.K_UP:
              try:
                if Lvl2[playup2+1][playover2] == 2:
                  Lvl2 = [[1, 1, 1, 3, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 2, 2, 2, 1, 1], [1, 1, 2, 2, 2, 1, 1], [1, 1, 2, 2, 2, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 4, 1, 1]]
                  playover2 = 3
                  playup2 = 0
                else:
                  Lvl2[playup2][playover2] = 2
                  playup2 = playup2 + 1
                  Lvl2[playup2][playover2] = 3
                
                pass
              except:
                Lvl2 = [[1, 1, 1, 3, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 2, 2, 2, 1, 1], [1, 1, 2, 2, 2, 1, 1], [1, 1, 2, 2, 2, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 4, 1, 1]]
                playover2 = 3
                playup2 = 0
                pass
           if event.key == pygame.K_DOWN:
              try:
                if Lvl2[playup2-1][playover2] == 2:
                  Lvl2 = [[1, 1, 1, 3, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 2, 2, 2, 1, 1], [1, 1, 2, 2, 2, 1, 1], [1, 1, 2, 2, 2, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 4, 1, 1]]
                  playover2 = 3
                  playup2 = 0
                elif playup2 - 1 < 0:
                  Lvl2 = [[1, 1, 1, 3, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 2, 2, 2, 1, 1], [1, 1, 2, 2, 2, 1, 1], [1, 1, 2, 2, 2, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 4, 1, 1]]
                  playover2 = 3
                  playup2 = 0
                else:
                  Lvl2[playup2][playover2] = 2
                  playup2 = playup2 - 1
                  Lvl2[playup2][playover2] = 3
                  #get rid of negative index accessability
                pass
              except:
                Lvl2 = [[1, 1, 1, 3, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 2, 2, 2, 1, 1], [1, 1, 2, 2, 2, 1, 1], [1, 1, 2, 2, 2, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 4, 1, 1]]
                playover2 = 3
                playup2 = 0
                pass
           if event.key == pygame.K_LEFT:
              try:
                if Lvl2[playup2][playover2-1] == 2:
                  Lvl2 = [[1, 1, 1, 3, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 2, 2, 2, 1, 1], [1, 1, 2, 2, 2, 1, 1], [1, 1, 2, 2, 2, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 4, 1, 1]]
                  playover2 = 3
                  playup2 = 0
                elif playover2 - 1 < 0:
                  Lvl2 = [[1, 1, 1, 3, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 2, 2, 2, 1, 1], [1, 1, 2, 2, 2, 1, 1], [1, 1, 2, 2, 2, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 4, 1, 1]]
                  playover2 = 3
                  playup2 = 0
                else:
                  Lvl2[playup2][playover2] = 2
                  playover2 = playover2 - 1
                  Lvl2[playup2][playover2] = 3
                  #get rid of negative index accesability
                pass
              except:
                Lvl2 = [[1, 1, 1, 3, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 2, 2, 2, 1, 1], [1, 1, 2, 2, 2, 1, 1], [1, 1, 2, 2, 2, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 4, 1, 1]]
                playover2 = 3
                playup2 = 0
                pass
           if event.key == pygame.K_RIGHT:
              try:
                if Lvl2[playup2][playover2+1] == 2:
                  Lvl2 = [[1, 1, 1, 3, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 2, 2, 2, 1, 1], [1, 1, 2, 2, 2, 1, 1], [1, 1, 2, 2, 2, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 4, 1, 1]]
                  playover2 = 3
                  playup2 = 0
                else:
                  Lvl2[playup2][playover2] = 2
                  playover2 = playover2 + 1
                  Lvl2[playup2][playover2] = 3
                  #get rid of negative index accesability
                pass
              except:
                Lvl2 = [[1, 1, 1, 3, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 2, 2, 2, 1, 1], [1, 1, 2, 2, 2, 1, 1], [1, 1, 2, 2, 2, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 4, 1, 1]]
                playover2 = 3
                playup2 = 0
        if winover2 == playover2 and winup2 == playup2:      
          levelpassed = True
          for h in range(len(Lvl2)):
             for l in range(len(Lvl2[h])):
                if Lvl2[h][l] == 1:
                  levelpassed = False
                  
          if levelpassed == True:
            level = level + 1
            winover2 = 10
          else:
            Lvl2 = [[1, 1, 1, 3, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 2, 2, 2, 1, 1], [1, 1, 2, 2, 2, 1, 1], [1, 1, 2, 2, 2, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 4, 1, 1]]
            playover2 = 3
            playup2 = 0   
        pass
      if level == 3:
        for h in range(len(Lvl3)):
          for l in range(len(Lvl3[h])):
            if Lvl3[h][l] == 1:
              colorvar = black
            elif Lvl3[h][l] == 2:
              colorvar = blue
            elif Lvl3[h][l] == 4:
              colorvar = green
            elif Lvl3[h][l] == 3:
              colorvar = yellow
              
              #blink(Lvl1wid[h][l], Lvl1hei[h][l])
            elif Lvl3[h][l] == 0:
              colorvar = blue
            pygame.draw.rect(dis, colorvar, pygame.Rect(Lvl3wid[h][l], Lvl3hei[h][l], 10, 10))     
            #end of lvl1
        for event in pygame.event.get():
         if event.type == QUIT:
           pygame.quit()
           sys.exit()
         if event.type == pygame.KEYDOWN:
           print(playup3, playover3)
           if event.key == pygame.K_UP:
              try:
                if Lvl3[playup3+1][playover3] == 2:
                  Lvl3 = [[1, 1, 3, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 4, 1, 1]]
                  playover3 = 2
                  playup3 = 0
                else:
                  Lvl3[playup3][playover3] = 2
                  playup3 = playup3 + 1
                  Lvl3[playup3][playover3] = 3
                
                pass
              except:
                Lvl3 = [[1, 1, 3, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 4, 1, 1]]
                playover3 = 2
                playup3 = 0
                pass
           if event.key == pygame.K_DOWN:
              try:
                if Lvl3[playup3-1][playover3] == 2:
                  Lvl3 = [[1, 1, 3, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 4, 1, 1]]
                  playover3 = 2
                  playup3 = 0
                elif playup3 - 1 < 0:
                  Lvl3 = [[1, 1, 3, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 4, 1, 1]]
                  playover3 = 2
                  playup3 = 0
                else:
                  Lvl3[playup3][playover3] = 2
                  playup3 = playup3 - 1
                  Lvl3[playup3][playover3] = 3
                  #get rid of negative index accessability
                pass
              except:
                Lvl3 = [[1, 1, 3, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 4, 1, 1]]
                playover3 = 2
                playup3 = 0
                pass
           if event.key == pygame.K_LEFT:
              try:
                if Lvl3[playup3][playover3-1] == 2:
                  Lvl3 = [[1, 1, 3, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 4, 1, 1]]
                  playover3 = 2
                  playup3 = 0
                elif playover3 - 1 < 0:
                  Lvl3 = [[1, 1, 3, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 4, 1, 1]]
                  playover3 = 2
                  playup3 = 0
                else:
                  Lvl3[playup3][playover3] = 2
                  playover3 = playover3 - 1
                  Lvl3[playup3][playover3] = 3
                  #get rid of negative index accesability
                pass
              except:
                Lvl3 = [[1, 1, 3, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 4, 1, 1]]
                playover3 = 2
                playup3 = 0
                pass
           if event.key == pygame.K_RIGHT:
              try:
                if Lvl3[playup3][playover3+1] == 2:
                  Lvl3 = [[1, 1, 3, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 4, 1, 1]]
                  playover3 = 2
                  playup3 = 0
                else:
                  Lvl3[playup3][playover3] = 2
                  playover3 = playover3 + 1
                  Lvl3[playup3][playover3] = 3
                  #get rid of negative index accesability
                pass
              except:
                Lvl3 = [[1, 1, 3, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 4, 1, 1]]
                playover3 = 2
                playup3 = 0
        if winover3 == playover3 and winup3 == playup3:      
          levelpassed = True
          for h in range(len(Lvl3)):
             for l in range(len(Lvl3[h])):
                if Lvl3[h][l] == 1:
                  levelpassed = False
                  
          if levelpassed == True:
            level = level + 1
            winover3 = 10
          else:
            Lvl3 = [[1, 1, 3, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 4, 1, 1]]
            playover3 = 2
            playup3 = 0
        pass
      if level == 2:
        for h in range(len(Lvl4)):
          for l in range(len(Lvl4[h])):
            if Lvl4[h][l] == 1:
              colorvar = black
            elif Lvl4[h][l] == 2:
              colorvar = blue
            elif Lvl4[h][l] == 4:
              colorvar = green
            elif Lvl4[h][l] == 3:
              colorvar = yellow
              
              #blink(Lvl1wid[h][l], Lvl1hei[h][l])
            elif Lvl4[h][l] == 0:
              colorvar = blue
            pygame.draw.rect(dis, colorvar, pygame.Rect(Lvl4wid[h][l], Lvl4hei[h][l], 10, 10))     
            #end of lvl1
        for event in pygame.event.get():
         if event.type == QUIT:
           pygame.quit()
           sys.exit()
         if event.type == pygame.KEYDOWN:
           print(playup4, playover4)
           if event.key == pygame.K_UP:
              try:
                if Lvl4[playup4+1][playover4] == 2:
                  Lvl4 = [[1, 1, 1, 3, 1, 1, 1], [1, 2, 1, 1, 1, 2, 1], [1, 1, 1, 4, 1, 1, 1]]
                  playover4 = 3
                  playup4 = 0
                else:
                  Lvl4[playup4][playover4] = 2
                  playup4 = playup4 + 1
                  Lvl4[playup4][playover4] = 3
                
                pass
              except:
                Lvl4 = [[1, 1, 1, 3, 1, 1, 1], [1, 2, 1, 1, 1, 2, 1], [1, 1, 1, 4, 1, 1, 1]]
                playover4 = 3
                playup4 = 0
                pass
           if event.key == pygame.K_DOWN:
              try:
                if Lvl4[playup4-1][playover4] == 2:
                  Lvl4 = [[1, 1, 1, 3, 1, 1, 1], [1, 2, 1, 1, 1, 2, 1], [1, 1, 1, 4, 1, 1, 1]]
                  playover4 = 3
                  playup4 = 0
                elif playup4 - 1 < 0:
                  Lvl4 = [[1, 1, 1, 3, 1, 1, 1], [1, 2, 1, 1, 1, 2, 1], [1, 1, 1, 4, 1, 1, 1]]
                  playover4 = 3
                  playup4 = 0
                else:
                  Lvl4[playup4][playover4] = 2
                  playup4 = playup4 - 1
                  Lvl4[playup4][playover4] = 3
                  #get rid of negative index accessability
                pass
              except:
                Lvl4 = [[1, 1, 1, 3, 1, 1, 1], [1, 2, 1, 1, 1, 2, 1], [1, 1, 1, 4, 1, 1, 1]]
                playover4 = 3
                playup4 = 0
                pass
           if event.key == pygame.K_LEFT:
              try:
                if Lvl4[playup4][playover4-1] == 2:
                  Lvl4 = [[1, 1, 1, 3, 1, 1, 1], [1, 2, 1, 1, 1, 2, 1], [1, 1, 1, 4, 1, 1, 1]]
                  playover4 = 3
                  playup4 = 0
                elif playover4 - 1 < 0:
                  Lvl4 = [[1, 1, 1, 3, 1, 1, 1], [1, 2, 1, 1, 1, 2, 1], [1, 1, 1, 4, 1, 1, 1]]
                  playover4 = 3
                  playup4 = 0
                else:
                  Lvl4[playup4][playover4] = 2
                  playover4 = playover4 - 1
                  Lvl4[playup4][playover4] = 3
                  #get rid of negative index accesability
                pass
              except:
                Lvl4 = [[1, 1, 1, 3, 1, 1, 1], [1, 2, 1, 1, 1, 2, 1], [1, 1, 1, 4, 1, 1, 1]]
                playover4 = 3
                playup4 = 0
                pass
           if event.key == pygame.K_RIGHT:
              try:
                if Lvl4[playup4][playover4+1] == 2:
                  Lvl4 = [[1, 1, 1, 3, 1, 1, 1], [1, 2, 1, 1, 1, 2, 1], [1, 1, 1, 4, 1, 1, 1]]
                  playover4 = 3
                  playup4 = 0
                else:
                  Lvl4[playup4][playover4] = 2
                  playover4 = playover4 + 1
                  Lvl4[playup4][playover4] = 3
                  #get rid of negative index accesability
                pass
              except:
                Lvl4 = [[1, 1, 1, 3, 1, 1, 1], [1, 2, 1, 1, 1, 2, 1], [1, 1, 1, 4, 1, 1, 1]]
                playover4 = 3
                playup4 = 0
        if winover4 == playover4 and winup4 == playup4:      
          levelpassed = True
          for h in range(len(Lvl4)):
             for l in range(len(Lvl4[h])):
                if Lvl4[h][l] == 1:
                  levelpassed = False
                  
          if levelpassed == True:
            level = level + 1
            winover4 = 10
          else:
            Lvl4 = [[1, 1, 1, 3, 1, 1, 1], [1, 2, 1, 1, 1, 2, 1], [1, 1, 1, 4, 1, 1, 1]]
            playover4 = 3
            playup4 = 0
        pass
      if level == 5:
        for h in range(len(Lvl5)):
          for l in range(len(Lvl5[h])):
            if Lvl5[h][l] == 1:
              colorvar = black
            elif Lvl5[h][l] == 2:
              colorvar = blue
            elif Lvl5[h][l] == 4:
              colorvar = green
            elif Lvl5[h][l] == 3:
              colorvar = yellow
              
              #blink(Lvl1wid[h][l], Lvl1hei[h][l])
            elif Lvl5[h][l] == 0:
              colorvar = blue
            pygame.draw.rect(dis, colorvar, pygame.Rect(Lvl5wid[h][l], Lvl5hei[h][l], 10, 10))     
            #end of lvl1
        for event in pygame.event.get():
         if event.type == QUIT:
           pygame.quit()
           sys.exit()
         if event.type == pygame.KEYDOWN:
           print(playup5, playover5)
           if event.key == pygame.K_UP:
              try:
                if Lvl5[playup5+1][playover5] == 2:
                  Lvl5 = [[2, 1, 1, 1, 1, 3, 1, 1, 2, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1], [1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1]]
                  playover5 = 5
                  playup5 = 0
                else:
                  Lvl5[playup5][playover5] = 2
                  playup5 = playup5 + 1
                  Lvl5[playup5][playover5] = 3
                
                pass
              except:
                Lvl5 = [[2, 1, 1, 1, 1, 3, 1, 1, 2, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1], [1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1]]
                playover5 = 5
                playup5 = 0
                pass
           if event.key == pygame.K_DOWN:
              try:
                if Lvl5[playup5-1][playover5] == 2:
                  Lvl5 = [[2, 1, 1, 1, 1, 3, 1, 1, 2, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1], [1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1]]
                  playover5 = 5
                  playup5 = 0
                elif playup5 - 1 < 0:
                  Lvl5 = [[2, 1, 1, 1, 1, 3, 1, 1, 2, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1], [1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1]]
                  playover5 = 5
                  playup5 = 0
                else:
                  Lvl5[playup5][playover5] = 2
                  playup5 = playup5 - 1
                  Lvl5[playup5][playover5] = 3
                  #get rid of negative index accessability
                pass
              except:
                Lvl5 = [[2, 1, 1, 1, 1, 3, 1, 1, 2, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1], [1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1]]
                playover5 = 5
                playup5 = 0
                pass
           if event.key == pygame.K_LEFT:
              try:
                if Lvl5[playup5][playover5-1] == 2:
                  Lvl5 = [[2, 1, 1, 1, 1, 3, 1, 1, 2, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1], [1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1]]
                  playover5 = 5
                  playup5 = 0
                elif playover5 - 1 < 0:
                  Lvl5 = [[2, 1, 1, 1, 1, 3, 1, 1, 2, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1], [1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1]]
                  playover5 = 5
                  playup5 = 0
                else:
                  Lvl5[playup5][playover5] = 2
                  playover5 = playover5 - 1
                  Lvl5[playup5][playover5] = 3
                  #get rid of negative index accesability
                pass
              except:
                Lvl5 = [[2, 1, 1, 1, 1, 3, 1, 1, 2, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1], [1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1]]
                playover5 = 5
                playup5 = 0
                pass
           if event.key == pygame.K_RIGHT:
              try:
                if Lvl5[playup5][playover5+1] == 2:
                  Lvl5 = [[2, 1, 1, 1, 1, 3, 1, 1, 2, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1], [1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1]]
                  playover5 = 5
                  playup5 = 0
                else:
                  Lvl5[playup5][playover5] = 2
                  playover5 = playover5 + 1
                  Lvl5[playup5][playover5] = 3
                  #get rid of negative index accesability
                pass
              except:
                Lvl5 = [[2, 1, 1, 1, 1, 3, 1, 1, 2, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1], [1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1]]
                playover5 = 5
                playup5 = 0
        if winover5 == playover5 and winup5 == playup5:      
          levelpassed = True
          for h in range(len(Lvl5)):
             for l in range(len(Lvl5[h])):
                if Lvl5[h][l] == 1:
                  levelpassed = False
                  
          if levelpassed == True:
            level = level + 1
            winover5 = 10
          else:
            Lvl5 = [[2, 1, 1, 1, 1, 3, 1, 1, 2, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1], [1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1]]
            playover5 = 5
            playup5 = 0
        pass
      if level == 6:
        pygame.draw.rect(dis, blue, pygame.Rect(0, 0, 1000, 1000))   
        message("You win!", red, 100, 175, 50) 
    for event in pygame.event.get():
      if event.type == QUIT:
       pygame.quit()
       sys.exit()
      if event.type == pygame.KEYDOWN:
        print(playup, playover)
        if event.key == pygame.K_p:
             progstart = False     
    pygame.display.update()
    
    
