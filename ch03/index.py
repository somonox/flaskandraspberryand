from flask import Flask, render_template
import RPi.GPIO as GPIO
import json
import db_model

app = Flask(__name__)
LED = 8
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

status = { GPIO.HIGH: 'ON', GPIO.LOW: 'OFF' }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/led/on')
def led_on():
    GPIO.output(LED, GPIO.HIGH)
    db_model.add_status(status[GPIO.HIGH])
    return json.dumps({'status': GPIO.HIGH})

@app.route('/led/off')
def led_off():
    GPIO.output(LED, GPIO.LOW)
    db_model.add_status(status[GPIO.LOW])
    return json.dumps({'status': GPIO.LOW})

if __name__ == '__main__':
    app.run(host='0.0.0.0')