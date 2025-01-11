#To use this demo jump to this label at start
label multi_choice:
    a "Time to make a multiple choice"
    call screen multi_choice(["Apple", "Banana", "Grape"], 2)
    $ inventory += _return
    a "You got [inventory]"
    call screen multi_choice(["Bread", "Meat", "Soup"], 2)
    $ inventory += _return
    a "You got [inventory]"