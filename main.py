from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return "<a href='/home'>Hi!</a>"

@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact')
def contact():
  return render_template('contact.html', phone = 7442457)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port = 5222, threaded = True, debug = True)