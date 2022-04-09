from abc import abstractmethod


class Vehicle:
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def take_damage(self):
        pass
