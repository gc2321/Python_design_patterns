############
### Observer - monitor and update
############

class Subject(object): #Represents what is being 'observed'

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        # If the observer is not already in the observers list,append the observer to the list
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer): #Simply remove the observer
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        # For all the observers in the list
        # Don't notify the observer who is actually updating the temperature
        # Alert the observers!
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)

class Core(Subject): #Inherits from the Subject class

    def __init__(self, name=""):
        Subject.__init__(self)
        self._name = name #Set the name of the core
        self._temp = 0 #Initialize the temperature of the core

    @property #Getter that gets the core temperature
    def temp(self):
        return self._temp

    @temp.setter #Setter that sets the core temperature
    def temp(self, temp):
        self._temp = temp
        self.notify() #Notify the observers whenever somebody changes the core temperature

class TempViewer:
    def update(self, subject): #Alert method that is invoked when the notify() method in a concrete subject is invoked
        print("Temperature Viewer: {} has Temperature {}".format(subject._name, subject._temp))

#Let's create our subjects
# c1 = Core("Core 1")
# c2 = Core("Core 2")

#Let's create our observers
# v1 = TempViewer()
# v2 = TempViewer()

#Let's attach our observers to the first core
# c1.attach(v1)
# c1.attach(v2)

#Let's change the temperature of our first core
# c1.temp = 80
# c1.temp = 90

############
### Visitor - add new feature to existing class with minimal changes
############

class House(object): #The class being visited
    def accept(self, visitor):
        """Interface to accept a visitor"""
        #Triggers the visiting operation!
        visitor.visit(self)

    def work_on_hvac(self, hvac_specialist):
        print(self, "worked on by", hvac_specialist) #Note that we now have a reference to the HVAC specialist object in the house object!

    def work_on_electricity(self, electrician):
        #Note that we now have a reference to the electrician object in the house object!
        print(self, "worked on by", electrician)

    def __str__(self):
        """Simply return the class name when the House object is printed"""
        return self.__class__.__name__


class Visitor(object):
    """Abstract visitor"""
    def __str__(self):
        """Simply return the class name when the Visitor object is printed"""
        return self.__class__.__name__

class HvacSpecialist(Visitor): #Inherits from the parent class, Visitor
    """Concrete visitor: HVAC specialist"""
    def visit(self, house):
        house.work_on_hvac(self) #Note that the visitor now has a reference to the house object

class Electrician(Visitor): #Inherits from the parent class, Visitor
    """Concrete visitor: electrician"""
    def visit(self, house):
        house.work_on_electricity(self)#Note that the visitor now has a reference to the house object

#Create an HVAC specialist
#hv = HvacSpecialist()

#Create an electrician
#e = Electrician()

#Create a house
#home = House()

#Let the house accept the HVAC specialist and work on the house by invoking the visit() method
#home.accept(hv)     # House worked on by HvacSpecialist

#Let the house accept the electrician and work on the house by invoking the visit() method
#home.accept(e)      # House worked on by Electrician

##########
# Iterator - customize iterator
##########

def count_to(count):
    """Our iterator implementation"""

    #Our list
    numbers_in_german = ["eins", "zwei", "drei", "vier", "funf"]

    #Our built-in iterator
	#Creates a tuple such as (1, "eins")
    iterator = zip(range(count), numbers_in_german)

    #Iterate through our iterable list
    # #Extract the German numbers
    # #Put them in a generator called number
    for position, number in iterator:
        yield number # Returns a 'generator' containing numbers in German

#Let's test the generator returned by our iterator
# for num in count_to(3):
#     print("{}".format(num))

############
# Strategy - replace default function with new one
############

import types #Import the types module

class Strategy:
    """The Strategy Pattern class"""

    def __init__(self, function=None):
        self.name = "Default Strategy"

        #If a reference to a function is provided, replace the execute() method with the given function

    def execute(self): #This gets replaced by another version if another strategy is provided.
        """The default method that prints the name of the strategy being used"""
        print("{} is used!".format(self.name))

#Replacement method 1
def strategy_one(self):
    print("{} is used to execute method 1".format(self.name))

#Replacement method 2
def strategy_two(self):
    print("{} is used to execute method 2".format(self.name))

#Let's create our default strategy
#s0 = Strategy()
#Let's execute our default strategy
#s0.execute()

#Let's create the first varition of our default strategy by providing a new behavior
#s1 = Strategy(strategy_one)
#Let's set its name
#s1.name = "Strategy One"
#Let's execute the strategy
#s1.execute()

# s2 = Strategy(strategy_two)
# s2.name = "Strategy Two"
# s2.execute()

#########################
# Chain of responsibility -
#########################

class Handler: #Abstract handler
    """Abstract Handler"""
    def __init__(self, successor):
        self._successor = successor # Define who is the next handler

    def handle(self, request):
        handled = self._handle(request) #If handled, stop here

        #Otherwise, keep going
        if not handled:
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError('Must provide implementation in subclass!')

class ConcreteHandler1(Handler): # Inherits from the abstract handler
    """Concrete handler 1"""
    def _handle(self, request):
        if 0 < request <= 10: # Provide a condition for handling
            print("Request {} handled in handler 1".format(request))
            return True # Indicates that the request has been handled

class DefaultHandler(Handler): # Inherits from the abstract handler
    """Default handler"""

    def _handle(self, request):
        """If there is no handler available"""
        #No condition checking since this is a default handler
        print("End of chain, no handler for {}".format(request))
        return True # Indicates that the request has been handled

class Client: # Using handlers
    def __init__(self):
        # Create handlers and use them in a sequence you want
        # Note that the default handler has no successor
        self.handler = ConcreteHandler1(DefaultHandler(None))

    def delegate(self, requests): # Send your requests one at a time for handlers to handle
        for request in requests:
            self.handler.handle(request)

# Create a client
c = Client()

# Create requests
requests = [2, 5, 30]

# Send the requests
c.delegate(requests)


