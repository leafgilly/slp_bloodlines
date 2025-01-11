#To use this demo jump to this label at start
label examples:

    a "Back to script for the choices."

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