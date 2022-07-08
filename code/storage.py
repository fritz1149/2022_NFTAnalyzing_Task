import pymongo

myclient = pymongo.MongoClient("mongodb://admin:20011013ccCC!@47.94.225.40:27017/")
mydb = myclient["ZJU_CAMP"]
mycol = mydb["NFT"]

def insert(data, _id):
    data["_id"] = _id
    mycol.insert_one(data)
    
def append(_id, data):
    query = {"_id": _id}
    push = {"$push": {"assets": data}}
    mycol.update_one(query, push)
    
if __name__ == "__main__":
    append("0xccc441ac31f02cd96c153db6fd5fe0a2f4e6a68d", {"name": "test"})