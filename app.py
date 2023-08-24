from flask import Flask, render_template
from game_of_life import GameOfLife

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/life')
def life():
    game = GameOfLife()
    return render_template('life.html')
