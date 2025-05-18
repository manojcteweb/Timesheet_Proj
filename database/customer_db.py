from pymongo import MongoClient
from bson import ObjectId

class Database:
    def __init__(self, uri: str, db_name: str):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def get_collection(self, collection_name: str):
        return self.db[collection_name]

# Initialize the database
database = Database("mongodb://localhost:27017/", "mydatabase")
customers_collection = database.get_collection("customers")

def insert_customer(customer_data: dict) -> ObjectId:
    """Insert a new customer into the database."""
    result = customers_collection.insert_one(customer_data)
    return result.inserted_id

def find_customer_by_id(customer_id: str) -> dict:
    """Find a customer by their ID."""
    return customers_collection.find_one({"_id": ObjectId(customer_id)})

def update_customer_by_id(customer_id: str, update_data: dict) -> bool:
    """Update a customer's information by their ID."""
    result = customers_collection.update_one(
        {"_id": ObjectId(customer_id)}, {"$set": update_data}
    )
    return result.matched_count > 0

def delete_customer_by_id(customer_id: str) -> bool:
    """Delete a customer by their ID."""
    result = customers_collection.delete_one({"_id": ObjectId(customer_id)})
    return result.deleted_count > 0
