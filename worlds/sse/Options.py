from dataclasses import dataclass
from Options import PerGameCommonOptions, Toggle, Choice, Range

class WorldLayout(Choice):
    """Determines how levels are unlocked.
    Characters: Levels are unlocked by having the characters that start said level in story mode.
    Stage: Levels are unlocked by having the level itself.
    """
    display_name = "World Layout"
    option_characters = 0
    option_stages = 1
    default = 0

class SplitCharacters(Toggle):
    """Enabling this will turn Zelda, Samus, and the Pokémon Trainer into multiple charcters.
    Note that logic will still consider them as a single character for accessing The Great Maze and Tabuu.
    ie: Zelda -> Zelda, Sheik
    Samus -> Zero Suit Samus, Samus
    Pokémon Trainer -> Squirtle, Ivysaur, Charizard
    This will have logical implications if world layout is set to Characters.
    """
    display_name = "Split Characters"
    default = False

class SecretCharacterShuffle(Toggle):
    """Shuffles Toon Link, Jigglypuff, Wolf, and their respective checks into the game.
    Note that logic won't consider these characters for accessing The Great Maze and Tabuu.
    """
    display_name = "Shuffle Secret Characters"
    default = False

class SplitGreatMaze(Toggle):
    """Enabling this will Split the Great Maze into four separate quadrants.
    For now, this will only matter if World Layout is set to Stages.
    """
    display_name = "Split Great Maze"
    default = False

class GreatMazeRequirements(Choice):
    """Determines how The Great Maze will be unlocked.
    This will only matter if World Layout is set to Characters.
    Open: having any fighter will unlock The Great Maze.
    Minimum Requirements: having Luigi, Ness, King Dedede, Bowser and Kirby will unlock the Great Maze.
    Amount of Characters: having a specified amount of fighters will unlock The Great Maze.
    Minimum Plus Characters: having Luigi, Ness, King Dedede, Bowser, Kirby, plus an specified amount of fighters will unlock The Great Maze.
    """
    display_name = "Great Maze Requirements"
    option_open = 0
    option_minimum_requirements = 1
    option_amount_of_characters = 2
    option_minimum_plus_characters = 3
    default = 1

class GreatMazeCharacterAmount(Range):
    """Determines the amount of characters you need to enter The Great Maze.
    This is only used if you have Amount of Characters or Minimum Plus Characters enabled in Great Maze Requirements.
    """
    display_name = "Great Maze Character Amount"
    range_start = 0
    range_end = 35
    default = 12

class TabuuRequirements(Choice):
    """Determines how you want Tabuu to be unlocked.
    Open: You can fight Tabuu as soon has you have access to The Great Maze.
    Amount of Characters: have a specified amount of fighters be required to unlock Tabuu.
    Boss Hunt: Defeat a specified amount of bosses in other levels to unlock Tabuu.
    Characters and Bosses: A combination of the previous two.
    """
    display_name = "Tabuu Requirements"
    option_open = 0
    option_amount_of_characters = 1
    option_boss_hunt = 2
    option_characters_and_bosses = 3
    default = 1

class TabuuCharacterAmount(Range):
    """Determines the ammount of fighters you need to fight Tabuu.
    This is only used if you have Amount of Characters or Characters and Bosses enabled in Tabuu Requirements.
    """
    display_name = "Tabuu Character Amount"
    range_start = 0
    range_end = 35
    default = 24

class TabuuBossHunt(Range):
    """Determines the amount of bosses that must be defeated to fight Tabuu.
    This is only used if you have Boss Hunts or Fighters and Bosses enabled.
    """
    display_name = "Tabuu Boss Ammount"
    range_start = 0
    range_end = 8
    default = 4

@dataclass
class SSEOptions(PerGameCommonOptions):
    world_layout: WorldLayout
    split_characters: SplitCharacters
    secret_character_shuffle: SecretCharacterShuffle
    split_great_maze: SplitGreatMaze
    great_maze_requirements: GreatMazeRequirements
    maze_character_amount: GreatMazeCharacterAmount
    tabuu_requirements: TabuuRequirements
    tabuu_character_amount: TabuuCharacterAmount
    tabuu_boss_amount: TabuuBossHunt