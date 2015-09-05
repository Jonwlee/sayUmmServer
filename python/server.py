from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/voice')
def read():
    return 'Received voice data'

if __name__ == '__main__':
    app.run()

