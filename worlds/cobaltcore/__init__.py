import string

from BaseClasses import Entrance, Item, ItemClassification, Location, MultiWorld, Region, Tutorial
from .Items import event_item_pairs, item_pool, item_table
from .Locations import location_table
from .Options import spire_options
from .Regions import create_regions
from .Rules import set_rules
from ..AutoWorld import WebWorld, World


class CobaltCoreWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Cobalt Core for Archipelago. "
        "This guide covers single-player, multiworld, and related software.",
        "English",
        "cobalt-core_en.md",
        "cobalt-core/en",
        ["Landmaster"]
    )]


class CobaltCoreWorld(World):
    """
    A sci-fi roguelike deckbuilder with a deep new single-axis spin on tactics games! Dodge missiles,
    line up your cannons, and blast 'em out of the sky... Then get to the bottom of these time loops,
    before it's too late!
    """

    option_definitions = spire_options
    game = "Cobalt Core"
    topology_present = False
    data_version = 2
    web = CobaltCoreWeb()
    required_client_version = (0, 3, 7)

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = location_table

    def create_items(self):
        # Fill out our pool with our items from item_pool, assuming 1 item if not present in item_pool
        pool = []
        for name, data in item_table.items():
            if not data.event:
                for amount in range(item_pool.get(name, 1)):
                    item = CobaltCoreItem(name, self.player)
                    pool.append(item)

        self.multiworld.itempool += pool

        # Pair up our event locations with our event items
        for event, item in event_item_pairs.items():
            event_item = CobaltCoreItem(item, self.player)
            self.multiworld.get_location(event, self.player).place_locked_item(event_item)

    def set_rules(self):
        set_rules(self.multiworld, self.player)

    def create_item(self, name: str) -> Item:
        return CobaltCoreItem(name, self.player)

    def create_regions(self):
        create_regions(self.multiworld, self.player)

    def fill_slot_data(self) -> dict:
        slot_data = {
            'seed': "".join(self.multiworld.per_slot_randoms[self.player].choice(string.ascii_letters) for i in range(16))
        }
        for option_name in spire_options:
            option = getattr(self.multiworld, option_name)[self.player]
            slot_data[option_name] = option.value
        return slot_data

    def get_filler_item_name(self) -> str:
        return self.multiworld.random.choice(["Card Draw", "Card Draw", "Card Draw", "Artifact", "Artifact"])


def create_region(world: MultiWorld, player: int, name: str, locations=None, exits=None):
    ret = Region(name, player, world)
    if locations:
        for location in locations:
            loc_id = location_table.get(location, 0)
            location = CobaltCoreLocation(player, location, loc_id, ret)
            ret.locations.append(location)
    if exits:
        for exit in exits:
            ret.exits.append(Entrance(player, exit, ret))

    return ret


class CobaltCoreLocation(Location):
    game: str = "Cobalt Core"

    def __init__(self, player: int, name: str, address=None, parent=None):
        super(CobaltCoreLocation, self).__init__(player, name, address, parent)
        if address is None:
            self.event = True
            self.locked = True


class CobaltCoreItem(Item):
    game = "Cobalt Core"

    def __init__(self, name, player: int = None):
        item_data = item_table[name]
        super(CobaltCoreItem, self).__init__(
            name,
            ItemClassification.progression if item_data.progression else ItemClassification.filler,
            item_data.code, player
        )
