from game_of_life import GameOfLife
from environs import Env

env = Env()
env.read_env()

game: GameOfLife = GameOfLife(width=int(env('WIDTH')),
                              height=int(env('HEIGHT')))
