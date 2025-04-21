from enum import Enum, Flag, auto
from typing import TYPE_CHECKING, Dict, Callable, NamedTuple, Optional, Tuple

from BaseClasses import Location, Region

if TYPE_CHECKING:
    from . import SSEWorld

class SSELocation(Location):
    game = "Super Smash Bros. Brawl: The Subspace Emissary"

class SSELocationType(Enum):
    GOLBOX = auto() # Golden Boxes
    PICKUP = auto() # Freestanding Trophies
    NEWCMR = auto() # Newcomers
    HOARDE = auto() # Subspace Hoardes
    BRAWL = auto() # Miniboss Brawls
    FTROPHY = auto() # Fighter Trophies in Subspace
    SECRET = auto() # Toon Link, Jigglypuff, Wolf checks
    BOSS = auto() # Bosses
    TABUU = auto() # Final Boss

class SSELocationData(NamedTuple):
    code: Optional[int]
    region: str
    type: SSELocationType
    stage_id: int
    bit: int
    can_create: Callable[["SSEWorld"], bool] = lambda world: True
    address: Optional[int] = None

location_data_table: Dict[str, SSELocationData] = {
    # Midair Stadium
    "Midair Stadium - Stadium Brawl": SSELocationData(
        0, "Midair Stadium", SSELocationType.BRAWL
    ),
    "Midair Stadium - Subspace Hoarde": SSELocationData(
        1, "Midair Stadium", SSELocationType.HOARDE
    ),
    "Midair Stadium - Petey Piranha": SSELocationData(
        2, "Midair Stadium", SSELocationType.BOSS
    ),
    "Newcomer (Kirby)": SSELocationData(
        3, "Midair Stadium", SSELocationType.NEWCMR
    ),
    "Newcomer (Rescued Princess)": SSELocationData(
        4, "Midair Stadium", SSELocationType.NEWCMR
    ),

    # Skyworld
    "Skyworld - Step 2 Golden Box": SSELocationData(
        5, "Skyworld", SSELocationType.GOLBOX
    ),
    "Newcomer (Pit)": SSELocationData(
        6, "Skyworld", SSELocationType.NEWCMR
    ),
    "Newcomer (Mario)": SSELocationData(
        7, "Skyworld", SSELocationType.NEWCMR
    ),

    # The Jungle
    "The Jungle - Step 1 Golden Box": SSELocationData(
        8, "The Jungle", SSELocationType.GOLBOX
    ),
    "The Jungle - Step 2 Freestanding Trophy": SSELocationData(
        9, "The Jungle", SSELocationType.PICKUP
    ),
    "The Jungle - Step 3 Freestanding Trophy": SSELocationData(
        10, "The Jungle", SSELocationType.PICKUP
    ),
    "The Jungle - Step 4a Golden Box": SSELocationData(
        11, "The Jungle", SSELocationType.GOLBOX
    ),
    "Newcomer (Diddy Kong)": SSELocationData(
        12, "The Jungle", SSELocationType.NEWCMR
    ),

    # The Plain
    "The Plain - Step 1 Golden Box": SSELocationData(
        13, "The Plain", SSELocationType.GOLBOX
    ),
    "The Plain - Step 1a Golden Box": SSELocationData(
        14, "The Plain", SSELocationType.GOLBOX
    ),

    # The Lake
    "The Lake - Rayquaza": SSELocationData(
        15, "The Lake", SSELocationType.BOSS
    ),
    "The Lake - Step 2 Golden Box": SSELocationData(
        16, "The Lake", SSELocationType.GOLBOX
    ),
    "The Lake - Step 5a Golden Box": SSELocationData(
        17, "The Lake", SSELocationType.GOLBOX
    ),
    "The Lake - Step 5 Golden Box": SSELocationData(
        18, "The Lake", SSELocationType.GOLBOX
    ),
    "The Lake - Dark Bowser Brawl": SSELocationData(
        19, "The Lake", SSELocationType.BRAWL
    ),
    "Newcomer (Fox)": SSELocationData(
        20, "The Lake", SSELocationType.NEWCMR
    ),

    # The Ruiend Zoo
    "The Ruined Zoo - Porky": SSELocationData(
        21, "The Ruined Zoo", SSELocationType.BOSS
    ),
    "The Ruined Zoo - Step 4 Golden Box": SSELocationData(
        22, "The Ruined Zoo", SSELocationType.GOLBOX
    ),
    "The Ruined Zoo - Step 5a Golden Box": SSELocationData(
        23, "The Ruined Zoo", SSELocationType.GOLBOX
    ),
    "Newcomer (Lucas)": SSELocationData(
        24, "The Ruined Zoo", SSELocationType.NEWCMR
    ),
    "Newcomer (Pokémon Trainer)": SSELocationData(
        25, "The Ruined Zoo", SSELocationType.NEWCMR
    ),

    # The Battlefield Fortress
    "The Battlefield Fortress - Step 1a Golden Box": SSELocationData(
        26, "The Battlefield Fortress", SSELocationType.GOLBOX
    ),
    "The Battlefield Fortress - Subspace Hoarde": SSELocationData(
        27, "The Battlefield Fortress", SSELocationType.HOARDE
    ),
    "The Battlefield Fortress - Step 4 Freestanding Trophy": SSELocationData(
        28, "The Battlefield Fortress", SSELocationType.PICKUP
    ),
    "The Battlefield Fortress - Step 5a Golden Box": SSELocationData(
        29, "The Battlefield Fortress", SSELocationType.GOLBOX
    ),
    "Newcomer (Marth)": SSELocationData(
        30, "The Battlefield Fortress", SSELocationType.NEWCMR
    ),
    "Newcomer (Meta Knight)": SSELocationData(
        31, "The Battlefield Fortress", SSELocationType.NEWCMR
    ),
    "Newcomer (Ike)": SSELocationData(
        32, "The Battlefield Fortress", SSELocationType.NEWCMR
    ),
    
    # The Forest
    "The Forest - Step 1a Golden Box": SSELocationData(
        33, "The Forest", SSELocationType.GOLBOX
    ),
    "The Forest - Step 2 Golden Box": SSELocationData(
        34, "The Forest", SSELocationType.GOLBOX
    ),
    "The Forest - Toon Link Brawl": SSELocationData(
        35, "The Forest", SSELocationType.SECRET
    ),
    "Newcomer (Link)": SSELocationData(
        36, "The Forest", SSELocationType.NEWCMR
    ),
    "Newcomer (Yoshi)": SSELocationData(
        37, "The Forest", SSELocationType.NEWCMR
    ),
    "Newcomer (Toon Link)": SSELocationData(
        38, "The Forest", SSELocationType.SECRET
    ),

    # The Research Facility I
    "The Research Facility I - Step 2 Golden Box": SSELocationData(
        39, "The Research Facility I", SSELocationType.GOLBOX
    ),
    "The Research Facility I - Step 5 Golden Box": SSELocationData(
        40, "The Research Facility I", SSELocationType.GOLBOX
    ),
    "Newcomer (Zero Suit Samus)": SSELocationData(
        41, "The Research Facility I", SSELocationType.NEWCMR
    ),
    "Newcomer (Pikachu)": SSELocationData(
        42, "The Research Facility I", SSELocationType.NEWCMR
    ),

    # The Lake Shore
    "The Lake Shore - Dark Princess Brawl": SSELocationData(
        43, "The Lake Shore", SSELocationType.BRAWL
    ),
    "The Lake Shore - Team Brawl": SSELocationData(
        44, "The Lake Shore", SSELocationType.BRAWL
    ),
    "The Lake Shore - Step 4 Golden Box": SSELocationData(
        45, "The Lake Shore", SSELocationType.GOLBOX
    ),
    "The Lake Shore - Step 5a Golden Box": SSELocationData(
        46, "The Lake Shore", SSELocationType.GOLBOX
    ),
    "The Lake Shore - Step 5b Golden Box": SSELocationData(
        47, "The Lake Shore", SSELocationType.GOLBOX
    ),
    "The Lake Shore - Step 5c Golden Box": SSELocationData(
        48, "The Lake Shore", SSELocationType.GOLBOX
    ),

    # The Path to the Ruins
    "The Path to the Ruins - Step 1a Freestanding Trophy Left": SSELocationData(
        49, "The Path to the Ruins", SSELocationType.PICKUP
    ),
    "The Path to the Ruins - Step 1a Freestanding Trophy Top": SSELocationData(
        50, "The Path to the Ruins", SSELocationType.PICKUP
    ),
    "The Path to the Ruins - Step 1a Freestanding Trophy Upright": SSELocationData(
        51, "The Path to the Ruins", SSELocationType.PICKUP
    ),
    "The Path to the Ruins - Step 1a Freestanding Trophy Far Right": SSELocationData(
        52, "The Path to the Ruins", SSELocationType.PICKUP
    ),
    "The Path to the Ruins - Step 1 Golden Box": SSELocationData(
        53, "The Path to the Ruins", SSELocationType.GOLBOX
    ),
    "The Path to the Ruins - Step 2 Golden Box": SSELocationData(
        54, "The Path to the Ruins", SSELocationType.GOLBOX
    ),
    "The Path to the Ruins - Wario Brawl": SSELocationData(
        55, "The Path to the Ruins", SSELocationType.BRAWL
    ),

    # The Cave
    "The Cave - Step 1a Golden Box": SSELocationData(
        56, "The Cave", SSELocationType.GOLBOX
    ),
    "The Cave - Step 1 Golden Box": SSELocationData(
        57, "The Cave", SSELocationType.GOLBOX
    ),
    "The Cave - Step 3a Golden Box": SSELocationData(
        58, "The Cave", SSELocationType.GOLBOX
    ),

    # The Ruins
    "The Ruins - Step 1 Freestanding Trophy": SSELocationData(
        59, "The Ruins", SSELocationType.PICKUP
    ),
    "The Ruins - Step 2 Golden Box": SSELocationData(
        60, "The Ruins", SSELocationType.GOLBOX
    ),
    "The Ruins - Step 3a Golden Box": SSELocationData(
        61, "The Ruins", SSELocationType.GOLBOX
    ),
    "The Ruins - Charizard Brawl": SSELocationData(
        62, "The Ruins", SSELocationType.BRAWL
    ),
    "The Ruins - Wolf Brawl": SSELocationData(
        63, "The Ruins", SSELocationType.SECRET
    ),
    "Newcomer (Wolf)": SSELocationData(
        64, "The Ruins", SSELocationType.SECRET
    ),

    # The Wilds I
    "The Wilds I - Step 1a Golden Box": SSELocationData(
        65, "The Wilds I", SSELocationType.GOLBOX
    ),
    "The Wilds I - Step 1 Golden Box": SSELocationData(
        66, "The Wilds I", SSELocationType.GOLBOX
    ),
    "The Wilds I - Step 2a Golden Box": SSELocationData(
        67, "The Wilds I", SSELocationType.GOLBOX
    ),
    # TODO - Galleom I can only be fought in story mode
    #"The Wilds I - Galleom I": SSELocationData(
    #    68, "The Wilds I", SSELocationType.BOSS
    #),

    # The Ruined Hall
    "The Ruined Hall - Galleom II": SSELocationData(
        69, "The Ruined Hall", SSELocationType.BOSS
    ),

    # The Wilds II
    "The Wilds II - Step 1 Freestanding Trophy": SSELocationData(
        70, "The Wilds II", SSELocationType.PICKUP
    ),
    "The Wilds II - Step 1a Golden Box": SSELocationData(
        71, "The Wilds II", SSELocationType.GOLBOX
    ),
    "The Wilds II - Step 2 Golden Box": SSELocationData(
        72, "The Wilds II", SSELocationType.GOLBOX
    ),

    # The Swamp
    "The Swamp - Step 1 Golden Box": SSELocationData(
        73, "The Swamp", SSELocationType.GOLBOX
    ),
    "The Swamp - Step 2a Golden Box": SSELocationData(
        74, "The Swamp", SSELocationType.GOLBOX
    ),
    "The Swamp - Giant Dark Diddy Kong Brawl": SSELocationData(
        75, "The Swamp", SSELocationType.BRAWL
    ),
    "The Swamp - Step 5 Golden Box": SSELocationData(
        76, "The Swamp", SSELocationType.GOLBOX
    ),
    "The Swamp - Step 5a Golden Box": SSELocationData(
        77, "The Swamp", SSELocationType.GOLBOX
    ),
    "The Swamp - Jigglypuff Brawl": SSELocationData(
        78, "The Swamp", SSELocationType.SECRET
    ),
    "Newcomer (Falco)": SSELocationData(
        79, "The Swamp", SSELocationType.NEWCMR
    ),
    "Newcomer (Jigglypuff)": SSELocationData(
        80, "The Swamp", SSELocationType.SECRET
    ),
    
    # The Research Facility II
    "The Research Facility II - Step 1a Golden Box": SSELocationData(
        81, "The Research Facility II", SSELocationType.GOLBOX
    ),
    "The Research Facility II - Dark Samus Duo Brawl": SSELocationData(
        82, "The Research Facility II", SSELocationType.BRAWL
    ),
    "The Research Facility II - Step 4 Freestanding Trophy": SSELocationData(
        83, "The Research Facility II", SSELocationType.PICKUP
    ),
    "The Research Facility II - Step 5a Golden Box": SSELocationData(
        84, "The Research Facility II", SSELocationType.GOLBOX
    ),
    "The Research Facility II - Step 6 Golden Box": SSELocationData(
        85, "The Research Facility II", SSELocationType.GOLBOX
    ),
    "The Research Facility II - Ridley": SSELocationData(
        86, "The Research Facility II", SSELocationType.BOSS
    ),
    "Newcomer (Samus)": SSELocationData(
        87, "The Research Facility II", SSELocationType.NEWCMR
    ),

    # Outside the Ancient Ruins
    "Outside the Ancient Ruins - Step 1a Freestanding Trophy": SSELocationData(
        88, "Outside the Ancient Ruins", SSELocationType.PICKUP
    ),
    "Outside the Ancient Ruins - Step 1b Golden Box Left": SSELocationData(
        89, "Outside the Ancient Ruins", SSELocationType.GOLBOX
    ),
    "Outside the Ancient Ruins - Step 1b Golden Box Right": SSELocationData(
        90, "Outside the Ancient Ruins", SSELocationType.GOLBOX
    ),
    "Outside the Ancient Ruins - Step 1b Freestanding Trophy": SSELocationData(
        91, "Outside the Ancient Ruins", SSELocationType.PICKUP
    ),
    "Outside the Ancient Ruins - Subspace Hoarde": SSELocationData(
        92, "Outside the Ancient Ruins", SSELocationType.HOARDE
    ),
    "Newcomer (Donkey Kong)": SSELocationData(
        93, "Outside the Ancient Ruins", SSELocationType.NEWCMR
    ),
    "Newcomer (Captain Falcon)": SSELocationData(
        94, "Outside the Ancient Ruins", SSELocationType.NEWCMR
    ),
    "Newcomer (Olimar)": SSELocationData(
        95, "Outside the Ancient Ruins", SSELocationType.NEWCMR
    ),

    # The Glacial Peak
    "The Glacial Peak - Step 2 Golden Box": SSELocationData(
        96, "The Glacial Peak", SSELocationType.GOLBOX
    ),
    "The Glacial Peak - Step 3a Golden Box": SSELocationData(
        97, "The Glacial Peak", SSELocationType.GOLBOX
    ),
    "The Glacial Peak - Step 3b Golden Box": SSELocationData(
        98, "The Glacial Peak", SSELocationType.GOLBOX
    ),
    "The Glacial Peak - Top of the Mountain Brawl": SSELocationData(
        99, "The Glacial Peak", SSELocationType.BRAWL
    ),
    "Newcomer (Ice Climbers)": SSELocationData(
        100, "The Glacial Peak", SSELocationType.NEWCMR
    ),
    "Newcomer (Lucario)": SSELocationData(
        101, "The Glacial Peak", SSELocationType.NEWCMR
    ),

    # The Canyon
    "The Canyon - Subspace Hoarde": SSELocationData(
        102, "The Canyon", SSELocationType.HOARDE
    ),

    # Battleship Halberd Interior
    "Battleship Halberd Interior - Step 2a Golden Box": SSELocationData(
        103, "Battleship Halberd Interior", SSELocationType.GOLBOX
    ),
    "Battleship Halberd Interior - Step 3a Golden Box": SSELocationData(
        104, "Battleship Halberd Interior", SSELocationType.GOLBOX
    ),
    "Battleship Halberd Interior - Step 3 Golden Box": SSELocationData(
        105, "Battleship Halberd Interior", SSELocationType.GOLBOX
    ),
    "Battleship Halberd Interior - Step 6 Golden Box": SSELocationData(
        106, "Battleship Halberd Interior", SSELocationType.GOLBOX
    ),
    "Battleship Halberd Interior - Dark Princess Duo Brawl": SSELocationData(
        107, "Battleship Halberd Interior", SSELocationType.BRAWL
    ),
    "Newcomer (Snake)": SSELocationData(
        108, "Battleship Halberd Interior", SSELocationType.NEWCMR
    ),

    # Battleship Halberd Exterior
    "Battleship Halberd Exterior - Step 2 Golden Box": SSELocationData(
        109, "Battleship Halberd Exterior", SSELocationType.GOLBOX
    ),
    "Battleship Halberd Exterior - Step 5 Golden Box": SSELocationData(
        110, "Battleship Halberd Exterior", SSELocationType.GOLBOX
    ),
    "Newcomer (Captured Princess)": SSELocationData(
        111, "Battleship Halberd Exterior", SSELocationType.NEWCMR
    ),

    # Battleship Halberd Bridge
    "Battleship Halberd Bridge - Duon": SSELocationData(
        112, "Battleship Halberd Bridge", SSELocationType.BOSS
    ),
    "Newcomer (Mr. Game & Watch)": SSELocationData(
        113, "Battleship Halberd Bridge", SSELocationType.NEWCMR
    ),

    # The Subspace Bomb Factory I
    "The Subspace Bomb Factory I - Step 1a Golden Box": SSELocationData(
        114, "The Subspace Bomb Factory I", SSELocationType.GOLBOX
    ),
    "The Subspace Bomb Factory I - Step 1c Golden Box": SSELocationData(
        115, "The Subspace Bomb Factory I", SSELocationType.GOLBOX
    ),

    # The Subspace Bomb Factory II
    "The Subspace Bomb Factory II - Step 1a Golden Box": SSELocationData(
        116, "The Subspace Bomb Factory II", SSELocationType.GOLBOX
    ),
    "The Subspace Bomb Factory II - Step 2a Golden Box": SSELocationData(
        117, "The Subspace Bomb Factory II", SSELocationType.GOLBOX
    ),
    "The Subspace Bomb Factory II - Step 3 Golden Box": SSELocationData(
        118, "The Subspace Bomb Factory II", SSELocationType.GOLBOX
    ),
    "The Subspace Bomb Factory II - Subspace Hoarde": SSELocationData(
        119, "The Subspace Bomb Factory II", SSELocationType.HOARDE
    ),
    "The Subspace Bomb Factory II - Step 6 Freestanding Trophy": SSELocationData(
        120, "The Subspace Bomb Factory II", SSELocationType.PICKUP
    ),
    "The Subspace Bomb Factory II - Meta Ridley": SSELocationData(
        121, "The Subspace Bomb Factory II", SSELocationType.BOSS
    ),
    "Newcomer (R.O.B.)": SSELocationData(
        122, "The Subspace Bomb Factory II", SSELocationType.NEWCMR
    ),

    #  Entrance to Subspace / Check of Legends
    "Entrance to Subspace - Step 1 Freestanding Trophy": SSELocationData(
        123, "Entrance to Subspace", SSELocationType.PICKUP
    ),

    # Subspace I
    "Subspace I - Step 1 Samus Trophy": SSELocationData(
        124, "Subspace I", SSELocationType.FTROPHY
    ),
    "Subspace I - Step 2a Pit Trophy": SSELocationData(
        125, "Subspace I", SSELocationType.FTROPHY
    ),
    "Subspace I - Step 2a Falco Trophy": SSELocationData(
        126, "Subspace I", SSELocationType.FTROPHY
    ),
    "Subspace I - Step 2a Golden Box": SSELocationData(
        127, "Subspace I", SSELocationType.GOLBOX
    ),
    "Subspace I - Step 2 Lucas Trophy": SSELocationData(
        128, "Subspace I", SSELocationType.FTROPHY
    ),
    "Subspace I - Step 3 Ike Trophy": SSELocationData(
        129, "Subspace I", SSELocationType.FTROPHY
    ),
    "Subspace I - Step 3a Pokémon Trainer Trophy": SSELocationData(
        130, "Subspace I", SSELocationType.FTROPHY
    ),
    "Subspace I - Step 3a Pikachu Trophy": SSELocationData(
        131, "Subspace I", SSELocationType.FTROPHY
    ),
    "Subspace I - Step 3 Donkey Kong Trophy": SSELocationData(
        132, "Subspace I", SSELocationType.FTROPHY
    ),
    "Subspace I - Step 3 Marth Trophy": SSELocationData(
        133, "Subspace I", SSELocationType.FTROPHY
    ),
    "Subspace I - Step 3b Olimar Trophy": SSELocationData(
        134, "Subspace I", SSELocationType.FTROPHY
    ),
    "Subspace I - Step 3b Fox Trophy": SSELocationData(
        135, "Subspace I", SSELocationType.FTROPHY
    ),
    "Subspace I - Step 4 Mr. Game & Watch Trophy": SSELocationData(
        136, "Subspace I", SSELocationType.FTROPHY
    ),
    "Subspace I - Step 5 Diddy Kong Trophy": SSELocationData(
        137, "Subspace I", SSELocationType.FTROPHY
    ),
    "Subspace I - Step 5 Captain Falcon Trophy": SSELocationData(
        138, "Subspace I", SSELocationType.FTROPHY
    ),
    "Subspace I - Step 6 Mario Trophy": SSELocationData(
        139, "Subspace I", SSELocationType.FTROPHY
    ),
    "Subspace I - Bowser Brawl": SSELocationData(
        140, "Subspace I", SSELocationType.BRAWL
    ),
    "Newcomer (Luigi)": SSELocationData(
        141, "Subspace I", SSELocationType.NEWCMR
    ),
    "Newcomer (Ness)": SSELocationData(
        142, "Subspace I", SSELocationType.NEWCMR
    ),
    "Newcomer (King Dedede)": SSELocationData(
        143, "Subspace I", SSELocationType.NEWCMR
    ),
    "Newcomer (Bowser)": SSELocationData(
        144, "Subspace I", SSELocationType.NEWCMR
    ),

    # Subspace II
    "Subspace II - Step 1 Peach Trophy": SSELocationData(
        145, "Subspace II", SSELocationType.FTROPHY
    ),
    "Subspace II - Step 1 Zelda Trophy": SSELocationData(
        146, "Subspace II", SSELocationType.FTROPHY
    ),
    "Subspace II - Step 1 Meta Knight Trophy": SSELocationData(
        147, "Subspace II", SSELocationType.FTROPHY
    ),
    "Subspace II - Step 1 Golden Box": SSELocationData(
        148, "Subspace II", SSELocationType.GOLBOX
    ),
    "Subspace II - Step 2 Link Trophy": SSELocationData(
        149, "Subspace II", SSELocationType.FTROPHY
    ),
    "Subspace II - Step 2 Yoshi Trophy": SSELocationData(
        150, "Subspace II", SSELocationType.FTROPHY
    ),
    "Subspace II - Step 2 Lucario Trophy": SSELocationData(
        151, "Subspace II", SSELocationType.FTROPHY
    ),
    "Subspace II - Step 2 R.O.B. Trophy": SSELocationData(
        152, "Subspace II", SSELocationType.FTROPHY
    ),
    "Subspace II - Step 3 Ice Climbers Trophy": SSELocationData(
        153, "Subspace II", SSELocationType.FTROPHY
    ),
    "Subspace II - Step 3 Golden Box": SSELocationData(
        154, "Subspace II", SSELocationType.GOLBOX
    ),
    "Subspace II - Step 3 Snake Trophy": SSELocationData(
        155, "Subspace II", SSELocationType.FTROPHY
    ),
    "Subspace II - Step 3 Wario Trophy": SSELocationData(
        156, "Subspace II", SSELocationType.FTROPHY
    ),
    "Newcomer (Ganondorf)": SSELocationData(
        157, "Subspace II", SSELocationType.NEWCMR
    ),
    "Newcomer (Wario)": SSELocationData(
        158, "Subspace II", SSELocationType.NEWCMR
    ),

    # The Great Maze NW
    "The Great Maze - Step 5b Golden Box (Skyworld Cache)": SSELocationData(
        159, "The Great Maze NW", SSELocationType.GOLBOX
    ),
    "The Great Maze - Step 5c Golden Box (Sea of Clouds)": SSELocationData(
        160, "The Great Maze NW", SSELocationType.GOLBOX
    ),
    "The Great Maze - Step 7a Golden Box (The Forest Dark World)": SSELocationData(
        161, "The Great Maze NW", SSELocationType.GOLBOX
    ),
    "The Great Maze - Step 7c Golden Box (The Plain)": SSELocationData(
        162, "The Great Maze NW", SSELocationType.GOLBOX
    ),

    # The Great Maze NE
    "The Great Maze - Step 9a Golden Box (The Ruined Zoo)": SSELocationData(
        163, "The Great Maze NE", SSELocationType.GOLBOX
    ),
    "The Great Maze - Step 13a Golden Box (Battleship Halberd Interior)": SSELocationData(
        164, "The Great Maze NE", SSELocationType.GOLBOX
    ),
    "The Great Maze - Step 21e Golden Box Lower (The Research Facility Mite Production)": SSELocationData(
        165, "The Great Maze NE", SSELocationType.GOLBOX
    ),
    "The Great Maze - Step 21e Golden Box Upper (The Research Facility Mite Production)": SSELocationData(
        166, "The Great Maze NE", SSELocationType.GOLBOX
    ),

    # The Great Maze SE
    "The Great Maze - Step 23b Golden Box (The Path to the Ruins Fire Cave)": SSELocationData(
        167, "The Great Maze SE", SSELocationType.GOLBOX
    ),
    "The Great Maze - Step 25a Golden Box (The Swamp Sping Platform)": SSELocationData(
        168, "The Great Maze SE", SSELocationType.GOLBOX
    ),
    "The Great Maze - Step 25b Golden Box (The Swamp Cache)": SSELocationData(
        169, "The Great Maze SE", SSELocationType.GOLBOX
    ),
    "The Great Maze - Step 25b Freestanding Trophy (The Swamp Cache)": SSELocationData(
        170, "The Great Maze SE", SSELocationType.PICKUP
    ),

    # The Great Maze SW
    "The Great Maze - Step 31c Freestanding Trophy (The Ruins)": SSELocationData(
        171, "The Great Maze SW", SSELocationType.PICKUP
    ),
    "The Great Maze - Step 33b Golden Box (The Path to the Ruins Windstorm)": SSELocationData(
        172, "The Great Maze SW", SSELocationType.GOLBOX
    ),
    
    # Victory
    "Tabuu": SSELocationData(
        173, "The Great Maze SW", SSELocationType.TABUU
    ),
    # lol
    "Newcomer (Sonic)": SSELocationData(
        174, "The Great Maze SW", SSELocationType.NEWCMR
    ),
}

location_table = {
    name: data.address for name, data in location_data_table.items() if data.address is not None
}