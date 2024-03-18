import pygame 
import sys 

from scripts.settings import *
from game_state import Game

# initialise pygame
pygame.init()


# define screen settings
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Main Menu")
clock = pygame.time.Clock()

# define music
pygame.mixer.init()
tts_music = 'data/music/Menu_Screen.wav'
pygame.mixer.music.load(tts_music)

# define fonts
font = pygame.font.Font(FONT1, 80)
font1 = pygame.font.Font(FONT2, 80)

# define variables for transparent surface
trans_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA, pygame.RESIZABLE)
trans_rect = pygame.Rect(WIDTH - 700, 0, 700, 900)
pygame.draw.rect(trans_surface, (0, 0, 0, 208), trans_rect)

# create button function
def draw_button(surface, x, y, width, height, text, text_colour, font, hover_colour=None):
    button_rect = pygame.Rect(x, y, width, height)

    # Check if the mouse is over the button
    is_hovered = button_rect.collidepoint(pygame.mouse.get_pos())

    button_text = font.render(text, True, text_colour)

    # Adjust font size based on the hover state
    if is_hovered:
        font_size = 40  # Increased font size when hovered
    else:
        font_size = 36

    button_text = pygame.font.Font.render(font, text, True, text_colour)
    button_text = pygame.transform.scale(button_text, (width, height))

    # Center the text on the button
    text_rect = button_text.get_rect(center=button_rect.center)

    surface.blit(button_text, text_rect.topleft)

    # Draw the arrows when hovered or clicked
    if is_hovered:
        pygame.draw.polygon(surface, WHITE, [(x-20, y+height/2), (x, y+height/2+20), (x, y+height/2-20)])  # Left arrow
        pygame.draw.polygon(surface, WHITE, [(x+width+20, y+height/2), (x+width, y+height/2+20), (x+width, y+height/2-20)])  # Right arrow

    return button_rect

# class for the main menu screen including game states 

class Main_Menu:
    # create title menu game state
    def title_screen():

        # define bg animation frames
        ticks = 8 
        frames = []
        number_of_frames= 29 
        for i in range(number_of_frames):
            image = pygame.image.load(f'data/images/tts/wooded trail, Ryan Haight-{i}.tiff')
            image = pygame.transform.scale(image, (WIDTH, HEIGHT))
            frames.append(image)
        
        current_frame = 0 

        while True:
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.play(-1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if the mouse click is on the "Play" button
                    if play_button.collidepoint(event.pos):
                        # Add code here to change game state
                        pygame.mixer.music.stop
                        Game().run()

                    # Check if the mouse click is on the "Information" button 
                    elif info_button.collidepoint(event.pos): 
                        print('options')
                    # Check if the mouse click is on the "Options" button 
                    elif options_button.collidepoint(event.pos):
                        print('information')
                    # Check if the mouse click is on the "Quit" button
                    elif quit_button.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

            
            # Clear Screen
            screen.fill((0, 0, 0))
            # Draw the title and buttons
            # tmbg = title menu background
            screen.blit(frames[current_frame], (0, 0))
            # Move to the next bg frame
            current_frame = (current_frame + 1) % number_of_frames

            # Draw the rectangle on the screen
            screen.blit(trans_surface, (0, 0))


            # Draw play button
            play_button = draw_button(screen, WIDTH - 450, 250, 200, 50, "Play", WHITE, font1, hover_colour=GRAY)

            # Draw information button 
            info_button = draw_button(screen, WIDTH - 450, 400, 200, 70, "Information", WHITE, font1, hover_colour=GRAY)

            # Draw options button 
            options_button = draw_button(screen, WIDTH - 450, 550, 200, 70, "Options", WHITE, font1, hover_colour=GRAY)

            # Draw quit button
            quit_button = draw_button(screen, WIDTH - 450, 700, 200, 50, "Quit", WHITE, font1, hover_colour=GRAY)

            pygame.display.flip()
            pygame.display.update()
            clock.tick(ticks)
        

Main_Menu.title_screen()