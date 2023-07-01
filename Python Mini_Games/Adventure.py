name = input("Type your name: ") #user input

print("\nWelcome", name, "to this adventure!")

score=0 #variable to maintain score

answer = input("\nYou are on a dirt road, it has come to an end and you can go left or right. (left/right)? ").lower() #user choice

if answer == "left": #Choice is equals to left
    answer = input("\nYou come to a river, you can walk around it or swim accross? (swim/walk): ")

    if answer == "swim":
        print("\nYou swam acrross and were eaten by an alligator.")
        print("\nYou lost")
        
    elif answer == "walk":
        print("\nYou walked for many miles, finally you found your destination.")
        print("\n**If you had choosen 'swim' you would be eaten by an alligator**")
        score+=2 #score iteration
        
    else:
        print('\nNot a valid option. You lose.')

elif answer == "right": #Choice is equals to right
    answer = input("\nYou come to a bridge , do you want to cross it or head back (cross/back)? ")

    if answer == "back":
        print("\nYou go back and lose.")
        
    elif answer == "cross":
        answer = input("\nYou cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")

        if answer == "yes":
            print("\nYou talk to the stanger and they give you gold. You WIN!")
            score+=2
            
        elif answer == "no":
            print("\nYou ignore the stranger and they are offended and you lose.")
            
        else:
            print('\nNot a valid option. You lose.')
            
    else:
        print('\nNot a valid option. You lose.')

else:
    print('\nNot a valid option. You lose.') #Choice not equals to left or right

print("\nThank you for trying", name,"  your score ",score,"/ 2\n") #Displaying Final score