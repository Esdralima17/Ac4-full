from flask import Flask, request, jsonify, make_response
from Models.Model import Model

app = Flask(__name__)

@app.route('v1/aula/consultar/', methods=["GET"])
def consultar():
    return ProModel.jsonReturn()

     

if __name__ =='__main__':
    app.run(debug=True,port=5000)
