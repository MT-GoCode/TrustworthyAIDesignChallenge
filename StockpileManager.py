from products import *
from Sellable import *
from interfaces.StoreManager import StoreManager


class StockpileManager(StoreManager):

    def __init__(self):
        self._menu_map = {"Pepperoni Pizza": PepperoniPizza,
                          "Hawaiian Pizza": HawaiianPizza,
                          "Kung Pao Chicken": KungPaoChicken,
                          "Mug": Mug,
                          "Jacket": Jacket
                          }
        # default menu maps each menu name to the correct type name.
        # when rotated, these mappings are adjusted

        self._stockpile = []  # A list to represent the stockpile
        self._rotate_amount = 0

    # def dump(self):
    #     print(self._stockpile)

    def add_stockpile(self, item_type, item_data):
        if item_type not in self._menu_map:
            print ("invalid type name")
            return 0

        keys = list(self._menu_map.keys())
        index = keys.index(item_type)
        new_index = (index + self._rotate_amount) % len(keys)
        item_type = keys[new_index]

        # check valid args
        if not Sellable.valid_config_check(item_type, item_data):
            print("invalid args")
            return 0

        # construct matching item
        constructor = self._menu_map[item_type]
        item = constructor(item_data)

        # add it!
        self._stockpile.append(item)
        return 1

    def remove_stockpile(self):
        for item in self._stockpile:
            if not item.has_secret():
                print('removed!')
                self._stockpile.remove(item)
                break

    def aggregate_pizza_size(self):
        nines = 0
        twelves = 0
        for item in self._stockpile:
            if 'Pizza' in item.name:
                nines+=(item.size == 9)
                twelves += (item.size == 12)
        return (nines, twelves)

    def aggregate_color(self):
        ret = {}
        for item in self._stockpile:
            if hasattr(item, 'color') and item.color in Sellable._type_definitions[item.name]['color']:
                ret[item.color] = ret.get(item.color, 0) + 1
        return ret


    # Other methods as specified...
