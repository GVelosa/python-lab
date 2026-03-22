# Object-Oriented Programming (OOP) in Python

------------------------------------------------------------------------

## 📺 Source

> This content was created based on the following video:\
> 👉 [Watch on
> YouTube](https://youtu.be/QAwNvlEd1aM?si=xpbyHqNZwUQQq7cR)
>
> 📺 Channel:\
> 👉 [Lan Code](https://www.youtube.com/@lan_code)

------------------------------------------------------------------------

# Overview

Object-Oriented Programming (OOP) works with entities that we create in
order to replicate their properties and methods into instances.

------------------------------------------------------------------------

# Classes

A class is essentially a mold (or template) used to create objects.

``` python
class Channel:
    pass
```

Attributes: - Name\
- Description\
- Subscribers

------------------------------------------------------------------------

# Objects

Objects are instances created from a class.

Example: - Name: "Lan Code"\
- Description: "Programming Channel"\
- Subscribers: 34,000

------------------------------------------------------------------------

## Implementation

``` python
class Channel:
    def __init__(self, name, description, subscribers):
        self.name = name
        self.description = description
        self.subscribers = subscribers
```

------------------------------------------------------------------------

# Methods

``` python
def subscribe(self, quantity=1):
    self.subscribers += quantity
```

------------------------------------------------------------------------

# Inheritance

``` python
class Employee:
    def __init__(self, id, name, salary):
        self.id = id 
        self.name = name
        self.salary = salary
```

------------------------------------------------------------------------

## Encapsulation

``` python
class EmployeeDirector(Employee):
    def __init__(self, id, name, salary):
        super().__init__(id, name, salary)
        self._team = []
```

------------------------------------------------------------------------

## Composition Example

``` python
class Channel:
    def __init__(self, name):
        self.name = name
```

------------------------------------------------------------------------

## Note

Study-only material based on a YouTube reference.
