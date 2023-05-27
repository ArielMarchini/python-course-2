class Animal:
    """
    Animal class represents an animal in the zoo.
    """
    zoo_name = "Hayaton"

    def __init__(self, name, hunger=0):
        """
        Initializes an instance of the Animal class.

        Parameters:
            name (str): The name of the animal.
            hunger (int): The hunger level of the animal (default: 0).
        """
        self._name = name
        self._hunger = hunger

    def get_name(self):
        """
        Get the name of the animal.

        Returns:
            str: The name of the animal.
        """
        return self._name

    def is_hungry(self):
        """
        Check if the animal is hungry.

        Returns:
            bool: True if the animal is hungry, False otherwise.
        """
        return self._hunger > 0

    def feed(self):
        """
        Feed the animal by reducing its hunger level by 1.
        """
        self._hunger -= 1

    def __str__(self):
        """
        Return a string representation of the animal's class name.

        Returns:
            str: The class name of the animal.
        """
        return self.__class__.__name__

    def talk(self):
        """
        Make the animal talk.
        This is a placeholder method and should be overridden by subclasses.
        """
        pass

    def special(self):
        """
        Perform the special action of the animal.
        This is a placeholder method and should be overridden by subclasses.

        This is much better than checking every kind of clss. This way
        the code can be updated in better way.
        """
        pass


class Dog(Animal):
    """
    Dog class represents a dog in the zoo.
    """

    def talk(self):
        """
        Make the dog bark.
        """
        print("woof woof")

    def fetch_stick(self):
        """
        Make the dog fetch a stick.
        """
        print("There you go, sir!")

    def special(self):
        """
        Perform the special action of the dog: fetching a stick.
        """
        self.fetch_stick()


class Cat(Animal):
    """
    Cat class represents a cat in the zoo.
    """

    def talk(self):
        """
        Make the cat meow.
        """
        print("meow")

    def chase_laser(self):
        """
        Make the cat chase a laser pointer.
        """
        print("Meeeeow")

    def special(self):
        """
        Perform the special action of the cat: chasing a laser pointer.
        """
        self.chase_laser()


class Skunk(Animal):
    """
    Skunk class represents a skunk in the zoo.
    """

    def __init__(self, name, hunger=0, stink_count=6):
        """
        Initializes an instance of the Skunk class.

        Parameters:
            name (str): The name of the skunk.
            hunger (int): The hunger level of the skunk (default: 0).
            stink_count (int): The number of times the skunk can stink (default: 6).
        """
        Animal.__init__(self, name, hunger)
        self._stink_count = stink_count

    def talk(self):
        """
        Make the skunk make a sound.
        """
        print("tsssss")

    def stink(self):
        """
        Make the skunk emit a strong odor.
        """
        print("Dear lord!")

    def special(self):
        """
        Perform the special action of the skunk: emitting a strong odor.
        """
        self.stink()


class Unicorn(Animal):
    """
    Unicorn class represents a unicorn in the zoo.
    """

    def talk(self):
        """
        Make the unicorn say a greeting.
        """
        print("Good day, darling")

    def sing(self):
        """
        Make the unicorn sing a song.
        """
        print("I’m not your toy...")

    def special(self):
        """
        Perform the special action of the unicorn: singing a song.
        """
        self.sing()


class Dragon(Animal):
    """
    Dragon class represents a dragon in the zoo.
    """

    def __init__(self, name, hunger=0, color="Green"):
        """
        Initializes an instance of the Dragon class.

        Parameters:
            name (str): The name of the dragon.
            hunger (int): The hunger level of the dragon (default: 0).
            color (str): The color of the dragon (default: "Green").
        """
        Animal.__init__(self, name, hunger)
        self._color = color

    def talk(self):
        """
        Make the dragon roar.
        """
        print("Raaaawr")

    def breath_fire(self):
        """
        Make the dragon breathe fire.
        """
        print("$@#$#@$")

    def special(self):
        """
        Perform the special action of the dragon: breathing fire.
        """
        self.breath_fire()


def main():
    """
    Main function to demonstrate the behavior of different animals in the zoo.
    """
    brownie = Dog("Brownie", 10)
    zelda = Cat("Zelda", 3)
    stinky = Skunk("Stinky", 0)
    keith = Unicorn("Keith", 7)
    lizzy = Dragon("Lizzy", 1450)
    doggo = Dog("Doggo", 80)
    kitty = Cat("Kitty", 80)
    stinky_jr = Skunk("Stinky Jr.", 80)
    clair = Unicorn("Clair", 80)
    mcfly = Dragon("McFly", 80)
    zoo_lst = [brownie, zelda, stinky, keith, lizzy, doggo, kitty, stinky_jr, clair, mcfly]
    for animal in zoo_lst:
        if animal.is_hungry():
            print(animal, animal.get_name())
            while animal.is_hungry():
                animal.feed()
            animal.talk()
            animal.special()
    print(Animal.zoo_name)


if __name__ == '__main__':
    main()
