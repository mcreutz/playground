# SOLID design principles

## Single Responsibility Principle
*Classes should only be responsible for kind of actions, not for all actions linked to a topic.*

Methods are doing one thing only
if-statements are hint for multiple responsibilities


## Open-Closed Principle
*Adding new functionality by extending the code, not by modifying it.*

Software Entities (classes, functions, modules) should be open for extension but closed to change.
Adding methods to classes is considered modification, adding classes not.
Create an abstact base class, then inherit functional classes for each variation of the task. Instatiate objects from child class. When using in signature, use abc.


## Liskov Substitution Principle
*A sub-class must be substitutable for its super-class.*

(identical signarure of methods and their arguments, enforced by interface/abc. Substitutability is NOT limited by attributes.)
First try to pass arguments to an abstract method as medthod parameters. If an argument is not the same for all daughter classes, use attributes.
Having a necessary method present that is not allowed to be called (eg. exception) - just to comply to LSP - is also a violation
Not all classes need to be derived from other classes. Where sinnvoll, standalone classes are fine as well


## Interface Segregation Principle
*It's better to have several specific interfaces, than to have one general-purpose interface.*

a) Inheritance: Build an inheriting tree of interfaces, that adds methods with each layer. Functional classes then inherit from the matching interface class
b) Composition: Extract those methods, that only some of the classes of an interface use, into a sepatate class and reference it from those classes of the interface, that need it.


## Dependency inversion principle
*When a class depends on (refereces) another class, it should depend on the interface type, not on a specific class type.*

High-level modules should not depend on low-level modules. They should depend on abstractions and abstractions should not depend on details, rather details should depend on abstractions


# Goals
- Re-usability
- Low coupling / high cohesion




# Links
- https://www.youtube.com/watch?v=pTB30aXS77U
- https://dev.to/ezzy1337/a-pythonic-guide-to-solid-design-principles-4c8i




# Others
- KISS
- DRY
- TDD (create test, fail test, create functional code, pass test, refactor functional code)
- CI/CD
- Separate creation from use (SRP)
- Dependency injection
- Contract analogy





# Helpers
- Pylint
- Pylance
- Mypy
- Black
- pydantic
