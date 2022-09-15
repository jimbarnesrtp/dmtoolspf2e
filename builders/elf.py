import string
from builders.ancestry import AncestryLanguage


# An elf keeps their personal name secret among their family, while giving a nickname when meeting other people. This nickname can change over time, 
# due to events in the elf’s life or even on a whim. A single elf might be known by many names by associates of different ages and regions.
# Elven names consist of multiple syllables and are meant to flow lyrically—at least in the Elven tongue. They so commonly end 
# in “-el” or “-ara” that other cultures sometimes avoid names ending in these syllables to avoid sounding too elven.

VOWELS = "aeiou"
CONSONANTS = "".join(set(string.ascii_lowercase) - set(VOWELS))


class ElfLanguage(AncestryLanguage):
    
    def generate_name(self):
        print("test")
        return "test"
    
    def save_name(self, name):
        print("save_name")