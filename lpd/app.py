
from flask import Flask, render_template
import matplotlib.pyplot as plt
import matplotlib
import time
import pandas as pd
import io
from scipy.stats import gaussian_kde
app = Flask(__name__)

def getwidhts():
    widhts = [(0, 3), (4, 7), (8, 10), (11, 15), (16, 23), (24, 34), (35, 45), (46, 49), (50, 57), (58, 62), (63, 70),
              (74, 80), (84, 90), (91, 100), (101, 108), (109, 118)]

    df = pd.read_fwf("ldp.dat",calspec = widhts)

    return df
@app.route('/image.png')
def image_scatter():
    df = getwidhts()

    fig =df['I0'].plot(kind= 'hist', x='A', title='Asymptotic level density ').get_figure()

    output = io.BytesIO()
    fig.savefig(output, format='png')
    return output.getvalue(), 200, {"Content-Type": "image/png"}








@app.route('/')
def index():

    return render_template("index.html")


if __name__ == '__main__':
    app.run()