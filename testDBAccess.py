import pymongo, mongoDbConnection

dbConn = mongoDbConnection.get_DB()
#sampleQuery = {"name":"Gurtok"}

#for document in dbConn.find():
    #print(document)

#findOneDB = dbConn.find_one(sampleQuery)
#findOneTuple = str(tuple(findOneDB.items()))

#docs = dbConn.find()
keys = dbConn.distinct(None)

#for key in keys:
    #print(key)

if keys != None:
    #rint("FIND ONE" + findOneTuple)
    #print(list(findOneDB.keys()))
    for key in keys:
        print(key)
else:
    print("Found NONE")