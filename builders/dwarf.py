import string
from builders.ancestry import AncestryLanguage


#dwarf Patterns
#Dwarven names usually contain hard consonants and are rarely more or fewer than two syllables

#Agna, Bodill, Dolgrin, Edrukk, Grunyar, Ingra, Kazmuk, Kotri, Lupp, Morgrym, Rogar, Rusilka, Torra, Yangrit


VOWELS = "aeiou"
CONSONANTS = "".join(set(string.ascii_lowercase) - set(VOWELS))

class DwarfLanguage(AncestryLanguage):
    
    first_syllable = ["VC", "CV", "CVC", "VCC", "CCV", "CCVC", "YVC", "CYC"]
    second_syllable = ["CV", "CVC+", "CCVC", "CVC", "CCV", "CC", "YVC"]
    third_syllable = ["CV"]

    def generate_name(self):
        print("test")
        return "test"
    
    def save_name(self, name):
        print("save_name")