class car:
    def __init__(self, make, model, yr, color, hp):
        self.make = make
        self.model = model
        self.yr = yr
        self.color = color
        self.hp = hp

    def func(car1):
        print('this car is a ' + car1.make)


class bus(car):
    def __init__(self, make, model, yr, color, hp, weight):
        super().__init__(make, model, yr, color, hp)
        self.weight = 2300


class lorry(bus):
    def __init__(self, make, model, yr, color, hp, weight, gears):
        super().__init__(make, model, yr, color, hp, weight)
        self.gears = gears


bus1 = bus('nissan', 'diesel', '2004', 'grey', '345', '2300')
print(bus1.make)
print(bus1.model)
print(bus1.yr)
print(bus1.color)
print(bus1.hp)
print(bus1.weight)

car1 = car('vw', 'beetle', '1936', 'black', '43')
print(car1.make)
print(car1.model)
print(car1.yr)
print(car1.color)
print(car1.hp)

lorry1 = lorry('mercedes', 'Actros', '2012', 'white', '445Hp', '3000', '7-speed')
print(lorry1.make)
print(lorry1.model)
print(lorry1.color)
print(lorry1.yr)
print(lorry1.hp)
print(lorry1.weight)
print(lorry1.gears)

# Python Iterators
"""An iterator is an object that contains a countable number of values.
An iterator is an object that can be iterated upon, meaning that you can traverse 
through all the values.
Technically, in Python, an iterator is an object which implements the iterator 
protocol, which consist of the methods __iter__() and __next__()."""

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))


# Creating an iterator

class MyNumbers:  # Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


# stop iteration

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:  # Will stop after 20 iterations
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)
for x in myiter:
    print(x)
