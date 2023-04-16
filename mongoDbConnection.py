import pymongo, sys

class MongoDbConnection:
    devMongoDbAdrStub = ("mongodb://")
    devMongoDbHost = "localhost"
    devMongoDbPort = "42000"
    devMongoDatabaseName = "basicDB"
    collectionName = "testCollection"
    # Build Mongo DB URI
    devMongoDbUri = devMongoDbAdrStub + devMongoDbHost + ":" + devMongoDbPort + "/" + devMongoDatabaseName
    monogoClient = ""
    db = ""
    collection = ""

    def __init__(self):
        print("Intitializing DB connection to Mongo")
        try:
            self.mongoClient = pymongo.MongoClient(self.devMongoDbUri)
            self.db = self.mongoClient.get_database()
            self.collection = self.db.get_collection(self.collectionName)
            print("print collection" + str(self.collection.find_one({})))
        except Exception as e:
            print("Failed to connect to MongoDB @", self.devMongoDbUri)
            print(e)
            sys.exit()
