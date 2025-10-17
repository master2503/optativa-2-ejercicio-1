from motor.motor_asyncio import AsyncIOMotorClient

MONGO_DETAILS = "mongodb://localhost:27017"  # o tu URL de Atlas
MONGO_DB = "kanbamdb"  # <- debe ser string, con comillas

client = AsyncIOMotorClient(MONGO_DETAILS)
db = client[MONGO_DB]
