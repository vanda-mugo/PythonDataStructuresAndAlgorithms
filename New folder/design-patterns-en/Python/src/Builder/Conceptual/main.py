"""
Builder Design Pattern

Intent: Lets you construct complex objects step by step. The pattern allows you
to produce different types and representations of an object using the same
construction code.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):
    # inherits from the ABC abstract class
    """
    The Builder interface specifies methods for creating the different parts of
    the Product objects.
    """

    # this defines an interface with which the products are created
    # all builders have to implement this interface
    @property
    # the property has not been implemented in the base class that is the base builder but it has to be implemented
    # differently in the classes that inherit from this
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass


class ConcreteBuilder1(Builder):
    """
    The Concrete Builder classes follow the Builder interface and provide
    specific implementations of the building steps. Your program may have
    several variations of Builders, implemented differently.
    """

    def __init__(self) -> None:
        """
        A fresh builder instance should contain a blank product object, which is
        used in further assembly.
        """
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    # note that in this case product is the property that has been defined in this case
    # the @property decorator indicates teh fact that a property is to be defined
    # recall that property is a class attribute and henceforth will appear in the dict of the class
    def product(self) -> Product1:  # type hints suggests that the return is Product1()
        # in the case of this the property attribute is like a getter
        """
        Concrete Builders are supposed to provide their own methods for
        retrieving results. That's because various types of builders may create
        entirely different products that don't follow the same interface.
        Therefore, such methods cannot be declared in the base Builder interface
        (at least in a statically typed programming language).

        Usually, after returning the end result to the client, a builder
        instance is expected to be ready to start producing another product.
        That's why it's a usual practice to call the reset method at the end of
        the `getProduct` method body. However, this behavior is not mandatory,
        and you can make your builders wait for an explicit reset call from the
        client code before disposing of the previous result.
        """
        product = self._product  # in this case this equates to Product1()
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("PartA1")

    def produce_part_b(self) -> None:
        self._product.add("PartB1")

    def produce_part_c(self) -> None:
        self._product.add("PartC1")


class Product1():
    """
    It makes sense to use the Builder pattern only when your products are quite
    complex and require extensive configuration.

    Unlike in other creational patterns, different concrete builders can produce
    unrelated products. In other words, results of various builders may not
    always follow the same interface.
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")


class Director:
    """
    The Director is only responsible for executing the building steps in a
    particular sequence. It is helpful when producing products according to a
    specific order or configuration. Strictly speaking, the Director class is
    optional, since the client can control builders directly.
    """

    def __init__(self) -> None:
        self._builder = None

    @property  # initialisation of the property which in this case is the builder property
    # basically the builder has been initialised in this getter
    def builder(self) -> Builder:
        return self._builder

    @builder.setter  # this is a setter for the builder property which was already declared initially
    # this is as per property used to set the value of the builder in this case a setter method for the property
    # with this the protected self._builder can actually be changed, that is the value can be altered
    def builder(self, builder: Builder) -> None:
        """
        The Director works with any builder instance that the client code passes
        to it. This way, the client code may alter the final type of the newly
        assembled product.
        """
        print("JUst to check if we can add some more functionality to the property ")
        self._builder = builder

    """
    The Director can construct several product variations using the same
    building steps.
    """

    def build_minimal_viable_product(self) -> None:
        self.builder.produce_part_a()
        # in this case the self.builder equates to the getter method that is used to actually get the value of builder
        # the value was already pre set to the director.builder = builder which equates to ConcreteBuilder1() instance
        # this allows the instance to actually be able to access the methods of the ConcreteBuilder class

    def build_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()


director = Director()  # instance of class Director
builder = ConcreteBuilder1()  # instance of the class ConcreteBuilder1() based on the product that one wants to achieve
# based on this notice that you decide the concrete builder that one wants to achieve based on the product intended by
# the user can then control all using the Director class as its definite that the builder is an attribute of this class
director.builder = builder # notice that this equates to the builder property in python

print("Standard basic product: ")
director.build_minimal_viable_product() # this function is a function in the Director class that actually equates
# to the director class using the self.builder which in this case is an instance of the class builder but also an
# an attribute of the class Director
builder.product.list_parts() # in this case the product is an attribute of the builder class henceforth in this case
# one will be accessing the property
# recall one cannot access the self._product which equates to the Product1()
# notice that this will equate to self._product which is Product1() which has the method list_parts() in its class
# methods


print("\n")

print("Standard full featured product: ")
director.build_full_featured_product()
builder.product.list_parts()

print("\n")

# Remember, the Builder pattern can be used without a Director class.
print("Custom product: ")
builder.produce_part_a()
builder.produce_part_b()
builder.product.list_parts()

if __name__ == "__main__":
    """
    The client code creates a builder object, passes it to the director and then
    initiates the construction process. The end result is retrieved from the
    builder object.
    """

    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder  # notice that the trick is that the director.builder in this case is equivalent to the
    # instance of the ConcreteBuilder1() . therefore having this translated through the property to being an attribute
    # of class director this enables this to be such as an attribute of the class director that will enable the
    # the director as a class to be able to dictate the procedure to be followed in the creation of complex objects


    print("Standard basic product: ")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("Standard full featured product: ")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")

    # Remember, the Builder pattern can be used without a Director class.
    print("Custom product: ")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.list_parts()
