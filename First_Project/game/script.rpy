## The script of the game goes in this file.

## Declare characters used by this game. The color argument colorizes the name
## of the character.

define e = Character('Eileen', color = '#00cc99')
define t = Character('Tom', color = '#ff944d')

image bg city_sunset = 'city_sunset.jpg'
image bg treehouse = 'treehouse.jpg'
image bg fireworks = 'fireworks.jpg'


## The game starts here.

label start:

    ## Show a background. This uses a placeholder by default, but you can add a
    ## file (named either "bg room.png" or "bg room.jpg") to the images
    ## directory to show it.

    scene bg city_sunset
    with fade
    e "This is the start of the story."
    t "We can go to two places. Where would you like to go?"

    ## This shows a character sprite. A placeholder is used, but you can replace
    ## it by adding a file named "eileen happy.png" to the images directory.

    menu:

        "A tree house":
            jump treehouse

        "The fireworks!":
            jump fireworks

label treehouse:
    scene bg treehouse
    with fade 

    e "Welcome to our secret base."
    return

label fireworks:
    scene bg fireworks
    with dissolve

    t "Aren't the fireworks pretty?"
    return

