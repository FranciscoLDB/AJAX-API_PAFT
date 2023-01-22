from flask import Flask
from flask import request
from flask import Response
from datetime import datetime
import json 
import re
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Olá Flask"

@app.route('/data/<diai>/<diaf>')
def difDias(diai, diaf):    
    di = datetime.strptime(str(diai), '%Y-%m-%d')
    df = datetime.strptime(str(diaf), '%Y-%m-%d')
    quantidade_dias = abs((df - di).days)
    quantidade_semanas = int(quantidade_dias/7)
    quantidade_meses = int(quantidade_dias/30)

    res = {
        "diferencaDias": quantidade_dias,
        "diferencaSemanas": quantidade_semanas,
        "diferencaMeses": quantidade_meses
    }
    return res

@app.route('/numeros/<numeros>')
def numeros(numeros):
    temp = re.findall(r'\d+', numeros)
    array = list(map(int, temp))
    array.sort()
    arrayC = array.copy();
    array.reverse();
    arrayR = array.copy();
    arrayP = []
    for i in array:
        if(i%2 == 0):
            arrayP.append(i)    
    res = {
        "ordemCrescente": arrayC,
        "ordemDecrescente": arrayR,
        "numerosPares": arrayP
    }
    return res

app.run(debug=True)