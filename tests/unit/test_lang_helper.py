
from builders.languagehelper import LanguageHelper



class TestClass:
    
    #Arrange
    # @pytest.fixture
    # def new_generator(self):
    #     return DwarfLanguage()
    
    def test_consonant(self):
        helper = LanguageHelper()
        new_name = helper.get_consonant()
        print("Consonant = ", new_name)
        
        assert len(new_name) > 0
        
    def test_vowel(self):
        helper = LanguageHelper()
        new_name = helper.get_vowel()
        print("Vowel = ", new_name)
        
        assert len(new_name) > 0
        
    def test_get_part(self):
        helper = LanguageHelper()
        new_name = helper.populate_part("CVC")
        print("part = ", new_name)
        
        assert len(new_name) > 0