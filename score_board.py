import pygame
#make the score board

class Scoreboard():
  def __init__(self,score):
    self.font = pygame.font.Font("arial.ttf",20)
    self.text = self.font.render('Points: ' + str(score), True, (0,0,0))
    self.text_rect = self.text.get_rect(center = (300,10))

  def show(self,display):
    display.blit(self.text,self.text_rect)