import pygame
import button
from Network import connect
from _thread import *
from json import dumps, loads
from Network.network import Network
from socket import gethostbyname, gethostname 
import client

start_server_once = [False]

pygame.init()

# Create game window
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")




class MainMenu:
    # Game variables
    def __init__(self):
        self.game_name = False
        self.menu_state = "main"
        self.server_address = ""
        self.user_name1 = ""
        self.id = "-1"

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
        self.join_img = pygame.image.load('Assets/Buttons/join_button.png').convert_alpha()
        self.create_img = pygame.image.load('Assets/Buttons/craete_button.png').convert_alpha()

        # Create button instances
        self.start_button = button.Button(310 * (1080 / 800), 60 * (72 / 60), self.resume_img, 1)
        self.options_button = button.Button(297 * (1080 / 800), 245 * (72 / 60), self.options_img, 1)
        self.quit_button = button.Button(325 * (1080 / 800), 450 * (72 / 60), self.quit_img, 1)
        self.video_button = button.Button(226 * (1080 / 800), 7 * (72 / 60), self.video_img, 1)
        self.audio_button = button.Button(225 * (1080 / 800), 200 * (72 / 60), self.audio_img, 1)
        self.keys_button = button.Button(246 * (1080 / 800), 325 * (72 / 60), self.keys_img, 1)
        self.back_button = button.Button(332 * (1080 / 800), 400 * (72 / 60), self.back_img, 1)
        self.join_button = button.Button(250 * (1080 / 800), 125 * (72 / 60), self.join_img, 1)
        self.create_button = button.Button(250 * (1080 / 800), 350 * (72 / 60), self.create_img, 1)

    def check_whos_in(self):
      def get_names():
          connect.collective_data = self.network.ping(connect.collective_data[self.id])
      while self.menu_state != "game":
          start_new_thread(get_names, ())
          
    def start_game(self):
      self.menu_state = "game"
      client.game_loop(screen=screen)


    def main_menu(self):
        # Game loop 
        run = True
        while run:
            screen.fill((52, 78, 91))

            # Event handler for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if not self.game_name:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN and self.user_name1:
                            self.game_name = True 
                        elif event.key == pygame.K_BACKSPACE:
                            self.user_name1 = self.user_name1[:-1]
                        else:
                            self.user_name1 += event.unicode
                elif self.menu_state == "join":
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN :
                            self.network = Network(self.server_address, {})

                                # fail to connect
                            if not self.network.connected:
                                pass

                            else:
                                # connected, go to waiting page
                                reply = self.network.ping({})
                                self.id = reply["id"]
                                connect.collective_data = reply["data"]
                                self.menu_state = "create"
                        if event.key == pygame.K_BACKSPACE:
                            self.server_address = self.server_address[:-1]
                        else:
                            self.server_address += event.unicode

            # Draw based on the menu state
            if self.game_name:
                # Handle menu states
                if self.menu_state == "main":
                    # if self.start_button.draw(screen):
                    #     print("Game started")
                    if self.options_button.draw(screen):
                        self.menu_state = "options"
                    if self.join_button.draw(screen):
                        self.menu_state = "join"
                    if self.create_button.draw(screen):
                        self.menu_state = "create"        
                    if self.quit_button.draw(screen):
                        run = False

                elif self.menu_state == "options": 
                    # Draw options menu
                    if self.video_button.draw(screen):
                        print("Video Settings")
                    if self.audio_button.draw(screen):
                        print("Audio Settings")
                    if self.keys_button.draw(screen):
                        print("Change Key Bindings")
                    if self.back_button.draw(screen):
                        self.menu_state = "main"
                
                elif self.menu_state == "join":
                    # Display server address input
                    input_rect = pygame.Rect(305 * (108 / 80), 200 * (72 / 60), 200, 32)
                    rec_color = pygame.Color("black")

                    text_surface = self.rec_font.render(self.server_address, True, (255, 255, 255))
                    pygame.draw.rect(screen, rec_color, input_rect, 2) 
                    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
                    
                    if self.back_button.draw(screen):
                        self.menu_state = "main"
                        self.server_address = ""
                
                elif self.menu_state == "create":
                    # Show created server IP address
                    if self.start_button.draw(screen) :
                        print("CALL FUNCTION")
                    
                    if self.back_button.draw(screen): 
                        self.menu_state = "main"
                    
                    player1_rect = pygame.Rect(150 * (108 / 80), 150, 175, 50) 
                    if not start_server_once[0]:
                      player1_server = gethostbyname(gethostname())
                      connect.init_server()
                      start_server_once[0] = True
                      if self.server_address == "":
                        self.server_address = player1_server
                      connect.collective_data['addr'] = player1_server
                      self.network = Network(self.server_address, {})
                    p1_serv = self.rec_font.render(player1_server, True, (255, 255, 255))
                    name_display = self.rec_font.render(self.user_name1, True, (255, 255, 255))
                    
                    pygame.draw.rect(screen, (0, 0, 0), player1_rect)
                    screen.blit(name_display, player1_rect.topleft)
                    screen.blit(p1_serv, (SCREEN_WIDTH * 0.42, SCREEN_HEIGHT * 0.05))

            else:
                # Username entry before the game starts
                user_rect = pygame.Rect(SCREEN_WIDTH // 2 - SCREEN_WIDTH // 12, SCREEN_HEIGHT - (SCREEN_HEIGHT - 50), 144, 32)
                pygame.draw.rect(screen, pygame.Color("white"), user_rect, 2)
                
                user_text_surface = self.rec_font.render(self.user_name1, True, (255, 255, 255))
                screen.blit(user_text_surface, (user_rect.x + 5, user_rect.y + 5))
                
                user_prompt = self.rec_font.render("Enter your username:", True, (255, 255, 255))
                screen.blit(user_prompt, (SCREEN_WIDTH // 8, SCREEN_HEIGHT - (SCREEN_HEIGHT - 55)))

            # Update the display
            pygame.display.flip()



# Initialize and start main menu
xd = MainMenu()
xd.main_menu()
pygame.quit()
