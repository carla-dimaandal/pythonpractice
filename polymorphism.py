class Dog:
    def bark(self):
        print("Dog barks")
    def meow(self):
        print("Dog does not meow")
class Cat:
    def bark(self):
        print("Cat does not bark")
    def meow(self):
        print("Cats meow")

def barking_test(Dog):
    Dog.bark()

chihuahua = Dog()
siamese = Cat()

barking_test(chihuahua)
barking_test(siamese)