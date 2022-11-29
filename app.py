#This class is for user interactions
#import conditions class
import conditions
#create app class
class App:
    def run(self):
        self.showMainMenu()
    
    def showMainMenu(self):
        while True:
            print("Welcome to the program!")
            choice =int(input("\nEnter 1 to create dictionary: \n2. to read dictionary: \n3. to update your dictionary: \n4. to delete your dictionary: \n5. to exit the program: "))
            #menu for CRUD
            if choice ==1:
                pass
            if choice==2:
                pass
            if choice==3:
                pass
            if choice==4:
                pass
            if choice ==5:
                break

app =App()
app.run()