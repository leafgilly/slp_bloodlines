#small script to automatically load character images
#works by going through each subfolder of images/characters and making an image like <character name> <image file without prefix>
#for example, if there's a file called images/characters/amanda/am_afraid_talking.png
#that will create an image called amanda afraid_talking
init python:
    image_files = [name for name in renpy.list_files() if name.startswith('images/characters/')]
    for name in image_files:
        character, file_name = name.split('/')[2:]
        image_name = character + ' ' + file_name.split('.')[0].split('_', 1)[1]
        renpy.image(image_name, name)


# Character declarations

define n = Character(None, who_color="#ffffff")

define a = Character("Amanda", who_color="#ffee00")
define a_think = Character("Amanda", who_color="#ffee00", what_italic=True)

define d = Character("Dolce")

#figure out window_background to show textbox vs textbox_narrator