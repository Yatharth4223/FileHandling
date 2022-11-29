#This class will implement all the functions in the program
#create a Conditions class
class Conditions:
    #def createDictionary(self,key,values)
    def createDictionary(self,key,values):
        self._dictionary ={key:values}
        return self.getDictionary()

    #def readDictionary(self,key,values)
    def readDictionary(self,key,values):
        pass

    #def updateDictionary(self,key,values)
    def updateDictionary(self,key,values):
        pass


    #def deleteDictionary(self,key,values)
    def deleteDictionary(self,key,values):
        pass

    #def getDictionary(self):
    def getDictionary(self):
        return self._dictionary
