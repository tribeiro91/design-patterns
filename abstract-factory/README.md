# Abstract Factory

## What is?
Abstract factory is a **creational** design pattern that provides an interface for creating families of related or dependent objects.

## What is its goal?
This design pattern aims to remove structural dependencies of an object in an implementation in order to facilitate the changing of an implementation to another object of the same family/type.

## When to use?
You can use when you have a domain of a objects with similar operations, such as:
- Database configuration.
- Types of payments.

## How to implement an abstract factory?
To implement the Abstract Factory, you have to follow the steps hereafter:
- Create an factory interface that will be a blueprint for the concrete classes.
- Create the concrete classes of the factory that implements the factory interface.
- Create the abstract class for each product that is called in each method of the concrete factory class.
- Create the concrete classes that implements each product.
- Create a dictionary that it will link the dictionary property to each concrete factory class.
- Implement the method to call the class thorugh the type dictionary.

## References
- [Design Patterns in Python: Abstract Factory](https://medium.com/@amirm.lavasani/design-patterns-in-python-abstract-factory-2dcae06e5d29)
- [Abstract Factory: O que é? Para que serve? - by Elemar Junior](https://www.youtube.com/watch?v=6SubIYR1HAY&t=2807s)







