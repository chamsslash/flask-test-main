


from sqlalchemy.orm import Session

#====================================================================
from flask import Flask, jsonify, request




# ======================================================================
#=======================================================================
app = Flask(__name__)
@app.route('/megasuperpuper/product/<id>',methods =['GET'])
def get_pr():
        otvet={'answer':'ок!'}
        return jsonify(otvet['answer'])
    

@app.route('/megasuperpuper/productadd',methods =['POST'])
def add_pr():
    name=request.json['name']
    desc = request.json['desc']
    otvet={'answer':'ок!'}
    
    return jsonify(otvet['answer'])

@app.route('/megasuperpuper/productupdate',methods = ['PUT'])
def upd_pr():
    id =request.json['id']
    name=request.json['name']
    desc = request.json['desc']
    otvet={'answer':'ок!'}
    return jsonify(otvet['answer'])





if __name__ == '__main__':#функция запускается только в родном файле(те если ее импортировать то запустить функцию не получится)
    app.run(debug=True)  
    
