import pymongo
from pymongo.errors import ConnectionFailure

class MongoDB:
    def __init__(self, dbname):
        "Constructor creates a connection to mongodb with database name dbname"
        try:
            try:
            # self.__conn = pymongo.MongoClient("localhost", 27017)
            # self.__conn = pymongo.MongoClient("34.69.115.166", 27118)
            # self.__conn = pymongo.MongoClient(host="34.69.115.166",port=27118, username="journeyai-dev-usr", password="pbOLhGsR+lUZdnmtmRPeu9s=")

                # self.__conn = pymongo.MongoClient('mongodb://journeyai-dev-usr:pbOLhGsR+lUZdnmtmRPeu9s=@34.69.115.166:27118/journeyai?authSource=journeyai')
                self.__conn = pymongo.MongoClient('mongodb://journeyai-dev-usr:pbOLhGsR+lUZdnmtmRPeu9s=@35.222.255.113:27118/journeyai?authSource=journeyai')

            except ConnectionFailure:
                print('Server not available :: ')

            self.__db = self.__conn[dbname]
            print("connected")
        except Exception:
            print("Error in Connection")

    def createCollection(self, name=""):
        "Creates collection of the name"
        try:
            print("getcollection")
            return self.__db[name]

        except Exception:
            print("Error in creating collection")

    def getCollection(self,collection_name):
        "Return  the collection object with name collection_name"
        self.collection=None
        try:
            self.collection = self.__db[collection_name]
        except Exception:
            print ("Collection %s not found " %collection_name)

        return self.collection

    def insertDocument(self,document,collection_name):
        "Insert Document in collection"
        result_flag = False
        try:
            self.collection = self.getCollection(collection_name)
            self.collection.insert_one(document)
        except Exception as e:
            print("Exception in insert document :: ")
            print(e)

        else:
            result_flag =True

        return result_flag

    def updateDocument(self, document_key, document_update, collection_name):
        "Update a document based on its key"
        result_flag = False
        try:
            self.collection = self.getCollection(collection_name)
            result_obj = self.collection.update(document_key, document_update)
            if result_obj['updatedExisting'] is True:
                result_flag = True
        except Exception:
            print("Exception while updating document")

        return result_flag

    def deleteDocument(self, document_key, collection_name):
        "Delete a given document"
        result_flag = False
        try:
            self.collection = self.getCollection(collection_name)
            result_obj = self.collection.remove(document_key)
            if result_obj['n'] is 1:
                result_flag = True
        except Exception:
            print("Exception while deleting document")
        else:
            return result_flag

if __name__== '__main__':
    database = MongoDB("journeyai")
    # print(database.getUsers())
    collection_name = "fuse"
    collection = database.createCollection(collection_name)

    print(collection)
    # import pdb; pdb.set_trace()
    document = {"name": "Jack", "address": [{"area": "NRI Layout", "city": "blr", "pin": "560016", "state": "KA"},
                                            {"area": "NRI Layout", "city": "blr", "pin": "560016", "state": "KA"}],
                "contact": "90000000006", "emp_id": "0007"}
    document_key = {"name": "Jack"}

    if database.insertDocument(document, collection_name) is True:
        print("document insert sucessful")
    else:
        print("document insert unsucessful")
