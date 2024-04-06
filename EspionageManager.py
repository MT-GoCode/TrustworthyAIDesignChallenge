from StockpileManager import StockpileManager
from Sellable import Sellable
from products import decoy_item_factory

class EspionageManager(StockpileManager):

    def __init__(self):
        super().__init__()

    def reveal_secret(self):
        return ''.join([item.get_secret() for item in self._stockpile])

    def change_encryption_method(self, name, new_field):
        Sellable.change_encrypt_strat(name, new_field)

    def dinner_time(self):
        for item in self._stockpile:
            item.obscure_secret()

    def add_decoy_item(self, type_name, type_definition, secret_field):

        Sellable.add_decoy_type(type_name, type_definition, secret_field)
        self._menu_map[type_name] = decoy_item_factory(type_name, Sellable, list(type_definition.keys()))

    def rotate_production_lines(self):
        self._rotate_amount+=1