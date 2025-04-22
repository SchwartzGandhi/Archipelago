from typing import Dict, Iterable, NamedTuple, Optional, Union

from BaseClasses import Item
from BaseClasses import ItemClassification as IC
from worlds.AutoWorld import World

class SSEItemData(NamedTuple):
    type: str
    classification: IC
    code: Optional[int]
    quantity: int
    item_id: Optional[int]

class SSEItem(Item):
    game: str = "Super Smash Bros. Brawl: The Subspace Emissary"
    type: Optional[str]

item_data_table: Dict[str, SSEItemData] = {
    # Fighters
    "Kirby": SSEItemData("Item", IC.progression, 0, 1),
    "Peach": SSEItemData("Item", IC.progression, 1, 1),
    "Zelda": SSEItemData("Item", IC.progression, 2, 1),
    "Pit": SSEItemData("Item", IC.progression, 3, 1),
    "Mario": SSEItemData("Item", IC.progression, 4, 1),
    "Diddy Kong": SSEItemData("Item", IC.progression, 5, 1),
    "Lucas": SSEItemData("Item", IC.progression, 6, 1),
    "Pokémon Trainer": SSEItemData("Item", IC.progression, 7, 1),
    "Squirtle": SSEItemData("Item", IC.progression, 8, 1),
    "Ivysaur": SSEItemData("Item", IC.progression, 9, 1),
    "Charizard": SSEItemData("Item", IC.progression, 10, 1),
    "Marth": SSEItemData("Item", IC.progression, 11, 1),
    "Meta Knight": SSEItemData("Item", IC.progression, 12, 1),
    "Ike": SSEItemData("Item", IC.progression, 13, 1),
    "Fox": SSEItemData("Item", IC.progression, 14, 1),
    "Zero Suit Samus": SSEItemData("Item", IC.progression, 15, 1),
    "Pikachu": SSEItemData("Item", IC.progression, 16, 1),
    "Link": SSEItemData("Item", IC.progression, 17, 1),
    "Yoshi": SSEItemData("Item", IC.progression, 18, 1),
    "Falco": SSEItemData("Item", IC.progression, 19, 1),
    "Samus": SSEItemData("Item", IC.progression, 20, 1),
    "Olimar": SSEItemData("Item", IC.progression, 21, 1),
    "Captain Falcon": SSEItemData("Item", IC.progression, 22, 1),
    "Donkey Kong": SSEItemData("Item", IC.progression, 23, 1),
    "Ice Climbers": SSEItemData("Item", IC.progression, 24, 1),
    "Lucario": SSEItemData("Item", IC.progression, 25, 1),
    "Snake": SSEItemData("Item", IC.progression, 26, 1),
    "Sheik": SSEItemData("Item", IC.progression, 27, 1),
    "Mr. Game & Watch": SSEItemData("Item", IC.progression, 28, 1),
    "R.O.B.": SSEItemData("Item", IC.progression, 29, 1),
    "Luigi": SSEItemData("Item", IC.progression, 30, 1),
    "Ness": SSEItemData("Item", IC.progression, 31, 1),
    "King Dedede": SSEItemData("Item", IC.progression, 32, 1),
    "Bowser": SSEItemData("Item", IC.progression, 33, 1),
    "Ganondorf": SSEItemData("Item", IC.progression_skip_balancing, 34, 1),
    "Wario": SSEItemData("Item", IC.progression_skip_balancing, 35, 1),
    "Sonic": SSEItemData("Item", IC.progression_skip_balancing, 36, 1),
    "Toon Link": SSEItemData("Item", IC.progression_skip_balancing, 37, 1),
    "Jigglypuff": SSEItemData("Item", IC.progression_skip_balancing, 38, 1),
    "Wolf": SSEItemData("Item", IC.progression_skip_balancing, 39, 1),
    
    # Stages
    "The Midair Stadium": SSEItemData("Item", IC.progression, 40, 1),
    "Skyworld": SSEItemData("Item", IC.progression, 41, 1),
    "Sea of Clouds": SSEItemData("Item", IC.progression, 42, 1),
    "The Jungle": SSEItemData("Item", IC.progression, 43, 1),
    "The Plain": SSEItemData("Item", IC.progression, 44, 1),
    "The Lake": SSEItemData("Item", IC.progression, 45, 1),
    "The Ruined Zoo": SSEItemData("Item", IC.progression, 46, 1),
    "The Battlefield Fortress": SSEItemData("Item", IC.progression, 47, 1),
    "The Forest": SSEItemData("Item", IC.progression, 48, 1),
    "The Research Facility I": SSEItemData("Item", IC.progression, 49, 1),
    "The Lake Shore": SSEItemData("Item", IC.progression, 50, 1),
    "The Path to the Ruins": SSEItemData("Item", IC.progression, 51, 1),
    "The Cave": SSEItemData("Item", IC.progression, 52, 1),
    "The Ruins": SSEItemData("Item", IC.progression, 53, 1),
    "The Wilds I": SSEItemData("Item", IC.progression, 54, 1),
    "The Ruined Hall": SSEItemData("Item", IC.progression, 55, 1),
    "The Wilds II": SSEItemData("Item", IC.progression, 56, 1),
    "The Swamp": SSEItemData("Item", IC.progression, 57, 1),
    "The Research Facility II": SSEItemData("Item", IC.progression, 58, 1),
    "Outside the Ancient Ruins": SSEItemData("Item", IC.progression, 59, 1),
    "The Glacial Peak": SSEItemData("Item", IC.progression, 60, 1),
    "The Canyon": SSEItemData("Item", IC.progression, 61, 1),
    "Battleship Halberd Interior": SSEItemData("Item", IC.progression, 62, 1),
    "Battleship Halberd Exterior": SSEItemData("Item", IC.progression, 63, 1),
    "Battleship Halberd Bridge": SSEItemData("Item", IC.progression, 64, 1),
    "The Subspace Bomb Factory I": SSEItemData("Item", IC.progression, 65, 1),
    "The Subspace Bomb Factory II": SSEItemData("Item", IC.progression, 66, 1),
    "Entrance to Subspace": SSEItemData("Item", IC.progression, 67, 1),
    "Subspace I": SSEItemData("Item", IC.progression, 68, 1),
    "Subspace II": SSEItemData("Item", IC.progression, 69, 1),
    "The Great Maze": SSEItemData("Item", IC.progression, 70, 1),
    "The Great Maze NW": SSEItemData("Item", IC.progression, 71, 1),
    "The Great Maze NE": SSEItemData("Item", IC.progression, 72, 1),
    "The Great Maze SE": SSEItemData("Item", IC.progression, 73, 1),
    "The Great Maze SW": SSEItemData("Item", IC.progression, 74, 1),

    # Boss Trophies
    "Petey Piranha Trophy": SSEItemData("Item", IC.progression, 75, 1),
    "Rayquaza Trophy": SSEItemData("Item", IC.progression, 76, 1),
    "Porky Trophy": SSEItemData("Item", IC.progression, 77, 1),
    "Galleom Trophy": SSEItemData("Item", IC.progression, 78, 2),
    "Ridley Trophy": SSEItemData("Item", IC.progression, 79, 1),
    "Duon Trophy": SSEItemData("Item", IC.progression, 80, 1),
    "Meta Ridley Trophy": SSEItemData("Item", IC.progression, 81, 1),

    "Victory": SSEItemData("Event", IC.progression, None,  1, None),
}

item_table = {
    name: data.code for name, data in item_data_table.items() if data.code is not None
}