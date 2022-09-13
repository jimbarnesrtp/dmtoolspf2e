import pytest
from dm-tools-pf2.app.dwarf import DwarfLanguage

class TestClass:
    
    #Arrange
    @pytest.fixture
    def new_generator(self):
        return DwarfLanguage()
    
    def test_one(self, new_generator):
        new_name = new_generator.generate_name()
        
        assert len(new_name) > 0