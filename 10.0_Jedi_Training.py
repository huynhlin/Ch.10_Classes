'''
Sign your name:________________
 
 1. Write code that defines a class named Animal:
     * Add a constructor for the Animal class that prints 'An animal has been born.'
     * Add an attribute for the animal name.
     * Add an eat() method for Animal that prints 'Munch munch.'
     * Add a make_noise() method for Animal that prints 'Grrr says [animal name].'

     
 2. Write code that defines a class named Cat:
     * Make Animal the parent.
     * Add a constructor for Cat that prints 'A cat has been born.'
     * Modify the constructor so it calls the parent constructor as well.
     * Add a make_noise() method for Cat that prints 'Meow says [animal name].'

     
 3. Write code that defines a class named Dog:
     
     * Make Animal the parent.
     * Add a constructor for Dog that prints 'A dog has been born.'
     * Modify the constructor so it calls the parent constructor as well.
     * Add a make_noise() method for Dog that prints 'Bark says [animal name].'

     
 4. Write a main program with:
     
     * Code that creates a cat, two dogs, and an animal with names.
     * Code that calls eat() and make_noise() for each animal.
     
 OUTPUT:
An animal has been born.
A cat has been born.
Munch munch
Meow says (cat name) .
An animal has been born.
A dog has been born.
Munch munch
Bark says (dog name).
An animal has been born.
A dog has been born.
Munch munch
Bark says (another dog name) .
An animal has been born.
Munch munch
Grrr says (animal name) .
'''


class Animal:
    def __init__(self, n):
        print("An animal has been born.")
        self.name = n

    def eat(self):
        print("Munch munch.")

    def make_noise(self):
        print("Grrr says", self.name)


class Cat(Animal):
    def __init__(self, n):
        super().__init__(n)
        print("A cat has been born.")

    def make_noise(self):
        print("Meow says", self.name)

class Dog(Animal):
    def __init__(self, n):
        super().__init__(n)
        print("A dog has been born.")
    def make_noise(self):
        print("Bark says", self.name)

def main():
    cat = Cat("Mittens")
    cat.eat()
    cat.make_noise()
    first_dog = Dog("Max")
    first_dog.eat()
    first_dog.make_noise()
    second_dog = Dog("Maverick")
    second_dog.eat()
    second_dog.make_noise()
    bear = Animal("Bear")
    bear.eat()
    bear.make_noise()


if __name__ == "__main__":
    main()

print("\n\n\nDid you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It’s not a story the Jedi would "
      "tell you. "
      "It’s a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the "
      "Force to influence the midichlorians to create life… He had such a knowledge of the dark side that he could even"
      " keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some "
      "consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which "
      "eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice "
      "killed him in his sleep. Ironic. He could save others from death, but not himself.")
