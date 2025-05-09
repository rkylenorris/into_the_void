from .room import Room
from random import choice, choices

class Theme:
    def __init__(self, name: str, core_concepts: list[str] = None,
                 room_types: list[str]  = None, adjectives: list[str] = None,
                 items: list[str] = None, actions: list[str] = None,
                 ambient_details: list[str] = None, motifs: list[str] = None,
                 tones: list[str] = None) -> None:
        self.name = name
        self.core_concepts = core_concepts if core_concepts is not None else []
        self.room_types = room_types if room_types is not None else []
        self.adjectives = adjectives if adjectives is not None else []
        self.items = items if items is not None else []
        self.actions = actions if actions is not None else []
        self.ambient_details = ambient_details if ambient_details is not None else []
        self.motifs = motifs if motifs is not None else []
        self.tones = tones if tones is not None else []
        
    def generate_room(self) -> Room:
        room_name = self._name_room()
        items = self._get_items(num=2)
        description = self._describe_room(items=items)
    
    
    def _name_room(self) -> str:
        # get room type and remove from list
        room_type = choice(self.room_types)
        room_index = 3 if room_type.startswith('An ') else 2
        self.room_types.remove(room_type)
        
        # get adjective and remove from list
        adjective = self._get_adjective()
        
        # create room name
        room_name = f"The {adjective} {room_type[room_index:]}".title()
        
        return room_name


    def _get_adjective(self) -> str:
        adjective = choice(self.adjectives)
        self.adjectives.remove(adjective)
        return adjective
    
    
    def _get_items(self, num: int = 2) -> list[str]:
        items = choices(self.items, k=num)
        for item in items:
            self.items.remove(item)
        return items
    
    def _describe_room(self, items: list[str]) -> str:
        concept = choice(self.core_concepts)
        self.core_concepts.remove(concept)
        
        adjective = self._get_adjective()
        
        detail = choice(self.ambient_details)
        self.ambient_details.remove(detail)
            
        items_seen = f"You can make out " + ", ".join(items[:-1]) + f", and {items[-1]}"
        
        description = f"The room feels {adjective} and of {concept}. {detail} {items_seen}"
        
        