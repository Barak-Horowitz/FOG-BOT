class Custom_Button():
        
    def __init__ (self, width, height, button_color, x_cord, y_cord, text, text_color, text_size):
        print("ENTERED BUTTON")
        self.rect = pygame.Rect(x_cord, y_cord, width, height)
        self.rect.center = (width // 2, height // 2)
        self.button_color = button_color
        self.text = text
        self.text_color = text_color
        self.font = pygame.font.Font(None, text_size)            
   
    def draw(self, surface, text=""):
        pygame.draw.rect(SCREEN, self.color, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
        
   def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
            
            