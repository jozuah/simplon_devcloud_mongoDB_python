require('dotenv').config()
const MongoClient = require('mongodb').MongoClient;
const url = process.env.DB_CONNECTION_STRING;

//Nom de la DB
const dbName = 'testdb'
//Nom de la collection
const colName = 'testcolleciton'

//Lecture du fichier le json est dans la variable all_data_parse
const fs = require('fs');
const all_data = fs.readFileSync('file_1.json');  
const all_data_parse = JSON.parse(all_data);  

//console.log(all_data_parse); 

MongoClient.connect(url, function(err, client) {
    //message d'erreur en cas d'echec de connection
    if (err) throw err;

    //initialisation de la db
    var db = client.db(dbName);
    
    //Insert one car on a une array grace au parsing
    db.collection(colName).insertOne(all_data_parse, function(err, res) {
        if (err) throw err;
        console.log("1 document inserted");
        client.close();
    });
});