#Beyon Joby
#lvl2csc

current_points = 0#setting up a points system and makeing it 0
Questions_left = 4#setting up the ammount of questions left value

def Print_points():#making a function
    print("Current points:", current_points,)#prints the users points and tells them how much questions are left



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
print("this game is made for people from the ages of 10 to 50")
print("")


age = int(input("how old are you "))
if age >50:
    print("sorry your too old to play this game")
    exit()
elif age <10:
    print("sorry your too young to play this game")
    exit()

print("now we know your in the right age group for this game lets start")
print("")
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

Questions_left += -1#questions go down by one
Print_points()#printing points

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

Questions_left += -1#questions go down by one
Print_points()#printing points

print(" ")#makes it look easyer to read by separating the parts
print(" ")#makes it look easyer to read by separating the parts

print("       Question 3")#question 3
print("Your in a argument and your feeling really angry")#info
print("  1. Start a fight with who your talking to")#choice 1
print("  2. Flip a table")#choice 2
print("  3. Calm yourself")#choice 3
print("  4. Walk away")#choice 4

question_3 = input("Enter one of these choices (1, 2, 3, 4): ")#getting info from the user


if question_3 == "1":#if question 3s answer is 1 then
    current_points += -20#points go down by 20
elif question_3 == "2":#if question 3s answer is 2 then
    current_points += -20#points go down by 20
elif question_3 == "3":#if question 3s answer is 3 then
    current_points += 30#points go up by 30
elif question_3 == "4":#if question 3s answer is 4 then
    current_points += 30#points go up by 25
else:#any other input
    print("Invalid input.")#prints invalid input

Questions_left += -1#questions go down by one
Print_points()#printing points



print("")#makes it look easyer to read by separating the parts
print("")#makes it look easyer to read by separating the parts
print("")#makes it look easyer to read by separating the parts



print("       Question 4 (bonus!)")#question 4(bonus)
print("You are feeling hungry where do you go?")#info
print("  1. Ice cream stand")#choice 1
print("  2. Pizza shop")#choice 2
print("")#makes it look easyer to read by separating the parts
print("")#makes it look easyer to read by separating the parts
question_4 = input("Enter one of these choices (1,2): ")#having the user give input


if question_4 == "1":#if question_4s answer is 1 then
    print("You go to the ice cream stand and you see a man sitting alone crying outside \n Do you..")#info
    print(" 1. Order your ice cream and go")#choice 1
    print(" 2. Talk to him and find out whats goin on")#choice 2
    question_4_1 = input("Enter one of these choices (1,2): ")#getting input from the user
    if question_4_1 == "1" :#if question_4_1s answer is 1 then
        print("")#makes it look easyer to read by separating the parts
        print("")#makes it look easyer to read by separating the parts
        print("You buy the ice cream and as you leave you hear him crying")#info of what happens after
        current_points += -2#points go down by 2
    elif question_4_1 == "2":#if they chose option 2 then
        print("")#makes it look easyer to read by separating the parts
        print("")#makes it look easyer to read by separating the parts
        print("He tells you that hes feeling down because he lost his job do you...")#info
        print(" 1.Yell him to", "   Keep his head up and everything will work out")#choice 1
        print(" 2.Tell him to", "   No one cares stop crying")#choice 2
        question_4_2 = input("enter (1.2): ")#getting input from the user
        if question_4_2 == "1":#if they chose option 1 then
            print("")
            print("")
            print("The man says," "Thank you child here is some points for helping me out.")
            current_points += 45
        elif question_4_2 == "2":
            print("")#makes it look easyer to read by separating the parts
            print("")#makes it look easyer to read by separating the parts
            print("He continues crying while you leave")#the result of what they chose
            current_points += -2#points go down by 2 points




elif question_4 == "2":#if they chose option 2 then
    print("")#makes it look easyer to read by separating the parts
    print("")#makes it look easyer to read by separating the parts
    print(" You see a kid crying on your way to the pizza shop do you...")#info
    print("  1. Ask him whats wrong")#choice 1
    print("  2. Ignore him and get the pizza")#choice 2
    question_4__1 = input("Enter (1.2): ")#getting input from the user
    if question_4__1 == "1":#if they chose option 1 then
        print("")#makes it look easyer to read by separating the parts
        print("")#makes it look easyer to read by separating the parts
        print("He tells you his lost his parents do you...")#info
        print(" 1.Laugh at him and keep walking")#option 1
        print(" 2.Bring him to a police station ")#option 2
        question_4__2 = input("Enter a number (1.2): ")#getting input from the user
        if question_4__2 == "1":#iif they chose option 1 then
            print("")#makes it look easyer to read by separating the parts
            print("")#makes it look easyer to read by separating the parts
            print("The boy starts to cry louder")#the result of their choice
            current_points += -5#points go down by 5
        elif question_4__2 == "2":#if they chose option 2 then
            print("")#makes it look easyer to read by separating the parts
            print("")#makes it look easyer to read by separating the parts
            print("You brought him to a police station and he found his mom there \n As a reward the police gave you 45 points")#info
            current_points += 45#they gain 45 points
    elif question_4__1 == "1": #if they chose option 1 then
        print("")#makes it look easyer to read by separating the parts
        print("")#makes it look easyer to read by separating the parts
        print("You get the pizza and as you walk off you feel sadness in your heart")#the result of what they chose
        current_points += -5#points go down by 5 points


print("")#makes it look easyer to read by separating the parts
print("")#makes it look easyer to read by separating the parts
print("")#makes it look easyer to read by separating the parts

if current_points < 0:#if they got lower than 0 then
    print("You got", current_points, "Which is quite low, try again to get a better score!")#prints that they got a low score and should try again
elif current_points > 0 and current_points < 130:#if they got between 0 and 144 then
    print("You got", current_points, "Not bad but i think you can do better try again!")#print that they got a decent score but they should try again 
elif current_points > 130:#if they got over 130 then print
    print("You got the best posible score good job!") #tell them they got the best score they could get and they did a good job