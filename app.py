from flask import Flask

DEBUG = True
PORT = 8000

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name = "Aheebwa Ramadhan"):
    return "<h1>Welcome to SendIT API, by {}</h1>".format(name)

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)


