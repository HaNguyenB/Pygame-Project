#using module pygame and random
import pygame
from character import Character
from tnt import TNT
from score_board import Scoreboard
import random

# create global variables
screen_height = 350
screen_width = 600
ground_height = screen_height - 100

#check for user input of what character / try-except statements
def filename():
    while True:
      try:
        userinput = input(("Enter filename for your character: "))
        character = Character(ground_height,userinput)
      except FileNotFoundError or UnicodeDecodeError:
        print("This filename does not exist, please try another!")
      else:
        break
    return character

#main function
def main(): 
  #start up the game
  pygame.init()

  #set up the window
  screen_display = pygame.display.set_mode((screen_width,screen_height))

  #create creeper character
  character = filename()

  #initialize the tnt 
  score = 0
  velocity = 320
  mingap = 300
  maxgap = 700
  tnt_list = []
  num_of_tnt = 5
  last_tnt = screen_width
  for i in range(num_of_tnt):
    last_tnt += mingap + (maxgap - mingap) * random.random()
    tnt_list.append(TNT(last_tnt, ground_height))
  
  #create lastframe variable
  last_frame = pygame.time.get_ticks()
  
  #the game (nested) loop
  run = True
  while run:
    #get current time
    t = pygame.time.get_ticks() 
    delta_time = (t - last_frame)/1000
    last_frame = t
    
    #fill the color of the screen
    screen_display.fill((255,255,255)) 
    
    character.update(delta_time)
    character.show(screen_display)
    characterRect = character.char_rect
    
    for tnt in tnt_list:
      tnt.update(delta_time, velocity)
      tnt.show(screen_display)
      check = tnt.check()
      if check == True:
        score += 1
        last_tnt += mingap + (maxgap - mingap)*random.random()
        tnt.x = last_tnt
      if tnt.tnt_rect.colliderect(characterRect):
        run = False
        
    last_tnt -= velocity * delta_time 

    #draw the surface the creeper run on
    pygame.draw.rect(screen_display, (0,0,0), [0, ground_height, screen_width, screen_height - ground_height]) 
    
    #make the score_board
    score_board = Scoreboard(score)
    score_board.show(screen_display)
    
    #event detection
    for event in pygame.event.get(): 
      if event.type == pygame.QUIT: 
        run = False
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          character.jump()
      
    pygame.display.update() 

main()

