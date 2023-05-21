from flask import Flask
from blueprints import menu

app = Flask(__name__)

app.register_blueprint(menu)

@app.route('/test')
def test():
    return 'Hola mundo'

if __name__ == '__main__':
    app.run(debug=True)
