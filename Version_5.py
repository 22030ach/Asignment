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
    reply = easygui.buttonbox("Choose one:", choices=choices)
    if reply == "Go hang out with friends":
        current_points += 30
    elif reply == "Stay inside and play video games":
        current_points -= 20
    elif reply == "Take a walk":
        current_points += 10
    elif reply == "Go back to bed":
        current_points += 0

    easygui.msgbox(f"Your current score is: {current_points}", title="Score")

def question_2():
    global current_points

    easygui.msgbox("Question 2: You are feeling depressed. What do you do?")
    choices = ["Do nothing", "Talk to your friends or family about it", "Try to find out what's wrong and fix it"]
    reply = easygui.buttonbox("Choose one:", choices=choices)
    if reply == "Do nothing":
        current_points -= 20
    elif reply == "Talk to your friends or family about it":
        current_points += 30
    elif reply == "Try to find out what's wrong and fix it":
        current_points += 30

    easygui.msgbox(f"Your current score is: {current_points}", title="Score")

def question_3():
    global current_points

    easygui.msgbox("Question 3: You're in an argument and you're feeling really angry.")
    choices = ["Start a fight with who you're talking to", "Flip a table", "Calm yourself", "Walk away"]
    reply = easygui.buttonbox("Choose one:", choices=choices)
    if reply == "Start a fight with who you're talking to":
        current_points -= 20
    elif reply == "Flip a table":
        current_points -= 20
    elif reply == "Calm yourself":
        current_points -= 30
    elif reply == "Walk away":
        current_points += 30

    easygui.msgbox(f"Your final score is: {current_points}", title="Final Score")

def question_4():
    global current_points

    easygui.msgbox("Question 4 (bonus!)\n\nYou are feeling hungry. Where do you go?")
    choices = ["Ice cream stand", "Pizza shop"]
    reply = easygui.buttonbox("Choose one:", choices=choices)
    if reply == "Ice cream stand":
        easygui.msgbox("You go to the ice cream stand and see a man sitting alone crying outside.\nDo you...")


    easygui.msgbox(f"Your current score is: {current_points}", title="Score")

# Run the questions
question_1()
question_2()
question_3()
question_4()