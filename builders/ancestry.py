from abc import ABC, abstractmethod

class AncestryLanguage(ABC):
    
    @abstractmethod
    def generate_name(self):
        pass
    
    @abstractmethod
    def save_name(self, name, status):
        pass