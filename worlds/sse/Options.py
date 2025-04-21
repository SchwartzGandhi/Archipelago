from dataclasses import dataclass
from Options import PerGameCommonOptions, Toggle, Choice, Range

class LayoutMode(Choice):
    """Determines how levels are unlocked.
    Characters: Levels are unlocked by having the characters that start said level in story mode.
    Stage: Levels are unlocked by having the level itself.
    """
    display_name = "Layout Mode"
    option_characters = 0
    option_stages = 1
    default = 0
# TODO: while this is cool/funny, do we really need this?
# class PokemonTrainerBehaviour(Choice):
#     """Determines how Pokémon Trainer is accounted for in logic.
#     Solo Trainer: Just Pokémon Trainer is shuffled and will have access to every Pokémon.
#     Require Trainer and Pokémon: Pokémon Trainer and his three Pokémon are shuffled into the pool separately, logic will require the Trainer as well as one Pokémon.
#     Progressive Trainer: Shuffle 4 Progressive Trainers into the pool, logic will require the Trainer as well as one Pokémon
#     (Progressive Trainer is in the following order: Pokémon Trainer, Squirtle, Ivysaur, Charizard)
#     """
#     display_name = "Pokémon Trainer Behaviour"
#     option_solo_trainer = 0
#     option_require_trainer_and_pokemon = 1
#     option_progressive_trainer = 2
#     default = 0

# class SamusBehaviour(Choice):
#     """Determines how Samus is accounted for in logic.
#     Any Samus: Having either Samus or Zero Suit Samus will allow you to enter all of her respective levels.
#     Separate Samus: Logic will require either Samus or Zero Suit Samus for her respective levels.
#     Progressive Samus: Shuffles 2 Progressive Samuses into the pool, Logic will behave the same as Separate Samus.
#     (Progressive Samus is in the following order: Zero Suit Samus, Samus)
#     """
#     display_name = "Samus Behaviour"
#     option_any_samus = 0
#     option_separate_samus = 1
#     option_progressive_samus = 2
#     default = 0

# class ZeldaBehaviour(Choice):
#     """Determines how Zelda and Sheik is accounted for in logic.
#     Any Zelda: Having either Zelda or Sheik will allow you to enter all of her respective levels.
#     Separate Zelda: Logic will require either Zelda or Sheik for her respective levels.
#     Progressive Zelda: Shuffles 2 Progressive Zeldas into the pool, Logic will behave the same as Separate Zelda.
#     (Progressive Zelda is in the following order: Zelda, Sheik)
#     """
#     display_name = "Zelda Behaviour"
#     option_any_zelda = 0
#     option_separate_zelda = 1
#     option_progressive_zelda = 2
#     default = 0

class SecretCharcterShuffle(Toggle):
    """Shuffles Toon Link, Jigglypuff, Wolf, and their respective checks into the game."""
    display_name = "Shuffle Secret Characters"
    default = False

class HoardeShuffle(Toggle):
    """Send a check whenever you complete a hoarde battle"""
    display_name = "Shuffle Hoarde Battles"
    default = False

class GreatMazeRequirements(Choice):
    """Determines how you want The Great Maze to be unlocked.
    Open: having any fighter will unlock The Great Maze.
    Minimum Fighters: having Luigi, Ness, King Dedede, Bowser and Kirby will unlock the Great Maze.
    Percentage of Fighters: having a specified amount of fighters will unlock The Great Maze.
    Minimum Plus Percentage: having Luigi, Ness, King Dedede, Bowser, Kirby, plus an specified amount of fighters will unlock The Great Maze.
    All Fighters: EVERYONE IS HERE!
    """
    display_name = "Great Maze Requirements"
    option_open = 0
    option_minimum_fighters = 1
    option_percentage_of_fighters = 2
    option_minimum_plus_percentage = 3
    option_all_fighters = 4
    default = 1

class GreatMazeFighterPercentage(Range):
    """Determines the ammount of fighters you need to enter The Great Maze.
    This is only used if you have Percentage of Fighters or Minimum Plus Percentage enabled in Great Maze Requirements.
    Keep in mind that this is a percentage of all the fighters you have shuffled.
    """
    display_name = "Great Maze Fighter Percentage"
    range_start = 0
    range_end = 100
    default = 50

class TabuuRequirements(Choice):
    """Determines how you want Tabuu to be unlocked.
    Open: You can fight Tabuu as soon has you have access to The Great Maze.
    Percentage of Fighters: have a specified amount of fighters be required to unlock Tabuu.
    Boss Hunt: Defeat a specified amount of bosses in other levels to unlock Tabuu.
    Fighters and Bosses: A combination of the previous two.
    DISCLAIMER: the last two options currently don't work.
    """
    display_name = "Tabuu Requirements"
    option_open = 0
    option_percentage_of_fighters = 1
    option_boss_hunt = 2
    option_fighters_and_bosses = 3
    default = 1

class TabuuFighterPercentage(Range):
    """Determines the ammount of fighters you need to fight Tabuu.
    This is only used if you have Percentage of Fighters or Fighters and Bosses enabled in Tabuu Requirements.
    Keep in mind that this is a percentage of all the fighters you have shuffled.
    """
    display_name = "Tabuu Fighter Percentage"
    range_start = 0
    range_end = 100
    default = 80

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
    layout_mode: LayoutMode
    #trainer_behaviour: PokemonTrainerBehaviour
    #samus_behaviour: SamusBehaviour
    #zelda_behaviour: ZeldaBehaviour
    secret_character_shuffle: SecretCharcterShuffle
    hoarde_shuffle: HoardeShuffle
    great_maze_requirements: GreatMazeRequirements
    maze_fighter_percentage: GreatMazeFighterPercentage
    tabuu_requirements: TabuuRequirements
    tabuu_fighter_percentage: TabuuFighterPercentage
    tabuu_boss_amount: TabuuBossHunt