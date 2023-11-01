"""
Factory Method Design Pattern

Intent: Provides an interface for creating objects in a superclass, but allows
subclasses to alter the type of objects that will be created.
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    """
    The Creator class declares the factory method that is supposed to return an
    object of a Product class. The Creator's subclasses usually provide the
    implementation of this method.
    """

    # please note that you cannot call the Creator class
    # this class only implements an abstract method that the subclasses have to use
    @abstractmethod
    def factory_method(self):
        """
        Note that the Creator may also provide some default implementation of
        the factory method.
        """
        pass

    def some_operation(self) -> str:
        """
        Also note that, despite its name, the Creator's primary responsibility
        is not creating products. Usually, it contains some core business logic
        that relies on Product objects, returned by the factory method.
        Subclasses can indirectly change that business logic by overriding the
        factory method and returning a different type of product from it.
        """

        # Call the factory method to create a Product object.
        # note in this case the subclass instances were the ones with which this method was called on
        # henceforth self in this case implies the subclass instance
        product = self.factory_method()

        # Now, use the product.
        result = f"Creator: The same creator's code has just worked with {product.operation()}"

        return result


"""
Concrete Creators override the factory method in order to change the resulting
product's type.
"""


class ConcreteCreator1(Creator):
    """
    Note that the signature of the method still uses the abstract product type,
    even though the concrete product is actually returned from the method. This
    way the Creator can stay independent of concrete product classes.
    """

    # realise that the factory method is called from the base class inherited from base class
    # the return is shifted back to the base class where its assigned the variable product, this variable is then
    # this variable has the concreteProduct method operation() called on it
    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()


class Product(ABC):
    """
    The Product interface declares the operations that all concrete products
    must implement.
    """

    @abstractmethod
    def operation(self) -> str:
        pass


"""
Concrete Products provide various implementations of the Product interface.
"""


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"


def client_code(creator: Creator) -> None:
    """
    The client code works with an instance of a concrete creator, albeit through
    its base interface. As long as the client keeps working with the creator via
    the base interface, you can pass it any creator's subclass.
    """

    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")  # method called on the concreteCreator passed in the client code arg
    # note that in this case the ConcreteCreator1 instance is the one with which the method some_operation was
    # called on   (  ConcreteCreator1().some_operation() )
    # notice that this is possible because the ConcreteCreator1() is an instance of a subclass of Creator class
    # with this in mind its possible to call the methods in the base class on the instance of its subclass


client_code(ConcreteCreator1())

if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())

"""
in this section we are going to highlight the usefulness of the factory method
its main purpose is that this can enable the base class to subclass the aspect of production of different instance types
in this case notice like the ability of the base class to use concreteProduct1 objects as well as concreteProduct2 
instances


Abstract class : this is not a concrete class and you can therefore not instantiate an object of an abstract class
the main essence is that the class allows creation of abstract methods that must be implemented in the subclasses 
abstract classes act as a blueprint for other classes and in this essence provide common interface for different 
implementations of a component 

Abstract method : this is a method that has a declaration but no implementation 

also note composition and aggregation are forms of associations 

product : interface that is common to all objects that can be produced by the creator and its subclasses 
( an association(dependency) relationship that exist between the Creator (Base class) and the interface (Product)

ConcreteProduct : this are different implementations of the product interface 

creator : declares the factory method that returns new product object. its important that the return type matches the 
product interface. the factory method can be declared as abstract to force all subclasses to implement their own version
of the method , note that the primary essence of the Creator class is not object creation but rather has some core logic 
related to the products. 

so in essence the factory method decouples this logic from concrete product classes 

concreteCreator : override the base factory method so as to return a different type of product 

"""
