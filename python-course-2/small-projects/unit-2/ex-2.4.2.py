# 1
class BigThing:
    def __init__(self, thing):
        self._thing = thing

    def size(self):
        if isinstance(self._thing, int):
            return self._thing
        elif isinstance(self._thing, list) or isinstance(self._thing, dict) or isinstance(self._thing, str):
            return len(self._thing)

# 2
class BigCat(BigThing):
    def __init__(self, thing, weight):
        super().__init__(thing)
        self._weight = weight

    def size(self):
        if self._weight > 20:
            return "Very Fat"
        elif self._weight > 15:
            return "Fat"
        else:
            return "OK"


def main():
    my_thing = BigThing("balloon")
    print(my_thing.size())
    cutie = BigCat("mitzy", 22)
    print(cutie.size())


if __name__ == '__main__':
    main()
