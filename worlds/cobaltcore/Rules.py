from BaseClasses import MultiWorld
from ..AutoWorld import LogicMixin
from ..generic.Rules import set_rule


class CobaltCoreLogic(LogicMixin):
    def _cobaltcore_has_artifacts(self, player: int, amount: int) -> bool:
        count: int = self.count("Artifact", player) + self.count("Boss Artifact", player)
        return count >= amount

    def _cobaltcore_has_cards(self, player: int, amount: int) -> bool:
        count = self.count("Card Draw", player) + self.count("Rare Card Draw", player)
        return count >= amount


def set_rules(world: MultiWorld, player: int):

    # Act 1 Card Draws
    set_rule(world.get_location("Card Draw 1", player), lambda state: True)
    set_rule(world.get_location("Card Draw 2", player), lambda state: True)
    set_rule(world.get_location("Card Draw 3", player), lambda state: state._cobaltcore_has_artifacts(player, 1))

    # Act 1 Artifacts
    set_rule(world.get_location("Artifact 1", player), lambda state: state._cobaltcore_has_cards(player, 1))
    set_rule(world.get_location("Artifact 2", player), lambda state: state._cobaltcore_has_cards(player, 2))

    # Act 1 Boss Event
    set_rule(world.get_location("Act 1 Boss", player), lambda state: state._cobaltcore_has_cards(player, 2) and state._cobaltcore_has_artifacts(player, 1))

    # Act 1 Boss Rewards
    set_rule(world.get_location("Rare Card Draw 1", player), lambda state: state.has("Beat Act 1 Boss", player))
    set_rule(world.get_location("Boss Artifact 1", player), lambda state: state.has("Beat Act 1 Boss", player))

    # Act 2 Card Draws
    set_rule(world.get_location("Card Draw 4", player), lambda state: state.has("Beat Act 1 Boss", player))
    set_rule(world.get_location("Card Draw 5", player), lambda state: state.has("Beat Act 1 Boss", player) and state._cobaltcore_has_artifacts(player, 2))
    set_rule(world.get_location("Card Draw 6", player), lambda state: state.has("Beat Act 1 Boss", player) and state._cobaltcore_has_cards(player, 3) and state._cobaltcore_has_artifacts(player, 3))

    # Act 2 Artifacts
    set_rule(world.get_location("Artifact 3", player), lambda state: state.has("Beat Act 1 Boss", player) and state._cobaltcore_has_cards(player, 3) and state._cobaltcore_has_artifacts(player, 2))
    set_rule(world.get_location("Artifact 4", player), lambda state: state.has("Beat Act 1 Boss", player) and state._cobaltcore_has_cards(player, 4) and state._cobaltcore_has_artifacts(player, 2))

    # Act 2 Boss Event
    set_rule(world.get_location("Act 2 Boss", player), lambda state: state.has("Beat Act 1 Boss", player) and state._cobaltcore_has_cards(player, 3) and state._cobaltcore_has_artifacts(player, 3) and state.has("Boss Artifact", player))

    # Act 2 Boss Rewards
    set_rule(world.get_location("Rare Card Draw 2", player), lambda state: state.has("Beat Act 2 Boss", player))
    set_rule(world.get_location("Boss Artifact 2", player), lambda state: state.has("Beat Act 2 Boss", player))

    # Act 3 Card Draws
    set_rule(world.get_location("Card Draw 7", player), lambda state: state.has("Beat Act 2 Boss", player))
    set_rule(world.get_location("Card Draw 8", player), lambda state: state.has("Beat Act 2 Boss", player))
    set_rule(world.get_location("Card Draw 9", player), lambda state: state.has("Beat Act 2 Boss", player) and state._cobaltcore_has_artifacts(player, 3))
    set_rule(world.get_location("Card Draw 10", player), lambda state: state.has("Beat Act 2 Boss", player) and state._cobaltcore_has_artifacts(player, 4))

    # Act 3 Artifacts
    set_rule(world.get_location("Artifact 5", player), lambda state: state.has("Beat Act 2 Boss", player) and state._cobaltcore_has_artifacts(player, 3))
    set_rule(world.get_location("Artifact 6", player), lambda state: state.has("Beat Act 2 Boss", player) and state._cobaltcore_has_artifacts(player, 4))
    set_rule(world.get_location("Artifact 7", player), lambda state: state.has("Beat Act 2 Boss", player) and state._cobaltcore_has_artifacts(player, 4))

    # Act 3 Boss Event
    set_rule(world.get_location("Act 3 Boss", player), lambda state: state.has("Beat Act 2 Boss", player) and state._cobaltcore_has_artifacts(player, 4) and state.has("Boss Artifact", player, 2))

    world.completion_condition[player] = lambda state: state.has("Victory", player)
