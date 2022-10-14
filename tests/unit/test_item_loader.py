
from builders.shopitemloader import ShopLoader



class TestClass:
    
    #Arrange
    # @pytest.fixture
    # def new_generator(self):
    #     return DwarfLanguage()
    
    def test_load_items(self):
        loader = ShopLoader()
        item_list = loader.load_items_from_csv()
        print("Item_list length:",len(item_list))
        assert len(item_list) > 0
    
    def test_normalize_data(self):
        loader = ShopLoader()
        item_list = loader.load_items_from_csv()
        cleaned_list = loader.normalize_data(item_list)
        assert len(cleaned_list) > 1000
        
    
   