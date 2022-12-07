#This class is for user interactions
#import conditions class
from exceptionHandling import NoDictionaryError
import conditions
#create app class
class App:
    def __init__(self):
        self._conditionInstance =conditions.Conditions()

    def run(self):
        self.showMainMenu()
    
    def showMainMenu(self):
        valueList =[]
        print("Welcome to the program!")
        print("This is a program where you can store your book values: ")

        while True:
            choice =int(input("\nEnter 1 to create dictionary: \n2. to search through dictionary: \n3. to update your dictionary: \n4. to delete your dictionary: \n5. to exit the program: "))
            #menu for CRUD
            if choice ==1:
                key =input("Enter the ISBN number for your book: ")
                print("Now enter the name of the book and year it was published! ")
                for index in range(0,2):
                    value =input(f"Enter the value: ")
                    valueList.append(value)
                userDictionary =self._conditionInstance.createDictionary(key,valueList)
                valueList = []
                print("Your dictionary has been succesfully created and your object has been stored succesfully! ")
                print(userDictionary)

            if choice==2:
                nonKeyValue = input("Enter a non-key value to search for your object like object name or year: ")
                searchReturn = self._conditionInstance.searchDictionary(nonKeyValue,None)
                if searchReturn == "No dictionary exists!":
                    raise NoDictionaryError
                elif searchReturn == False:
                    keyValue = input("Now enter a key value to search the resource(key valus is the ISBN number!): ")
                    searchReturn = self._conditionInstance.searchDictionary(None,keyValue)
                    if searchReturn =="Value not found!":
                        print("Invalid ISBN number entered! ")
                    else:
                        print(f"Your ISBN number has been found and it contains: {searchReturn}")
                else:
                    print(f"Your key has been found and it belongs to the ISBN number: {searchReturn}")
            
            if choice==3:
                keyValue = input("To add a new book or change an existing book, enter the new book's ISBN number:")
                #numOfValues =int(input(f"Enter how many attributes are there for your book: "))
                for index in range(0,2):
                    value =input(f"Enter the value: ")
                    valueList.append(value)
                
                userDictionary = self._conditionInstance.createDictionary(keyValue,valueList)
                valueList = []
                print("Your dictionary has been succesfully created and your object has been stored succesfully! ")
                print(userDictionary)


            if choice==4:
                keyValue = input("Enter the key value to be deleted: ")
                searchReturn = self._conditionInstance.searchDictionary(None,keyValue)
                if searchReturn ==False:
                    print("No such key exits! ")
                else:
                    dictionary =self._conditionInstance.deleteDictionary(keyValue)
                    print(f"Your dictionary has been updated: {dictionary}")
            if choice ==5:
                break

app =App()
app.run()