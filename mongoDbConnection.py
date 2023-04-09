import pymongo


devMongoDbAddress = ("mongodb://localhost:42000/")
collectionName = "testCollection"

def dbConnection():
    mongoClient = pymongo.MongoClient(devMongoDbAddress)
    db = mongoClient['basicDB']
    collection = db[collectionName]
    return collection
