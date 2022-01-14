# SOLID design principles

## Single Responsibility Principle
*Classes and methods should only have one reason to change.*

- Classes and methods are doing one thing only. They are responsible for only one thing.
- This leads to high cohesion and ensures reusability of code.
- if-statements are hint for multiple responsibilities


## Open-Closed Principle
*Software entities should be open for extension but closed for modification.*

- Adding new functionality by extending the code, not by modifying it.
- Adding methods to classes is considered modification, adding classes is extension.
- Create an interface or abstact base class, then inherit functional classes for each variation of the task. Instatiate objects from child class, but declare them with the type of the interface.


## Liskov Substitution Principle
*A sub-class must be substitutable for its super-class.*

- (Substitutability here means identical signarure of methods and their arguments, enforced by interface/abc. It is NOT affected by different attributes of the subclaasses.) True?
- Implementing a method that is not functional (eg. just throws an exception) - just to make the class compliant to LSP - is also a violation
- Not all classes need to be derived from other classes. When sufficient, standalone classes are fine as well


## Interface Segregation Principle
*It's better to have several specific interfaces, than to have one general-purpose interface.*

a) Inheritance: Build an inheriting tree of interfaces, that adds further abstract methods with each layer. Functional classes then inherit from that interface, that matches the class.
b) Composition: Extract those methods, that only some of the sub-classes of an interface use, into a separate class (that does not inherit from the interface). Then pass a reference of an object of that independent new class to those sub-classes, that use it.


## Dependency inversion principle
*When a class depends on (references) another class, it should depend on (reference) the interface/abc type, not on a specific class type.*

- High-level modules should not depend on low-level modules. They should depend on abstractions
- Abstractions should not depend on details, rather details should depend on abstractions


# Goals
- Re-usability of code
- Flexibility
- Maintainability




# Links
- https://www.youtube.com/watch?v=pTB30aXS77U




# Others
- KISS
- DRY
- TDD (create test, fail test, create functional code, pass test, refactor functional code)
- CI/CD
- Separate creation from use (SRP)
- Dependency injection
- Contract analogy: An interface is like a contract, that needs to be fulfilled by implementing classes




# Helpers
- Pylint
- Pylance
- Mypy
- Black
- pydantic




## Abstraction
Reducing (an object) to its (for the given context) relevant features

## Encapsulation
Limiting the access of properties and methods from outside a class by access modifiers and getters/setters to improve understandability and control about property value modifications

## Decomposition
The division of a whole into smaller pieces ant their relationships. Or the connection of smaller pieces to form a bigger whole.

### Association
Two classes have a loose relationship but do exist independently of each other.
Airline - person
Line connects the classes

### Aggregation
An association, where..
Parts belong to other parts, loose 'has-a'-relationship. But the connection is temporal and the objects can exist separately.
Plane - crew
Hollow diamond marks the containing class

### Composition
An aggregation, where..
Parts belong to other parts, strong 'has-a'-relationship. Parts cannot exist separately.
Human - brain
Daughter object does not need to be created within mother object. Dependency injection is also possible.
Filled diamond marks the containing class


## Generalizaiton
Liskov substitution for both cases

### Inheritance
Keyword extends
Only one superclass per subclass possible
Drawn as hollow arrow pointing upwards to superclass

### Interface
Keyword implements
Multiple interfaces per class possible
Only methods, no attributes
No implementations
Drawn as hollow arrow with dashed line, pointing upwards to the interface

### Polymorphism
Objects with the same (method-)signature but different implementations



## Coupling
Degree: The number of connections to other modules (classes, methods)
Ease: Connections should be easy to make and understand, without knowledge about the implementation of the other module.
Flexibility: Interchangeability between similar modules 

## Cohesion


## Separaton of concerns


## Information hiding
Provide outside access only to necessary parts through access modifiers

## Object types
Entity, boundry, control

