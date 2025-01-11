define DEMO_CHOICE_TEXT = "Choose 2 foods"
define DEMO_INCORRECT_TEXT = "You need to choose 2 foods"
#To use this demo jump to this label at start
label multi_choice:
    a "Time to make a multiple choice"
    call screen multi_choice(["Apple", "Banana", "Grape"], 2, choice_text=DEMO_CHOICE_TEXT, incorrect_text=DEMO_INCORRECT_TEXT)
    $ inventory += _return
    a "You got [inventory]"
    call screen multi_choice(["Bread", "Meat", "Soup"], 2)
    $ inventory += _return
    a "You got [inventory]"
    if "Meat" in inventory:
        a "So you eat meat?"