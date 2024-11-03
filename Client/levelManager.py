import pygame

from random import choice
from perlin_noise import PerlinNoise
from time import time

from Client.helpers import add_vecs, multiply_vec_float

class Level:

    def __init__(self):
        self.block_width = 30

    def old_create_new_level(self, size):


        #make size odd
        size = size if size % 2 == 1 else size + 1
        self.size = size

        dirs = [[1,0], [0,1], [-1,0], [0,-1]]
        last_dir = None

        self.level = [[1 for i in range(size)] for j in range(size)]

        pos = [round(size/2+.5), round(size/2+.5)]
        self.middle = pos
        iterations = 25

        self.level[pos[1]][pos[0]] = 0
        for i in range(iterations):
            direction = choice(dirs)
            pos = add_vecs(pos, direction)
            self.level[pos[1]][pos[0]] = 0

            #expand
            for direction in dirs:
                temp_loc = add_vecs(pos, direction)
                self.level[temp_loc[1]][temp_loc[0]] = 0


    def create_new_level(self, size):

        level_openness = .05
        freq = 20

        seed = time()

        #make size odd
        size = size if size % 2 == 1 else size + 1
        middle = (size - 1) / 2

        self.level = [[1 for i in range(size)] for j in range(size)]
        self.size = size

        noise = PerlinNoise()

        max_distance_to_center = (size - 1) / 2
        for y in range(size):
            for x in range(size):
                dist_to_center = ((middle - y)**2 + (middle - x)**2)**.5

                if noise([(x+seed/10)/freq,(y+seed/10)/freq]) > -.1 + (dist_to_center / max_distance_to_center)**20: #+ ((dist_to_center / max_distance_to_center)**4)*1.5:
                    self.level[y][x] = 0



    #Danial you lazy fuck
    #Thanks gpt
    def get_border_walls(self):
        rows = len(self.level)
        cols = len(self.level[0])
        border_walls = []

        # Helper function to check if a cell is within bounds and empty
        def is_empty(r, c):
            return 0 <= r < rows and 0 <= c < cols and self.level[r][c] == 0

        # Directions to check neighboring cells (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Find all walls adjacent to empty space
        for r in range(rows):
            for c in range(cols):
                if self.level[r][c] == 1:  # Only check walls
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if is_empty(nr, nc):  # If neighboring cell is empty
                            border_walls.append((c, r))
                            break  # Stop checking other directions for this wall
        self.border_walls = border_walls
        return [pygame.Rect(*multiply_vec_float(add_vecs(wall, [-self.size/2]*2), self.block_width), self.block_width, self.block_width) for wall in border_walls]
        

    def draw(self, screen, camera_scroll):

        for y in range(len(self.level)):
            for x in range(len(self.level[y])):

                if self.level[y][x] == 1:

                    screen_pos = [(x - self.size / 2) * self.block_width,
                                    (y - self.size / 2) * self.block_width]
                    draw_pos = [screen_pos[0] + 1 - camera_scroll[0] , screen_pos[1] + 1 - camera_scroll[1]]
                    #if (x,y) in self.border_walls:
                    #pygame.draw.rect(screen, (255,0,255) if (x,y) in self.border_walls else (255,0,0), [*draw_pos, self.block_width - 2, self.block_width - 2])






