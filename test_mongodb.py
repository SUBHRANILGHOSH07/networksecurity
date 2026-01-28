import certifi
from pymongo.mongo_client import MongoClient

# We add 'tlsDisableOCSPEndpointCheck=true' to skip the check causing the handshake error
uri = "mongodb+srv://subhranilblue07_db_user:<@password>@cluster0.cjqg51b.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0&tlsDisableOCSPEndpointCheck=true"

# Create a new client and connect to the server
client = MongoClient(uri, tlsCAFile=certifi.where())

try:
    client.admin.command('ping')
    print("✅ Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(f"❌ Connection failed: {e}")