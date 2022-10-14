from abc import ABC, abstractmethod

class AncestryLanguage(ABC):
    
    @abstractmethod
    def generate_name(self):
        pass
    