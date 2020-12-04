from flask import Flask, render_template
import RPi.GPIO as GPIO
app = Flask(__name__)
## stuff idk yet lmaoo
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/my-link/')
def my_link():
    print('YOY I GOT CLICKED')
    return 'Turned on?'
if __name__ == '__main__':
    app.run(debug=False)