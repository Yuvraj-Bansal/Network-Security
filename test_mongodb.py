from pymongo.mongo_client import MongoClient
from urllib.parse import quote_plus

uri = f"mongodb+srv://yuvrajbnsl:yuvraj12345@cluster0.g4yaw6z.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0&authSource=admin"

client = MongoClient(uri)

try:
    client.admin.command("ping")
    print("Connected successfully to MongoDB!")
except Exception as e:
    print("Connection failed:", e)
