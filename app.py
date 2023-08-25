from flask import Flask, render_template
from game_config import game

app = Flask(__name__)


@app.route('/')
def index():
    game.create_new_world()
    return render_template('index.html')


@app.route('/life')
def life():
    game.form_new_generation()
    return render_template('life.html', game=game)

