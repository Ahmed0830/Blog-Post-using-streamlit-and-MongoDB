from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
load_dotenv(".env")

uri = os.getenv("uri")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client["test-db"]

collection = db["blog_posts"]

def upload_blog(blog_title, blog_post):
    collection.insert_one({"title": blog_title, "blog": blog_post})

def fetch_all_blogs():
    return collection.find()
