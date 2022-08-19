from flask import Flask ,render_template
import pandas  as pd

import io
import matplotlib.pyplot as plt
import matplotlib
app = Flask(__name__)


def get_masses():
    #(2i4, 1x(bosluk),a2, 1x,i1, 4f10.3, 4f8.3)
    widhts = [(1,4),(5,8),(9,11), (12,13),(14,23),(24,33),(34,43),(44,53),(54,61),(62,69),(70,77),(78,-1)]
    df = pd.read_fwf("mass.dat",colspecs= widhts)
    #mass deki dataleı widthlere göre dataframe bırakıcak
    df.dropna(subset = ["Mexp"], inplace= True)
    #Mexp sutununda nan olan satırları çıkarıcak dropna ile
    return df

#resmi python ile yazma
@app.route("/masses.png")
def masses_png():
    df = get_masses()
    fig = df.plot(kind="scatter", x="Z", y="A").get_figure()
    output = io.BytesIO()
    fig.savefig(output, format ="png")
    #resim bir yere kaydolmucak outputa kaydediyorum  ramde çalışcak
    return output.getvalue(),200,{"Content-Type": "image/png"}
    #olumlu 200 requestini vericek sonuç

#dynamic root
@app.route("masses_<int:z>.html")
def masses_z_html(z):
    df = get_masses()
    df = df[df["Z"]== z]
    return render_template("masses_z.html",z=z,masses_a = df["A"].tolist())



@app.route('/')
def index():
    get_masses()
    return render_template('index.html')


if __name__ == '__main__':

    app.run()
 """ df.plot(kind='scatter', x='A', y='', title='Asymptotic level density ',
            xlabel='A - Mass Number', ylabel='ainf + - aerr [1/Mev\]')

    df['IO'].plot(kind='hist', title='Spin of the ground state',ylabel='Frequency')

    plt.show()
    
 1.ci
fig = df.plot(kind= 'scatter', x= 'A', y = 'dW', title = 'Shell Correction Energy', x_lim = df['A'](-15,10), y_lim = df['dW'](0,300) ,
            xlabel = 'A - Mass Number', ylabel = 'dW[Mev]').get_figure()
fig.savefig(output, format = 'png')fig = df.plot(kind='box', x='A', y='ainf', title='Asymptotic level density',xlabel='A - Mass