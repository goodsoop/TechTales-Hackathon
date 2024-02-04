import os
import sys
import pygame
import time
import random 
# GLOBALS 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# colours for the game (can be changed)
white = (255, 255, 255)
black = (0, 0, 0)

class Scene(object): # virtual class 
    def __init__(self):
        pass

    def render(self, screen):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def handle_events(self, events):
        raise NotImplementedError
    
class SceneHandler(object):
    def __init__(self):
        # 1st STATE
        self.go_to(TitleScreen())

    def go_to(self, scene):
        self.scene = scene
        self.scene.manager = self

class TitleScreen(object): # TITLE SCENE / MAIN MENU
    def __init__(self):
        super(TitleScreen, self).__init__()
        # Set up fonts
        self.text_font = pygame.font.SysFont("Arial", 36)
        # game_name_here = Game_Button(pygame.image.load("your_button_icon"),(x,y),"The name of your game here",text_font,"Blue","Green")
        button1 = Game_Button(pygame.image.load("Button.png"),(200,200),"Game1",self.text_font,"Blue","Green")
        button2 = Game_Button(pygame.image.load("Button.png"), (200, 320), "Flash Cards", self.text_font, "Blue", "Red")
        self.game1_button = button1 
        self.game2_button = button2

    def render(self, main_screen):
        main_screen.fill(white)
        main_screen.blit(pygame.image.load("Background.png"),(0,0))
        menu = self.text_font.render("Choose a game", True, "#b68f40")
        menu_rectangle = menu.get_rect(center=(400,100))
        #push text onto main screen
        main_screen.blit(menu,menu_rectangle)       
        # This displays button on screen
        self.game1_button.display_button(main_screen)
        self.game2_button.display_button(main_screen)
        #This highlights the button text when the mouse hovers over button
        self.game1_button.Highlight_button(self.position_of_mouse)
        self.game2_button.Highlight_button(self.position_of_mouse)

    def update(self):
        pass 

    def handle_events(self, events):
        pos_of_mos = pygame.mouse.get_pos()
        self.position_of_mouse = pos_of_mos

        for event in events:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # create all if statements for function/game calls
                if self.game1_button.check_if_clicked(self.position_of_mouse):
                    print('Button clicked')
                if self.game2_button.check_if_clicked(self.position_of_mouse):
                    print('Launching flash cards game .... ')
                    # CREATE CLASS 4 FLASH CARDS & LOAD ASSESTS
                    words = ["TV", "DOG", "AIRPLANE"];  # WORDS 
                    img_list = ["tv.png", "dog.png", "airplane.png"] # FILE PATH 
                    self.manager.go_to(Flash_Cards(img_list, words))
                else:
                    break
                    # put name of game here

class GameScene(Scene): # instance of buttons -> Game1, Game2, etc... 
    def __init__(self, button): # initialize pygame
        super(GameScene, self).__init__()

    def render(self, window):
        pass

    def update(self):
        pass

    def handle_events(self, event):
        pass

class Game_Button():
	def __init__(self, image, coordinates, game_name, font, button_color, highlight_color):
		self.image = image
		self.x_pos = coordinates[0]
		self.y_pos = coordinates[1]
		self.font = font
		self.base_color, self.hovering_color = button_color, highlight_color
		self.text_input = game_name
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def display_button(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def check_if_clicked(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def Highlight_button(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

class Flash_Cards(Scene): # NEW SCENE -> had to be custom & not apart of game scene
    def __init__(self, lst, words_list): # entire range of pictures
        self.test_font = pygame.font.SysFont('Comic Sans MS', 30)
        self.index = 0 # changes during gameplay 
        self.img_list = lst
        self.SIZE = len(lst)-1 
        self.word_list = words_list

    def get_lst(self):
        return self.img_list[self.index]
        
    def draw_text(self, word): # will be list later 4 each respective image 
        text_surface = self.test_font.render(word, False, (0, 0, 0))
        return text_surface
 
    def get_index(self):
        if (self.index >= self.SIZE):
            self.index = 0 # RESET 
        else:
            self.index = self.index + 1
        return self.index

    def check_click(self, hitbox, mouse):
        if hitbox.collidepoint(mouse):
            self.get_index() 
            print("hit RED")

    def load_image(self, name, colorkey=None): # where name = 'image.png'
        fullname = os.path.join('pictures', name)
        try:
            image = pygame.image.load(fullname)
        except pygame.error:
            print ("Cannot load image:", name)
            raise SystemExit
        image = image.convert()
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
                image.set_colorkey(colorkey, RLEACCEL)
        img_rect = image.get_rect(topleft = (200,100))
        return image, img_rect
    
    def update(self):
        pass

    def render(self, main_screen): #  - - - RENDER - -- - -
        frame_rect = pygame.Rect(250, 100, 300, 300)
        pygame.draw.rect(main_screen, black, frame_rect, 300)
        #main_screen.blit(pygame.image.load("Background.png"),(0,0))
        main_screen.fill(white)
        # draw_arrow()
        vertices = ((50, 70),(70,70),(70,50),(90, 80),(70, 110),(70, 90),(50, 90))            
        pygame.draw.lines(main_screen, pygame.Color("red"), True, vertices, 1)
        # img border
        frame_rect = pygame.Rect(250, 100, 300, 300)
        pygame.draw.rect(main_screen, black, frame_rect, 300)
        # RENDER IMG 
        ts = self.draw_text(self.word_list[self.index])
        main_screen.blit(ts, (SCREEN_WIDTH/2,SCREEN_HEIGHT-100))
        # load assets
        # name = img_list[i] ; i = get_index() 
        file_path_str = self.get_lst()
        img, img_rect = self.load_image(file_path_str)
        main_screen.blit(img, img_rect)

    def handle_events(self, events):
        position_of_mouse = pygame.mouse.get_pos()
        for event in events:
#            if pygame.event.get(pygame.QUIT):
#                self.manager.go_to(TitleScene())
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                hitbox = pygame.Rect(50, 70, 50, 110)
                self.check_click(hitbox, position_of_mouse)

def main():
    RUNNING = True
    input_text = ""
    pygame.init()

    # screen setup
    MAIN_SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("TechTales")
    clock = pygame.time.Clock()
    handler = SceneHandler()
    while RUNNING:
        clock.tick(60) 

        # process input 
        handler.scene.handle_events(pygame.event.get())
        # clear screen
        handler.scene.render(MAIN_SCREEN)                
        # update the display
        handler.scene.update()

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main() 
