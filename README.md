# design-patterns
Play design patterns


https://sourcemaking.com/design_patterns/
https://www.udemy.com/python-design-patterns/


Creational Patterns
	Separate system from how its objects are created and composed
	Explicitly express which concrete classes the system uses
	Hide how instances of these concrete classes are created and combined
	
	Factory

	Abstract Factory

	Builder

	Prototype

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