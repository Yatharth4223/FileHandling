#This class will implement all the functions in the program
#create a Conditions class
from exceptionHandling import NoDictionaryError
class Conditions:
    def __init__(self):
        #creating buffer value for dictionary
        self._dictionary = {}
        self._repitition = 0

    #def createDictionary(self,key,values)
    def createDictionary(self,key,values):
        self._dictionary[key] = values
        return self.getDictionary()

    #def readDictionary(self,key,values)
    def searchDictionary(self,nonKeyValue,keyValue):
        index = -1
        if self._dictionary:
            if nonKeyValue !=None:
                for dictValues in list(self.getDictionary().values()): 
                    for searchValue in dictValues:
                        if nonKeyValue == searchValue:
                            index = list(self.getDictionary().values()).index(dictValues)
                            self._repitition +=1
                #TODO: exception handling here  if value is invalid raise invalid value error
                if self._repitition <=1 and index>-1:
                    return list(self.getDictionary().keys())[index]
                else:
                    return False
            else:
                for keyValues in list(self.getDictionary().keys()):
                    if keyValue == keyValues:
                        return self.getDictionary()[keyValue]
                    else:
                        return "Value not found!"
            self._repitition = 0        
        else:
            self._repitition = 0
            return "No dictionary exists!"


    #def updateDictionary(self,key,values)
    def updateDictionary(self,key,values):
        pass


    #def deleteDictionary(self,key,values)
    def deleteDictionary(self,key,values):
        pass

    #def getDictionary(self):
    def getDictionary(self):
        return self._dictionary

