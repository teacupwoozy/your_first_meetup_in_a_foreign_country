# Text-based Strategy Game: Your First Meetup in A Foreign Country
# Exercise 36 in Learn Python the Hard Way
from sys import exit

# LIST OF BEERS
beers = ['Victoria', 'Indio', 'a local IPA', 'Corona Light']

# LIST OF SNACKS
botanas = ['cacahuates japonesa', 'chicharon', 'chapulines', 'palomitas']

# WELCOME -- start of game
def welcome():
    print("You are an American living in Mexico while you learn to program and speak Spanish.")
    print("You know that you need to try and network with other people in tech, but are nervous about it because you speak Spanish poorly and are just starting out as a programmer.")
    print("You find out about a tech meetup later in the week and decide to go, despite your misgivings.")
    print("On the day of the meetup, you walk to an old colonial building that now serves as an art space and a community meeting space.")
    foyer()

# LEAVE FUNCTION -- go home and end game
def go_home():
    print("The trick to going to a meetup is to actually stay at the meetup.")
    print("How are you ever going to meet other developers if you don't go where they hang out?")
    print("On your walk home you are filled with fomo and start to wish you had stayed.")
    print("You resolve that the next time you go to a meetup you'll actually stay at the meetup!")
    exit(0)

# FOYER
def foyer():
    # Print intro language
    print("You walk through the front entrance and there is an official-looking man sitting at a desk.")
    print("He starts speaking to you very quickly and you notice he's using lots of slang.")
    print("He's waving around a roll of raffle tickets and you can't follow what he's saying.")
    # Decision point: check in dude speaking Spanish v quickly c slang and waiving a roll of raffle tickets around. No compredes.
    print("What do you do?")
    # 1. Turn around, leave, go home --> leave function
    print("1. Turn around, exit out the front door, and walk home.")
    # 2. Decide to stay and try your best to learn something and talk to strangers.
    print("2. Realize this is just a small obstacle, take a deep breath, and attempt to understand what is going on.")
    print("How will you proceed?")
    foyer_choice = input("🌈 ")

    if foyer_choice == "1":
        go_home()
    elif foyer_choice == "2":
        # Tell him you are learning Spanish y por fa' despacio. He apologizes, repeats himself more slowly. He's telling you 
        # about your free beer ticket and a snack. He lists the beers available, you must select your choice so he can write it down.
        print("In Spanish, explain that you are learning Spanish and ask if he could speak slower.")
        print("He immediately appologizes and then repeats himself speaking much slower. He explains you get a free beer ticket and a snack at the meetup.")
        print("He says he needs to keep track of which beers people want and motions to the list on his clipboard.")
        # Print list of beers
        print(f"He tells you they've got {', '.join(beers)}. Which would you like?")
        # Select and store beer choice.
        beer_choice = input("🍺 ").lower()
        
        # If statements for beer_choice
        if "victoria" in beer_choice:
            print("A worthy choice.")
            snacks()
        elif "indio" in beer_choice:
            print("Classic choice.")
            snacks()
        elif "ipa" in beer_choice:
            print("Such a hipster. ¡Salud!")
            snacks()
        elif "corona" in beer_choice:
            print("Hmmmm....")
            snacks()
        else:
            print("That's not an option. I guess no beer for you.")
            snacks()
    else:
        print("You can't do that.")
        foyer()


# Print list of snacks.
# Select and store snack choice.
def snacks():
    print("He then tells you everyone gets snacks too!")
    print(f"He tells you they've got {', '.join(botanas)}. Which would you like?")
    snack_choice = input("🍿 ").lower()
    # If statement for snack selection
    if "cacahuates" in snack_choice:
        print("Thats my favorite snack!")
    elif "chicharon" in snack_choice:
        print("¡Que rico!")
    elif "chapulines" in snack_choice:
        print("Tasty!")
    elif "palomites" in snack_choice:
        print("I could eat palomitas every single day!")
    else:
        print("That wasn't one of the choices. I guess no snacks for you. 🤷🏻‍♀️")
    # He gives you two tickets and tells you to continue upstairs. --> Bar
    print(f"He gives you a drink ticket, your {snack_choice}, then tells you the meetup is upstairs.")
    arrive_on_terrace()

# TERRACE
def arrive_on_terrace():
    # Describe the terrace that has been converted to a make-shift bar, where people are standing around in small groups.
    print("You walk up the stairs onto a rooftop terrace that has a bar set up to your right. And, to the left is a big open doorway to the room where the presentations will occur.")
    print("There are a scattering of people milling around on the terrace and chatting in small groups.")
    print("You notice everyone is speaking in Spanish and seems like they've known each other for years.")
    print("Ug. Your Stranger Danger switch flips on. You have two options:")
    print("1. Turn around, leave, go home.")
    print("2. Decide to stay and try your best to learn something and talk to strangers.")
    terrace_choice = input("What do you do? ")
    # Proceed with terrace choice
    if terrace_choice == "1":
        go_home()
    elif terrace_choice == "2":
        print("Good choice! It's not easy stepping out of your comfort zone - way to be brave!")
        the_bar()
    # FIX INSECTO -- not working if a non-int is input
    else:
        print("That's not one of your options, try again.")
        arrive_on_terrace()


# THE BAR
# Function to get free beer at bar
def the_bar():
    print("You decide to give yourself something to do and go collect your free drink.")
    print("You want up to the bar and say hello, then hold out your drink ticket and say, \"Una cervecita por favor.\"")
    print(f"The bartender takes your ticket and tells you they have {', '.join(beers)}.")
    beer_choice = input("What beer is your choice? ")
    print(f"The bartender hands you your {beer_choice}.")
    print("You take it and step away from the bar as your scan the terrace.")
    terrace_decision()

# THE TERRACE
# What to do while stalling on the terrace.
def terrace_decision():
    print("You stand there looking around at everyone. They are all still talking in small groups and no one has magically invited you to join them.")
    print("You take a swig of your beer. Because it's Mexico and everything always starts late, you know the presentations won't start for 30 minutes. You realize you can do one of three things:")
    print("1. Slam your beer and go order another one.")
    print("2. Take another sip of your beer and decide to try and talk to someone.")
    print("3. Take yourself and your beer into the presentation room.")
    terrace_choice = input("What do you do? ")
    print(terrace_choice)
    if "1" in terrace_choice:
        drunk_decision()
    elif "2" in terrace_choice:
        # A woman in a group standing next to you at the bar says hi. She's wearing blinking ßrainbow LEDs in her hair.
    # 1. You tell her they're cool: she says thanks and starts telling you how she programmed them. You talk w the group.
        # A guy comes up with a bag of snacks, he lists them and asks which you would like.
        # leave and --> leave function
        # --> presentation room (skip where to sit)
        print("You turn towards the group of three people standing just to your right.")
        print("A woman a little younger than you looks your way and says, \"¡Que padre! Me encanta tu suéter.\" She's wearing a coronet of blinking rainbow LEDs in her hair.")
        print("You smile and thank her, then tell her that it's your favorite. You tell her how cool her LEDs are.")
        print("She starts explaining how she made the programming that's directing the lights. She has you get out your phone and go to her website where you can change the color patterns live.")
        print("You hang out with the group until it's time for the presentations to start.")
        print("")
        print("You spend the next 35 minutes happily chatting away with your new friends. You learn about a record store that also hosts coding nights twice a week and you exchange WhatsApp infor with all of them.")
        print("It turns out your new friends are giving one of the talks, so they leave to go finish setting up their presentation.")
        presentation_room()
    elif "3" in terrace_choice:
        print("That was a good call. A creeper in the corner had been watching you and was just about to walk over to you and start hitting on you.")
        presentation_room()
    else:
        print("That's not one of your options, try again.")
        terrace_decision()

# How drunk are you getting?
def drunk_decision():
    print("In a feat that makes Homer Simpson look like a teetotaler, you finish your beer in 7 seconds flat.")
    print("You turn around and ask the bartender for another beer.")
    number_of_beers = int(input("How many more beers do you end up drinking before the presentations start? 🍺 "))
    if number_of_beers == 1:
        print("It's good that you didn't leave and are sticking with the plan to attend this meetup, but you're never actually going to meet anyone if you only hang out with your beer.")
        presentation_room()
    elif number_of_beers == 2:
        print("Whew! You're on a roll and, at this point, you definitely have lost your ability to speak Spanish. Probably not your greatest plan.")
        presentation_room()
    elif number_of_beers == 3 or number_of_beers == 4:
        print("That is a lot of beer to drink in 30 minutes. You get lost trying to find the bathroom.")
        print("You finally find the bathroom. As you're peeing you look over and see there's no toilet paper 😑")
        print("After a valiant attempt to drip dry, you make your way back to the terrace.")
        presentation_room()
    elif number_of_beers >= 5 and number_of_beers <= 10:
        print("You end up wandering into the back office while looking for the bathroom. The security guard politely escorts you out of the office while shaking his head and mumbling something aout gringos.")
        print("You end up locked in the bathroom until after the presentations are over and someone discovers you.")
        exit(0)
    elif number_of_beers > 10:
        print("Are you even a human being anymore?")
        print("This didn't go as planned. You end up passing out on the far side of the terrace, behind the tinaco.")
        print("You wake up five hours later and find that you've been locked inside. It is a long, cold night for you.")
        exit(0)
    # FIX INSECTO -- doesn't work with non-int input. Maybe use if input not an int (false)... then....
    else:
        print("That is not a valid input.")
        drunk_decision()


# PRESENTATION ROOM FUNCTION -- enter presentation room
def presentation_room():
    print("You walk into the room where the presenations will happen. A big screen is set up at the front of the room and there are twenty rows of chairs.")
    print("Where are you going to sit?")
    print("1. In the front row.")
    print("2. A few rows back.")
    print("3. At the back of the room in the very last row of chairs.")
    seat_selection = input("🌈 ")

    if seat_selection == "1":
        print("You walk to the front of the room and sit down in a chair. Just as you're getting comfortable, someone walks up to you and is talking to you in Spanish.")
        print("After they repeat themselves a couple of times, you realize that the front row is reserved for presenters and you are sitting in their chair.")
        presentation_room()
    elif seat_selection == "2":
        print("This is a perfect spot: you're close enough that you will be able to to see the screen and hear the presenters as they're speaking in Spanish.")
    else:
        print("You choose a seat at the very back of the room. You end up not being able to see the screen. And, because of two people next to you loudly talking, you miss most of what the presenters are saying.")

# After presentations
def after_presentations():
    print("The presentations have ended. As you're getting up to leave, you see someone two chairs over putting away a laptop with a bunch of RStudio stickers on it.")
    print("Recently, you've been learning about large datasets and how to create data visualizations. What do you do?")
    print("1. Leave. Stranger Danger is real.")
    print("2. Say is iffy Spanish \"¿Qué usas RStudio?\"")
    rstudio_choice = input("What do you do? 🤓 ")
    if rstudio_choice == "1":
        go_home()
    elif rstudio_choice == "2":
        rstudio_connections()
    else:
        print("That wasn't an option.")
        after_presentations()

# RStudio Fun
def rstudio_connections():
    print("He tells you he works for a local organization that is working to reduce poverty in Latin America. You exclaim, \"¡Qué padre!\"")
    print("The two of you talk a while longer and learn he's on a team that's building an app that will use data visualizations to tell different stories about poverty.")
    print("It turns out that his teammates are giving a lunchtime talk next week and it will be all about their app project. He invites you to the talk, you exchange WhatsApp, and he messages you the details.")
    print("Good job networking!")

# ADD: add to go home succeccful function a test to see if this function ran. If so, add the below!
# 1. Accept invite, attend talk, and ultimately land a great internship where you learn tons and work on great projects. This 
# work directly leads to your first job and a successful and exciting career in technology.



# NOT VALID SELECTION -- keeping this?
def not_valid():
    print("Sorry, that's not a valid selection.")

    
# TEST
presentation_room()
# arrive_on_terrace()

# welcome()