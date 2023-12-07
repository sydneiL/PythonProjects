#****This is a text-based simulator Choices & Tasks showing various outcomes based on the choices and tasks input by users****#


#MANDATORY PROJECT TERMS#

#2 Loops#
#Logical choices-if/else statements-3 levels meet the goal

#Make a while loop so users are allowed to run the simulator as often as possible#

  #Show user text describing the awesomeness of this simulator game#
  #Input print()statements below#
print("Welcome to Choices & Tasks, a text-based simulator game. Play as often as you want!")
print("You find yourself lost in the woods and see a crossroad sign. Which path do you take?")
print("1. Take the path through the woods.")
print("2.Take a bridge over a deep ravine.")

#Must collect input from user for what chosen path they want#
#Input input()statement below#
#Must store user input choices as a variable#
choice1=input("Enter choice(1 or 2):")

#THIS IS PUR FIRST LOGICAL CHOICE#
#Input choice logic to have different options#
#If choice 1 is picked, then write an if statement#
if choice1=='1':
    print("You discover camping supplies. You win!")
    #If they chose choice 2, then write an elif statement(else if)
elif choice1=='2':
    print("You keep walking and reach a waterfall.")
else:
    print("Choice invalid. Select 1 or 2.")
# for any other input, write an else statement
#If the users chose choice 2, write an elif statement(else if)
#for any other input, write an else statement

#If users selected choice 2, write an elif statement(else if)
# Insert choice logic to handle various scenarios
#If choice 1 is picked, then write an if statement
#Print information about venturing in this direction
# Insert an input()statement so users have more options on what paths to go down
#Add another while loop below
#for any other input,then write an else statement


#Ask user if they want to continue. If no is the option, break the loop.

replay=input("Do you wish to play again?(yes/no):")

if  replay.lower() =='no':
    print("Thank you for playing!")

flag=False
answer="Tent"

if answer=="Tent":
    flag= True
else:
    flag= False

