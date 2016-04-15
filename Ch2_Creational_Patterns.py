############
### Factory
############

class Dog:
    #def __init__(self, name):
       #self._name = name

    def __str__(self):
        return "Dog"

    def speak(self):
        return "Woof!"

class Cat:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return "Cat"

    def speak(self):
        return "Meow!"

def get_pet(pet="dog"):
    """The factor method"""
    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))
    return pets[pet]

#print(get_pet("dog").speak())
#print(get_pet("cat").speak())

####################
### Abstract factory
####################

class DogFactory:
    """Concrete Factory"""
    def get_pet(self):
        """Return a dog object"""
        return Dog()

    def get_food(self):
        """Returns a Dog Food object"""
        return "Dog Food"

class PetStore:
    """PetStore house our Abstract Factory"""
    def __init__(self, pet_factory=None):
        """pet_factory is our Abstract Factory"""
        self._pet_factory = pet_factory

    def show_pet(self):
        """Utility method to display the details of the objects returned by the DogFactory"""

        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print("Our pet is '{}'!".format(pet))
        print("Our pet says hello by '{}'!".format(pet.speak()))
        print("Its food is '{}'!".format(pet_food))

# Create a concrete factory
#factory = DogFactory()

# Create a pet store housing Abstract factory
#shop = PetStore(factory)

# Invoking the utility method to show the details of pet
#shop.show_pet()

#############
### Singleton
#############

class Borg:
    """make class attributes global"""
    _shared_state = {} # attribute dictionary

    def __init__(self):
        self.__dict__ = self._shared_state # make it an attribute dictionary

class Singleton(Borg):# inherits from the Borg class
    """makes the singleton objects an object-orientated global variable"""

    def __init__(self, **kwargs):
        Borg.__init__(self)
        # Update the attribute dictionary by inserting a new key-value pair
        self._shared_state.update(kwargs)

    def __str__(self):
        # Returns the attribute dictionary for printing
        return str(self._shared_state)

# create a singleton object and add our first acronym
#x = Singleton(HTTP = "Hyper Text Transfer Protocol")

# print the object
#print (x)   # {'HTTP': 'Hyper Text Transfer Protocol'}

# create another singleton object and if it is refers to the same attribute dictionary by adding another acronym
#y = Singleton(SNMP="Simple Network Management Protocol")
# print the object, keeping x dictionary
#print (y)   # {'HTTP': 'Hyper Text Transfer Protocol', 'SNMP': 'Simple Network Management Protocol'}

###########
### Builder
###########

class Director():
    """director"""
    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

    def get_car(self):
        return self._builder.car

class Builder():
    """abstract builder"""
    def __init__(self):
        self.car = None

    def create_new_car(self):
        self.car = Car()

class SkyLarkBuilder(Builder):
    """concrete builder --> provides parts and tools to work on the parts"""

    def add_model(self):
        self.car.model = "Skylark"

    def add_tires(self):
        self.car.tires = "Regular tires"

    def add_engine(self):
        self.car.engine = "Turbo engine"

class Car():
    """product"""
    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self):
        return '{} | {} | {}'.format(self.model, self.tires, self.engine)


# builder = SkyLarkBuilder()
# director = Director(builder)
# director.construct_car()
# car = director.get_car()
# print (car)

#############
### prototype
#############

import copy

class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        """unregister an object"""
        del self._objects[name]

    def clone(self, name, **attr):
        """clone a registered object and update its attributes"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj

class Car:
    def __init__(self):
        self.name = "Skylark"
        self.color = "Red"
        self.options = "Ex"

    def __str__(self):
        return '{} | {} | {}'.format(self.name, self.color, self.options)


c = Car()
prototype = Prototype()
prototype.register_object("skylark", c)
c1 = prototype.clone('skylark')
print (c1)



