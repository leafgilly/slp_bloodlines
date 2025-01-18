define DEMO_CHOICE_TEXT = "Choose 2 foods"
define DEMO_INCORRECT_TEXT = "You need to choose 2 foods"
define CHOICES_1 = {
    "apple": "Apple",
    "banana": "Banana",
    "grape": "Grape"
}
define CHOICES_2 = {
    "bread": "Bread",
    "meat": "Meat",
    "soup": "Soup"
}
#To use this demo jump to this label at start
label multi_choice:
    a "Time to make a multiple choice."
    call screen multi_choice(CHOICES_1, 2, choice_text=DEMO_CHOICE_TEXT)
    $ inventory += _return
    a "You got [inventory]."
    call screen multi_choice(CHOICES_2, 2)
    $ inventory += _return
    a "You got [inventory]."
    if "meat" in inventory:
        a "So you eat meat?"