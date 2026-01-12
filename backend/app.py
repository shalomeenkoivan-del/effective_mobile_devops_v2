from flask import Flask

port = 8080
app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return "<h1>Hello from Effective Mobile!</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=False)