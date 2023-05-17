import pymongo

def test(a,b,c,d,e,f,g,h):
    client = pymongo.MongoClient("mongodb+srv://python:python@cluster1.zptukby.mongodb.net/majority")
    print(client)
    db = client['labview']
    collection = db['python']
    insertThese =[
         {'_id':'1','Input':'Spray-Pump','Reading': a},
         {'_id':'2','Input':'Scrubber-Pump','Reading': b},
         {'_id':'3','Input':'Inlet-Temperature','Reading': c},
         {'_id':'4','Input':'Bed-Temperature','Reading': d},
         {'_id':'5','Input':'Exhaust-Temperature','Reading': e},
         {'_id':'6','Input':'Spray Gun-1 Pressure','Reading': f},
         {'_id':'7','Input':'Spray Gun-2 Pressure','Reading': g},
         {'_id':'8','Input':'Spray Gun-3 Pressure','Reading': h},
      
    ]
    collection.insert_many(insertThese)
   

 