from abc import ABC, abstractmethod

class StoreManager(ABC):

    def add_stockpile(self, item_type, item_data):
        pass

    def remove_stockpile(self):
        pass

    def aggregate_pizza_size(self):
        pass

    def aggregate_color(self):
        pass

    def reveal_secret(self):
        pass

    def change_encryption_method(self, name, new_field):
        pass

    def dinner_time(self):
        pass

    def add_decoy_item(self, type_name, type_definition, secret_field):
        """
        input constraints:
        type_name must be a string

        type_definition must be a dictionary that specifies string keys and valid types per key, as an array.

            {
                'id': 0, <--------- id can just be any integer
                'size': [9, 12],
                'price': [15, 18],
                'taste': ['sweet', 'savory', 'spicy'],
                'crust': ['Thick', 'Thin']
            }

        secret_field must be a field that is found in type_definition.

        """
        pass

    def rotate_production_lines(self):
        pass