#This application is created by Yatharth Jain
#This class is for user interactions
#import collection class
from exceptionHandling import NoDictionaryError
from exceptionHandling import NoValueExistsError
from exceptionHandling import InvalidChoiceException
from exceptionHandling import KeyNotUnique
import collection
#create app class
class App:
    def __init__(self):
        self._collectionInstance = collection.Collection()

    def run(self):
        self.showMainMenu()
    
    def showMainMenu(self):
        valueList =[]
        print("---------------Welcome to the program!---------------")
        print("---------------This is a program where you can store your book values!---------------")
        while True:
            try:
                print("\nEnter 1 to create dictionary: \n2. to search through dictionary: \n3. to update your dictionary: \n4. to delete your dictionary:\n5. to display the collection \n6. to exit the program: ")
                choice =int(input("\nEnter your choice: "))
                if choice!=1 and choice!=2 and choice!=3 and choice!=4 and choice!=5 and choice!=6:
                    raise InvalidChoiceException 
                #menu for CRUD
                if choice == 1:
                    key =input("Enter the ISBN number for your book: ")
                    name =input("Now enter the name of the book: ")
                    valueList.append(name)
                    year = input("Now enter the year it was published! ")
                    valueList.append(year)
                    self._collectionInstance.createDictionary(key,valueList)
                    #clearing the list again for future use!
                    valueList = []
                    print("Your dictionary has been succesfully created and your object has been stored succesfully! ")
                    
                if choice==2:
                    nonKeyValue = input("Enter a non-key value to search for your object like object name or year: ")
                    searchReturn = self._collectionInstance.searchDictionary(nonKeyValue,None)
                    if searchReturn == "No dictionary exists!":
                        raise NoDictionaryError

                    elif searchReturn == "More than one resource exists!":
                        keyValue = input("More than one resource have this non-key value enter a key value to search it now: ")
                        keySearchReturn = self._collectionInstance.searchDictionary(None,keyValue)
                        if  keySearchReturn == None:
                            raise NoValueExistsError
                        else:
                            print(f"Your key has been found and the attributes related to the key are: {keySearchReturn}")
                    elif searchReturn == None:
                        raise NoValueExistsError
                    else:
                        print(f"Your key has been found and it belongs to the ISBN number: {searchReturn}")
                
                if choice == 3:
                    keyValue = input("To add a new book or change an existing book, enter the new book's ISBN number:")
                    searchReturn  = self._collectionInstance.searchDictionary(None,keyValue)
                    #if searchReturn is none means no such key already exists! 
                    if searchReturn == "No dictionary exists!":
                        raise NoDictionaryError
                    else:
                        if searchReturn == None:
                            name =input("Enter the book's name: ")
                            year =input("Enter the book's publishing year: ")
                            valueList.append(name)
                            valueList.append(year)
                            self._collectionInstance.updateDictionary(keyValue,valueList)
                            #clearing the list again for future use!
                            valueList = []
                            print("Your dictionary has been succesfully created and your object has been stored succesfully! ")
                        else:
                            raise KeyNotUnique
                        
                if choice==4:
                    keyValue = input("Enter the key value to be deleted: ")
                    searchReturn = self._collectionInstance.searchDictionary(None,keyValue)
                    if searchReturn == None:
                        raise NoValueExistsError
                    else:
                        self._collectionInstance.deleteDictionary(keyValue)
                        print("Your dictionary has been updated! ")
                
                if choice ==5:
                    print(f"\n {self._collectionInstance.displayDictionary()}")
                
                if choice ==6:
                    #clearing the dictionary and json before exiting the program each time
                    strObj = ""
                    self._collectionInstance.clearJSON(strObj)
                    break
            
            except KeyNotUnique:
                print("A non unique key entered! ")
            except NoValueExistsError:
                print("No key found for this value! ")

            except NoDictionaryError:
                print("No dictionary exists! ")

            except ValueError:
                print("wrong value entered! ")

            except InvalidChoiceException:
                print("Ivalid choice entered: ")
        

app =App()
app.run()