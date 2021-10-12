from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

class Death(Scene):

    quips = [
        "You died, You kinda suck it this.",
        "Your Mom would be proud.....if she were smarter."
        "Such a luser.",
        "I've a small puppy that's better at this.",
        "You're worse them your Dad's jokes."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class MagicForest(Scene):

    def enter(self):
        print(dedent("""
            You enter the magic forest. There is an amazing light around you.
            You feel a warm, calming feeling.
            In the distance a light is shown.
            What are you going to do?
        """))
        
        action = input("> ")

        if action == "walk":
            print(dedent("""
            You walk towards the light.
            """))
            return 'Light_fountain'

        elif action == "stay":
            pass
