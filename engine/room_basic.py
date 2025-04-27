from string import Template

class Room:
    
    _intro_template_ = Template("You enter $name, a place suffused with the essence of $theme.")
    
    def __init__(self, room_id: int, name: str, 
                theme: str, exits: list[str] = None,
                items: list[str] = None):
        self.id = room_id
        self.name = name
        self.theme = theme
        self.exits = exits if exits is not None else []
        self.items = items if items is not None else []
        self.intro = self.generate_intro()
        
    def generate_intro(self):
        return self._intro_template_.substitute({"name": self.name, "theme": self.theme})
    
    def generate_description(self):
        pass
    
    def add_exit(self, room_id):
        self.exits.append(room_id)
    
    def __repr__(self):
        return f"Room(id={self.id}, name={self.name}, theme={self.theme})"
    

class Item:
    
    _description_template_ = Template("$a_or_an $adj $noun, tied to the essence of $theme")
    _reference_template_ = Template("$a_or_an $adj $noun")
    
    def __init__(self, item_id: int, name: str, theme: str,
                 adjective: str, noun: str):
        self.id = item_id
        self.name = name
        self.theme = theme
        self.adjective = adjective
        self.noun = noun
        self.description = self.generate_description()
        
    def generate_description(self):
        return self._description_template_.substitute({
            "a_or_an": "An" if self.adjective[0].lower() in "aeiou" else "A",
            "adj": self.adjective,
            "noun": self.noun,
            "theme": self.theme
        })
    
    def generate_reference(self):
         return self._reference_template_.substitute({
             "a_or_an": "an" if self.adjective[0].lower() in "aeiou" else "a",
             "adj": self.adjective,
             "noun": self.noun
         })
    
    def __repr__(self):
        return f"Item(id={self.id}, name={self.name})"