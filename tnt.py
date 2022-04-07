import pygame

class TNT():
  def __init__(self, x_position, ground_height):
    self.x = x_position
    self.size = 30
    self.ground_height = ground_height
    self.image = pygame.transform.scale(pygame.image.load("tnt.png"), (self.size, self.size))
    self.tnt_rect = ''
    
  def show(self, display):
    display.blit(self.image, (self.x, self.ground_height - self.size))

  #update the position of the tnt every time
  def update(self, deltaTime, velocity):
    self.x -= velocity*deltaTime
    self.tnt_rect = self.image.get_rect(topleft = (self.x,self.ground_height-self.size))

  #check if the tnt get out of the screen
  def check(self):
    if self.x < 0:
      return True
    else: 
      return False


