#This class will implement all the functions in the program
from dataManager import DataManager
#create a Conditions class
from exceptionHandling import NoDictionaryError
class Collection:
    def __init__(self):
        #creating buffer value for dictionary
        self._repitition = 0
        self._dictionary ={}
        self._dataManagerInstance = DataManager()

    #def createDictionary(self,key,values)
    def createDictionary(self,key,values):
        #creating a buffer dictionary and passing keys and values to dump it in json later
        # This condition will work when there is no predefined dictionary and you are creating one! 
        dictionary ={}
        dictionary[key] =values
        self._dataManagerInstance.updateJSON(dictionary)
    
    def updateDictionary(self,key,values):
        if type(self._dataManagerInstance.readJSON()) == dict:
            dictionary = self._dataManagerInstance.readJSON()
            dictionary[key] = values
            #dumping it in json file
            self._dataManagerInstance.updateJSON(dictionary)

    #def readDictionary(self,key,values)
    def searchDictionary(self,nonKeyValue,keyValue):
        if type(self._dataManagerInstance.readJSON()) == dict:
            if nonKeyValue !=None:
                #updating the value of self._repitition for next use! 
                self._repitition =0
                for i in self._dataManagerInstance.readJSON():
                    for index in list(self._dataManagerInstance.readJSON()[i]):
                        if index == nonKeyValue:
                            self._repitition +=1
                            keyFound = i
                if self._repitition ==1:
                    return keyFound
                elif self._repitition >1:
                    return "More than one resource exists!"
                else :
                    return None
            else:
                self._repitition = 0
                for i in self._dataManagerInstance.readJSON():
                    if i == keyValue:
                        return self._dataManagerInstance.readJSON()[i]
        else:
            self._repitition = 0
            return "No dictionary exists!"

    def deleteDictionary(self,key):
        collection =self._dataManagerInstance.readJSON()
        del collection[key]
        self._dataManagerInstance.updateJSON(collection) 

    #This method will be called before the computer closes the program to put a buffer value in json file
    def clearJSON(self,strObj):
        self._dataManagerInstance.updateJSON(strObj)

    def displayDictionary(self):
        return self._dataManagerInstance.readJSON()

    def getDictionary(self):
        return self._dictionary 


