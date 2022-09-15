
from builders.dwarf import DwarfLanguage



class TestClass:
    
    #Arrange
    # @pytest.fixture
    # def new_generator(self):
    #     return DwarfLanguage()
    
    def test_one(self):
        lang = DwarfLanguage()
        new_name = lang.generate_name()
        
        assert len(new_name) > 0