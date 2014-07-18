from finch import Finch
from time import sleep
from flask import Flask
from flask import render_template, redirect
from random import randint

app = Flask(__name__)
finch = Finch()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/change_color')
def change_color():
    finch.led(randint(0, 255), randint(0, 255), randint(0, 255))
    return redirect('/')

@app.route('/halt')
def halt():
    finch.halt()
    return redirect('/')

@app.route('/sensors')
def sensors():
    c = finch.temperature()
    f = ((c * 9)/5 ) + 32

    x, y, z, tap, shake = finch.acceleration()

    left, right = finch.obstacle()

    return render_template('sensors.html', **locals())

try:
    app.run()
finally:
    print('Closing Finch!')
    finch.halt()
    finch.close()
