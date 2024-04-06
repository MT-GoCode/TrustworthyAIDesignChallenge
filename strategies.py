from interfaces.EncryptionStrategy import EncryptionStrategy

class CrustEncryptionStrategy(EncryptionStrategy):
    def obscure_secret(self, item, value):
        item.crust = value
    def get_secret(self, item):
        return item.crust

    def store_secret(self, item, secret): item.crust = secret

class RiceEncryptionStrategy(EncryptionStrategy):
    def obscure_secret(self, item, value):
        item.rice = value
    def get_secret(self, item):
        return item.rice

    def store_secret(self, item, secret): item.rice = secret

class SizeEncryptionStrategy(EncryptionStrategy):
    def obscure_secret(self, item, value):
        item.size = value
    def get_secret(self, item):
        return item.size

    def store_secret(self, item, secret): item.size = secret


class PriceEncryptionStrategy(EncryptionStrategy):
    def obscure_secret(self, item, value):
        item.price = value
    def get_secret(self, item):
        return item.price

    def store_secret(self, item, secret): item.price = secret


class TasteEncryptionStrategy(EncryptionStrategy):
    def obscure_secret(self, item, value):
        item.taste = value
    def get_secret(self, item):
        return item.taste

    def store_secret(self, item, secret): item.taste = secret



class ColorEncryptionStrategy(EncryptionStrategy):
    def obscure_secret(self, item, value):
        item.color = value

    def get_secret(self, item):
        return item.color

    def store_secret(self, item, secret): item.color = secret



