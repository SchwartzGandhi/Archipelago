from typing import Callable, TYPE_CHECKING

from BaseClasses import CollectionState

if TYPE_CHECKING:
    from . import SSEWorld

def get_stages_layout_rule(world: "SSEWorld", stage: str) -> Callable[[CollectionState], bool]:
    return lambda state: state.has(stage, world.player)

# TODO
# team_sky = ["Pit", "Mario"]
# team_forest = (state.has("Link", world.player), "Yoshi"]
# team_shore = team_sky + team_forest + "Kirby"

# team_facility = ["Zero Suit Samus", "Pikachu"]
# team_lake = ["Diddy Kong", ]
# team_fortress
# team_zoo
# team_halberd
# team_skiff
# team_factory
# team_canyon
def samus_aran(world: "SSEWorld") -> Callable[[CollectionState], bool]:
    if world.options.samus_behaviour.value == 0:
        return lambda state: state.has("Samus", world.player)
    if world.options.samus_behaviour.value == 1:
        return lambda state: state.has("Samus", world.player)
    if world.options.samus_behaviour.value == 2:
        return lambda state: state.has("Progressive Samus", world.player, 2)

def get_stadium_rule(world: "SSEWorld") -> Callable[[CollectionState], bool]:
    return lambda state: (
        state.has("Kirby", world.player)
        or state.has("Mario", world.player)
    )

def get_skyworld_rule(world: "SSEWorld") -> Callable[[CollectionState], bool]:
    return lambda state: state.has("Pit", world.player)

def get_cloud_sea_rule(world: "SSEWorld") -> Callable[[CollectionState], bool]:
    return lambda state: (
        state.has("Kirby", world.player) 
        and state.has("Princess", world.player)
    )

def get_jungle_rule(world: "SSEWorld") -> Callable[[CollectionState], bool]:
    return lambda state: (
        state.has("Donkey Kong", world.player)
        and state.has("Diddy Kong", world.player)
    )

def get_plain_rule(world: "SSEWorld") -> Callable[[CollectionState], bool]:
    return lambda state: (
        state.has("Mario", world.player)
        and state.has("Pit", world.player)
    )

def get_lake_rule(world: "SSEWorld") -> Callable[[CollectionState], bool]:
    return lambda state: (
        state.has("Fox", world.player)
        and state.has("Diddy Kong", world.player)
    )

def get_zoo_rule(world: "SSEWorld") -> Callable[[CollectionState], bool]:
    return lambda state: (
        state.has("Lucas", world.player)
    )

def get_fortress_rule(world: "SSEWorld") -> Callable[[CollectionState], bool]:
    return lambda state: (
        state.has("Marth", world.player)
    )

def get_forest_rule(world: "SSEWorld") -> Callable[[CollectionState], bool]:
    return lambda state: (
        state.has("Link", world.player)
        and state.has("Yoshi", world.player)
    )

def get_facility1_rule(world: "SSEWorld") -> Callable[[CollectionState], bool]:
    return lambda state: (
        state.has("Zero Suit Samus", world.player)
    )

def get_shore_rule(world: "SSEWorld") -> Callable[[CollectionState], bool]:
    return lambda state: (
        (
            state.has("Mario", world.player) and state.has("Pit", world.player)
        ) or (
            state.has("Link", world.player) and state.has("Yoshi", world.player)
        )
    )

def get_path_rule(world: "SSEWorld") -> Callable[[CollectionState], bool]:
    return lambda state: (
        state.has("Lucas", world.player)
        and state.has("Pokémon Trainer", world.player)
    )

def get_cave_rule(world: "SSEWorld") -> Callable[[CollectionState], bool]:
    return lambda state: (
        state.has("Pit", world.player)
        and state.has("Mario", world.player)
        and state.has("Link", world.player)
        and state.has("Yoshi", world.player)
        and state.has("Kirby", world.player)
    )

def get_ruins_rule(world: "SSEWorld") -> Callable[[CollectionState], bool]:
    return lambda state: (
        state.has("Lucas", world.player)
        and state.has("Pokémon Trainer", world.player)
    )

def get_wilds1_rule(world: "SSEWorld") -> Callable[[CollectionState], bool]:
    return lambda state: (
        state.has("Marth", world.player)
        and state.has("Meta Knight", world.player)
        and state.has("Ike", world.player)
    )

def get_hall_rule(world: "SSEWorld") -> Callable[[CollectionState], bool]:
    return lambda state: (
        state.has("Lucas", world.player)
        and state.has("Pokémon Trainer", world.player)
    )

def get_wilds2_rule(world: "SSEWorld") -> Callable[[CollectionState], bool]:
    return lambda state: (
        state.has("Pit", world.player)
        and state.has("Mario", world.player)
        and state.has("Link", world.player)
        and state.has("Yoshi", world.player)
        and state.has("Kirby", world.player)
    )

def get_facility2_rule(world: "SSEWorld") -> Callable[[CollectionState], bool]:
    return lambda state: (
        state.has("Zero Suit Samus", world.player)
        and state.has("Pikachu", world.player)
    )

def get_outside_rule(world: "SSEWorld") -> Callable[[CollectionState], bool]:
    return lambda state: (
        state.has("Olimar", world.player)
        and state.has("Captain Falcon", world.player)
    )

def get_glacier_rule(world: "SSEWorld") -> Callable[[CollectionState], bool]:
    return lambda state: (
        state.has("Meta Knight", world.player)
        and state.has("Ice Climbers", world.player)
    )

def get_canyon_rule(world: "SSEWorld") -> Callable[[CollectionState], bool]:
    return lambda state: (
        state.has("Pit", world.player)
        and state.has("Mario", world.player)
        and state.has("Link", world.player)
        and state.has("Yoshi", world.player)
        and state.has("Kirby", world.player)
    )

def get_halberd_int_rule(world: "SSEWorld") -> Callable[[CollectionState], bool]:
    return lambda state: (
        state.has("Snake", world.player)
    )

def get_halberd_ext_rule(world: "SSEWorld") -> Callable[[CollectionState], bool]:
    return lambda state: (
        state.has("Peach", world.player)
        and state.has("Sheik", world.player)
    )

def get_duon_rule(world: "SSEWorld") -> Callable[[CollectionState], bool]:
    return lambda state: (
        state.has("Snake", world.player)
        and state.has("Lucario", world.player)
        and state.has("Peach", world.player)
        and state.has("Sheik", world.player)
        and state.has("Fox", world.player)
        and state.has("Falco", world.player)
    )

def get_factory1_rule(world: "SSEWorld") -> Callable[[CollectionState], bool]:
    return lambda state: (
        state.has("Samus", world.player)
        and state.has("Pikachu", world.player)
    )

def get_factory2_rule(world: "SSEWorld") -> Callable[[CollectionState], bool]:
    return lambda state: (
        state.has("Diddy Kong", world.player)
        and state.has("Donkey Kong", world.player)
        and state.has("Olimar", world.player)
        and state.has("Captain Falcon", world.player)
    )

def get_entrance_rule(world: "SSEWorld") -> Callable[[CollectionState], bool]:
    return lambda state: (
        state.has("Pit", world.player)
        and state.has("Mario", world.player)
        and state.has("Link", world.player)
        and state.has("Yoshi", world.player)
        and state.has("Kirby", world.player)
        and state.has("Marth", world.player)
        and state.has("Meta Knight", world.player)
        and state.has("Ike", world.player)
        and state.has("Lucas", world.player)
        and state.has("Pokémon Trainer", world.player)
        and state.has("Ice Climbers", world.player)

        and state.has("Samus", world.player)
        and state.has("Pikachu", world.player)
        and state.has("Diddy Kong", world.player)
        and state.has("Donkey Kong", world.player)
        and state.has("Olimar", world.player)
        and state.has("Captain Falcon", world.player)
        and state.has("R.O.B.", world.player)

        and state.has("Snake", world.player)
        and state.has("Lucario", world.player)
        and state.has("Peach", world.player)
        and state.has("Zelda", world.player)
        and state.has("Fox", world.player)
        and state.has("Falco", world.player)
        and state.has("Meta Knight", world.player)
        and state.has("Mr. Game & Watch", world.player)
    )

def get_subspace1_rule(world: "SSEWorld") -> Callable[[CollectionState], bool]:
    return lambda state: (
        state.has("Luigi", world.player)
        and state.has("Ness", world.player)
        and state.has("King Dedede", world.player)
    )

def get_subspace2_rule(world: "SSEWorld") -> Callable[[CollectionState], bool]:
    return lambda state: (
        state.has("Kirby", world.player)
    )

def get_maze_rule(world: "SSEWorld") -> Callable[[CollectionState], bool]:
    return lambda state: (
        state.has("Luigi", world.player)
        and state.has("Ness", world.player)
        and state.has("King Dedede", world.player)
        and state.has("Kirby", world.player)
        and state.has("Bowser", world.player)
    )

characters_layout_rules = [
    get_stadium_rule,
    get_skyworld_rule,
    get_cloud_sea_rule,
    get_jungle_rule,
    get_plain_rule,
    get_lake_rule,
    get_zoo_rule,
    get_fortress_rule,
    get_forest_rule,
    get_facility1_rule,
    get_shore_rule,
    get_path_rule,
    get_cave_rule,
    get_ruins_rule,
    get_wilds1_rule,
    get_hall_rule,
    get_wilds2_rule,
    get_facility2_rule,
    get_outside_rule,
    get_glacier_rule,
    get_canyon_rule,
    get_halberd_int_rule,
    get_halberd_ext_rule,
    get_duon_rule,
    get_factory1_rule,
    get_factory2_rule,
    get_entrance_rule,
    get_subspace1_rule,
    get_subspace2_rule,
    get_maze_rule,
]