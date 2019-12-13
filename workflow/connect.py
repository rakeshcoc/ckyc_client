from pymongo import MongoClient
import json,ast
from django.conf import settings
db =settings.DATABASE_LOCAL
myclient = MongoClient()
mydb = myclient[db]
mycol = mydb["temp_info"]

def to_db(digital_id,detail,status,t):
	value = [detail]
	mycol.insert_one({"_id":str(digital_id),"value":value,"status":status,"type":t})

def set_txn_value(x):
	pass
	# print("!")

def update_db(key,updated_detail):
	count = mycol.count({"_id":str(key)})
	if count == 1:
		x = mycol.find({"_id":str(key)})
		for i in x:
			payload = i["value"]
			payload.append(updated_detail)
			mycol.update_one({"_id":str(key)},{'$set':{"value":payload}})
	else:
		mycol.insert_one({"_id":str(key),"value":[updated_detail]})
		print("Key not present")


def retrieve_info_by_key(key):
	count = mycol.count({"_id":str(key)})
	if count == 0:
		return count
	else:
		x = mycol.find({"_id":str(key)})
		for i in x:
			return i

def localfind(key):
	count = mycol.count({"_id":str(key)})
	return count

def str_to_dict(x):
	y=eval(ast.literal_eval(x.decode('utf-8')))
	return y
