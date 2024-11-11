from abc import ABC, abstractmethod

class Burger(ABC):
    cheese_price = 20
    badel_price = 50
    @abstractmethod
    def get_type(self) ->str:
        pass
    
    @abstractmethod
    def get_details(self) -> dict:
        pass
    
    @abstractmethod
    def get_total(self) -> float:
        pass
    
class ChickenBurger(Burger):
    def __init__(self, extra_cheese = False, extra_badelMeat = False ) -> None:
        self.type = "Chicken Burger"
        self.price = 100
        self.extra_cheese = extra_cheese
        self.extra_badelMeat = extra_badelMeat

    def get_type(self) -> str:
        return self.type
    
    def get_total(self) -> float:
        total_price = self.price
        if self.extra_cheese:
            total_price += Burger.cheese_price
        if  self.extra_badelMeat:
            total_price += Burger.badel_price
        return total_price

    def get_details(self) -> dict:
        return {
            "type": self.type,
            "extra_cheese": self.extra_cheese,
            "extra_badelMeat": self.extra_badelMeat,
            "price": self.price,
            "total_price": self.get_total()
        }
        
class CrispyChickenBurger(Burger):
    def __init__(self, extra_cheese = False, extra_badelMeat = False ) -> None:
        self.type = "Crispy Chicken Burger"
        self.price = 120
        self.extra_cheese = extra_cheese
        self.extra_badelMeat = extra_badelMeat
    
    def get_type(self) -> str:
        return self.type
    
    def get_total(self) -> float:
        total_price = self.price
        if self.extra_cheese:
            total_price += Burger.cheese_price
        if  self.extra_badelMeat:
            total_price += Burger.badel_price
        return total_price
    
    def get_details(self) -> dict:
        return {
            "type": self.type,
            "extra_cheese": self.extra_cheese,
            "extra_badelMeat": self.extra_badelMeat,
            "price": self.price,
            "total_price": self.get_total()
        }
    
class FreakStreet:
    @staticmethod
    def get_burger(burger_type: str, extra_cheese = False, extra_badelMeat = False) -> Burger:
        if burger_type == "cb":
            return ChickenBurger(extra_cheese, extra_badelMeat)
        elif burger_type == "ccb":
            return CrispyChickenBurger(extra_cheese, extra_badelMeat)
        else:
            raise ValueError("Invalid burger type")

chicken_burger = FreakStreet.get_burger("cb",True, True)
crispy_burger = FreakStreet.get_burger("ccb",False, False)

print(chicken_burger.get_details())
print(crispy_burger.get_details())

