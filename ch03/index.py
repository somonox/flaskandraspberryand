from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)
LED = 8
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/led/on')
def led_on():
    GPIO.output(LED, GPIO.HIGH)
    return 'LED is ON'

@app.route('/led/off')
def led_off():
    GPIO.output(LED, GPIO.LOW)
    return 'LED is OFF'

if __name__ == '__main__':
    app.run(host='0.0.0.0')