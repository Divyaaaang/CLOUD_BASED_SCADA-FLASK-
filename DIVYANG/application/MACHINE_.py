import pymongo

def test(x,y,z):
    client = pymongo.MongoClient("mongodb+srv://python:python@cluster1.zptukby.mongodb.net/majority")
    print(client)
    db = client['Machine']
    collection = db['Time']
    insertThese =[
         {'_id':'1','Input':'Spray-Pump','Duration': x},
         {'_id':'2','Input':'Scrubber-Pump','Duration': y},
         {'_id':'3','Input':'Inlet-Temperature','Duration': z},
       
    ]
    collection.insert_many(insertThese)
