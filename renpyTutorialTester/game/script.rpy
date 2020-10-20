# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define p = Character("Professor Page", color= "#043927")
define j = Character("Jeff Goldblum", color= "#01796F")

transform slightRight:
    xalign 0.75
    yalign 0.0

# The game starts here.

label start:

    #this is a say statement. Put this in quotes.
    #if you DON'T put a name in quotes before your say statement,
    #it will come from the narrator. (Like an inner thought).
    #putting a character's name in quotes is INCONVENIENT.
    #to make up for this, we define characters.

    "Hm... This thing on?"

    "Look, ma! \"quotes\"!"

    #when we want to put an image into our game, we have to:
    #first, name the image.
    #use the following format: tag name
    #tag refers to the type of element your image is going to be
    #bg is background, lucy is a character, etc.

    #for example, if we wanted a professor page photo...
    #page tired

    #images must be saved under the EXACT SAME NAME
    #you type into RenPy



    "Professor Page" "Ok, let's get started."

    p "We can create dialogue coming from a character using definitions, too!"

    p "Saves a lot of time in the long run..."

    p "Wait... we get the dialogue, but can y'all see me?"

    p "Let's get some visuals in here."

    #to show an image, write SHOW in front of the image name

    scene bg asc
    show page tired

    p "I haven't had enough coffee yet today..."

    show page happy

    p "But the week's almost over!"

    hide page happy

    p "But... what if time is just a construct?"

    #using an "at statement" will determine where the image is
    #common at statements include: left, right, center, behind

    show page tired at left
    hide page tired
    hide bg asc

    p "Let's take a trip back... millions of years ago... to the time of the dinosaurs."

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg jurassic park gate

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show page happy at left

    p "This seems like a good place to start! Maybe we need a friend to join us, though..."

    show jeff snappy at right

    j "You rang?"

    show jeff sheepish at left

    j "Step aside... I know this place well. I got this handled."


    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
