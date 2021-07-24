# install mongo db and it will be run in service mode
# do not install mongo compress
# install Robo 3T as a db editor
# database/collection(list of dict)/item(dict)

import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client.test
print(db.name)
collection = db.my_collection
print(collection)
collection.insert_one({"x": 10}).inserted_id
collection.insert_one({"x": 8}).inserted_id
collection.insert_one({"x": 11}).inserted_id

print("=" * 20)
print(collection.find_one())
# {'_id': ObjectId('60fbcec04e6a3d6d1ac37382'), 'x': 10}

print("=" * 20)
for item in collection.find():
    print(item["x"])
# 10, 8, 11

print("=" * 20)
collection.create_index("x")
for item in collection.find().sort("x", pymongo.ASCENDING):
    print(item["x"])
# 8, 10, 11

print("=" * 20)
print([item["x"] for item in collection.find().limit(2).skip(1)])
# 8, 11
print([item["x"] for item in collection.find().skip(1).limit(2)])
# 8, 11

# delete one
collection.delete_one({"x": 10})
print([x for x in collection.find()])
# [{'_id': ObjectId('60fbd08ddf865a1468ffe5a1'), 'x': 8}, {'_id': ObjectId('60fbd08ddf865a1468ffe5a2'), 'x': 11}]

# clean
collection.delete_many({})
