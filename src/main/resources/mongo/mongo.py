import pymongo
from pymongo import MongoClient
client = MongoClient("mongodb://developer:developer@oc-cluster.127.0.0.1.nip.io:31017/?authSource=sampledb")
db = client['sampledb']
print (db)
db = client.sampledb
print (db)
Employee = db.Employee
Employee.find()
Employee = db.Employee.insert_one({
    "name": "Varun Singh",
    "Designation": "Developer",
    "description": "Phython Software Developer"
});
print(db.Employee.count_documents({}))