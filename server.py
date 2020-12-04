from flask import Flask, render_template
import RPi.GPIO as GPIO
import time
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/my-link/')
def switch1_On():
  # set the pins numbering mode
    GPIO.setmode(GPIO.BOARD)

    # Select the GPIO pins used for the encoder K0-K3 data inputs
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)

    # Select the signal to select ASK/FSK
    GPIO.setup(18, GPIO.OUT)

    # Select the signal used to enable/disable the modulator
    GPIO.setup(22, GPIO.OUT)

    # Disable the modulator by setting CE pin lo
    GPIO.output (22, False)

    # Set the modulator to ASK for On Off Keying 
    # by setting MODSEL pin lo
    GPIO.output (18, False)

    # Initialise K0-K3 inputs of the encoder to 0000
    GPIO.output (11, False)
    GPIO.output (15, False)
    GPIO.output (16, False)
    GPIO.output (13, False)
    print('YOY I GOT CLICKED')
    GPIO.output(11, False)
    print('got till line 45')
    GPIO.output(15, True)
    print('got till line 48')
    GPIO.output(16, True)
    GPIO.output(13, True)
    print('got till line 51')
    time.sleep(0.1)
    GPIO.output(22, True) # Enable Modulator
    time.sleep(0.25)
    GPIO.output(22, False) # Disable Modulator
    print('worked!')
    return 'Turned on?'
if __name__ == '__main__':
    app.run(debug=False)