from flask import Flask, render_template, request
from procfile import read_file, write_file
app = Flask(__name__)

@app.route('/')
def index():
  return "<a href='/home'>Hi!</a>"

@app.route('/read_file')
def read_from_file():
  content = read_file()
  return content
@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact')
def contact():
  return render_template('contact.html', phone = 7442457)

@app.route('/params')
def params():
  return request.args

@app.route('/post', methods = ['POST'])
def post():
  return request.get_json()

@app.route('/write_file', methods = ['POST'])
def write_to_file():
  request_type = request.content_type
  if request_type == 'application/json':
    contentJSON= request.get_json()
    write_file=(contentJSON['data'])
    return f"line {contentJSON['data']} added to data.txt"
  else:
    return f"request type{request_type} is not supported"

@app.route('/file', methode = ['GET', 'POST'])
def fileWork():
  if request.method == 'GET':
    return read_from_file()
  elif request.method == 'POST':
    return write_to_file()
  else:
    return f"Request method{request.method}not supported!"
if __name__ == '__main__':
  app.run(host='0.0.0.0', port = 5222, threaded = True, debug = True)