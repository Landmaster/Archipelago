import typing

from BaseClasses import Item
from typing import Dict


class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    progression: bool
    event: bool = False


item_table: Dict[str, ItemData] = {
    'Card Draw': ItemData(250500, True),
    'Rare Card Draw': ItemData(250501, True),
    'Artifact': ItemData(250502, True),
    'Boss Artifact': ItemData(250503, True),

    # Event Items
    'Beat Act 1 Boss': ItemData(None, True, True),
    'Beat Act 2 Boss': ItemData(None, True, True),
    'Victory': ItemData(None, True, True),

}

item_pool: Dict[str, int] = {
    'Card Draw': 10,
    'Rare Card Draw': 2,
    'Artifact': 7,
    'Boss Artifact': 2
}

event_item_pairs: Dict[str, str] = {
    "Act 1 Boss": "Beat Act 1 Boss",
    "Act 2 Boss": "Beat Act 2 Boss",
    "Act 3 Boss": "Victory"
}
