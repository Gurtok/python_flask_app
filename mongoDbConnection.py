import pymongo, sys


devMongoDbAddress = ("mongodb://localhost:42000/")
collectionName = "testCollection"

monogoClient = ""
db = ""

# When this class is instantiated, we establish DB connection.
# Following DB calls will be run through this pool to avoid pool exhaustion errors.
def __init__():
    try:
        mongoClient = pymongo.MongoClient(devMongoDbAddress)
        db = mongoClient['basicDB']
        print("Connected to Mongo: ", devMongoDbAddress)
    except Exception as e:
        print("Failed to connect to MongoDB @", devMongoDbAddress)
        print(e)
        sys.exit()


# Called by monboDbInsert & mongoDbRead classes
# All instances should call this method to avoid multiple DB connections
# Return: Object to the database for read/writes
def get_DB():
    if db != None:
        print("Connected to Mongo: ", devMongoDbAddress)
        return db
    else:
        print("DB connection failed")


# Called by mongoDbRead
# Returns object of type COLLECTION
def get_DB_Collection():
    collection = db[collectionName]
    if collection != None:
        return collection
    else:
        print("DB Collection is NULL")


