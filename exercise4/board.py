import numpy as np


class Board:


     def __init__(self,width, height):
         self.width = width
         self.height = height
         self.grid = np.zeros((height,width), dtype=int)

     def clear(self):
         self.grid = np.zeros((self.height,self.width),dtype=int)

     def set_cell(self,x,y,alive =True):
         if 0 <= x < self.width and 0 <= y < self.height:
                self.grid[y,x] = 1 if alive else 0

     def get_cell(self,x,y):

         if 0 <= x < self.width and 0 <= y < self.height:
             return self.grid[y,x]

     def toggle_cell(self,x,y):
         if 0 <= x <self.width and 0 <= y < self.height:
             self.grid[y,x] = 1- self.grid[y,x]


     def set_pattern(self, pattern, start_x=0, start_y=0):

         for dx,dy in pattern:
             x = start_x + dx
             y = start_y + dy

             if 0<=x <self.width and 0<=y < self.height:\
                 self.grid[y,x] = 1

     def count_neigbours(self,x,y,boundery = 'periodic'):
         count = 0
         directions = [
             (-1, -1), (-1, 0), (-1, 1),
             (0, -1), (0, 1),
             (1, -1), (1, 0), (1, 1)
         ]

         for dx,dy in directions:
             nx,ny = x+dx, y+dy
             #zapetlenie
             if boundery == 'periodic':
                 nx = nx% self.width
                 ny = ny% self.height
                 count += self.grid[ny,nx]
             if boundery == 'reflective':

                 if 0 <= nx < self.width and 0 <= ny < self.height:
                     cout = self.grid[ny,nx]
                 # gdy poza planszą to traktuje jako martwy

         return count


     def next_generation(self,boundery = 'periodic'):

         # new_grid= np.zeros((self.height,self.width), dtype=int)
         #
         # for y in range(0,self.height):
         #     for x in range(0,self.width):
         #         neighbors = self.count_neigbours(x,y,boundery)
         #         current_cell = self.grid[y][x]
         #         if current_cell ==1:
         #             if neighbors ==2 or neighbors ==3:
         #                 new_grid[y, x] = 1
         #                 # innaczej umiera
         #
         #         else:
         #             if neighbors == 3:
         #                 new_grid[y, x] = 1
         # self.grid = new_grid

        new_grid = np.zeros((self.height, self.width), dtype=int)

        for y in range(0, self.height):
            for x in range(0, self.width):
                neighbors = self.count_neigbours(x, y, boundery)
                current_cell = self.grid[y][x]

                if current_cell == 1:
                    if neighbors >= 2 and neighbors <= 6:  # przeżywa przy 2-6 sąsiadach
                        new_grid[y, x] = 1
                else:
                    if neighbors >= 2 and neighbors <= 4:  # rodzi się przy 2-4 sąsiadach
                        new_grid[y, x] = 1

        self.grid = new_grid