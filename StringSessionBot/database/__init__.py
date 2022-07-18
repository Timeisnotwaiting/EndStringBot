from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

MONGO_DB_URI = "mongodb+srv://keshavalpha:keshavalpha@cluster0.htiys.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

mongo = MongoClient(MONGO_DB_URI)
db = mongo.SSB
