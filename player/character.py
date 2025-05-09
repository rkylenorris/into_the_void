from .psyche import Psyche

class PlayerCharacter:
    def __init__(self, name: str, psyche: Psyche, avatar: str, abilities: list):
        self.name = name
        self.psyche = psyche
        self.avatar = avatar
        self.abilities = abilities
        self.tarot_collection = []
        
    def _create_void_journal(self):
        pass
    
    def _create_toolkit(self):
        pass
    