from enum import Enum

MAX_PRESENCE = 50
MIN_PRESENCE = -50



    
class Conflict:
    def __init__(self, aspect: str, opposes: str, name:str, description: str, strength: float) -> None:
        self.aspect_name = aspect
        self.opposes = opposes
        self.name = name
        self.description = description
        self.strength = strength
        

class ThresholdEventType(Enum):
    WHISPER = (10, "A subtle inner shift. Fleeting, but meaningful.")
    ECHO = (25, "A memory resurfaces. Something forgotten stirs.")
    TREMOR = (40, "Emotional disturbance disrupts the surface.")
    SURFACING = (55, "A repressed trait begins to manifest.")
    RECKONING = (70, "The aspect demands action. Choices begin to reflect it.")
    UNMASKING = (85, "A crisis or transformation point is reached.")
    AWAKENING = (100, "Full emergence. A new part of you takes shape.")
    
    SHADOW_WHISPER = (-10, "Something stirs beneath. You try to ignore it.")
    FRACTURE = (-25, "You react poorly, blaming others or withdrawing.")
    MIRROR_CRACK = (-40, "A twisted version of the self begins to show.")
    DESCENT = (-55, "You spiral into projection or repression.")
    BREAK = (-70, "A distorted belief takes root.")
    DISSOCIATION = (-85, "Reality blurs. You lose grip on your center.")
    SHADOW_POSSESSION = (-100, "The aspect consumes you. You act not as yourself.")
    
    def __new__(cls, threshold, description):
        obj = object.__new__(cls)
        obj._value_ = threshold
        obj._description_ = description
        return obj
    
    @property
    def description(self):
        return self._description_
    
    @property
    def threshold(self):
        return self._value_

        
class ThresholdEvent:
    def __init__(self, name: str, effect: str, type: ThresholdEventType) -> None:
        self.name = name
        self.effect = effect
        self.type = type
        
        
class Threshold:
    def __init__(self, aspect: str, value: int, event: ThresholdEvent) -> None:
        self.aspect = aspect
        self.value = value
        self.event = event
        
    @property
    def polarity(self):
        if self.value > 0:
            return "positive"
        elif self.value < 0:
            return "negative"
        return "neutral"
        
        
class Aspect:
    def __init__(self, name: str, ascending_name: str, descending_name:str, description: str, visible: bool, conflicts: list[Conflict] = None, thresholds: list[Threshold] = None) -> None:
        self.name = name
        self.ascending_name = ascending_name
        self.descending_name = descending_name
        self.display_name = name
        self.description = description
        self.presence = 0
        self._max_presence = MAX_PRESENCE
        self._min_presence = MIN_PRESENCE
        self._visible = visible
        self.conflicts = conflicts if conflicts is not None else []
        self.thresholds = thresholds if thresholds is not None else []
        
    def alter_display_name(self):
        if self.polarity == "positive":
            self.display_name = self.ascending_name
        elif self.polarity == "negative":
            self.display_name = self.descending_name
        else:
            self.display_name = self.name
    
    @property    
    def polarity(self) -> str:
        if self.presence > 0:
            return "positive"
        elif self.presence < 0:
            return "negative"
        else:
            return "neutral"

    def __repr__(self):
        return f"Aspect(name={self.name}, description={self.description})"
    
class Psyche:
    def __init__(self, aspects: list[Aspect]):
        if len(aspects) != 7:
            raise ValueError("Psyche must have exactly 7 aspects.")
        self.ego = next((a for a in aspects if a.name == "The Mask"))
        self.id = next((a for a in aspects if a.name == "The Flame"))
        self.superego = next((a for a in aspects if a.name == "The Chain"))
        self.shadow = next((a for a in aspects if a.name == "That Which Remains"))
        self.anima = next((a for a in aspects if a.name == "The Mirror"))
        self.persona = next((a for a in aspects if a.name == "The Veil"))
        self.the_self = next((a for a in aspects if a.name == "The One Who Remembers"))
        