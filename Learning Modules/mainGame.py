import gameUsingDictionary
from gameUsingDictionary import webDevelopment as Web
from gameUsingDictionary import aiMachineLearning
from gameUsingDictionary import DataBase
from gameUsingDictionary import MobileApp_For_Andriod
from gameUsingDictionary import MobileApp_For_iOS


enter_program = input("Enter Programming Language: ")
if enter_program.upper() in Web:
    print("SHOULD VENTURE INTO WEB DEVELOPMENT")
elif enter_program.upper() in aiMachineLearning:
    print("Should Venture into Artficial Intelligence/Machine Learning")
elif enter_program.upper() in DataBase:
    print("Should Venture into DATABASE MANAGEMENT")
elif enter_program.upper() in MobileApp_For_Andriod:
    print("Should Venture into Mobile Development For Android")
elif enter_program.upper() in MobileApp_For_iOS:
    print("Should Venture into Mobile Development For ios Device")

else:
    print("LANGUAGE NOT RECOGNISED")
