import random
import string

VOWELS = "aeiou"
CONSONANTS = "".join(set(string.ascii_lowercase) - set(VOWELS))

class LanguageHelper():
    
    def get_consonant(self):
        a = random.randint(0,len(CONSONANTS)-1)
        return CONSONANTS[a]
    
    def get_vowel(self):
        a = random.randint(0,len(VOWELS)-1)
        return VOWELS[a]
    
    def populate_part(self, part):
        syl = ""
        for piece in part:
            if piece == "C":
                character = self.get_consonant()
            elif piece == "V":
                character = self.get_vowel()
            elif piece == "+":
                character = syl[-1]
            elif piece == "Y":
                character = "y"
            syl += character
        return syl
    
    def save_name(self, name, language):
        print("save name")
        
    
    