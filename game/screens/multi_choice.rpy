screen incorrect_number():
    frame:
        xalign 0.25
        yalign 0.25
        modal True
        vbox:
            text "You chose the incorrect number of items"
            textbutton "Ok":
                action Hide()

screen multi_choice(options, num_choices):
    default selected_options = {option: False for option in options}
    frame:
        xalign 0.5
        yalign 0.5
        has vbox spacing 10
        text "Choices"
        for option in options:
            hbox:
                spacing 20
                imagebutton:
                    xsize 50
                    ysize 50
                    if not selected_options[option]:
                        idle "gui/button/checkmark_unchecked.png"
                    else:
                        idle "gui/button/checkmark_checked.png"
                    action ToggleDict(selected_options, option)
                text option
        textbutton "Done":
            if len([option for option, selected in selected_options.items() if selected]) == num_choices:
                action Return([val for val in selected_options if selected_options[val]])
            else:
                action Show("incorrect_number")
