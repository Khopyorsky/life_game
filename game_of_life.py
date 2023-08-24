import random

from singleton_metaclass import SingletonMeta


class GameOfLife(metaclass=SingletonMeta):
    SYSTEM = tuple((i, j) for i in range(-1, 2) for j in range(-1, 2) if i != 0 or j != 0)

    def __init__(self, width=20, height=20):
        self.__width = width
        self.__height = height
        self.__generation = 0
        self.world = [[random.randint(0, 1) for _ in range(self.__width)] for _ in range(self.__height)]

    @property
    def generation(self):
        return self.__generation

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
        self.__generation += 1

    def __count_neighbours(self, coord_i: int, coord_j: int):
        counter = 0
        for value in self.SYSTEM:
            try:
                if self.world[coord_i + value[0]][coord_j + value[1]]:
                    counter += 1
            except IndexError:
                continue

        return counter
