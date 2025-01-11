screen multi_choice(options, num_choices):
    default selected_options = {option: False for option in options}
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            text "Choices"
            for option in options:
                textbutton option:
                    action ToggleDict(selected_options, option)
            textbutton "Done":
                action Return([val for val in selected_options if selected_options[val]])
