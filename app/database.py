from pymongo import MongoClient
import pymongo
from app.config import settings

client = MongoClient(settings.DATABASE_URL)
print('Connected to MongoDB...')

db = client[settings.MONGO_INITDB_DATABASE]
md_line_of_business = db.md_line_of_business
md_line_of_business.create_index([("_id", pymongo.ASCENDING)], unique=True)

