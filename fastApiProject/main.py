from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import io
import mpld3


app = FastAPI()
"""html sayfası erişimi için"""
origins = ["null", "http://localhost:63342" ]

"""html sayfaları bu sayfaya istek yaparken izin veriliyor"""

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials= True,
    allow_methods= ["*"],
    allow_headers= ["*"]
)

class RandomNumbers:
    def __init__(self,n):
        self.n = n
        self.data = np.random.randint(0,100,n)
        """ product n numbers between 0 and 100  and hold this number   in np(list)"""

    def get_data(self):
        return self.data.tolist()

    def add(self,n):
        self.data = np.append(self.data,np.random.randint(0,100,n))



@app.get("/random/{n}")
async def random_numbers(n: int):
    r= RandomNumbers(n)
    return r.get_data()

"""we create  histogram with seaborn and save it buffer and return rasponse """
@app.get("/histogram/{n}", responses={
    404: {"description": "Not Found"},
    200: {"content": {"image/png":{}}}
})
async def histogram_seaborn(n:int):
    r= RandomNumbers(n)
    fig = sns.histplot(r.get_data(), bins= 10).get_figure()
    with io.BytesIO() as fig_bytes:
        fig.savefig(fig_bytes, format = 'png')
        fig_bytes.seek(0)
        response = Response(fig_bytes.getvalue(),media_type = "image/png")
        plt.close()
        """üst üste plt ler oluşmaması için her çağrıldığında """
    return response


@app.get("/interactive_histogram/{n}")
async def interactive_histogram(n: int):
    r= RandomNumbers(n)
    fig = sns.histplot(r.get_data(), bins = 10).get_figure()
    plt.close()
    return HTMLResponse(mpld3.fig_to_html(fig))

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/")
async def root():
    return {"message": "Hello World"}