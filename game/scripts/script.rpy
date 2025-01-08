# The game starts here.

label start:

    scene bg_nowhere

    #[The sound of a dialtone ringing]

    a "{cps=1}. . . . . .{/cps}"

    #[The dialtone goes to voicemail]

    show am_sulking
    with dissolve

    a "…"

    hide am_sulking
    show am_disappointed_scream

    a "I don’t know why I bother."

    hide am_disappointed_scream
    show am_neutral

    n "Amanda whips the phone back down onto the receiver and stomps away from the payphone."

    hide am_neutral
    show am_angry

    a "No more wasting money on those assholes."

    hide am_angry
    show am_sulking

    a_think "It’s not like Mom actually cares how I’m doing over here, anyway."

    hide am_sulking
    show am_thinking

    a_think "But this is Dad’s favorite place on Earth. Doesn’t he care to hear how his little girl is doing?"

    a_think "…"

    hide am_thinking
    show am_sympathetic

    a_think "I’m so stupid."

    n "She stuffs her hands in her pockets, holding her bag close to her chest, and joins the foot traffic on the side of the street."

    scene bg_cairo
    with dissolve

    pause 1

    n "The air is dense with smog from a jumbled mass of cars creeping down the street. There aren’t any road lines in sight; the cars squeeze into six narrow lanes on a stretch of asphalt that should really only have three." 

    n "After every pulse of movement, pedestrians step freely into the street to cross. They squeeze between the bumper to bumper traffic without care for the blaring horns, the revving of engines, the shouts of impatience from rolled down windows."

    a_think "And I thought Los Angeles traffic was bad."

    n "She sticks to the sidewalk closer to the shop windows than to the curb."

    a_think "I didn’t plan a vacation in Cairo to get hit by a goddamn car in my second week."

    scene bg_hotel
    with dissolve

    n "A few minutes later, Amanda is back at her hotel."

    n "It’s a nice room: a queen bed in the bedroom, a soft-looking couch in the living area, a bathroom with barely enough counter space, and a kitchenette."

    a_think "Nothing compared to my room back at home, but certainly better than the shitty housing at UCLA."

    n "She tosses her purse on the couch, kicks off her shoes, and makes her way to the balcony." #[sound of sliding door]

    show am_angry
    with dissolve

    n "It’s small—too small for her to stretch her legs—and that is yet another minor irritation." #[angy face]

    hide am_angry
    show am_thinking

    n "But the patio chair is comfortable, and the maids put fresh jasmine flowers on the table that morning."

    hide am_thinking
    show am_mischievous

    a_think "And they didn’t touch my cigarettes, thank god."

    hide am_mischievous
    show am_neutral

    n "A small box of cigarettes rests by the flowerpot. Cleopatra-brand. Normally Amanda smokes Marlboros, and she had brought enough to last the trip, but she was enticed by the box’s design a glittering gold foil wrapping with the Pharaoh herself printed in an eye-catching red."

    n "The smoke is infused with sweetness and some kind of spice Amanda isn’t used to and she doesn’t quite like it. But something about the image of Cleopatra, elegant and bejeweled in splendor, is enough to bring another filter to Amanda’s lips." #[sound of lighter]

    n "She takes a long breath, nicotine flooding her system."

    hide am_neutral
    show am_happy

    n "Then she blows it out, her body overcome by lassitude as the plush seat and the cigarette seep all tension from her limbs."

    hide am_happy
    show am_neutral

    a_think "…"

    n "And as she stares passively out at the city below, the combination of physical and chemical pleasures mollify her sour mood, letting her to look inward with an almost passive indifference."

    hide am_neutral
    show am_sympathetic

    a_think "…"

    a_think "What am I even doing here?"

    n "She leans forward onto the railing and watches the city writhe beneath her. A haze of dust obscures the finer details the further out she looks, but she can still see the outline of the pyramids towering over the skyline."


    n "That is where her eye is drawn, and has been every time she’s sat out on the patio. It’s just such a vast and unusual sight, and one she knows she’ll never see again. They have a grandeur that almost compels her to look."

    n "This place is her father’s world. Or it was, until he retired two years ago a successful and respected archaeologist."

    n "Amanda really thought that by coming here, she’d feel that spark of something that her father felt."

    hide am_sympathetic
    show am_sulking

    a_think "..."

    hide am_sulking
    show am_angry
    
    a_think "..."

    hide am_angry
    show am_neutral

    a_think "..."

    n "But she feels nothing, and that isn’t even the worst of it."

    n "Her cigarette burns to a stub. She takes one final drag and tosses it over the railing."

    n "The worst is that she knows how, in the eyes of her father, compared to a city that evokes no excitement, no passion, no love…"

    hide am_neutral
    show am_sad

    a_think "{cps=25}…I can never compare.{/cps}"

    hide am_sad
    show am_sympathetic

    a_think "…"

    #[knock at the door]

    hide am_sympathetic
    show am_alarmed

    a_think "Hmm?"

    n "Unhurriedly, she makes her way over to the door."

    hide am_alarmed
    show am_excited_talking

    a "Who is it?"

    #opens the door

    show am_excited_talking at left
    with move

    show am_angry at right
    with dissolve

    a_think 'THIS IS THE END OF THE SCRIPT SO FAR'

    jump examples




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
