# TrustworthyAIDesignChallenge

This writeup describes Code, a diagram, detils on how SOLID is used, and a Bug Log.

## Code Details
test.py includes all test cases with comments on expected outputs.

![Diagram for Trustworthy AI Design Challenge](https://github.com/MT-GoCode/TrustworthyAIDesignChallenge/assets/36799073/c87cceb3-47e3-4330-82db-055c5f9ff05a)

## How did I use SOLID?
#### Single Responsibility Principle
Each class focuses on one responsibility.
EncryptionStrategy classes all focus on getter and setter methods for one specific field - crust, size, color, etc.
Sellable class focuses only on common data/methods for all products. It will only change when product-related specifications change.

#### Open-closed principle
If we wanted to add new products, we could extend Sellable’s _type_definitions, products.py’s class definitions, StockpileManager’s menu of constructors. No need to modify anything already written.
The add_decoy_type takes advantage of this fact to add new types through creating a series of dictionaries.
If we want to extend more fields and allow them to be used for secrets, we could create new EncryptionStrategy classes in strategies.py and extend some of the type definitions.

#### Liskov Substitution principle 
This is most apparent through my Sellable class, that is a parent class for all products/merch. The Stockpile Manager calls methods that are common to all products as they are defined in Sellable, such as get_secret, obscure_secrt, change_encrypt_strat. Any product subclass can be substituted.
The Sellable class calls methods defined by the EncryptionStrategy interface, which can be a handful of subclasses. Any of these can be substituted.

#### Interface Segregation Principle
Every instantiated class exposes only methods and data that are absolutely necessary to using it.

#### Dependency Inversion Principle
I use interfaces to separate abstractions from lower-level details. For example, I have an overarching StoreManager interface that is implemented by StoreManager() and EspionageManager(). StoreManager has declared all the functions defined in the specification, so if their implementation changes, that does not affect StoreManager’s interface.
Additionally, the EncryptionStrategy classes also utilize an interface.

## Bug Log/Things I could not implement
I didn’t implement various input validation / usability features that were not mentioned in the spec and weren’t too critical, such as handling old secrets when a secret field is changed to be a new one, or checking that IDs across the stockpile were unique. My code could easily be extended to have these features.
I did implement the input validation check for creating new products, ensuring that prices, sizes, taste, color, etc. had valid values.
