# oops
---

The *class* is a fundamental building block in Python

Let us explore the term *Object Oriented Programming* and explore how it ties together with Python Classes. 

## Everything Is An Object 

In defining new function, *def* keyword plays a role. Similarly, *class* keyword helps define new *class*.  And what is a class? Simply a logical grouping of data and functions. The functions from class are frequently referred to as "methods". They are defined within a class.

Many times, classes are based on objects in the real world (like Customer, Person, Employee or Product). Other times, classes are based on concepts in our system, like HTTPRequest, REST API, Owner.

Regardless, classes are a modeling technique; a way of thinking about programs. When you think about and implement your system in 
this way, you're said to be performing Object-Oriented Programming. "Classes" and "objects" are words that are often used 
interchangeably, but they're not really the same thing. Understanding what makes them different is the key to understanding what 
they are and how they work.

## So Everything Has A Class?

You can think of Classes can be thought of as Template or blueprints for creating objects. When I define a Customer class using the 
class keyword, I haven't actually created a customer. Instead, what I've created is a sort of instruction manual for 
constructing "customer" objects. Let's look at the following example code:

```
class Customer(object):
    def __init__(self, name, balance=0.0):
        self.name    = name
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
```

It's just a template to create a Customer object, The script calls the class's __init__ method with the proper number of arguments 
(minus self).

we call the class name almost as if it were a function: 

```
hari = Customer('Hari Sadu', 1000.0)

```

This line simply says "use the Customer template to create me a new object, which I'll refer to as *hari*
The *hari* object, known as an instance, is the realized version of the Customer class. 
Before we called Customer(), no Customer object existed. We can create as many Customer objects as we'd like. 
There is still, however, only one Customer class, regardless of how many instances of the class we create.

## self? 

so what's that *self* everywhere? 

When we say def withdraw(self, amount):, we're saying, "here's how you withdraw money from a 
Customer object (which we'll call self) and a dollar figure (which we'll call amount). 
*self* is the instance of the Customer that withdraw is being called on. That's not me making analogies, either. *hari.withdraw(100.0)* is just shorthand for *Customer.withdraw(hari, 100.0)*, which is perfectly valid (if not often seen) code.

## __init__

When we call __init__, we're in the process of creating an object, so how can there already be a self? 
Python allows us to extend the self pattern to when objects are constructed as well. Just imagine that 

```
hari = Customer('Hari Sadu', 1000.0) 

```
is the same as calling 

```
hari = Customer(hari, 'Hari Sadu', 1000.0)

```
the *hari* that's passed in is also made the result.

This is why when we call *__init__*, we initialize objects by saying things like self.name = name. 
Remember, since self is the instance, this is equivalent to saying hari.name = name, which is the same as hari.name = 'Hari Sadu'.
Similarly, self.balance = balance is the same as hari.balance = 1000.0. 
After these two lines, we consider the Customer object "initialized" and ready for use.

Be careful what you __init__

After __init__ has finished, the caller can rightly assume that the object is ready to use. 
That is, after hari = Customer('Hari Sadu', 1000.0), we can start making deposit and withdraw calls on *hari*; 
*hari* is a fully-initialized object.


Just imagin - if our __int__ was as below:

```
    def __init__(self, name):
        self.name = name

```
In this case, may be we would have defined: 

```
def set_balance(self, balance=0.0):
        self.balance = balance
```
Our sequeance of calling would have been to call - 
```
hari = Customer('Hari Sadu')
hari.set_balance(1000.0)
hari.withdraw(100.0). 
```
This only says - object was not fully initialized

The rule of thumb is, don't introduce a new attribute outside of the __init__ method, otherwise you've given the caller an object that isn't fully initialized.  The  object should start in a valid state as well. Its very important to initialize everything in the __init__ method.

# Instance Attributes and Methods

An function defined within a class block is called a "method". Methods have access to all the data contained on the instance of the object;
They can access and modify anything previously set on self. 

Class also have other type of methods.

## Static Method 

## Class Method

It's possible to set a few aitributes at the class-level. As we know, normal attributes are introduced in the __init__ method, 
but some attributes of a class hold for all instances in all cases. 

For example, consider the following definition of a Car object:

```
class Car(object):

    wheels = 4
    def __init__(self, make, model):
        self.make = make
        self.model = model

mustang = Car('Ford', 'Mustang')

print mustang.wheels
# 4
print Car.wheels
# 4

```

There is a class of methods, though, called static methods, that don't have access to self. 
Just like class attributes, they are methods that work without requiring an instance to be present. 
Since instances are always referenced through self, static methods have no self parameter.

Let us look at the following example:

```

class Car(object):
    ...
    @staticmethod
    def make_car_sound():
        print 'VRooooommmm!'

```
Here - @staticmethod decorator is used. This is used just to make it clear that this method should not receive the instance as the first parameter 

## Class Methods


A variant of the static method is the class method. Instead of receiving the instance as the first parameter, it is passed the class. It, too, is defined using a decorator:

```
class Vehicle(object):
    ...
    @classmethod
    def is_motorcycle(cls):
        return cls.wheels == 2
```

Class methods may not make much sense right now, but that's because they're used most often in connection with our next topic: inheritance.



# Inheritance 


Inherticance is the process by which a "child" class derives the data and behavior of a "parent" class. 

Let us look at the example to understand this concept


# Abstract Classes (Encapsulation of Data) 

The terms encapsulation and abstraction (also data hiding) are often used as synonyms. They are nearly synonymous, i.e. abstraction is achieved though encapsulation. Data hiding and encapsulation are the same concept, so it's correct to use them as synonyms. 


Generally speaking encapsulation is the mechanism for restricting the access to some of an object's components, this means that the internal representation of an object can't be seen from outside of the objects definition. Access to this data is typically only achieved through special methods: Getters and Setters. By using solely get() and set() methods, we can make sure that the internal data cannot be accidentally set into an inconsistent or invalid state. 

The protection mechanism in Python is called  mangling. 

A method to set private data can also be used to do some plausibility checks. In our example, we can check, if the birthday makes sense, e.g. it's not very likely that a customer is more than are 100 years old. Or we can rule out that a customer with a giro account is less than 14 years old. 



# 

Encapsulation
  -- constructor 
  -- destructor 
Data Abstraction
Polymorphism
Inheritance

###

