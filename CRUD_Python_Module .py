# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 
    def __init__(self,username,password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        #USER = 'aacuser' 
        #PASS = 'Candy340' 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        # self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.client = MongoClient('localhost',
                     username=username,
                     password=password,
                     authSource='admin',
                     authMechanism='SCRAM-SHA-1')
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        if data is not None: 
            insertSuccess=self.database.animals.insert_one(data)  # data should be dictionary 
            if not insertSuccess.inserted_id:
                return False
            #default return
            return True
        else: 
            raise Exception("Nothing to save, because data parameter is empty") 

    # Create method to implement the R in CRUD.

    def read(self,searchData):
        if searchData:
            data =self.database.animals.find(searchData, {"_id": 0})
        else:
            data =self.database.animals.find({}, {"_id": 0})
        return data 
  
  #Create method to implement the the U in CRUD.

    def update(self, searchData, updateData):
        if searchData is not None:
            result = self.database.animals.update_many(searchData,{ "$set": updateData})
        else:
            return"{}"
        return result.raw_result

 #Create method to implement the the D in CRUD.

    def delete(self, deleteData):
        if deleteData is not None:
            result = self.database.animals.delete_many(deleteData)
        else:
            return"{}"
        return result.raw_result
     