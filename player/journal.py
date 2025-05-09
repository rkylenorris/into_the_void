from dataclasses import dataclass
from enum import Enum


class ReadingTypes(Enum):
    SINGLE_CARD = 1
    TRIPLE_CARD = 2


@dataclass
class TarotCard:
    name: str
    suit: str
    art_path: str
    description: str
    meanings: list[str]



@dataclass
class TarotReading:
    cards: list[TarotCard]
    type: ReadingTypes
    reflection: str
        

@dataclass
class GroundingTechnique:
    name: str
    description: str
    steps: list[str]


class VoidJournal:
    def __init__(self, character_id: int):
        self.character_id = character_id
        self.entries: list[str] = []
        self.tarot_readings: list[TarotReading] = []
        self.grounding_techniques: list[GroundingTechnique] = []
        self.key_npcs = []
        self.rituals = []
        
    