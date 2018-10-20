# Text-based Strategy Game: Your First Meetup in A Foreign Country
# Exercise 36 in Learn Python the Hard Way
from sys import exit

# LIST OF BEERS
beers = ['Victoria', 'Indio', 'a local IPA', 'Corona Light']

# LIST OF SNACKS
botanas = ['cacahuates japonesa', 'chicharon', 'chapulines', 'palomitas']

# WELCOME
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
    foyer_choice = int(input("🌈 "))

    if foyer_choice == 1:
        go_home()
    elif foyer_choice == 2:
        # Tell him you are learning Spanish y por fa' despacio. He apologizes, repeats himself more slowly. He's telling you 
        # about your free beer ticket and a snack. He lists the beers available, you must select your choice so he can write it down.
        print("In Spanish, explain that you are learning Spanish and ask if he could speak slower.")
        print("He immediately appologizes and then repeats himself speaking much slower. He explains you get a free beer ticket and a snack at the meetup.")
        print("He says he needs to keep track of which beers people want and motions to the list on his clipboard.")
        # Print list of beers
        print(f"He tells you they've got {', '.join(beers)}. Which would you like?")
        # Select and store beer choice.
        beer_choice = input("🍺 ").upper()
        
        # If statements for beer_choice
        if "VICTORIA" in beer_choice:
            print("A worthy choice.")
            snacks()
        elif "INDIO" in beer_choice:
            print("Classic choice.")
            snacks()
        elif "IPA" in beer_choice:
            print("Such a hipster. ¡Salud!")
            snacks()
        elif "CORONA" in beer_choice:
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
    snack_choice = input("🍿 ").upper()
    print(snack_choice)
    # If statement for snack selection
    if "CACAHUATES" in snack_choice:
        print("Thats my favorite snack!")
    elif "CHICHARON" in snack_choice:
        print("¡Que rico!")
    elif "CHAPULINES" in snack_choice:
        print("Tasty!")
    elif "PALOMITAS" in snack_choice:
        print("I could eat palomitas every single day!")
    else:
        print("That wasn't one of the choices. I guess no snacks for you. 🤷🏻‍♀️")
    # He gives you two tickets and tells you to continue upstairs. --> Bar
    print(f"He gives you a drink ticket, your {snack_choice.lower()}, then tells you to go upstairs. ")


# BAR

# Describe the terrace that has been converted to a make-shift bar, where people are standing around in small groups.

# Everyone seems to know each other and is speaking Spanish. Ug. Do you:
# 1. Turn around, leave, go home --> leave function
# 2. Decide to stay and try your best to learn something and talk to strangers.

# Give yourself something to do, walk up to the bar, and hold out your drink ticket.
# Bartender takes your drink ticket, gives the list of options
# Select your choice.

# The talk doesn't start for 30 minutes, what do you do?
# 1. Slam your beer and order more
    # How many more beers do you drink?
    # one more: drink it, then --> presentation room
    # 2 - 3 more: get lost trying to find bathroom, finally do and then discover there's no toilet paper. --> presentation room
    # 4+ more: Wander into the offices while trying to find the bathroom and end up locked in their bathroom. Miss 
    # presentations --> end game
# 2. Drink your beer (maybe make some friends)
    # A woman in a group standing next to you at the bar says hi. She's wearing blinking ßrainbow LEDs in her hair.
    # 1. You tell her they're cool: she says thanks and starts telling you how she programmed them. You talk w the group.
        # A guy comes up with a bag of snacks, he lists them and asks which you would like.
        # leave and --> leave function
        # --> presentation room (skip where to sit)
    # 2. You take a swig of your beer, then --> presentation room
# 3. Take your beer into the presentation room (dodge creeper)
    # Good job! A creeper had been eyeing you and was just about to walk over and start hitting on you --> presentation room






# PRESENTATION ROOM FUNCTION -- enter presentation room
def presentation_room():
    print("You walk into the room where the presenations will happen. A big screen is set up at the front of the room and there are twenty rows of chairs.")
    print("Where are you going to sit?")
    print("1. In the front row.")
    print("2. A few rows back.")
    print("3. At the back of the room in the very last row of chairs.")
    seat_selection = int(input("🌈 "))

    if seat_selection == 1:
        print("You walk to the front of the room and sit down in a chair. Just as you're getting comfortable, someone walks up to you and is talking to you in Spanish.")
        print("After they repeat themselves a couple of times, you realize that the front row is reserved for presenters and you are sitting in their chair.")
        presentation_room()
    
    elif seat_selection == 2:
        print("This is a perfect spot: you're close enough that you will be able to to see the screen and hear the presenters as they're speaking in Spanish.")
    
    else:
        print("You choose a seat at the very back of the room. You end up not being able to see the screen. And, because of two people next to you loudly talking, you miss most of what the presenters are saying.")



# NOT VALID SELECTION -- keeping this?
def not_valid():
    print("Sorry, that's not a valid selection.")

# test

foyer()





# PRESENTATION ROOM
# Where to sit
# 1. Front row: in presenter's seat, have to move, loop back to where to sit
# 2. Few rows back: Good job! You can see and hear the presentations --> After presentations
# 3. Back of the room: can't hear, barely see anything. --> After presentations

# After presentations
# The presenations have finished, as you're getting up to leave you see s/o at the end of your row putting away a laptop with
# a bunch of R Studio stickers on it. You have been learning about large data sets and creating data visualizations, what do you do:
# 1. Leave --> leave function
# 2. Say in broken Spanish "What do you use R Studio for?" He works for a company using data for social justice projects. He
# invites you to a lunchtime talk later that week at his work. A co-worker will be talking about their latest data visualization project. 
# What do you do
# 1. Accept invite, attend talk, and ultimately land a great internship where you learn tons and work on great projects. This 
# work directly leads to your first job and a successful and exciting career in technology.
# 2. Make some non-commital reply and quickly --> Leave function