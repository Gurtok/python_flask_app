import pymongo, MongoDbConnection


dbConn = MongoDbConnection.MongoDbConnection()

sampleQuery = {"name":"Gurtok"}
query = "{}"
collection = dbConn.collection
#print("Print Collection: " + collection)
##documents = collection.find()

if collection == None:
    print("failed DB collection")
else:
    print("print collection" + str(collection.find_one({})))



""" 
print(documents)

for document in documents:
    print(document)
"""


#findOneDB = dbConn.find_one(sampleQuery)
#findOneTuple = str(tuple(findOneDB.items()))

#docs = dbConn.find()
#keys = dbConn.distinct(None)

#for key in keys:
    #print(key)
"""
if keys != None:
    #rint("FIND ONE" + findOneTuple)
    #print(list(findOneDB.keys()))
    for key in keys:
        print(key)
else:
    print("Found NONE")
"""