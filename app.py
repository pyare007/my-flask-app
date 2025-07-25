from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello All, It is a GCP CI/CD implementation...'

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)