import easygui#import EasyGui

current_points = 0#setting the points to 0

def intro():#function that shows at the start of the game
    easygui.msgbox(#prints the following
        "INFO:\n\n"
        "You are a teenager making choices in your life.\n"
        "Each decision affects your mental health score.\n\n"
        "Positive choices add points, bad choices subtract points.\n"
        "At the end, you can see how many points you have to see how well you did.",
        title="Welcome to the Mental Health Game"#the title of message
    )



def question_1():#question 1 function
    global current_points

    easygui.msgbox("Question 1: You wake up, it's the weekend. Do you:")#question 1
    choices = ["Go hang out with friends", "Stay inside and play video games", "Take a walk", "Go back to bed"]#choices for question 1
    choice = easygui.buttonbox("Choose one:", choices=choices)#getting input from the user

    
    if choice == "Go hang out with friends":#if they chose this then..
        current_points += 30#they gain 30 points
    elif choice == "Stay inside and play video games":#if they chose this then..
        current_points -= 20#they gain 20 points
    elif choice == "Take a walk":#if they chose this then..
        current_points += 10#they gain 10 points
    elif choice == "Go back to bed":#if they chose this then..
        current_points += 0#no points given

    easygui.msgbox(f"Your current score is: {current_points}", title="Score")#prints points


def question_2():#question 2 function
    global current_points

    easygui.msgbox("Question 2: You are feeling depressed. What do you do?")#Display the question
    choices = ["Do nothing", "Talk to your friends or family about it", "Try to find out what's wrong and fix it"]#choices for question 2
    choice = easygui.buttonbox("Choose one:", choices=choices)#Getting input from the user

    
    if choice == "Do nothing":#If they chose to do nothing
        current_points -= 20#They lose 20 points
    elif choice == "Talk to your friends or family about it":#If they chose to talk to someone
        current_points += 30#they gain 30 points
    elif choice == "Try to find out what's wrong and fix it":#If they chose to self-reflect
        current_points += 30#They gain 30 points

    easygui.msgbox(f"Your current score is: {current_points}", title="Score")  # Display the updated score

def question_3():#Function for Question 3
    global current_points

    easygui.msgbox("Question 3: You're in an argument and you're feeling really angry.")#display the question
    choices = ["Start a fight with who you're talking to", "Flip a table", "Calm yourself", "Walk away"]#choices for question 3
    choice = easygui.buttonbox("Choose one:", choices=choices)#Get input from the user


    if choice == "Start a fight with who you're talking to":#If they chose to start a fight
        current_points -= 20#They lose 20 points
    elif choice == "Flip a table":#If they chose to flip a table
        current_points -= 20#They lose 20 points
    elif choice == "Calm yourself":#If they chose to calm themselves
        current_points += 30#They gain 30 points
    elif choice == "Walk away":#If they chose to walk away
        current_points += 30#They gain 30 points

    easygui.msgbox(f"Your final score is: {current_points}", title="Final Score")#final score


def question_4():#function for question 4
    global current_points

    easygui.msgbox("Question 4 (bonus!)\n\nYou are feeling hungry. Where do you go?")#Choices for question 4
    choices = ["Ice cream stand", "Pizza shop"]#options for this question
    choice = easygui.buttonbox("Choose one:", choices=choices)#get input from the user
    if choice == "Ice cream stand":#if they chose ice cream stand
        easygui.msgbox("You go to the ice cream stand and see a man sitting alone crying outside.\nDo you...")#info on what the user sees in the ice cream stand
        choices = ["Order your ice cream and go", "Talk to him and find out what's going on"]#choices for this question
        choice = easygui.buttonbox("Choose one:", choices=choices)#gets input from the user
        if choice == "Order your ice cream and go":#if they chose order ice cream and go then
            current_points -= 2#points go down by 2
        elif choice == "Talk to him and find out what's going on":#if the user chose to talk to him then
            easygui.msgbox("He tells you that he's feeling down because he lost his job.\nDo you...")#displays what the person says
            choices = ["Tell him to keep his head up and everything will work out", "Tell him no one cares, stop crying"]#choices for this question
            choice = easygui.buttonbox("Choose one:", choices=choices)#getting input from the user
            if choice == "Tell him to keep his head up and everything will work out":#if the user chose the nice thing to do then
                current_points += 45#their points go up by 45
            elif choice == "Tell him no one cares, stop crying":#if they chose the bad thing to do then
                current_points -= 2#points go down by 2

    elif choice == "Pizza shop":#if they chose to go to the pizza shop theb
        easygui.msgbox("You see a kid crying on your way to the pizza shop do you...")#info on what happens while going to the pizza shop
        choices = ["Ask him what's wrong", "Ignore him and get the pizza"]#choices for this question
        choice = easygui.buttonbox("Choose one:", choices=choices)#getting input from the user
        if choice == "Ask him what's wrong":#if they chose to ask him whats wrong then..
            easygui.msgbox("He tells you he lost his parents. Do you...")#the kid says he lost his parrents
            choices = ["Laugh at him and keep walking", "Bring him to a police station"]#choices for this question
            choice = easygui.buttonbox("Choose one:", choices=choices)#getting input from the user
            if choice == "Laugh at him and keep walking":#if they chose the bad option
                current_points -= 2#they lose 2 points
            elif choice == "Bring him to a police station":#if they chose the good option
                current_points += 45#they get 45 points
        elif choice == "Ignore him and get the pizza":#if they ignore him
            current_points -= 2#they lose 2 points

    easygui.msgbox(f"Your current score is: {current_points}", title="Score")#prints the current score


def final_points():#function for displying the final points
    if current_points < 0:#if they get less than 0 points then 
        easygui.msgbox(f"You got {current_points}. Which is quite low, try again to get a better score!")#tell them its a low score and to try again
    elif 0 <= current_points < 100:#if they got in between 0 and 100 then 
        easygui.msgbox(f"You got {current_points}. Not bad but I think you can do better, try again!")#tell them they did good but to try again
    elif current_points >= 100:#if they got over 100 then
        easygui.msgbox(f"You got {current_points}. The best possible score, good job!")#tell them they got the best score possible

def loop_game():
    global current_points
    while True:
        current_points = 0
        intro()
        question_1()
        question_2()
        question_3()
        question_4()
        final_points()

        play_again = easygui.buttonbox("Do you want to play again?", choices=["Yes", "No"])
        if play_again == "No":
            easygui.msgbox("Thanks for playing!")
            break

if easygui.buttonbox("Do you want to play the game?", choices=["Yes", "No"]) == "Yes":
    loop_game()
else:
    exit()

