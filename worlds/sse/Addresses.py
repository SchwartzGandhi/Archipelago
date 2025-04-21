class SSEAddresses():
    # This byte increments every time the player collects a Trophy, Sticker, or CD
    # and resets every time the player leaves the level.
    SSE_COLLECT_ITEM = 0x8049ED4F

    # These words tell what room the player is in.
    SSE_LOCATION_DATA = 0x815CBC4C, 0x815CBBE8

    # The first byte of the room address correlates to the level the player is in.
    # Outside the Ancient Ruins is an exception where the Skiff Hoarde Brawl at the end is a different value.
    SSE_MIDAIR_STADIUM = "03"
    SSE_SKYWORLD = "04"
    SSE_SEA_OF_CLOUDS = "05"
    SSE_THE_JUNGLE = "06"
    SSE_THE_PLAIN = "07"
    SSE_THE_LAKE = "08"
    SSE_THE_RUINED_ZOO = "09"
    SSE_THE_BATTLEFIELD_FORTRESS = "10"
    SSE_THE_FOREST = "12"
    SSE_THE_RESEARCH_FACILITY_ONE = "14"
    SSE_THE_LAKE_SHORE = "16"
    SSE_THE_PATH_TO_THE_RUINS = "18"
    SSE_THE_CAVE = "20"
    SSE_THE_RUINS = "22"
    SSE_THE_WILDS_ONE = "24"
    SSE_THE_RUINED_HALL = "25"
    SSE_THE_WILDS_TWO = "26"
    SSE_THE_SWAMP = "27"
    SSE_THE_RESEARCH_FACILITY_TWO = "28"
    SSE_OUTSIDE_THE_ANCIENT_RUINS = "29"
    SSE_OUTSIDE_THE_ANCIENT_RUINS_SKIFF = "30"
    SSE_THE_GLACIAL_PEAK = "31"
    SSE_THE_CANYON = "32"
    SSE_BATTLESHIP_HALBERD_INTERIOR = "33"
    SSE_BATTLESHIP_HALBERD_EXTERIOR = "34"
    SSE_BATTLESHIP_HALBERD_BRIDGE = "35"
    SSE_THE_SUBSPACE_BOMB_FACTORY_ONE = "36"
    SSE_THE_SUBSPACE_BOMB_FACTORY_TWO = "37"
    SSE_ENTRANCE_TO_SUBSPACE = "39"
    SSE_SUBSPACE_ONE = "40"
    SSE_SUBSPACE_TWO = "41"
    SSE_THE_GREAT_MAZE = "42"