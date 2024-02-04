import pygame
import time
import random
import cv2
import pygame_gui
import sys
# initialize pygame
pygame.init()

# screen setup
screen_width = 800
screen_height = 600
main_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("TechTales")
text_font = pygame.font.SysFont("Arial",20)
# colours for the game (can be changed)
white = (255, 255, 255)
black = (0, 0, 0)






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

#this checks if user input is correct or not and shows corresponding image on correctness
# def Word_Spell_Check(user_input,correct_word):
#      while True:
        
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()

#         if user_input == correct_word:
#             image_choice = pygame.image.load("Correct.png")
#             image_choice = pygame.transform.scale(image_choice, (100, 100))  # Adjust the size as needed
#             main_screen.blit(image_choice,(280,400))
#             pygame.display.update()
#             pygame.time.delay(600)
#             return
#         elif user_input != correct_word:
#             image_choice = pygame.image.load("Incorrect.png")
#             image_choice = pygame.transform.scale(image_choice, (100, 100))  # Adjust the size as needed
#             main_screen.blit(image_choice,(280,400))
#             pygame.display.update()
#             pygame.time.delay(600)
#             return
       

        

def Word_spell():
    
    clock = pygame.time.Clock()
    

    #gui manager for text input
    manager = pygame_gui.UIManager((screen_width, screen_height))
    
    
    #Create text input line with cursor
    text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((100, 450), (150, 30)), manager=manager, object_id='#main_text_entry')
    UI_REFRESH_RATE = clock.tick(60)/1000

    #dictionary for possible images
    image_collection = {"House.png":"house","door.png":"door","Apple.png":"apple"}
    
    #choose random picture
    #chosen_picture,word = random.choice(list(image_collection.items()))
    #Show given image
    image_key = random.choice(list(image_collection.keys()))
    image_choice = pygame.image.load(image_key)
    image_choice = pygame.transform.scale(image_choice, (300, 300))
    main_screen.blit(image_choice, (250, 140))
    pygame.display.update()

    # word corresponding with image
    word = image_collection[image_key]

    tries = 3
    while True:
        


        word_spell_mous_pos = pygame.mouse.get_pos()

        main_screen.fill("white")

        Word_spell_text = text_font.render("Spell the name of the given object", True, "Black")

        #Display Game prompt
        Word_spell_rect = Word_spell_text.get_rect(center=(400, 100))
        main_screen.blit(Word_spell_text, Word_spell_rect)

        
        


        #Display Quit button
        Word_Spell_Back_Bttn = Game_Button(image=None, coordinates = (640, 460),game_name="QUIT", font=text_font, button_color="Black", highlight_color="Green")
        Word_Spell_Back_Bttn.Highlight_button(word_spell_mous_pos)
        Word_Spell_Back_Bttn.display_button(main_screen)

        

        main_screen.blit(image_choice, (250, 140))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            manager.process_events(event)
                
            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == '#main_text_entry'):
               if event.text == word:
                   image_choice = pygame. image.load( "Correct.png") 
                   image_choice = pygame.transform.scale(image_choice, (100, 100))  # Adjust the size as needed
                   main_screen.blit(image_choice,(280,400))
                   pygame.display.update()
                   pygame.time.delay(1000)
                   image_key = random.choice(list(image_collection.keys()))
                   image_choice =  pygame.image.load(image_key)
                   image_choice =  pygame.transform.scale(image_choice, (300, 300))
                   main_screen.blit(image_choice, (250, 140))
                   word =image_collection[image_key]
                   tries = 3
               else:
                   
                   incorrect = pygame.image.load("Incorrect.png")
                   incorrect = pygame.transform.scale(incorrect, (100, 100))  # Adjust the size as needed
                   main_screen.blit(incorrect,(280,400))
                   pygame.display.update()
                   pygame.time.delay(1000)
                   tries -=1
                   if tries == 0:
                       
                       image_key = random.choice(list(image_collection.keys()))
                       image_choice =  pygame.image.load(image_key)
                       image_choice =  pygame.transform.scale(image_choice, (300, 300))
                       main_screen.blit(image_choice, (250, 140))
                       word = image_collection[image_key]
                       tries = 3
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Word_Spell_Back_Bttn.check_if_clicked(word_spell_mous_pos):
                    main()
        manager.update(UI_REFRESH_RATE)
        manager.draw_ui(main_screen)
            
        pygame.display.update()






def main():
    running = True

    while running:
        main_screen.blit(pygame.image.load("Background.png"),(0,0))

        position_of_mouse = pygame.mouse.get_pos()

        menu = text_font.render("Choose a game", True, "#b68f40")
        menu_rectangle = menu.get_rect(center=(400,100))

        #push text onto main screen
        


        # Please create your game buttons using the this format
        # game_name_here = Game_Button(pygame.image.load("your_button_icon"),(x,y),"The name of your game here",text_font,"Blue","Green")
        Word_Spell_button = Game_Button(pygame.image.load("button.png"),(200,200),"Word Spell",text_font,"Blue","Green")

        main_screen.blit(menu,menu_rectangle)

        #This displays button on screen
        Word_Spell_button.display_button(main_screen)

        #This highlights the button text when the mouse hovers over button
        Word_Spell_button.Highlight_button(position_of_mouse)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #create all if statements for function/game calls
                if Word_Spell_button.check_if_clicked(position_of_mouse):
                    Word_spell() # this can be erased and replaced with function call
                    
                else:
                    break
                    # put name of game here

        # update the display
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()


