def create_regions(world, player: int):
    from . import create_region
    from .Locations import location_table

    world.regions += [
        create_region(world, player, 'Menu', None, ['Starting Bonus']),
        create_region(world, player, 'Sectors', [location for location in location_table])
    ]

    # link up our region with the entrance we just made
    world.get_entrance('Starting Bonus', player).connect(world.get_region('Sectors', player))
