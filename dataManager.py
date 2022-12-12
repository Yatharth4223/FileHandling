import json
class DataManager:
    def updateJSON(self,collection):
        fileRef =open("books.json","w")
        json.dump(collection,fileRef)
        fileRef.close()
    
    def readJSON(self):
        fileRef =open("books.json","r")
        collection = json.load(fileRef)
        fileRef.close()
        return collection