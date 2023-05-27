class ant:
    count_animals = 0
    def __init__(self, age, name="anto"):
        self._name = name
        self._age = age
        ant.count_animals += 1

    def print_name(self):
        print("Hello my queen my name is:", self._name)


    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


def main():
    ant_1 = ant(12,"ariel")
    ant_2 = ant(90)
    print(ant_1.get_name())
    print(ant_2.get_name())
    ant_1.set_name("new name")
    print(ant_1.get_name())
    print(ant.count_animals)




if __name__ == '__main__':
    main()