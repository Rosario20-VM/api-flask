
from flask import Flask, jsonify, send_file
from flask_cors import CORS, cross_origin


app = Flask (__name__)

CORS(app)

@cross_origin
@app.route('/', methods=['GET'])

def home():
    ruta= open ("./correos.txt","r")
    spam=ruta.read(4)
    ham=ruta.read(4)
    response = jsonify(cantidad =[{"spam": str(spam), "ham": str(ham) }])
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@cross_origin
@app.route('/prediccion', methods=['GET'])

def prediccion():
    ruta= open ("./prediccion.txt","r")
    prediccion=ruta.read()
    response= jsonify(prediccion =[{"Prediccion": str(prediccion)}])
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@cross_origin
@app.route('/porcentaje', methods=['GET'])

def porcentaje():
    ruta= open ("./porcentaje.txt","r")
    porcentaje=ruta.read()
    response= jsonify(porcentaje =[{"Porcentaje": str(porcentaje)}])
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@cross_origin
@app.route('/imagen', methods=['GET'])

def imagen():
    response = send_file('./Correos.jpg', attachment_filename='Correos.jpg')
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response





if __name__ == '__main__':
    app.run(port=5000)