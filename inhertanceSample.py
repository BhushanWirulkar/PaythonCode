class Animal:
    def walk(self):
        print("walk")


class Dog(Animal):
    def bark(self):
        print("Barkkkkkkkkkkkk")


class Cat(Animal):
    def mew(self):
        print("Mewwwwwwwwwwwwwwwwwwww")


dog1 = Dog()
dog1.bark()
dog1.walk()
cat1 = Cat()
cat1.mew()
cat1.walk()