from flask import Flask, request, Response
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

def calculate_dif_dates(diai, diaf):
    days = abs(diaf-diai).days
    weeks = int(days/7)
    months = 12 * (diaf.year - diai.year) + abs(diaf.month - diai.month)
    return {
        "diferencaDias": days,
        "diferencaSemanas": weeks,
        "diferencaMeses": months
    }

@app.route('/data', methods=['GET'])
def difDias2():
    if 'diai' in request.args and 'diaf' in request.args:
        diai = datetime.strptime(str(request.args.get('diai')), '%Y-%m-%d')
        diaf = datetime.strptime(str(request.args.get('diaf')), '%Y-%m-%d')
        return calculate_dif_dates(diai, diaf)

    return Response("<h1>400-BAD REQUEST - Input error </h1>", status = 400)

@app.route('/numeros/<numeros>')
def numeros(numeros):
    temp = re.findall(r'\d+', numeros)
    array = list(map(int, temp))
    array.sort()
    arrayC = array.copy();
    array.reverse();
    arrayR = array.copy();
    arrayP = [];
    for i in array:
        if(i%2 == 0):
            arrayP.append(i);  
    res = {
        "ordemCrescente": arrayC,
        "ordemDecrescente": arrayR,
        "numerosPares": arrayP
    }
    return res

@app.route('/mimimi/<texto>')
def mimimi(texto):
    texto.lower();
    res = texto;
    vogais = ["a", "A", "e", "E", "o", "O", "u", "U", "I"];
    for vogal in vogais:
        res = res.replace(vogal, "i");
    res = {
        "mimimi": res
    }
    return res;

app.run(debug=True)