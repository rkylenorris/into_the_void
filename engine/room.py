from enum import Enum

class DangerLevel(Enum):
    LOW=1
    MEDIUM=2
    HIGH=3


class Room:
    
    def __init__(self, id: int, name: str, theme: str, description: str, danger_level: DangerLevel, ritual_site: bool = False, special_features: list[str] = None, tone_tags: list[str] = None, items: list[str] = None, exits: dict[str, str] = None):
        self.id = id
        self.name = name
        self.theme = theme
        self.description = description
        self.ritual_site = ritual_site
        self.danger_level = danger_level
        self.special_features = special_features if special_features is not None else []
        self.tone_tags = tone_tags if tone_tags is not None else []
        self.items = items if items is not None else []
        self.exits = exits if exits is not None else {}
        