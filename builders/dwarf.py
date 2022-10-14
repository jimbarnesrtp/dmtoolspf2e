from builders.ancestry import AncestryLanguage
import random
from builders.languagehelper import LanguageHelper


#dwarf Patterns
#Dwarven names usually contain hard consonants and are rarely more or fewer than two syllables

#Agna, Bodill, Dolgrin, Edrukk, Grunyar, Ingra, Kazmuk, Kotri, Lupp, Morgrym, Rogar, Rusilka, Torra, Yangrit


class DwarfLanguage(AncestryLanguage):
    
    first_syllable = ["VC", "CV", "CVC", "VCC", "CCV", "CCVC", "YVC", "CYC"]
    second_syllable = ["CV", "CVC+", "CCVC", "CVC", "CCV", "CC", "YVC"]
    third_syllable = ["CV"]
    lang_helper = None

    def generate_name(self):
        self.lang_helper = LanguageHelper()

        a = random.randint(1,14)
        sy1_pos = random.randint(0,len(self.first_syllable)-1)
        sy2_pos = random.randint(0,len(self.second_syllable)-1)
        sy3_pos = random.randint(0,len(self.third_syllable)-1)

        name = self.lang_helper.populate_part(self.first_syllable[sy1_pos]) + self.lang_helper.populate_part(self.second_syllable[sy2_pos])
        if a == 1:
            name += self.lang_helper.populate_part(self.third_syllable[sy3_pos])
        return name
    

    
    
        