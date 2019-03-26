#pip install pymongo

import pymongo

#connect to db
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

#create DB and collections
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

#check DB and collection
print(myclient.list_database_names())

dblist = myclient.list_database_names()
if "mydatabase" in dblist:
    print("The database exists.")

collist = mydb.list_collection_names()
if "customers" in collist:
    print("The collection exists.")


#Insert Document
mydict = { "name": "John", "address": "Highway 37" }
x = mycol.insert_one(mydict)

#print(x.inserted_id)


#Insert list

mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
#print(x.inserted_ids) 



#MongoDB Find
#x = mycol.find_one()

#print(x)


#find all
#for x in mycol.find():
#  print(x) 

#find some columns
#for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
#  print(x)

print("****************************************************")
#Query
"""myquery = { "address": { "$gt": "S" } }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x) """

#sort
mydoc = mycol.find().sort("name")
#sort("name", 1) #ascending
#sort("name", -1) #descending 
for x in mydoc:
  print(x) 



#delete
myquery = { "address": "Mountain 21" }

mycol.delete_one(myquery) 


#delete many
myquery = { "address": {"$regex": "^S"} }

x = mycol.delete_many(myquery)

print(x.deleted_count, " documents deleted.")

#delete all
x = mycol.delete_many({})

print(x.deleted_count, " documents deleted.")


#delete collection
mycol.drop()


#Update Collection

myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }

mycol.update_one(myquery, newvalues)

#print "customers" after the update:
for x in mycol.find():
  print(x) 


#update many
myquery = { "address": { "$regex": "^S" } }
newvalues = { "$set": { "name": "Minnie" } }

x = mycol.update_many(myquery, newvalues)

print(x.modified_count, "documents updated.")


#limit the result


myresult = mycol.find().limit(5)

#print the result:
for x in myresult:
  print(x) 