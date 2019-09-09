from pymongo import MongoClient
myclient = MongoClient()
mydb = myclient["ckyc"]
mycol = mydb["info"]
mycol.delete_one({"a":"b"})
print(myclient.list_database_names())
	