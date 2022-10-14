
from builders.elf import ElfLanguage



class TestClass:
    
    #Arrange
    # @pytest.fixture
    # def new_generator(self):
    #     return DwarfLanguage()
    
    def test_one(self):
        lang = ElfLanguage()
        new_name = lang.generate_name()
        
        assert len(new_name) > 0