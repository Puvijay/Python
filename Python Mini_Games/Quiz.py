print("Welcome to my computer quiz!") #Title

playing = input("Do you want to play? (Y) : ") #User Input

if playing.lower() != "y":
    quit() #Termination

print("Let's play :)")
score = 0 #Initilizing a variable to 0 to store points

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1 #Iterating when the answer is correct
else:
    print("Incorrect!")

answer = input("What does BIOS stand for? ")
if answer.lower() == "basic input output system":
    print('Correct!')
    score += 1 #Iterating when the answer is correct
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1 #Iterating when the answer is correct
else:
    print("Incorrect!")

answer = input("What does OS stand for? ")
if answer.lower() == "operating system":
    print('Correct!')
    score += 1 #Iterating when the answer is correct
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!") #Displaying Score
print("You got " + str((score / 4) * 100) + "%.") #Score percentage