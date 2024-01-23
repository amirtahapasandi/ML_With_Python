import pymongo as pm
import time 

class MongoDB:
    def __init__(self, DataBaseName:str = "local") -> None:
        try:
            self.Client = pm.MongoClient(host="127.0.0.1", port=27017)
            self.DataBaseName = DataBaseName
            self.DataBase = self.Client.get_database(self.DataBaseName)
            self.Collections = self.DataBase.get_collection(self.DataBaseName)
            print("Connected!")
        except:
            print("Not Connected!")
        time.sleep(0.01)
