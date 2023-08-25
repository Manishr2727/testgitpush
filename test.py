import pymongo

''''
*code is for for tesseract server*
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://tesseractonline23:mongodb27@cluster0.gmbmgin.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
'''''

client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


m = {
    "name":"manish",
    "email":"manish@ineuron.ai",
    "surname":"rajput"
}
db1 = client['mongorule']
coll = db1['rule']
coll.insert_one(m)
