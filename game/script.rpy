# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Amanda")

define dissolve1 = Dissolve(1.0)

transform slightleft:
    xalign 0.25
    yalign 1.0

transform slightright:
    xalign 0.75
    yalign 1.0
 


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg_room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    play music "audio/SweetDreams.mp3" fadeout 1
 
    show amanda_happy at slightleft

    # These display lines of dialogue.

    a "You've created a new Ren'Py game."

    play music "audio/SweetDreams.mp3" fadeout 1

    show amanda_happy:
        linear 1.0 slightright

    a "Once you add a story, pictures, and music, you can release it to the world!"

    show amanda_happy:
        xalign 0.75
        yalign 1.0

    a "..."

    scene bg_outside
    with dissolve1

    pause .5

    play sound "audio/aloneintheuniverse.mp3"

    "An unknown narrator."

    show amanda_happy


    menu:
        a "And now it's me again. Here's a question"

        "Yes, I do.":
            jump choice1_yes

        "No, I don't.":
            jump choice1_no

    label choice1_yes:

        $ choice1 = True

        a "You said yes. Yes will remember this."

        jump choice1_done

    label choice1_no:

        $ choice1 = False

        a "You said no. No will remember this."

        jump choice1_done

    label choice1_done:

        # ... the game continues here.

    a "You are done making your choice. Which affects the next line."

    if choice1:

        a "For example, you said yes."

    else:

        a "For example, you said no."
 
 
 

    # This ends the game.

    return
