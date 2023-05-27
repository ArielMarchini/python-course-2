class Pixel:
    def __init__(self, x=0, y=0, red=0, green=0, blue=0):
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        avg = (self._red + self._green + self._blue) // 3
        self._red = avg
        self._green = avg
        self._blue = avg

    def print_pixel_info(self):
        num_of_0 = int(self._red == 0) + int(self._green == 0) + int(self._blue == 0)
        main_color_value = self._red + self._blue + self._green
        if num_of_0 == 2 and main_color_value > 50:
            color_name = ""
            if main_color_value == self._green:
                color_name = "green"
            elif main_color_value == self._red:
                color_name = "red"
            else:
                color_name = "blue"
            print("X: {}, Y: {}, Color: ({}, {}, {})".format(self._x, self._y, self._red, self._green, self._blue), color_name)
        else:
            print("X: {}, Y: {}, Color: ({}, {}, {})".format(self._x, self._y, self._red, self._green, self._blue))


def main():
    p = Pixel(5, 6, 250)
    p.print_pixel_info()
    p.set_grayscale()
    p.print_pixel_info()



if __name__ == '__main__':
    main()
