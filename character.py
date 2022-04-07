import pygame

#create a character class
class Character():
  def __init__(self, ground_height,userinput):
    self.x = 60
    self.y = 0
    self.ground_height = ground_height
    self.height = 65
    self.width = 35
    self.yvelocity = 0  
    self.image = pygame.transform.scale(pygame.image.load(str(userinput)), (self.width, self.height))
    self.char_rect = ''
  
  def jump(self):
    if self.y == 0: #to prevent jumping mid-air
     self.yvelocity = 300
     
  def update(self, deltaTime):
    self.yvelocity += -500 * deltaTime
    self.y += self.yvelocity * deltaTime
    if self.y < 0:
      self.y = 0
      self.yvelocity = 0
    self.char_rect = self.image.get_rect(topleft = (self.x,self.ground_height-self.y-self.height))

  def show(self, display): 
    display.blit(self.image, (self.x, self.ground_height-self.height-self.y))
    


  