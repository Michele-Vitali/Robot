from abc import ABC, abstractmethod

# Component's interface

class Component(ABC):
    
    @abstractmethod
    def check_health(self) -> bool:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_status_info(self) -> str:
        """Returns a string with the component's status information."""
        pass