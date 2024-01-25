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

def Inserting(self, Mode:str, Dataset: dict)  -> None:
    """
    :param Mode has two options : 'One' | 'Many'
    """
    if Mode == 'One':
        try:
            self.collections.insert_one(Dataset)
            print("Pushed:)")
        except:
            print("Not pushed:(")
    elif Mode == 'Many':
        try:
            self.collections.insert_many(Dataset)
            print("Pushed:)")
        except:
            print("Not pushed:(")
            
def GettingCollectionsName(self) -> None:
    