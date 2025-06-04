#Beyon Joby
#lvl2csc

current_points = 0#setting up a points system and makeing it 0
Questions_left = 4

def Print_points():
    print("Current points:", current_points, "you have",Questions_left, "questions left")#prints the current points for the user



print("*"*100)#makes it look neat
print("*"*30, "Welcome to my game about mental health", "*"*30)#the title
print("*"*100)#makes it look neat
print()#makes it look easyer to read by separating the parts
print("  INFO:")#info
print("You are a teenager and get choices on what to do in your life,")
print("Every choice you do you get points that goes in your mental health bar.")#explans how the game works
print("A good answer would give a postitive number like 20 points ")
print ("But a bad one will give you a negative number like -30 points")
print("You can also get zero points.")#how game works
print(" at the end you can see how much points you have to see how well you did.")#how game works






print("       Question 1")#question 1
print("You wake up, it is the weekend Do you:") #info
print("  1. Go hang out with friends.")#choice 1
print("  2. Stay inside and play video games")#choice 2
print("  3. Take a walk")#choice 3
print("  4. Go back to bed")#choice 4

question_1 = input("Enter one of these choices (1, 2, 3, 4): ")#getting the imput from the user

if question_1 == "1":#if question 1s answer is 1 then
    current_points += 30#points go up by 30
elif question_1 == "2":#if question 1s answer is 2 then
    current_points += -20#points go down by 20
elif question_1 == "3":#if question 1s answer is 3 then
    current_points += 10#points go up by 10
elif question_1 == "4":#if question 1s answer is 4 then
    current_points += 0#points dont go up or down
else:#any other input 
    print("Invalid input.")#prints invalid input

Questions_left += -1
Print_points()

print(" ")#makes it look easyer to read by separating the parts
print(" ")#makes it look easyer to read by separating the parts

print("       Question 2")#question 2
print("You are feeling depressed what do you do")#info
print("  1. Do nothing")#choice 1
print("  2. Talk to your friends or family about it")#choice 2
print("  3. Try find out whats wrong and fix it")#choice 3


question_2 = input("Enter one of these choices (1, 2, 3, 4): ")#getting input from user

if question_2 == "1":#if question 2s answer is 1 then
    current_points += -20#points go down by 20
elif question_2 == "2":#if question 2s answer is 2 then
    current_points += 30#points go up by 30
elif question_2 == "3":#if question 2s answer is 3 then
    current_points += 30#points go up by 30
else:#any other input
    print("Invalid input.")# prints invalid input