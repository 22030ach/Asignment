import easygui

# Initialize current_points
current_points = 0

def intro():
    easygui.msgbox(
        "INFO:\n\n"
        "You are a teenager making choices in your life.\n"
        "Each decision affects your mental health score.\n\n"
        "Positive choices add points, bad choices subtract points.\n"
        "At the end, you can see how many points you have to see how well you did.",
        title="Welcome to the Mental Health Game"
    )

# Call the intro function to display the information
intro()

def question_1():
    global current_points

    easygui.msgbox("Question 1: You wake up, it's the weekend. Do you:")
    choices = ["Go hang out with friends", "Stay inside and play video games", "Take a walk", "Go back to bed"]
    choice = easygui.buttonbox("Choose one:", choices=choices)
    if choice == "Go hang out with friends":
        current_points += 30
    elif choice == "Stay inside and play video games":
        current_points -= 20
    elif choice == "Take a walk":
        current_points += 10
    elif choice == "Go back to bed":
        current_points += 0

    easygui.msgbox(f"Your current score is: {current_points}", title="Score")

def question_2():
    global current_points

    easygui.msgbox("Question 2: You are feeling depressed. What do you do?")
    choices = ["Do nothing", "Talk to your friends or family about it", "Try to find out what's wrong and fix it"]
    choice = easygui.buttonbox("Choose one:", choices=choices)
    if choice == "Do nothing":
        current_points -= 20
    elif choice == "Talk to your friends or family about it":
        current_points += 30
    elif choice == "Try to find out what's wrong and fix it":
        current_points += 30

    easygui.msgbox(f"Your current score is: {current_points}", title="Score")

def question_3():
    global current_points

    easygui.msgbox("Question 3: You're in an argument and you're feeling really angry.")
    choices = ["Start a fight with who you're talking to", "Flip a table", "Calm yourself", "Walk away"]
    choice = easygui.buttonbox("Choose one:", choices=choices)
    if choice == "Start a fight with who you're talking to":
        current_points -= 20
    elif choice == "Flip a table":
        current_points -= 20
    elif choice == "Calm yourself":
        current_points -= 30
    elif choice == "Walk away":
        current_points += 30

    easygui.msgbox(f"Your final score is: {current_points}", title="Final Score")

def question_4():
    global current_points

    easygui.msgbox("Question 4 (bonus!)\n\nYou are feeling hungry. Where do you go?")
    choices = ["Ice cream stand", "Pizza shop"]
    choice = easygui.buttonbox("Choose one:", choices=choices)
    if choice == "Ice cream stand":
        easygui.msgbox("You go to the ice cream stand and see a man sitting alone crying outside.\nDo you...")
        choices = ["Order your ice cream and go", "Talk to him and find out what's going on"]
        choice = easygui.buttonbox("Choose one:", choices=choices)
        if choice == "Order your ice cream and go":
            easygui.msgbox("You buy the ice cream and as you leave you hear him crying.")
            current_points -= 2
        elif choice == "Talk to him and find out what's going on":
            easygui.msgbox("He tells you that he's feeling down because he lost his job.\nDo you...")
            choices = ["Tell him to keep his head up and everything will work out", "Tell him no one cares, stop crying"]
            choice = easygui.buttonbox("Choose one:", choices=choices)
            if choice == "Tell him to keep his head up and everything will work out":
                easygui.msgbox("The man says, 'Thank you, child. Here are some points for helping me out.'")
                current_points += 45
            elif choice == "Tell him no one cares, stop crying":
                easygui.msgbox("He continues crying while you leave.")
                current_points -= 2


    elif choice == "Pizza shop":
        easygui.msgbox("You see a kid crying on your way to the pizza shop do you...")
        choices = ["Ask him whats wrong", "Ignore him and get the pizza"]
        choice = easygui.buttonbox("Choose one:", choices=choices)
        if choice == "Ask him whats wrong":
            easygui.msgbox("He tells you his lost his parents do you...")
            choices = ["Laugh at him and keep walking", "Bring him to a police station"]
            choice = easygui.buttonbox("Choose one:", choices=choices)
            if choice == "Laugh at him and keep walking":
                easygui.msgbox("The boy starts to cry louder")
                current_points -= 2
            elif choice == "Bring him to a police station":
                easygui.msgbox("You brought him to a police station and he found his mom there \n As a reward the police gave you 45 points")
                current_points +=45
        elif choice == "Ignore him and get the pizza":
            easygui.msgbox("You get the pizza and as you walk off you feel sadness in your heart")
            current_points -= 2

    easygui.msgbox(f"Your current score is: {current_points}", title="Score")

# Run the questions
question_1()
question_2()
question_3()
question_4()

def final_points():
    if current_points < 0:#if they got lower than 0 then
        easygui.msgbox("You got", current_points, "Which is quite low, try again to get a better score!")#prints that they got a low score and should try again
    elif current_points > 0 and current_points < 100:#if they got between 0 and 100 then
        easygui.msgbox("You got", current_points, "Not bad but i think you can do better try again!")#print that they got a decent score but they should try again 
    elif current_points > 144:#if they got over 144 then print
        easygui.msgbox("You got", current_points, "the best posible score good job!") #tell them they got the best score they could get and they did a good job



#def Loop_game():
    #easygui.msgbox("do you want to play again?")
    #play_again = ["Yes", "no"]
    #play_again = easygui.buttonbox("Choose one:", choices=play_again)
    #if play_again == "yes":
        #question_1()
        #question_2()
        #question_3()
        #question_4()
        #final_points()
        #Loop_game




