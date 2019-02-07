# design-patterns
Play design patterns


* Design pattern book https://sourcemaking.com/design_patterns/
* Udemy course https://www.udemy.com/python-design-patterns/
* Refactoring-guru 
https://refactoring.guru/design-patterns/
* Python examples https://python-3-patterns-idioms-test.readthedocs.io


Creational Design Patterns
	These patterns provide various object creation mechanisms, which
	increase flexibility and reuse of existing code.
	
	Factory
		is a creational design pattern that provides an interface
		for creating objects in superclass, but allow subclasses to alter
		the type of objects that will be created.

		(https://refactoring.guru/design-patterns/factory-method)

	Abstract Factory
		Is a creational design pattern that lets you produce
		families of related objects without specifying their concrete classes.

		(https://refactoring.guru/design-patterns/abstract-factory)

	Builder
		Is a creational design pattern that lets you produce different
		types and representations of an object using the same building process.
		Builder allows constructing complex objects step by step.

		(https://refactoring.guru/design-patterns/builder)

	Prototype
		Is a creational design pattern that lets you produce new objects
		by copying existing ones without compromising their internals.

		(https://refactoring.guru/design-patterns/prototype)

	Singleton
		Is a creational design pattern that lets you ensure that a class has 
		only one instance and provide a global access point to this instance.

		(https://refactoring.guru/design-patterns/singleton)

	Borg
		The Borg Idiom (a.k.a monostate pattern) lets a class have as many
		instances as one likes, but ensures that they all share the same state. 


Structural Patterns
	These patterns explain how to assemble objects and classes into
	larger structures, while keeping this structures flexible and efficient.

	Facade
		Is a structural design pattern that provides a simplified interface
		to a library, a framework, or any complex set of classes.

		(https://refactoring.guru/design-patterns/facade)

	Proxy
		Is a structural design pattern that lets you provide a subsitute or
		placeholder for another object. A proxy controls access to the original
		object, allowing you to perform something either before or after the
		request gets through to the original object.

		(https://refactoring.guru/design-patterns/proxy)

	Decorator
		Is a structural design pattern that lets you attach new behaviors to
		objects by placing these objects inside special wrapper objects that
		contain the behaviors.

		(https://refactoring.guru/design-patterns/decorator)

	Adapter
		Is a structural design pattern that allows objects with incompatible
		interfaces to collaborate.

		(https://refactoring.guru/design-patterns/adapter)

	Bridge
		Is a structural design pattern that lets you split a large class or a set
		of closely related classes into two separate hierarchies - abstraction and
		implementation - which can be developed independently of each other.

		https://refactoring.guru/design-patterns/bridge

	Composite
		Is a structural design pattern that lets you compose objects into tree
		structures and when work with these structures as if they were individual
		objects.

		(https://refactoring.guru/design-patterns/composite)
	
	Flyweight
		Is a structural design pattern that lets you fit more objects into the
		available amount of RAM by sharing common parts of state between multiple
		objects instead of keeping all of the data in each object.

		(https://refactoring.guru/design-patterns/flyweight)


Behavioral
	These patterns are concerned with algorithms and the assignment
	of responsabilities between objects.

	Command
		Is a behavioral design pattern that turns a request into stand-alone
		object that contains all information about the request. This transformation
		lets you parametrize methods with different requests, delay or queue a
		request's execution, and support undoable operations.

		(https://refactoring.guru/design-patterns/command)

	Interpreter
		Is a behavioral design pattern that denife a grammatical representation
		for a language and an interpreter to interpret the gramar.

	State
		Is a behavioral design pattern that lets an object alter its behavior
		when its internal state changes. It appears as if the object changed
		its class.

		(https://refactoring.guru/design-patterns/state)

	Chain of responsability
		Is a behavioral design pattern that lets you pass requests along
		a chain of handlers. Upon receiving a request, each handler decides
		either to process the request or to pass it to the next handler in
		the chain.

		(https://refactoring.guru/design-patterns/chain-of-responsibility)

	Observer
		Is a behavioral design pattern that lets you define a subscription
		mechanism to notify multiple objects about any events that happen to
		the object they're observing.

		(https://refactoring.guru/design-patterns/observer)

	Strategy
		Is a behavioral design pattern that lets you define a family of algorithms,
		put each of them into a separate class, and make their objects interhangeable.

		(https://refactoring.guru/design-patterns/strategy)

	Memento
		Is a behavioral design pattern that lets you save and restore the previous
		state of an object without revealing the details of its implementation.

		(https://refactoring.guru/design-patterns/memento)

	Template Method
		Is a behavioral design pattern that defines the skeleton of an algorithm in
		the superclass but lets subclasses override specific steps of the algorithm
		without changing its structure.

		(https://refactoring.guru/design-patterns/template-method)

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