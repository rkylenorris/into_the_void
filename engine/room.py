
class Room:
    
    def __init__(self, name: str, description: str, items: list[str] = None, exits: dict[str, str] = None):
        self.name = name
        self.description = description
        self.items = items if items is not None else []
        self.exits = exits if exits is not None else {}
        pass