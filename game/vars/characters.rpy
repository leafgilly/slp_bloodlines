init python:
    image_files = [name for name in renpy.list_files() if name.startswith('images/characters/')]
    for name in image_files:
        character, file_name = name.split('/')[2:]
        image_name = character + ' ' + file_name.split('.')[0].split('_', 1)[1].replace('_', ' ')
        renpy.image(image_name, file_name)


# Character declarations

define n = Character(None, who_color="#ffffff")

define a = Character("Amanda", who_color="#ffee00")
define a_think = Character("Amanda", who_color="#ffee00", what_italic=True)

define d = Character("Dolce")

#figure out window_background to show textbox vs textbox_narrator