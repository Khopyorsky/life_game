import random

from singleton_metaclass import SingletonMeta


class GameOfLife(metaclass=SingletonMeta):
    SYSTEM = tuple((i, j) for i in range(-1, 2) for j in range(-1, 2) if i != 0 or j != 0)

    def __init__(self, width=20, height=20):
        self.__width = width
        self.__height = height
        self.__generation = None
        self.world = None
        self.old_world = None

    @property
    def generation(self):
        return self.__generation

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    def create_new_world(self):
        self.world = [[random.randint(0, 1) for _ in range(self.__width)] for _ in range(self.__height)]
        self.old_world = [[0 for _ in range(self.__width)] for _ in range(self.__height)]
        self.__generation = 0

    def form_new_generation(self):
        new_stage = [[0 for _ in range(self.__width)] for _ in range(self.__height)]
        for i in range(self.__height):
            for j in range(self.__width):
                if self.world[i][j]:
                    if self.__count_neighbours(i, j) in (2, 3):
                        new_stage[i][j] = 1
                elif self.__count_neighbours(i, j) == 3:
                    new_stage[i][j] = 1
        if self.generation > 0:
            self.old_world = self.world
        self.world = new_stage
        self.__generation += 1

    def __count_neighbours(self, coord_i: int, coord_j: int):
        counter = 0
        for i, j in self.SYSTEM:
            neighbour_coord_i = coord_i + i
            neighbour_coord_j = coord_j + j
            if (0 <= neighbour_coord_i < self.__height and 0 <= neighbour_coord_j < self.__width and
                    self.world[neighbour_coord_i][neighbour_coord_j]):
                counter += 1

        return counter
