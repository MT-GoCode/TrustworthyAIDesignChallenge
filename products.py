
from Sellable import Sellable

class PepperoniPizza(Sellable):
    def __init__(self, info_dict):
        super().__init__('Pepperoni Pizza', info_dict)
        self.size = info_dict['size']
        self.crust = info_dict['crust']
        self.taste = info_dict['taste']

class HawaiianPizza(Sellable):
    def __init__(self, info_dict):
        super().__init__('Hawaiian Pizza', info_dict)
        self.size = info_dict['size']
        self.crust = info_dict['crust']
        self.taste = info_dict['taste']

class KungPaoChicken(Sellable):
    def __init__(self, info_dict):
        super().__init__('Kung Pao Chicken', info_dict)
        self.size = info_dict['size']
        self.rice = info_dict['rice']
        self.taste = info_dict['taste']

class Mug(Sellable):
    def __init__(self, info_dict):
        super().__init__('Mug', info_dict)
        self.color = info_dict['color']

class Jacket(Sellable):
    def __init__(self, info_dict):
        super().__init__('Jacket', info_dict)
        self.color = info_dict['color']
        self.size = info_dict['size']


def decoy_item_factory(name, base_class, attributes):

    def __init__(self, info_dict):
        super(new_class, self).__init__(name, info_dict)
        for attr in attributes:
            if attr in info_dict:
                setattr(self, attr, info_dict[attr])

    class_dict = {
        '__init__': __init__,
    }

    new_class = type(name, (base_class,), class_dict)

    return new_class