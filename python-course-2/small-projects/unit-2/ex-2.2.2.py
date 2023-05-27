class ant:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print("Hello my queen my name is:", self.name)


    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age



def main():
    ant_1 = ant("ariel", 19)
    ant_2 = ant("the queen", 90)
    ant_2.birthday()
    print(ant_1.get_age())
    print(ant_2.get_age())


if __name__ == '__main__':
    main()