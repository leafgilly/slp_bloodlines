label scene1_hotel:
    scene bg_nowhere

    play sound "dialtone.mp3"
    #phone ringing

    #pause 5

    a "{cps=3}. . . . . .{/cps}"

    show am_sulking
    with dissolve

    a "…"

    hide am_sulking
    show am_disappointed_scream

    a "I don’t know why I bother."

    hide am_disappointed_scream
    show am_neutral

    stop sound fadeout 1.0
    play sound "hangup.mp3"

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

    stop sound fadeout 1.0
    play sound "cairo_ambient.mp3" fadein 3.0 fadeout 3.0

    pause 1

    n "The air is dense with smog from a jumbled mass of cars creeping down the street. There aren’t any road lines in sight; the cars squeeze into six narrow lanes on a stretch of asphalt that should really only have three." 

    n "After every pulse of movement, pedestrians step freely into the street to cross. They squeeze between the bumper to bumper traffic without care for the blaring horns, the revving of engines, the shouts of impatience from rolled down windows."

    a_think "And I thought Los Angeles traffic was bad."

    n "She sticks to the sidewalk closer to the shop windows than to the curb."

    a_think "I didn’t plan a vacation in Cairo to get hit by a goddamn car in my second week."

    stop sound fadeout 1.0

    scene bg_hotel
    with dissolve

    n "A few minutes later, Amanda is back at her hotel."

    n "It’s a nice room: a queen bed in the bedroom, a soft-looking couch in the living area, a bathroom with barely enough counter space, and a kitchenette."

    a_think "Nothing compared to my room back at home, but certainly better than the shitty housing at UCLA."

    n "She tosses her purse on the couch, kicks off her shoes, and makes her way to the balcony."

    play sound "sliding_door.mp3"

    show am_angry
    with dissolve

    n "It’s small—too small for her to stretch her legs—and that is yet another minor irritation."

    hide am_angry
    show am_thinking

    n "But the patio chair is comfortable, and the maids put fresh jasmine flowers on the table that morning."

    hide am_thinking
    show am_mischievous

    a_think "And they didn’t touch my cigarettes!"

    hide am_mischievous
    show am_neutral

    n "A small box of cigarettes rests by the flowerpot. Cleopatra-brand. Normally Amanda smokes Marlboros, and she had brought enough to last the trip, but she was enticed by the box’s design a glittering gold foil wrapping with the Pharaoh herself printed in an eye-catching red."
    
    n "The smoke is infused with sweetness and some kind of spice Amanda isn’t used to and she doesn’t quite like it. But something about the image of Cleopatra, elegant and bejeweled in splendor, is enough to bring another filter to Amanda’s lips." #[sound of lighter]

    play sound "lighting_cigarette.mp3"

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

    play sound "doorknock.mp3"

    pause 0.5

    hide am_sympathetic
    show am_alarmed

    a_think "Hmm?"

    n "Unhurriedly, she makes her way over to the door."

    hide am_alarmed
    show am_excited_talking

    a "Who is it?"

    play sound "door_opening.mp3"

    show am_excited_talking at left
    with move

    #todo: Dolce sprite
    show am_angry at right
    with dissolve

    d "Ah, Amanda! It is wonderful to see you."

    n "The man at the door is a tourist from Italy. The two of them met at a coffee shop on Amanda’s second day in Cairo, and they struck up a friendly conversation. When he learned that Amanda could speak a little Italian, he was instantly smitten. Even if the conversation continued in English after a few broken sentences."

    n "Amanda finds him tedious, but he is a man, and a trusted man at your side is never a bad thing when traveling alone."

    n "In fact, their acquaintanceship worked out quite well—to Dolce’s delight, they were staying in the same hotel. They've been meeting up for tourist excursions almost every day since."

    n "Amanda leans against the door, tilting her head coyly."

    a "Hey, Dolce. How was the Citadel?"

    d "Incredible. You would have loved it, such a shame you were ill. How are you feeling?"

    a "Much better. It was just a nasty hangover."

    n "It wasn’t much of a hangover so much as a break from this man’s earnestness, but Amanda isn’t in the business of breaking hearts so quickly."

    d "Poor dear. Gabanna was not feeling very well himself. He is resting his eyes back in the room right now."

    n "Gabanna being his travelling companion. Dolce says they’ve been friends since they were little."

    d "But I wanted to ask, if you are up for it…"

    a "Oh?"

    d "Would you accompany us for a night on the town tonight?"

    n "It sounds like the perfect distraction after a shitty day."

    a "I’d love to. When are you leaving?"

    d "Would a half hour be enough time for you to prepare?"

    n "It seems that Amanda has spent enough time on this trip with Dolce and Gabanna that he’s actually starting to know her."

    a "Only if you don’t mind me being fashionably late. Can’t go out looking like this."

    d "Oh, {i}Ciccina{/i}, you are perfect as you are, but I understand. Just knock on our door when you are ready."

    a "I will."

    d "See you soon."

    #todo: Dolce sprite
    hide am_angry
    with dissolve

    play sound "door_closing.mp3"

    pause 0.5

    show am_excited_talking at center
    with move

    n "Amanda heads over to her closet with a newfound lightness in her steps and peruses her wardrobe."

    a_think "What to wear…"

    n "She glides her hand over the soft fabric of at least a dozen dresses, some she brought with her, others she bought in the past week. There are so many options, but one finally catches her eye."

    a_think "This one was from the bazaar last week…"

    n "It is also one of the more salacious dresses in her collection."

    a "And these go perfect with my dancing shoes."

    n "She reaches for the shoe rack and removes a pair of red stilettos with a two inch heel."

    play sound "zipper.mp3"
    pause 0.5

    n "Amanda slipped on the outfit and then checked over herself in the mirror."

    a "Perfect."

    a_think "Poor Dolce. He doesn’t stand a chance."

    n "Amanda snatches up her purse from where she left it on the couch."

    a_think "Hmm… Too big to take to nightclubs."

    n "She kneels down and opens one of her suitcases, revealing six purses of various weights, sizes, and styles. Each of them is made of real leather; their designer brands twinkle in golds and silvers as she pulls them into the light."

    n "Finally she selects a simple, black cross-body bag. It’s much smaller than her original purse."

    a_think "I’m not gonna be able to take everything with me."

    n "She places both purses down on the table near the kitchen and unzips them both. After she puts her wallet inside, there’s a limited amount of space remaining."

    a "I have enough room for three things. But which ones?"

    call screen multi_choice(ITEM_CHOICES, 3, choice_text="Pick three")
    $ inventory += _return
    n "Amanda took the following: [inventory]"
    
    if "Passport" in inventory:
        a "Passport chosen."

    a "I’ve got my wallet, my [inventory[0]], my [inventory[1]], and my [inventory[2]]." #todo CHANGE THIS SO IT ITERATES THROUGH A LIST

    #[optional dialogue for any interesting combinations goes here]

    n "Amanda hangs her purse on the doorknob so she won’t forget it and then makes her way to the bathroom. Her makeup sits on the countertop, organized with an almost obsessive meticulousness."

    a_think "I might as well put on a new face."

    n "She spends the next half hour reapplying her makeup and touching up her hair, moving through it with an efficiency born from a decade of daily practice."

    n "All the while she scrutinizes herself in the mirror, ensuring that every blemish and unruly strand of hair is smoothed over. Not a single imperfection escapes her notice, blotted over and stamped out."

    n "After all, {w}in the matter of putting on appearances, Amanda has always been uniquely skilled."

    scene bg_hotel
    with dissolve

    n "Amanda places down her brush and snaps the last compact closed. She tousles her hair for a little extra wildness, and then considers herself."

    n "The result speaks for itself, staring back at Amanda in the mirror."

    a "Oh, hello."

    n "Amanda turns her head this way and that, watching the light cut across her carefully sculpted cheekbones, her striking red lips, her luscious hair."

    n "The woman is beautiful. She looks like the life of a party—gregarious, fun, carefree. She evokes a sense of mystery that pulls the viewer closer. She has a smile that lights up the room."

    scene bg_nowhere
    # with dissolve
    n "And that is who Amanda will be."

    jump scene1_interim