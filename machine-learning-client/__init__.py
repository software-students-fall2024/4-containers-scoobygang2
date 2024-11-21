from pymongo import MongoClient

# MongoDB setup
client = MongoClient("mongodb://database/scoobygang")
db = client.audio_analysis
collection = db.audio_logs

__all__ = ["client", "db", "collection"]