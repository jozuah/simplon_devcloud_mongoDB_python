from pymongo import MongoClient
from flask import Flask, jsonify,render_template, request

app = Flask(__name__)

# pprint library is used to make the output look more pretty
from pprint import pprint

# connect to MongoDB
# On remplace l'adresse ip par 'localhost' en local
# Connection sur une VM privée ici
client = MongoClient('mongodb://10.21.0.5.57:27017/')

# #Utilisation de la base de donnée déja créé qui s'apppelle 'test'
# db=client.test

# #On va chercher les données de la collection inventory qui est affilié a test. Pour mongoDb: Collection == Table en SQL
# data = db.inventory.find()

# #Data est un jason, donc on doit aficher les element du json. On peut aussi utiliser les index => data[i]
# for document in data:
#     print(document)


# print("Avec pretty print:")
# pprint(data)


@app.route('/')
def index():
    return "Mon serveur du Tiekson"

#http://localhost:3500/createDB?dbname=madb&colname=fakecollection <== creer un db ainsi qu'une collection + insertion d'une ligne. Si on créé une db et un collection sans insertion elle n'existera pas
@app.route('/createDB',methods = ['GET', 'POST'])
def createDB():
    if request.method == 'GET':
        #récupération des paramètres de l'urll
        db_name = request.values.get('dbname')
        col_name = request.values.get('colname')
        #création de la db
        db = client[f'{db_name}']
        #creation de la collection
        col = db[f'{col_name}']
    
        mydict = { "name": "John", "lastname": "Doe" }
        #insertion de données dans la collection
        insert_into_db = col.insert_one(mydict)

        render = f'la db "{db_name}" a été créé'
        return render
    return "aucune db n'a été créé"

#http://localhost:3500/all_db <== montrer toutes les db de ma mongoDB
@app.route('/all_db')
def show_db():
    #affichage des db de ma db en remote
    return jsonify(client.list_database_names())

#http://52.168.123.57:3500/show?dbname=madb&colname=fakecollection
@app.route('/show', methods = ['GET', 'POST'])
def show_data():
    db_name = request.values.get('dbname')
    col_name = request.values.get('colname')
    db = client[db_name]
    #data = db.fakecollection.find()
    data = [doc for doc in db[col_name].find({}, {"_id":0})]
    return jsonify({'cursor': data })




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3500, debug=True)