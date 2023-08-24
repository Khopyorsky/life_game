import random

from singleton_metaclass import SingletonMeta


class GameOfLife(metaclass=SingletonMeta):
    SYSTEM = tuple((i, j) for i in range(-1, 2) for j in range(-1, 2) if i != 0 or j != 0)

    def __init__(self, width=20, height=20):
        self.__width = width
        self.__height = height
        self.world = self.generate_universe()

    def generate_universe(self):
        return [[random.randint(0, 1) for _ in range(self.__width)] for _ in range(self.__height)]

    def form_new_generation(self):
        new_stage = [[0 for _ in range(self.__width)] for _ in range(self.__height)]
        for i in range(self.__height):
            for j in range(self.__width):
                if self.world[i][j]:
                    if self.__count_neighbours(i, j) in (2, 3):
                        new_stage[i][j] = 1
                elif self.__count_neighbours(i, j) == 3:
                    new_stage[i][j] = 1
        self.world = new_stage

    def __count_neighbours(self, coord_i, coord_j):
        counter = 0
        for value in self.SYSTEM:
            if self.world[(coord_i + value[0]) % self.__height][(coord_j + value[1]) % self.__width]:
                counter += 1
        return counter
