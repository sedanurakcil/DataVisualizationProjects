from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    cars = [{'year': 100 ,'km': 207,'price' : 4040,
             'year': 1000 ,'km': 200,'price' : 4008,
             'year': 1000, 'km': 2078, 'price': 580   }  ]
    return render_template('index.html')

if __name__ == '__main__':
    app.run( host= '0.0.0.0', port = 5000)