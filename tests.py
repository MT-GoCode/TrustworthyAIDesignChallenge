from interfaces.StoreManager import StoreManager
from EspionageManager import EspionageManager

print('test case 1 ----------------------------')
# tests addition of normal products
# tests reveal_secret()
# tests change_encryption_method()
# tests reveal_secret() reflects updated encryption methods
# tests input tests of adding new products reflects updated encryption methods

Store: StoreManager = EspionageManager()

# check that we can add a normal object with a secret in the default location
Store.add_stockpile('Pepperoni Pizza', {
    'id': 0,
    'size': 9,
    'price': 15,
    'taste':'sweet',
    'crust': 'cocacola recipe'
})

# check that we can retrieve the secret
print(Store.reveal_secret()) # expected 'cocacola recipe'

# check that we can change secret field
Store.change_encryption_method('Pepperoni Pizza', 'taste')

# we should be able to add pizzas with a secret in taste.
Store.add_stockpile('Pepperoni Pizza', {
    'id': 1,
    'size': 9,
    'price': 15,
    'taste':'pepsicola recipe',
    'crust': 'Thick'
})

print(Store.reveal_secret()) # expected "sweetpepsicola recipe"
# sweet comes from the original taste of pizza 1 being reinterpreted as a secret. The spec didn't say how to handle this.

# should print 0, as we've changed the secret field. so this is now invalid product.
print(Store.add_stockpile('Pepperoni Pizza', {
    'id': 1,
    'size': 9,
    'price': 15,
    'taste':'pepsicola recipe',
    'crust': 'shouldn\'t have a secret here'
}))

print('test case 2 ----------------------------')
# tests use of different products which have different secret fields
# tests addition of multiple objects
# tests dinner_time()


Store: StoreManager = EspionageManager()

Store.add_stockpile('Kung Pao Chicken', {
    'id': 2,
    'size': 'SECRET A ',
    'rice': 'White',
    'price': 11,
    'taste':'Sweet',
})

Store.add_stockpile('Kung Pao Chicken', {
    'id': 3,
    'size': 'SECRET B ',
    'rice': 'White',
    'price': 12,
    'taste':'Sweet',
})

# testing dinner time

print(Store.reveal_secret()) # expected 'SECRET A SECRET B'
Store.dinner_time()
print(Store.reveal_secret()) # expected 'SmallSmall,' as secrets were replaced

print('test case 3 ----------------------------')

# testing decoy items.

Store: StoreManager = EspionageManager()

Store.add_decoy_item('DecoyShirt',{
    'id': 0,
    'size': ['XS', 'S', 'M', 'L'],
    'color': ['red', 'blue', 'green'],
    'price': [10, 20, 30],
}, 'color')

Store.add_stockpile('DecoyShirt', {
    'id': 0,
    'size': 'M',
    'color': 'nancy pelosi bought nvidia call options ',
    'price': 20,
})

Store.add_stockpile('DecoyShirt', {
    'id': 50,
    'size': 'L',
    'color': ' and most US senators practice insider trading',
    'price': 30,
})

print(Store.reveal_secret()) # "nancy pelosi bought nvidia and most US senators do insider trading"
# "SmallSmall' comes from the obscured secrets of the KungPaoChicken from last test case.

print('test case 4 ----------------------------')
# testing remove_stock_pile(). we will attempt to add some new objects with and without secrets,
# and call remove_stockpile(), which should only remove the first on without a secret


Store: StoreManager = EspionageManager()

Store.add_stockpile('Hawaiian Pizza', {
    'id': 2,
    'size': 9,
    'crust': 'Apple uses ',
    'price': 13,
    'taste':'Sweet',
})

Store.add_stockpile('Mug', { # will be removed later as it has no secret
    'id': 2,
    'color': 'Blue',
    'price': 10,
})

Store.add_stockpile('Jacket', {
    'id': 7,
    'color': 'Black',
    'size': 'sweatshops on Mars',
    'price': 35,
})

print(len(Store._stockpile)) # prints 3
Store.remove_stockpile()
print(len(Store._stockpile)) # prints 2

print(Store.reveal_secret()) # prints "Apple uses sweatshops on Mars"

print('test case 5 ----------------------------')
# test of aggregate_pizza_size

# I will use the store from last test case. there is currently one 9-inch hawaiian, and a jacket

Store.add_stockpile('Pepperoni Pizza', {
    'id': 1,
    'size': 9,
    'price': 15,
    'taste':'pepsicola recipe',
    'crust': 'Thick'
})
Store.add_stockpile('Hawaiian Pizza', {
    'id': 2,
    'size': 12,
    'crust': 'SECRET!!!',
    'price': 13,
    'taste':'Sweet',
})

print(Store.aggregate_pizza_size()) # expect "(2,1)" as there's 2 9-inches and 1 12-inch

print('test case 6 ----------------------------')
# test of aggregate_color.

Store: StoreManager = EspionageManager()

Store.add_stockpile('Mug', {
    'id': 2,
    'color': 'Blue',
    'price': 10,
})

Store.add_stockpile('Mug', {
    'id': 2,
    'color': 'Blue',
    'price': 10,
})

Store.add_stockpile('Mug', {
    'id': 2,
    'color': 'SECRETT', # this secret will not be included in aggregate_color
    'price': 10,
})

Store.add_stockpile('Jacket', {
    'id': 7,
    'color': 'Black',
    'size': 'SECRETTT',
    'price': 35,
})

print(Store.aggregate_color()) # expected "{'Blue': 2, 'Black': 1}"

print('test case 7 ----------------------------')
# ROTATE PRODUCTION LINES TEST

Store: StoreManager = EspionageManager()

Store.rotate_production_lines()

# now, if I add a Kung Pao Chicken, I should actually be specifying the definition of a Mug, which is different
# as the code still runs and prints out the Mug's secret, this means the rotate_production_lines worked
Store.add_stockpile('Kung Pao Chicken', {
    'id': 7,
    'color': 'This is a secret stored in color, which would not normally be the case for Chicken',
    'price': 10,
})

print(Store.reveal_secret())