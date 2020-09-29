# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Reena")

#RenPy default positions = left, right, center, behind, front
#RenPy position values=

#Left = 0.0
#Center = 0.5
#Right = 1.0

#Up = 1.0
#Center = 0.5
#Down = 0.0

transform bottomLeft:
    xalign 0.0
    yalign 0.5

transform bottomRight:
    xalign 1.0
    yalign 0.5

transform bottomCenter:
    xalign 0.5
    yalign 0.5

transform bottomRightish:
    xalign 0.75
    yalign 0.5


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room morning

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



    show reena neutral 1 at bottomLeft with dissolve

    r "Ugh, morning already?"

    show reena angry 1 at bottomCenter with Dissolve(0.25)

    r "I have to get ready to go to the cafe!"

    show reena neutral 1 at bottomRightish
    show reena neutral 2 with dissolve
    show reena sad 1 with Dissolve(0.1)
    show reena sad 2 with Dissolve(0.1)
    show reena sad 3 with Dissolve(0.1)

    r "I guess I'll go now..."

    scene bg cafe day

    show reena happy 1 at bottomLeft

    r "Woah! Smells like coffee in here! That perked me up!"

    show reena happy 2 with Dissolve(0.25)
    show reena happy 3 with Dissolve(0.25)
    show reena happy 4 with Dissolve(0.25)

    r "So glad it's National Coffee Day!"

    scene bg cafe fire

    r "Wait... that's not the smell of coffee..."

    show reena sad 1 at bottomRightish
    show reena sad 2 with Dissolve(0.1)
    show reena sad 3 with Dissolve(0.1)

    r "Ah!!!!! It's fire!"





    # These display lines of dialogue.



    # This ends the game.

    return
