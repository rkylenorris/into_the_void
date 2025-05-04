from .room import Room
from random import choice

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
    
    def _name_room(self) -> str:
        # get room type and remove from list
        room_type = choice(self.room_types)
        self.room_types.remove(room_type)
        
        # get adjective and remove from list
        adjective = self._get_adjective()
        
        # create room name
        room_name = f"The {adjective} {room_type[2:]}".title()
        
        return room_name

    def _get_adjective(self) -> str:
        adjective = choice(self.adjectives)
        self.adjectives.remove(adjective)
        return adjective
    
    def _describe_room(self) -> str:
        concept = choice(self.core_concepts)
        self.core_concepts.remove(concept)
        
        adjective = self._get_adjective()
        
        