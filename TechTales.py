import os
import sys
import pygame
import time

# initialize pygame
pygame.init()

# screen setup
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("TechTales")

# colours for the game (can be changed)
white = (255, 255, 255)
black = (0, 0, 0)

# Set up fonts
font = pygame.font.Font(None, 36)
test_font = pygame.font.SysFont('Comic Sans MS', 30) 

# entire range of pictures
index = 0 # changes during gameplay 
img_list = ["tv.png", "dog.png", "airplane.png"]
SIZE = len(img_list)-1 

# matching sounds to letters
# will need to set up these sounds
# letter_sounds = {
#     'a': 'sounds/a_sound.wav',
#     'b': 'sounds/b_sound.wav',
#     'c': 'sounds/c_sound.wav',
#     'd': 'sounds/d_sound.wav',
#     'e': 'sounds/e_sound.wav',
#     'f': 'sounds/f_sound.wav',
#     'g': 'sounds/g_sound.wav',
#     'h': 'sounds/h_sound.wav',
#     'i': 'sounds/i_sound.wav',
#     'j': 'sounds/j_sound.wav',
#     'k': 'sounds/k_sound.wav',
#     'l': 'sounds/l_sound.wav',
#     'm': 'sounds/m_sound.wav',
#     'n': 'sounds/n_sound.wav',
#     'o': 'sounds/o_sound.wav',
#     'p': 'sounds/p_sound.wav',
#     'q': 'sounds/q_sound.wav',
#     'r': 'sounds/r_sound.wav',
#     's': 'sounds/s_sound.wav',
#     't': 'sounds/t_sound.wav',
#     'u': 'sounds/u_sound.wav',
#     'v': 'sounds/v_sound.wav',
#     'w': 'sounds/w_sound.wav',
#     'x': 'sounds/x_sound.wav',
#     'y': 'sounds/y_sound.wav',
#     'z': 'sounds/z_sound.wav',
# }

# function to play sounds 
# need sounds folder to run this
# def play_sound(letter):
#     """ this function will play the sound of the letter passed as an argument
#     args:
#         letter (str): inputted letter to play the sound of
#     """
#     sound_path = letter_sounds.get(letter)
#     if sound_path:
#         pygame.mixer.Sound(sound_path).play()
def img_border():
    frame_rect = pygame.Rect(250, 100, 300, 300)
    pygame.draw.rect(screen, black, frame_rect, 300)

def draw_text(word): # will be list later 4 each respective image 
    text_surface = test_font.render(word, False, (0, 0, 0))
    screen.blit(text_surface, (screen_width/2,screen_height-100))

def draw_arrow():
    vertices = ((50, 70),(70,70),(70,50),(90, 80),(70, 110),(70, 90),(50, 90))            
    pygame.draw.lines(screen, pygame.Color("red"), True, vertices, 1)
 
def change_img():
    global index 
    if (index >= SIZE):
        index = 0 # RESET 
    i = index + 1
    index = index + 1
    print(i)
    name = img_list[i]
    myimg, myrect = load_image(name)
    screen.blit(myimg, myrect) # draw

def check_click(self, mouse):
        if self.collidepoint(mouse):
            change_img() 
            print("hit RED")

def load_image(name, colorkey=None): # where name = 'image.png'
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

def main():
    running = True
    input_text = ""
    # load assets
    file_path = img_list[index] #tv/dog/airplane.png
    img, img_rect = load_image(file_path)
    # preset word 4 testing
    words = ["TV", "DOG", "AIRPLANE"]; 

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                hitbox = pygame.Rect(50, 70, 50, 110)
                check_click(hitbox, event.pos)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # after the enter key is pressed, play the sound for the entered word
                    for letter in input_text:
                        play_sound(letter)
                        time.sleep(0.5)  # add a short delay between sounds
                    input_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    # case for backspace key
                    input_text = input_text[:-1]
                else: # add pressed key to the input text
                    input_text += event.unicode
     
        # clear screen
        screen.fill(white)

        # display the input text on the screen
        text = font.render(input_text, True, black)
        screen.blit(text, (10, 10))
        
        # render arrow + text + pic 
        draw_arrow()
        img_border()
        draw_text(words[index])
        screen.blit(img, img_rect)

        # update the display
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
