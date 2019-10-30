from flask import Flask, jsonify, request
import pymongo 

app = Flask(__name__)

@app.route('/',methods=['GET'])
def verifica():
    return "API Alexa, hosted by Heroku",200

@app.route('/estado',methods=['GET'])
def status():
    my_client = pymongo.MongoClient('url_do_moogo_atlas')

    my_database = my_client.iot
    my_collection = my_database.dispositivos

    my_cursor = my_collection.find()
    
    for item in my_cursor:
        return jsonify(item),200

@app.route('/ligado',methods=['GET'])
def muda_ligado():
    my_client = pymongo.MongoClient('url_do_moogo_atlas')
    my_database = my_client.iot
    my_collection = my_database.dispositivos
    
    my_collection.update_one(
    { "_id": 1 }, # query
    {
        "$set": {       # new data
            "status": "ligado"
        }
    })

    return "OK",200

@app.route('/desligado',methods=['GET'])
def muda_desligado():
    my_client = pymongo.MongoClient('url_do_moogo_atlas')
    my_database = my_client.iot
    my_collection = my_database.dispositivos
    
    my_collection.update_one(
    { "_id": 1 }, # query
    {
        "$set": {       # new data
            "status": "desligado"
        }
    })

    return "OK",200

if __name__ == '__main__':
    app.run()
