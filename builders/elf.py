import string
from builders.ancestry import AncestryLanguage
from builders.languagehelper import LanguageHelper

# An elf keeps their personal name secret among their family, while giving a nickname when meeting other people. This nickname can change over time, 
# due to events in the elf’s life or even on a whim. A single elf might be known by many names by associates of different ages and regions.
# Elven names consist of multiple syllables and are meant to flow lyrically—at least in the Elven tongue. They so commonly end 
# in “-el” or “-ara” that other cultures sometimes avoid names ending in these syllables to avoid sounding too elven.

#Aer el,, , Dardl ara,  , Jath al, , Opar al, , Soumr al, , Tess ara, Vari el, , 
# Am runel ara, Cal adr el, Held al el, Tal ath el, Yal and lara
#Lan liss , Seld lon, Zord lon, Faun ra,
class ElfLanguage(AncestryLanguage):
    
    first_syllable = ["VVC", "VC", "CVC", "CVCCC", "CVCC", "CVVC", "CVCCC", "VCV", "VCC", "VCVC", "CVCV"]
    second_syllable = ["CVC", "CVCV", "CVCVC", "VC", "CV", "VC", "CVCC", "VCC", "VCV", "VVC"]
    other_last = ["el", "ara", "al"]
    lang_helper = None
    
    #7/16 = one and other last, 
    #5/16 2 and third
    #4/16 2 syllabels
    
    
    def generate_name(self):
        print("test")
        return "test"
    
    def save_name(self, name):
        print("save_name")