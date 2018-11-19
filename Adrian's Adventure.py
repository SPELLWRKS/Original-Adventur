
#November 16, 2018
#Lesson 6 Discussion

#Adrian's Quest

#This program is a simple test-based game. The user enters their name
#and is assigned 1 of 3 roles: Knight, Mage or Barbarian. The user is
#then given the option to choose between 3 paths: left, right or middle.
#The ending to the game is based on the user's choice.


#imports the random function 
import random



#the main function
def main():
    #initializes all variables
    endProgram = "yes"
    left = 1
    middle = 2
    right = 3
    characterName = 'NO NAME'
    characterTrait = 0
    choice = 'none'
    role = 'none'
    

    #this loop resets all variables based on user input
    while endProgram == "yes":
        characterName = name(characterName) #calls the characterName function
        characterTrait = 0
        role = assignRole(characterName, characterTrait) #calls the assignRole function
       
        choice = path1(choice) #calls the path1 function
        
        endProgram = str(input("Would you like to play again (yes or no)?: "))


#this function stores the user's name as a variable for later use
def name(characterName):
    characterName = str(input("Welcome warrior! What is your name?: "))
    return characterName


#this function assigns a random role to the user, based on 3 possible outcomes
#utilizing the random function. These roles assigned using an if-elif statement
def assignRole(characterName, characterTrait):
    characterTrait = random.randint(1, 3)
    if characterTrait == 1:
        print(characterName + ", you have been chosen as a Knight! You must find and rescue the princess!")
    elif characterTrait == 2:
        print(characterName + ", you have been chosen as a Mage! You must find and rescue the princess!")
    elif characterTrait == 3:
        print(characterName + ", you have been chosen as a Barbarian! You must find and rescue the princess!")
    return characterName, characterTrait


#this function allows the user to choose a path, determining the end of the game
#if the user chooses the "middle" option, the characterName variable is called
def path1(characterName, choice):
        choice = str(input("You stand in front of three paths, which will you take? (choose: left, middle or right): "))
        if choice == "left":
            print("You have chosen the left path. A bear has attacked you and you have died!")
        elif choice == "middle":
            print("You have chosen the middle path. You have found the princess! Excellent Job, " + characterName +"!")
        elif choice == "right":
            print("You have chosen the right path. You fall into a pit from which there is no escape!")
        else:
            print('Invalid entry. Please enter "left", "middle" or "right": ')
            choice = false
        return choice

        
#calls the main
main()
