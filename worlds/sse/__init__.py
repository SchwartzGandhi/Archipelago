"""
Archipelago init file for The Subspace Emissary
"""
import random
from typing import Dict, Any, List
import os

from BaseClasses import Region, ItemClassification
from worlds.AutoWorld import WebWorld, World
from worlds.LauncherComponents import Component, components, launch_subprocess
from .Items import SSEItem, item_table, item_data_table
from .Locations import location_data_table, SSELocation, location_table
from .Options import SSEOptions
from .Regions import region_data_table, _stage_names, SSERegionData
from .Rules import get_stages_layout_rule, characters_layout_rules


class SSEWebWorld(WebWorld):
    theme = "ocean"


class SSEWorld(World):
    """
    The Adventure mode campaign of Super Smash Bros. Brawl, Nintendo characters from all over come together to destroy the looming threat of subspace.
    """
    game = "Super Smash Bros. Brawl: The Subspace Emissary"
    web = SSEWebWorld()

    data_version = 1

    options_dataclass = SSEOptions
    options: SSEOptions

    item_name_to_id = item_table
    location_name_to_id = location_table

    def generate_early(self):
        #TODO: start with 4 random fighters and 1 stage, if applicable
        """"""

    def create_regions(self):
        # Add the stages to region data table
        for stage in _stage_names:
            region_data_table.update({stage: SSERegionData()})

        # Create regions
        for region_name in region_data_table.keys():
            region = Region(region_name, self.player, self.multiworld)
            self.multiworld.regions.append(region)
        
        # Create locations
        for region_name, region_data in region_data_table.items():
            region = self.get_region(region_name)
            region.add_locations({
                location_name: location_data.address for location_name, location_data in location_data_table.items()
                if location_data.region == region_name and location_data.can_create(self)
            }, SSELocation)
            region.add_exits(region_data_table[region_name].connecting_regions)

    def create_item(self, name: str):
        return SSEItem(name, item_data_table[name].type, item_data_table[name], self.player)

    def create_items(self) -> None:
        item_pool: List[SSEItem] = []

        for name, item in item_data_table.items():
            item_pool.append(self.create_item(name))

        self.multiworld.itempool += item_pool

    def get_filler_item_name(self) -> str:
        return "Sticker"

    def set_rules(self):
        if self.options.layout_mode.value == 0:
            for i, stage in enumerate(_stage_names):
                self.get_location(stage).access_rule = characters_layout_rules[i]
        elif self.options.layout_mode.value == 1:
            for stage in _stage_names:
                self.get_location(stage).access_rule = get_stages_layout_rule(self, stage)
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)

    def fill_slot_data(self) -> Dict[str, Any]:
        return {
            "layout_mode": self.options.layout_mode.value,
            #"trainer_behaviour": self.options.trainer_behaviour.value,
            #"samus_behaviour": self.options.samus_behaviour.value,
            #"zelda_behaviour": self.options.zelda_behaviour.value,
            "secret_character_shuffle": self.options.secret_character_shuffle.value,
            "hoarde_shuffle": self.options.hoarde_shuffle.value,
            "great_maze_requirements": self.options.great_maze_requirements.value,
            "maze_fighter_percentage": self.options.maze_fighter_percentage.value,
            "tabuu_requirements": self.options.tabuu_requirements.value,
            "tabuu_fighter_percentage": self.options.tabuu_fighter_percentage.value,
            "tabuu_boss_amount": self.options.tabuu_boss_amount.value,
        }


def launch_client():
    from .SSEClient import main
    launch_subprocess(main, name="SSE Client")


def add_client_to_launcher() -> None:
    version = "0.2.0"
    found = False
    for c in components:
        if c.display_name == "Subspace Emissary Client":
            found = True
            if getattr(c, "version", 0) < version:
                c.version = version
                c.func = launch_client
                return
    if not found:
        components.append(
            Component("Subspace Emissary Client", "SSEClient", func=launch_client)
        )


add_client_to_launcher()
