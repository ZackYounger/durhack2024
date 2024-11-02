import pygame
import button

pygame.init()

# Create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

class MainMenu:
    # Game variables
    def __init__(self):
        self.game_start = False
        self.menu_state = "main"

        # Define fonts
        self.font = pygame.font.SysFont("arialblack", 40)

        # Define colors
        self.TEXT_COL = (255, 255, 255)

        # Load button images
        self.resume_img = pygame.image.load("images/button_resume.png").convert_alpha()
        self.options_img = pygame.image.load("images/button_options.png").convert_alpha()
        self.quit_img = pygame.image.load("images/button_quit.png").convert_alpha()
        self.video_img = pygame.image.load('images/button_video.png').convert_alpha()
        self.audio_img = pygame.image.load('images/button_audio.png').convert_alpha()
        self.keys_img = pygame.image.load('images/button_keys.png').convert_alpha()
        self.back_img = pygame.image.load('images/button_back.png').convert_alpha()

        # Create button instances
        self.start_button = button.Button(304, 125, self.resume_img, 1)
        self.options_button = button.Button(297, 250, self.options_img, 1)
        self.quit_button = button.Button(336, 375, self.quit_img, 1)
        self.video_button = button.Button(226, 75, self.video_img, 1)
        self.audio_button = button.Button(225, 200, self.audio_img, 1)
        self.keys_button = button.Button(246, 325, self.keys_img, 1)
        self.back_button = button.Button(332, 450, self.back_img, 1)

    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    def main_menu(self):
        # Game loop
        run = True
        while run:
            screen.fill((52, 78, 91))

            # Check if game is started
            if not self.game_start:
                # Check menu state
                if self.menu_state == "main":
                    # Draw pause screen buttons
                    if self.start_button.draw(screen):
                        self.game_start = True
                        print("Game started")
                    if self.options_button.draw(screen):
                        self.menu_state = "options"
                    if self.quit_button.draw(screen):
                        run = False
                else : 
                    if self.menu_state == "options":
                    # Draw the different options buttons
                        if self.video_button.draw(screen):
                            print("Video Settings")
                        if self.audio_button.draw(screen):
                            print("Audio Settings")
                        if self.keys_button.draw(screen):
                            print("Change Key Bindings")
                        if self.back_button.draw(screen):
                            self.menu_state = "main"        
            
            else :
                print("GAME START")
            # Event handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            pygame.display.update()

class SeverMenu() :
    def __init__(self):
        pass            
    
    
    
xd = MainMenu()
xd.main_menu()

pygame.quit()

