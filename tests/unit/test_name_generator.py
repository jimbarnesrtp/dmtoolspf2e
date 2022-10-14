
from builders.namegenerator import NameGenerator



class TestClass:
    
    #Arrange
    # @pytest.fixture
    # def new_generator(self):
    #     return DwarfLanguage()
    
    def test_load_languages(self):
        gen = NameGenerator()
        lang_list = gen.get_available_languages()
        print(len(lang_list))
        assert len(lang_list) > 0
    
    def test_get_sequence(self):
        gen = NameGenerator()
        seq = gen.get_sequence_by_ancestry("elf")
        print(seq)
        assert len(seq) > 0
        
    # def test_get_names(self):
    #     gen = NameGenerator()
    #     names = gen.generate_new_name_by_ancestry("halfling")
    #     print("Names:", names)
    #     assert len(names) > 0
        
    # def test_get_leshy_name(self):
    #     gen = NameGenerator()
    #     names = gen.generate_new_name_by_ancestry("leshy")
    #     print("Names:", names)
    #     assert len(names) > 0