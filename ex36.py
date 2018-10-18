# Text-based Strategy Game: Your First Meetup in A Foreign Country
# Exercise 36 in Learn Python the Hard Way
from sys import exit

# LIST OF BEERS
beer = ['Victoria', 'Indio', 'a local IPA', 'Corona Light']

# LIST OF SNACKS
snacks = ['cacahuates japonesa', 'chicharon', 'chapulines']

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
    

# Decision point: check in dude speaking Spanish v quickly c slang and waiving a roll of raffle tickets around. No compredes.
# 1. Turn around, leave, go home --> leave function
# 2. Decide to stay and try your best to learn something and talk to strangers.
# Tell him you are learning Spanish y por fa' despacio. He apologizes, repeats himself more slowly. He's telling you 
# about your free beer ticket and a snack. He lists the beers available, you must select your choice so he can write it down.

# Print list of beers
# Select and store beer choice.

# Print list of snacks.
# Select and store snack choice.

# He gives you two tickets and tells you to continue upstairs. --> Bar




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