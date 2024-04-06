from abc import ABC, abstractmethod
from strategies import *

class Sellable():

    _where_are_secrets_stored = {'Pepperoni Pizza' : 'crust',
                                 'Kung Pao Chicken': 'size',
                                 'Mug': 'color',
                                 'Jacket': 'size',
                                 'Hawaiian Pizza': 'crust'}

    _type_definitions = {
        'Pepperoni Pizza': {
            'id': 0,
            'size': [9, 12],
            'price': [15, 18],
            'taste': ['sweet', 'savory', 'spicy'],
            'crust': ['Thick', 'Thin']
        },
        'Kung Pao Chicken': {
            'id': 0,
            'size': ['Small', 'Medium', 'Large'],
            'rice': ['White', 'Brown'],
            'price': [9, 11, 12],
            'taste': ['Sweet', 'Savory', 'Spicy'],
        },
        'Hawaiian Pizza': {
            'id': 0,
            'size': [9, 12],
            'price': [13, 16],
            'taste': ['Sweet', 'Savory', 'Spicy'],
            'crust': ['Thick', 'Thin']
        },
        'Mug': {
            'id': 0,
            'color': ['Blue', 'Red', 'Yellow'],
            'price': [10],
        },
        'Jacket': {
            'id': 0,
            'color': ['Black', 'White'],
            'size': ['L', 'M', 'S'],
            'price': [35],
        },


    }

    _field_secret_map = {
        'crust': CrustEncryptionStrategy(),
        'size': SizeEncryptionStrategy(),
        'taste': TasteEncryptionStrategy(),
        'price': PriceEncryptionStrategy(),
        'color': ColorEncryptionStrategy()
    }


    @classmethod
    def add_decoy_type(cls, name, type_def, secret_field):
        cls._type_definitions[name] = type_def
        cls._where_are_secrets_stored[name] = secret_field

    @classmethod
    def valid_config_check(cls, name, info_dict):
        definition = cls._type_definitions[name]

        # print(info_dict)
        # print("compare against: ")
        # print(definition)
        # print('secret is')
        # print(cls._where_are_secrets_stored[name])

        if set(definition.keys()) != set(info_dict.keys()):
            # print('no id')
            return False
        if 'id' not in set(info_dict.keys()):

            return False

        # print('passes key check')
        for key, acceptable_values in definition.items():

            if key != 'id' and key != cls._where_are_secrets_stored[name]: # this not a secret key (therefore check if it has a valid value)
                if info_dict[key] not in acceptable_values: # invalid value
                    # print('not acceptable!')
                    return False
        return True

    @classmethod
    def change_encrypt_strat(cls, type_name, new_field):
        # secret_field = cls._where_are_secrets_stored[type_name]
        cls._where_are_secrets_stored[type_name] = new_field

        # encrypt_strat = cls._field_secret_map[secret_field]
        # store = encrypt_strat.get_secret(self)
        #
        # encrypt_strat.obscure_secret(self)
        #
        #
        # encrypt_strat.store_secret(self, store)

    def __init__(self, name, info_dict):
        self.id = info_dict['id']
        self.price = info_dict['price']
        self.name = name  # typename

    def get_secret(self):
        secret_field = self._where_are_secrets_stored[self.name]
        encrypt_strat = self._field_secret_map[secret_field]
        return encrypt_strat.get_secret(self)

    def obscure_secret(self):
        secret_field = self._where_are_secrets_stored[self.name]
        encrypt_strat = self._field_secret_map[secret_field]
        dummy_value = self._type_definitions[self.name][secret_field][0]
        encrypt_strat.obscure_secret(self, dummy_value)

    def has_secret(self):

        secret_field = self._where_are_secrets_stored[self.name]
        encrypt_strat = self._field_secret_map[secret_field]

        # print('secret field: ')
        # print(secret_field)
        # print(encrypt_strat)

        return encrypt_strat.get_secret(self) not in self._type_definitions[self.name][secret_field]