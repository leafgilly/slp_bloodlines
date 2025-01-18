define DEFAULT_CHOICE_TEXT = "Choices"

screen multi_choice(options, num_choices, choice_text=DEFAULT_CHOICE_TEXT):
    default selected_options = {option: False for option in options}
    default hovered_option = None
    frame:
        xalign 0.5
        yalign 0.5
        has vbox spacing 10
        text choice_text
        for option in options:
            hbox:
                imagebutton:
                    xsize 50
                    ysize 50
                    xalign 0.5
                    yalign 0.5
                    if not selected_options[option]:
                        if hovered_option == option:
                            idle "gui/button/checkmark_unchecked_highlighted.png"
                        else:
                            idle "gui/button/checkmark_unchecked.png"
                    else:
                        if hovered_option == option:
                            idle "gui/button/checkmark_highlighted.png"
                        else:
                            idle "gui/button/checkmark_checked.png"
                    action ToggleDict(selected_options, option)
                    hovered SetScreenVariable("hovered_option", option)
                    unhovered SetScreenVariable("hovered_option", None)
                textbutton option:
                    action ToggleDict(selected_options, option)
                    selected hovered_option == option
                    hovered SetScreenVariable("hovered_option", option)
                    unhovered SetScreenVariable("hovered_option", None)

        textbutton "Done":
            sensitive len([option for option, selected in selected_options.items() if selected]) == num_choices
            action Return([val for val in selected_options if selected_options[val]])