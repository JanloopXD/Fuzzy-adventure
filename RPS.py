import random #load the random module
# define original values for variables
x_range = 5 # total number of games
comp_score = 0 # reset computer's score
user_score = 0 # reset user/player's score

#start of the game
for x in range (x_range):
    randimize=random.randint(1,2,3)
    if randimize==1:
        comp_value="R"
    elif randimize==2:
        comp_value="P"
    else:
        comp_value="S"

    print ("R is for rock; S is for scissors; P is for paper")
    print ("choose R, P or S")
    user_value=input()
    print ("this is the user's choice: ", user_value)

    print ("the computer's choice is: ", comp_value)

#later
    if user_value=="R":
            #Rock
            if comp_value=="R":
                #rock
                print ("it's a tie, play again?")
            elif comp_value=="P":
                #paper
                print ("you lose :(") 
                comp_score=comp_score + 1
            else:
                #scissors
                print ("you win :) !")
                user_score=user_score + 1
    elif user_value=="P":
        #Paper
            if comp_value=="R":
                #rock
                print ("you win :) !")
                user_score=user_score + 1            
            elif comp_value=="P":
                #paper
                print ("it's a tie, play again?")            
            else:
                #scissors
                print ("you lose :(")
                comp_score=comp_score + 1
    elif user_value=="S":
        #Scissors
            if comp_value=="R":
                #rock
                print ("you lose")
                comp_score=comp_score + 1
            elif comp_value=="P":
                #paper
                print ("you win")
                user_score=user_score + 1
            else:
                #scissors
                print ("it's a tie play again?")
    else:
        print ("Wrong choice, i won") 
        comp_score=comp_score + 1
    #end of the round
    print ("this is your score: ", user_score)
    print ("this is the computer's score: ", comp_score)
    print("")
    print("")
#end of the game

if comp_score<user_score:
    print ("you win")
elif comp_score>user_score:
    print ("i win")
else:
    print ("its a tie")

print ("this is your final score: ", user_score)
print ("this is my final score: ", comp_score)


