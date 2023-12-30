import typing
from Options import TextChoice, Option, Range, Toggle


class Character1(TextChoice):
    """Enter the internal ID of the character to use."""
    display_name = "Character 1"
    option_Dizzy = 1
    option_Riggs = 2
    option_Peri = 3
    option_Isaac = 4
    option_Drake = 5
    option_Max = 6
    option_Books = 7
    option_Cat = 0

class Character2(TextChoice):
    """Enter the internal ID of the character to use."""
    display_name = "Character 2"
    option_Dizzy = 1
    option_Riggs = 2
    option_Peri = 3
    option_Isaac = 4
    option_Drake = 5
    option_Max = 6
    option_Books = 7
    option_Cat = 0

class Character3(TextChoice):
    """Enter the internal ID of the character to use."""
    display_name = "Character 3"
    option_Dizzy = 1
    option_Riggs = 2
    option_Peri = 3
    option_Isaac = 4
    option_Drake = 5
    option_Max = 6
    option_Books = 7
    option_Cat = 0

class Ship(TextChoice):
    """Enter the internal ID of the ship to use."""
    display_name = "Ship"
    option_Artemis = 0
    option_Ares = 1
    option_Jupiter = 2
    option_Gemini = 3
    option_Tiderunner = 4

class Difficulty(TextChoice):
    """What difficulty do you wish to play with."""
    display_name = "Difficulty"
    option_Normal = 0
    option_Hard = 1
    option_Harder = 2
    option_Hardest = 3

spire_options: typing.Dict[str, type(Option)] = {
    "character1": Character1,
    "character2": Character2,
    "character3": Character3,
    "ship": Ship,
    "difficulty": Difficulty,
}
