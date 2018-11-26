# design-patterns
Play design patterns


https://sourcemaking.com/design_patterns/
https://www.udemy.com/python-design-patterns/


Creational Design Patterns
	Creational design patterns are responsible for efficient object creation mechanisms,
	which increase the flexibility and reuse of existing code.
	
	Factory
		is a creational design pattern that provides an interface
		for creating objects in superclass, but allow subclasses to alter
		the type of objects that will be created.

		https://refactoring.guru/design-patterns/factory-method

	Abstract Factory
		Is a creational design pattern that lets you produce
		families of related objects without specifying their concrete classes.

		https://refactoring.guru/design-patterns/abstract-factory

	Builder
		Is a creational design pattern that lets you produce different
		types and representations of an object using the same building process.
		Builder allows constructing complex objects step by step.

		https://refactoring.guru/design-patterns/builder
	Prototype
		Is a creational design pattern that lets you produce new objects
		by copying existing ones without compromising their internals.

		https://refactoring.guru/design-patterns/prototype
	Singleton versus Borg


Structural Patterns
	Looks for a simple way to realize relationships between entities
	Structure refers to a composition of classes or objects

	MVC (Model-View-Controller)

	Façade

	Proxy

	Decorator

	Adapter


Behavioural
	Identity and realise common communication patterns between objects
	To do with assignment of responsability between objects
	Encapsulate behaviour in a object and delegate to it

	Command

	Interpreter

	State

	Chain of responsability

	Strategy

	Observer

	Memento

	Template

	Reactive design patterns


Python buitin patterns

	Iterables and Iterators
		The iterator pattern aims to provide a way to access
		the elements of an aggregate object sequentially without
		exposing its underlying representation

	List comprehension
		A list comprehension is a tool for transforming any iterable into a new list.
		Elements of the iterable can be conditionally included and transformed as required.

	Wrapper functions (or decorators)
		A decorator is a function that takes another function and extends the behaviour of
		the second function without explicitly modifying it
		Can be reused across multiple functions (but does no apply to classes)
		Functions are first-class objects, which means they can be defined in a 
		returned by other functions.