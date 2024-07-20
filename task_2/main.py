from pymongo import MongoClient, errors
from bson.objectid import ObjectId
from pymongo.server_api import ServerApi

# Підключення до MongoDB
client = MongoClient(
    "mongodb+srv://goit-test:rVoIjkuy~8DPWi!mV7@testcluster.dwyiq17.mongodb.net/?retryWrites=true&w=majority&appName=TestCluster")
db = client['pet_database']
collection = db['pets']

# Перевірка з'єднання
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except errors.PyMongoError as e:
    print(e)


def create_pet(name, age, features):
    try:
        pet = {"name": name, "age": age, "features": features}
        collection.insert_one(pet)
        print("Pet inserted successfully.")
    except errors.PyMongoError as e:
        print(f"An error occurred: {e}")


def read_all_pets():
    try:
        pets = collection.find()
        for pet in pets:
            print(pet)
    except errors.PyMongoError as e:
        print(f"An error occurred: {e}")


def read_pet_by_name(name):
    try:
        pet = collection.find_one({"name": name})
        if pet:
            print(pet)
        else:
            print(f"No pet found with name: {name}")
    except errors.PyMongoError as e:
        print(f"An error occurred: {e}")


def update_pet_age(name, new_age):
    try:
        result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.modified_count:
            print("Pet age updated successfully.")
        else:
            print(f"No pet found with name: {name}")
    except errors.PyMongoError as e:
        print(f"An error occurred: {e}")


def add_feature_to_pet(name, feature):
    try:
        result = collection.update_one({"name": name}, {"$push": {"features": feature}})
        if result.modified_count:
            print("Feature added successfully.")
        else:
            print(f"No pet found with name: {name}")
    except errors.PyMongoError as e:
        print(f"An error occurred: {e}")


def delete_pet_by_name(name):
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count:
            print("Pet deleted successfully.")
        else:
            print(f"No pet found with name: {name}")
    except errors.PyMongoError as e:
        print(f"An error occurred: {e}")


def delete_all_pets():
    try:
        collection.delete_many({})
        print("All pets deleted successfully.")
    except errors.PyMongoError as e:
        print(f"An error occurred: {e}")


def main():
    print("Welcome to the Pets Database!")
    print("Available commands: create, read_all, read, update_age, add_feature, delete, delete_all, exit")

    while True:
        command = input("Enter command: ").strip().lower()

        if command == "create":
            name = input("Enter pet name: ").strip()
            age = int(input("Enter pet age: ").strip())
            features = input("Enter pet features (comma-separated): ").strip().split(",")
            create_pet(name, age, features)

        elif command == "read_all":
            read_all_pets()

        elif command == "read":
            name = input("Enter pet name: ").strip()
            read_pet_by_name(name)

        elif command == "update_age":
            name = input("Enter pet name: ").strip()
            new_age = int(input("Enter new age: ").strip())
            update_pet_age(name, new_age)

        elif command == "add_feature":
            name = input("Enter pet name: ").strip()
            feature = input("Enter new feature: ").strip()
            add_feature_to_pet(name, feature)

        elif command == "delete":
            name = input("Enter pet name: ").strip()
            delete_pet_by_name(name)

        elif command == "delete_all":
            delete_all_pets()

        elif command == "exit":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
