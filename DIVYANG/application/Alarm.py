import pymongo

if __name__ =="__main__":

    client = pymongo.MongoClient("mongodb+srv://python:python@cluster1.zptukby.mongodb.net/majority")
    print(client)
    db = client['Alarm']
    collection = db['labview']
    insertThese =[
  { "_id": 1, "name": "INLET TEMPERATURE HIGH" },
  { "_id": 2, "name": "EMERGENCY STOP" },
  { "_id": 3, "name": "POWER FAILURE" },
  { "_id": 4, "name": "MAIN AIR PRESSURE LOW" },
  { "_id": 5, "name": "PRODUCT CONTAINER NOT IN POSITION" },
  { "_id": 6, "name": "BED TEMPERATURE IS LOW" },
  { "_id": 7, "name": "BED TEMPERATURE IS LOW" },
  { "_id": 8, "name": "EARTHING FAULT" },
  { "_id": 9, "name": "BED TEMPERATURE IS HIGH" },
  { "_id": 10, "name": "EXHAUST BLOWER OVERLOAD" },
  { "_id": 11, "name": "PRODUCT CONTAINER NOT IN POSITION" },
  { "_id": 12, "name": "SOLID FLOW MONITOR TRIPPED" },
  { "_id": 13, "name": "INLET TEMPERATURE HIGH" },
  { "_id": 14, "name": "AHU DOOR NOT CLOSED" },
  { "_id": 15, "name": "UPS POWER FAIL" },
  { "_id": 16, "name": "EMERGENCY STOP" },
  { "_id": 17, "name": "EMERGENCY STOP" },
  { "_id": 18, "name": "MAIN AIR PRESSURE LOW" },
  { "_id": 19, "name": "POWER FAILURE" },
  { "_id": 20, "name": "MAIN AIR PRESSURE LOW" },
  { "_id": 21, "name": "PRODUCT CONTAINER NOT IN POSITION" },
  { "_id": 22, "name": "BED TEMPERATURE IS LOW" },
  { "_id": 23, "name": "EARTHING FAULT" },
  { "_id": 24, "name": "BED TEMPERATURE IS HIGH" },
  { "_id": 25, "name": "EMERGENCY STOP" },
  { "_id": 26, "name": "EMERGENCY STOP" },
  { "_id": 27, "name": "INLET TEMPERATURE HIGH" },
  { "_id": 28, "name": "AHU DOOR NOT CLOSED" },
  { "_id": 29, "name": "MAIN AIR PRESSURE LOW" },
  { "_id": 30, "name": "UPS POWER FAIL" },
  { "_id": 31, "name": "MAIN AIR PRESSURE LOW" },
  { "_id": 32, "name": "INLET TEMPERATURE HIGH" },
  { "_id": 33, "name": "SOLID FLOW MONITOR TRIPPED" },
  { "_id": 34, "name": "SOLID FLOW MONITOR TRIPPED" },
  { "_id": 35, "name": "SOLID FLOW MONITOR TRIPPED" },
  { "_id": 36, "name": "SOLID FLOW MONITOR TRIPPED" },
  { "_id": 37, "name": "EMERGENCY STOP" },
  { "_id": 38, "name": "POWER FAILURE" },
  { "_id": 39, "name": "MAIN AIR PRESSURE LOW"},
  { "_id": 40, "name": "BED TEMPERATURE IS LOW" },
  { "_id": 41, "name": "BED TEMPERATURE IS LOW" },
  { "_id": 42, "name": "BED TEMPERATURE IS HIGH" },
  { "_id": 43, "name": "EARTHING FAULT" },
  { "_id": 44, "name": "EARTHING FAULT" },
  { "_id": 45, "name": "EXHAUST BLOWER OVERLOAD" },
  { "_id": 46, "name": "EXHAUST BLOWER OVERLOAD" },
  { "_id": 47, "name": "UPS POWER FAIL" },
  { "_id": 48, "name": "UPS POWER FAIL" },
  { "_id": 49, "name": "UPS POWER FAIL" },
  { "_id": 50, "name": "INLET TEMPERATURE HIGH" },

  
    ]

    collection.insert_many(insertThese)
   