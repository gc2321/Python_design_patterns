#############
### Decorator - add decoration to function
#############

from functools import wraps


def make_blink(function):
    """define the decorator"""

    # make the decorator transparent in its name and docstring
    @wraps(function)
    # define the inner function
    def decorator():
        # grab the return value of the function being decorated
        ret = function()
        # add new functionality to the function being decorated
        return "<blink>" + ret + "</blink>"

    return decorator


# apply the decorator
@make_blink
def hello_world():
    """original function"""
    return "Hello world!"


# check the result of decorating
#print(hello_world())        # <blink>Hello world!</blink>

# check if the function name is still the name of the function being decorated
#print(hello_world.__name__) # hello_world

# check if docstring is still the same as that of the function being decorated
#print(hello_world.__doc__)  # original function


#########
### Proxy - create object when necessary, because creating object is resource intensive
#########

import time

class Producer:
    """define the resource-intensive' object to instantiate"""
    def produce(self):
        print ("Producer is occupied!")
    def meet(self):
        print ("Producer has time to meet you now!")


class Proxy:
    """define the 'relatively less resource-intensive' proxy to instantiate as a middleman"""
    def __init__(self):
        self.occupied = 'No'
        self.producer = None

    def produce(self):
        """chekc if producer is available"""
        print ("Artist checking if Producer is available...")

        if self.occupied == "No":
            # if the producer is available, create a producer object!
            self.producer = Producer()
            time.sleep(2)

            # make the producer meet the guest!
            self.producer.meet()

        else:
            # otherwise, don't instantiate a producer
            time.sleep(2)
            print("Producer is busy!")

# instantiate a proxy
#p = Proxy()

# make the proxy: artist produces until Producer is available
#p.produce()         # Producer has time to meet you now!

# change the state to 'occupied'
#p.occupied += "Yes"

# make the Producer produce
#p.produce()         # Producer is busy!


###########
### Adaptor - convert to appropriate function
###########

class Korean:
    """Korean speaker"""
    def __init__(self):
        self.name = "Korean"

    def speak_korean(self):
        return "An-neyong?"

class British:
    """English speaker"""
    def __init__(self):
        self.name = "British"

    def speak_english(self):
        return "Hello!"

class Adapter:
    """this changes the generic method name to individualize method names"""

    def __init__(self, object, **adapted_method):
        """change the name of the method"""
        self._object = object

        # add a new dictionary item that establishes the mapping between the generic method name: speak() and the
        # concrete method
        # For example, speak() will be translated to speak_korean() if the mapping says so
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        """simply return the rest of the attributes!"""
        return getattr(self._object, attr)


# create a Korean object
#korean = Korean()

# create a British object
#british = British()

# list ot store speaker objects, append objects
# objects = []
# objects.append(Adapter(korean, speak=korean.speak_korean))
# objects.append(Adapter(british, speak=british.speak_english))
#
# for obj in objects:
#     print("{} says '{}'".format(obj.name, obj.speak()))

# Korean says 'An-neyong?'
# British says 'Hello!'

#############
### Composite - recursive tree structure
#############

class Component(object):
    """abstract class"""
    def __init__(self, *args, **kwargs):
        pass

    def component_function(self):
        pass

class Child(Component): # inherits from the abstract class, Component
    """concrete class"""

    def __init__(self, *args, **kwargs):
        Component.__init__(self,*args, **kwargs)

        # store the name of child item
        self.name = args[0]

    def component_function(self):
        # print the name of child item
        print("{}".format(self.name))

class Composite(Component): # inherits from the abstract class, Component
    """concrete class and maintains the tree recursive structure"""

    def __init__(self, *args,**kwargs):
        Component.__init__(self, *args, **kwargs)

        # store the name of the composite object
        self.name = args[0]

        # store child items
        self.children = []

    def append_child(self, child):
        """add a child"""
        self.children.append(child)

    def remove_child(self, child):
        """remove a child"""
        self.children.remove(child)

    def component_function(self):

        # print the name of the composite object
        print("{}".format(self.name))

        # iterate through the child objects and invoke their component function printing their names
        for i in self.children:
            i.component_function()

# build a composite submenu 1
#sub1 = Composite("submenu 1")

# create a new child sub_submenu 11
#sub11 = Child("sub_submenu 11")
# create a new child sub_submenu 12
#sub12 = Child("sub_submenu 12")

# add the submenu 11 and submenu 12 to submenu 1
# sub1.append_child(sub11)
# sub1.append_child(sub12)

# build a top-level composite menu
#top = Composite("top_menu")

# add a submenu 2 that is not a composite
#sub2 = Child("submenu 2")

# add the composite submenu 1 to the top-level composite menu
#top.append_child(sub1)

# add the plain submenu 2 to the top-level composite menu
#top.append_child(sub2)

# test composite pattern
#top.component_function()


##########
### Bridge - combining implementation-specific and implementation-independent functions
##########

class DrawingAPIOne(object):
    """implementation-specific abstraction: concrete class one"""
    def draw_circle(self, x, y, radius):
        print("API 1 drawing a circle at ({}, {} with radius {}!)".format(x,y, radius))

class DrawingAPITwo(object):
    """implementation-specific abstraction: concrete class two"""
    def draw_circle(self, x, y, radius):
        print("API 2 drawing a circle at ({}, {} with radius {}!)".format(x, y, radius))

class Circle(object):
    """implementation-independent abstraction: for example, there could be a rectangle class!"""

    def __init__(self, x, y, radius, drawing_api):
        """initialize the necessary attributes"""
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        """implementation-specific abstraction taken care of by another class: Drawing API"""
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, percent):
        """implementation-independent"""
        self._radius *= percent

# build the first Circle object using API One
circle1 = Circle(1,2,3, DrawingAPIOne())

# draw a circle
circle1.draw()

# build a second Circle object using API Two
circle2 = Circle(2,3,4, DrawingAPITwo())

# draw a circle
circle2.draw()


































