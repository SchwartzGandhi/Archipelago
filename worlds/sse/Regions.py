from typing import Dict, List, NamedTuple

_stage_names = [
    "The Midair Stadium",
    "Skyworld",
    "Sea of Clouds",
    "The Jungle",
    "The Plain",
    "The Lake",
    "The Ruined Zoo",
    "The Battlefield Fortress",
    "The Forest",
    "The Research Facility I",
    "The Lake Shore",
    "The Path to the Ruins",
    "The Cave",
    "The Ruins",
    "The Wilds I",
    "The Ruined Hall",
    "The Wilds II",
    "The Swamp",
    "The Research Facility II",
    "Outside the Ancient Ruins",
    "The Glacial Peak",
    "The Canyon",
    "Battleship Halberd Interior",
    "Battleship Halberd Exterior",
    "Battleship Halberd Bridge",
    "The Subspace Bomb Factory I",
    "The Subspace Bomb Factory II",
    "Entrance to Subspace",
    "Subspace I",
    "Subspace II",
    "The Great Maze",
    "The Great Maze NW",
    "The Great Maze NE",
    "The Great Maze SE",
    "The Great Maze SW",
]

class SSERegionData(NamedTuple):
    connecting_regions: List[str] = []


region_data_table: Dict[str, SSERegionData] = {
    "Menu": SSERegionData(
        [
            stage for stage in _stage_names
        ]
    ),
}
