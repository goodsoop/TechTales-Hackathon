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

def main():
    running = True
    input_text = ""

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
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
                else:
                    # add pressed key to the input text
                    input_text += event.unicode

        # clear screen
        screen.fill(white)

        # display the input text on the screen
        text = font.render(input_text, True, black)
        screen.blit(text, (10, 10))

        # update the display
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
