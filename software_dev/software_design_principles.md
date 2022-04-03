# Goals
- Re-usability of code
- Flexibility
- Maintainability





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




# Other priciples

## Principle Of Least Knowledge / Law of Demeter
*Classes should know about and interact with as few other classes as possible.*

Methods should only call other methods, that are either
- defined within the same object
- defined within an object of its own parameters
- defined within an object, that is instantiated within this method
- difined within an object, that is a direct component of its own object.

Returned objects should be of a type that is declared either
- locally in the method
- in the method's parameters
- in instance variables of the class that encapsulates the method


## Composing Objects Principle
*Use composition over inheritance, where possible*



# High level priciples

## Inversion of Control

## Dependency Injection

## Abstraction
Reducing (an object) to its (for the given context) relevant features

## Encapsulation
Limiting the access of properties and methods from outside a class by access modifiers and getters/setters to improve understandability and control about property value modifications

## Information hiding
Provide outside access only to necessary parts through access modifiers

## Separaton of concerns
Separate creation and usage of an object onto different classes

## Decomposition
The division of a whole into smaller pieces and their relationships. Or the connection of smaller pieces to form a bigger whole.

## Generalizaiton
Base classes carry the common attributes (properties and methods). Sub-classes inherit these and contain individual and more specialized attributes themselves additionaly.

### Inheritance
Keyword extends
Only one superclass per subclass possible

### Interface
Keyword implements
Multiple interfaces per class possible
Only methods, no attributes
No implementations

### Polymorphism
Objects with the same (method-)signature but different implementations

## Coupling
Degree: The number of connections to other modules (classes, methods)
Ease: Connections should be easy to make and understand, without knowledge about the implementation of the other module.
Flexibility: Interchangeability between similar modules 

## Cohesion
Measures, how tight the elements of a component belong and work together




## Class relationships
Good documentation: https://www.c-sharpcorner.com/UploadFile/b1df45/dependency-generalization-association-aggregation-compos/

### Dependency
One class is dependent on the other. It uses parts of the other class, but is no associated.
Dashed line connects the classes, an open tip marks the daughter class

### Association
Two classes have a loose relationship (one uses the other, but no ownership) and they do exist independently of each other (regarding lifetime). An association is also a dependency.

Airline - person
Line connects the classes, sometimes an open tip marks the daughter class

### Aggregation
An association, where 
- one object also owns the other one. But the lifetime of the objects is still unrelated.
- Parts belong to other parts, loose 'has-a'-relationship. But the connection is temporal and the objects can exist separately.
Plane - crew
Line connects the classes, hollow diamond marks the mother class

### Composition
An aggregation, where..
- one object not only uses and owns another object, but also the lifetime of the other object depends on the owning class.
- Parts belong to other parts, strong 'has-a'-relationship. Parts cannot exist separately.
Plane - Engine
Daughter object does not need to be created within mother object. Dependency injection is also possible.
Line connects the classes, solid diamond marks the mother class

### Inheritance
One class inherits from another concrete class
Line connects the classes, a hollow tip marks the base class, usually pointing upwards

### Implementation
One class implements an interface or an abstract base class
Dashed line connects the classes, an hollow tip marks the base class, usually pointing upwards



## Object types
Entity, boundry, control



## Delegation




# Others
- KISS
- DRY
- TDD (create test, fail test, create functional code, pass test, refactor functional code)
- CI/CD
- Separate creation from use (SRP)
- Dependency injection
- Contract analogy: An interface is like a contract, that needs to be fulfilled by implementing classes








# Clean Code
## Methods
- Methods should have as few parameters as possible. 3 or more parameters only in emergencies.
- Types of methods:...
- Max one level of abstraction
- Do one thing only
- Have no side effects
- Command/Query separation
- Throw exceptions if not returning as advertised

## Classes
- 

## Code smells
- Bad comments
- Duplicated code
- Long method
- Large class
- Small class
- Long parameter list
- Feature envy
- Inappropriate intimacy
- Message chains
- Primitive obsession
- Switch statements
- Speculative generality
- Refused request
(On code changes)
- Divergent change
- Shotgun surgery