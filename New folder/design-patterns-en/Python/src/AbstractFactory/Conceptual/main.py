"""
Abstract Factory Design Pattern

Intent: Lets you produce families of related objects without specifying their
concrete classes.
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    # Please note that the Abstract factory actually declares a set of methods that return different abstract products
    #  eg this will declare abstract methods that create all product types required in a particular situation
    # this products are called a family and are related by high level theme or concept . note that a family of products
    # a family of products may have several variants but products of one variant are incompatible with the products of
    # another variant
    """
    The Abstract Factory interface declares a set of methods that return
    different abstract products. These products are called a family and are
    related by a high-level theme or concept. Products of one family are usually
    able to collaborate among themselves. A family of products may have several
    variants, but the products of one variant are incompatible with products of
    another.
    """

    @abstractmethod
    def create_product_a(self) -> AbstractProductA: # note that in this case the (A) signifies a product family
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass
    # note by in such a case as this the products of the abstract factory are only product_a and product_b
    # now the concrete factories will only now implement this interface but in the different variants of the product


class ConcreteFactory1(AbstractFactory):  # this is a variant
    """
    Concrete Factories produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible. Note
    that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """

    # note that the products created here are of the same variant but different product families
    # in this case the variant is A1 and B1 however A and B are different product families
    def create_product_a(self) -> AbstractProductA:
        # override the abstract factory method which it implements
        # returns ConcreteProductA1()
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    """
    Each Concrete Factory has a corresponding product variant.
    """

    # note that the products created here are of the same variant but different product families
    # in this case we have the product family A and product family B
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()


class AbstractProductA(ABC):
    # distinct product should have a base interface that all variants of the product should implement
    # this is a distinct product in other words a family
    """
    Each distinct product of a product family should have a base interface. All
    variants of the product must implement this interface.
    """

    # all  variants of the product A family must implement this abstract method
    # the different variants of a product family must implement this
    @abstractmethod
    def useful_function_a(self) -> str:
        pass


"""
Concrete Products are created by corresponding Concrete Factories.
"""


class ConcreteProductA1(AbstractProductA):  # A1 can be considered a variant of the product family A
    # notice that the relationship here is inheritance
    def useful_function_a(self) -> str:
        return "The result of the product A1."


class ConcreteProductA2(AbstractProductA):  # A2 can be considered a variant of the product family A
    def useful_function_a(self) -> str:
        return "The result of the product A2."


class AbstractProductB(ABC):  # note that B is a product family
    # therefore now the variants of the product B family must inherit this abstract class
    """
    Here's the base interface of another product. All products can interact
    with each other, but proper interaction is possible only between products of
    the same concrete variant.
    """

    @abstractmethod
    def useful_function_b(self) -> None:
        """
        Product B is able to do its own thing...
        """
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:  # note by AbstractProductA is a family
        """
        ...but it also can collaborate with the ProductA.

        The Abstract Factory makes sure that all products it creates are of the
        same variant and thus, compatible.
        """
        pass


"""
Concrete Products are created by corresponding Concrete Factories.
"""


class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B1."

    """
    The variant, Product B1, is only able to work correctly with the variant,
    Product A1. Nevertheless, it accepts any instance of AbstractProductA as an
    argument.
    """

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()  # note that the method called here above is of implementing the class
        # AbstractProductA which in this case will get implemented based on the variant that is created by the
        # the variant that is created by the concreteFactory called , so this makes this dependent on the variant that
        # on the variant ConcreteFactory that is being created
        return f"The result of the B1 collaborating with the ({result})"


class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B2."

    def another_useful_function_b(self, collaborator: AbstractProductA):  # the argument in this case will be
        # an instance of a class that implements the AbstractProductA interface( inherits from it )
        """
        The variant, Product B2, is only able to work correctly with the
        variant, Product A2. Nevertheless, it accepts any instance of
        AbstractProductA as an argument.
        """
        result = collaborator.useful_function_a()  # in this case this will interact with the AbstractProductA based on
        # variant that was created in the ConcreteFactory class
        return f"The result of the B2 collaborating with the ({result})"


def client_code(factory: AbstractFactory) -> None:  # this argument in this case will be an instance of one the classes
    # an instance of one of the ConcreteFactories based on the abstract factory class
    # note by you can pass any factory in this case
    """
    The client code works with factories and products only through abstract
    types: AbstractFactory and AbstractProduct. This lets you pass any factory
    or product subclass to the client code without breaking it.
    """
    # note by saying that the client code works with abstract types this is what we mean
    # AbstractFactory that defines methods for creation of all products that belong to each product family
    # AbstractProduct that defines the interface that each product family must implement
    product_a = factory.create_product_a()  # factory in this case will be an instance of subclass of AbstractFactory()
    # this product will depend on the concrete class of the argument passed onto the client code
    product_b = factory.create_product_b()  # the result to this will be a product based on the concreteFactory return
    # the concrete factory return is dependent on the concrete factory instance created
    # thus an instance of a concrete product class

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")  # notice that the argument is an instance
    # this case this is an instance of the concrete product returned by the concrete class that was called


client_code(ConcreteFactory1())
# in this case the product_a or product_b made within the client code will be based on return types of the class in this
# case the class being the ConcreteFactory1 which created all products but of variant 1 in this case products of the
# A1 and B1 variant. note that A and B are actual product families
#
if __name__ == "__main__":
    """
    The client code can work with any concrete factory class.
    """
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory1())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreteFactory2())

"""I have understood abstract factory :)"""
