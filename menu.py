import pygame
import button
from Network import connect
from socket import gethostbyname, gethostname 

pygame.init()

# Create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

class MainMenu:
    # Game variables
    def __init__(self):
        self.game_name = False
        self.menu_state = "main"
        self.server_address = ""
        self.user_name1 = ""

        # Define fonts
        self.font = pygame.font.SysFont("arialblack", 40)
        self.rec_font = pygame.font.Font(None, 32)

        # Define colors
        self.TEXT_COL = (255, 255, 255)

        # Load button images
        self.resume_img = pygame.image.load("Assets/Buttons/button_resume.png").convert_alpha()
        self.options_img = pygame.image.load("Assets/Buttons/button_options.png").convert_alpha()
        self.quit_img = pygame.image.load("Assets/Buttons/button_quit.png").convert_alpha()
        self.video_img = pygame.image.load('Assets/Buttons/button_video.png').convert_alpha()
        self.audio_img = pygame.image.load('Assets/Buttons/button_audio.png').convert_alpha()
        self.keys_img = pygame.image.load('Assets/Buttons/button_keys.png').convert_alpha()
        self.back_img = pygame.image.load('Assets/Buttons/button_back.png').convert_alpha()
        self.f1_img = pygame.image.load('images/sq/x/f1.png').convert_alpha()
        self.f2_img = pygame.image.load('images/sq/x/f2.png').convert_alpha()

        # Create button instances
        # TEMP values
        self.start_button = button.Button(304, 125, self.resume_img, 1)
        self.options_button = button.Button(297, 250, self.options_img, 1)
        self.quit_button = button.Button(336, 375, self.quit_img, 1)
        self.video_button = button.Button(226, 75, self.video_img, 1)
        self.audio_button = button.Button(225, 200, self.audio_img, 1)
        self.keys_button = button.Button(246, 325, self.keys_img, 1)
        self.back_button = button.Button(332, 450, self.back_img, 1)
        self.join_button = button.Button(225, 40, self.f1_img, 1)
        self.create_button = button.Button(200, 375,self.f2_img, 1)

    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    def main_menu(self):
        # Game loop 
        run = True
        while run:
            screen.fill((52, 78, 91))
             
           
            # Check if game is started
            if self.game_name:
                # Check menu state
                if self.menu_state == "main":
                    # Draw pause screen buttons
                    if self.start_button.draw(screen):
                        self.game_name = True
                        print("Game started")
                    if self.options_button.draw(screen):
                        self.menu_state = "options"
                    if self.join_button.draw(screen) :
                        self.menu_state = "join"
                    if self.create_button.draw(screen) :
                        self.menu_state = "create"        
                    if self.quit_button.draw(screen):
                        run = False
                
                elif self.menu_state == "options" : 
                    # Draw the different options buttons
                    if self.video_button.draw(screen):
                        print("Video Settings")
                    if self.audio_button.draw(screen):
                        print("Audio Settings")
                    if self.keys_button.draw(screen):
                        print("Change Key Bindings")
                    if self.back_button.draw(screen):
                        self.menu_state = "main"
                
                elif self.menu_state == "join" :
                    # TEMP values
                    # input_box = pygame.Rect(300, 400, 500, 100)
                    # pygame.draw.rect(screen, (0, 0, 0), input_box)
                    #T0DO
                    input_rect = pygame.Rect(200, 200, 144, 32)
                    rec_color = pygame.Color("black")
                    
                    for event in pygame.event.get() :
                        if event.type == pygame.QUIT:
                            run = False
                        
                        if event.type == pygame.KEYDOWN :
                            #if event.key == pygame.K_E
                            if event.key == pygame.K_BACKSPACE :
                                self.server_address = self.server_address[:-1]
                            else :
                                self.server_address += event.unicode
                    
                    text_surface = self.rec_font.render(self.server_address, True, (255, 255, 255))
                    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
                    pygame.draw.rect(screen, rec_color, input_rect, 2) 
                    
                    if self.back_button.draw(screen) :
                        self.menu_state = "main"
                        self.server_address = ""
                
                elif self.menu_state == "create" :
                    if self.back_button.draw(screen) : 
                        self.menu_state = "main"
                        
                        
                    player1_rect = pygame.Rect(600, 0, 150, 100) 
                    player1_server = gethostbyname(gethostname())
                    connect.init_server()
                    p1_serv = self.rec_font.render(player1_server, True, "white")
                    
                    player2_rect = pygame.Rect(100, 100, 150, 100)  
                    player3_rect = pygame.Rect(200, 200, 150 , 100)
                    player4_rect = pygame.Rect(300, 300, 150, 100)      
                        
                    pygame.draw.rect(screen, (255, 0, 255), player1_rect)
                    screen.blit(p1_serv, (330, 0))
                    pygame.draw.rect(screen, (255, 0, 255), player2_rect)
                    pygame.draw.rect(screen, (255, 0, 255), player3_rect)
                    pygame.draw.rect(screen, (255, 0, 255), player4_rect)
                                    
                    
            else :
                user_rect = pygame.Rect(SCREEN_WIDTH//2 - SCREEN_WIDTH//12, SCREEN_HEIGHT - (SCREEN_HEIGHT - 50), 144, 32)
                user_rec_color = pygame.Color("white")
                    
                for event in pygame.event.get() :
                    if event.type == pygame.QUIT :
                        run = False
                     
                    if event.type == pygame.KEYDOWN :
                        if event.key == pygame.K_RETURN and self.user_name1 != ""  : 
                            self.game_name = True 
                        
                        if event.key == pygame.K_BACKSPACE :
                            self.user_name1 = self.user_name1[:-1]
                        else :
                            self.user_name1 += event.unicode
                    
                user_text_surface = self.rec_font.render(self.user_name1, True, (255, 255, 255))
                screen.blit(user_text_surface, (user_rect.x + 5, user_rect.y + 5))
            
                user1_render = self.rec_font.render("Enter your username : ", True, "white")
                screen.blit(user1_render, (SCREEN_WIDTH//8, SCREEN_HEIGHT - (SCREEN_HEIGHT - 55)))
            
                pygame.draw.rect(screen, user_rec_color, user_rect, 5)

            pygame.display.update()
            #     print("GAME START")
            # # Event handler
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         run = False
            
            
            
             
xd = MainMenu()
xd.main_menu()

pygame.quit()

