full_dot = '●'
empty_dot = '○'
def create_character(name, strength, intelligence, charisma):
    if type(name) != str:
        return "The character name should be a string"
    if name == "":
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"

    if type(strength) != int or type(intelligence) != int or type(charisma) != int:
        return "All stats should be integers"
    
    if strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"
        
    if strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"
        
    if (strength + intelligence + charisma) != 7:
        return "The character should start with 7 points"

    def get_bar(value):
        full = "●" * value
        empty = "○" * (10 - value)
        return f"{full}{empty}"

    return (f"{name}\n"
            f"STR {get_bar(strength)}\n"
            f"INT {get_bar(intelligence)}\n"
            f"CHA {get_bar(charisma)}")