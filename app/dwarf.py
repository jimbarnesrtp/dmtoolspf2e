import string
from ancestry import AncestryLanguage
#dwarf Patterns
#Dwarven names usually contain hard consonants and are rarely more or fewer than two syllables

#Agna, Bodill, Dolgrin, Edrukk, Grunyar, Ingra, Kazmuk, Kotri, Lupp, Morgrym, Rogar, Rusilka, Torra, Yangrit

# First syllable

# VC, CV, CVC, VCC, CCV, CCVC, YVC, CYC

# Second Syllable

# CV, CVC+, CCVC, CVC, CCV, CC, YVC

# Third Syllable .07%
# CV


VOWELS = "aeiou"
CONSONANTS = "".join(set(string.ascii_lowercase) - set(VOWELS))

class DwarfLanguuage(AncestryLanguage)

    def generate_name(self):
        

